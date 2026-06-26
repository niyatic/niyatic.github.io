#!/usr/bin/env python3
"""Build the faceted content search index for the Hyperbots content hub.

Implements §3 of CONTENT-HUB-IA-PLAN-v3. Walks the repo (stdlib only),
emits library/content-index.json — one record per content piece:
  {title, topic, channel, type, audience, date, status, url, tags}

Harvest sources:
  - _internal/topics/**/*.md  -- YAML front-matter blocks
  - library/videos/index.html -- per-card data-* attributes (channel=video)
  - marketing/**/*.html       -- published/draft marketing pages (title<-page,
                                 channel/type/date inferred from path+name)
  - benchmarks/**/*.html
    parse-deep-bench/**/*.html -- research studies/leaderboards/papers
  - repos/*/blog.html         -- one record PER CONCEPT (slugs deduped to base
                                 concepts the same way build_repos_index.py does,
                                 ~683 records), url = English blog.html.

This indexes the real published corpus (~1,400+ records), not just the 26
scaffold records. Robust: skips non-content (assets, gate.js, index pages),
never crashes on a malformed page, and dedupes by url.
"""
import html
import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS_DIR = os.path.join(REPO_ROOT, "_internal", "topics")
VIDEOS_HTML = os.path.join(REPO_ROOT, "library", "videos", "index.html")
REPOS_DIR = os.path.join(REPO_ROOT, "repos")
MARKETING_DIR = os.path.join(REPO_ROOT, "marketing")
# Research-linked content dirs (channel=research).
RESEARCH_DIRS = (os.path.join(REPO_ROOT, "benchmarks"),
                 os.path.join(REPO_ROOT, "parse-deep-bench"))
OUT_PATH = os.path.join(REPO_ROOT, "library", "content-index.json")

FIELDS = ("title", "topic", "channel", "type", "audience", "date", "status",
          "url", "tags")

# Recognized language suffixes (slug suffix -> display language), longest first
# so "-zh-hans" wins over "-zh". Mirrors tools/build_repos_index.py so the
# concept dedup matches the repos index exactly.
LANG_SUFFIXES = [
    "zh-hans", "zh-hant", "pt-br", "ar", "de", "es", "fr", "hi", "it", "ja",
    "ko", "nl", "pt", "ru", "tr", "pl", "vi", "th", "id", "ms", "sv", "da",
    "no", "fi", "cs", "el", "he", "uk", "ro", "hu", "zh",
]

_DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
_TITLE_TAG_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
_H1_TAG_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)
_TAGSTRIP_RE = re.compile(r"<[^>]+>")


def _strip(v):
    v = v.strip()
    if len(v) >= 2 and v[0] in "\"'" and v[-1] == v[0]:
        v = v[1:-1]
    return v


def parse_front_matter(text):
    """Parse a leading YAML-ish front-matter block. Returns dict or None.

    Deliberately minimal (stdlib only): handles `key: value` and inline
    `tags: [a, b, c]` lists. Never raises on a malformed block.
    """
    if not text.startswith("---"):
        return None
    # Find the closing delimiter line.
    m = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", text, re.DOTALL)
    if not m:
        return None
    block = m.group(1)
    data = {}
    try:
        for line in block.splitlines():
            line = line.rstrip()
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if ":" not in line:
                continue
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if key == "tags":
                tags = []
                inner = val
                if inner.startswith("[") and inner.endswith("]"):
                    inner = inner[1:-1]
                for t in inner.split(","):
                    t = _strip(t)
                    if t:
                        tags.append(t)
                data["tags"] = tags
            else:
                data[key] = _strip(val)
    except Exception:
        return None
    return data or None


def record_from_fm(fm, url):
    return {
        "title": fm.get("title", ""),
        "topic": fm.get("topic", ""),
        "channel": fm.get("channel", ""),
        "type": fm.get("type", ""),
        "audience": fm.get("audience", ""),
        "date": fm.get("date", ""),
        "status": fm.get("status", ""),
        "url": url,
        "tags": fm.get("tags", []) if isinstance(fm.get("tags"), list) else [],
    }


def harvest_topics(records):
    if not os.path.isdir(TOPICS_DIR):
        return
    for dirpath, _dirs, files in os.walk(TOPICS_DIR):
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            # Skip the empty 7-channel skeleton template.
            if os.path.basename(dirpath) == "_TEMPLATE":
                continue
            path = os.path.join(dirpath, fn)
            try:
                with open(path, encoding="utf-8") as f:
                    text = f.read()
            except Exception:
                continue
            fm = parse_front_matter(text)
            if not fm:
                continue
            rel = os.path.relpath(path, REPO_ROOT)
            records.append(record_from_fm(fm, "/" + rel.replace(os.sep, "/")))


# Per-video <div class="card" ...> block, capturing attrs + h3 + link href.
_CARD_RE = re.compile(r"<div class=\"card[^\"]*\"([^>]*)>(.*?)</div>\s*", re.DOTALL)
_ATTR_RE = re.compile(r"data-([a-z]+)=\"([^\"]*)\"")
_H3_RE = re.compile(r"<h3>(.*?)</h3>", re.DOTALL)
_HREF_RE = re.compile(r"<a[^>]*class=\"link\"[^>]*href=\"([^\"]*)\"")


def harvest_videos(records):
    if not os.path.isfile(VIDEOS_HTML):
        return
    try:
        with open(VIDEOS_HTML, encoding="utf-8") as f:
            html_text = f.read()
    except Exception:
        return
    # Cards may contain nested divs (.tags); use a tolerant scan per card start.
    for am in re.finditer(r"<div class=\"card[^\"]*\"([^>]*)>", html_text):
        attrs = dict(_ATTR_RE.findall(am.group(1)))
        if not attrs:
            continue
        # Body = from this tag to the next card or section end.
        start = am.end()
        nxt = html_text.find('<div class="card', start)
        end = nxt if nxt != -1 else html_text.find("</section>", start)
        body = html_text[start:end if end != -1 else len(html_text)]
        h3 = _H3_RE.search(body)
        title = html.unescape(re.sub(r"<[^>]+>", "", h3.group(1)).strip()) if h3 else ""
        href = _HREF_RE.search(body)
        url = href.group(1) if href else "/library/videos/"
        tags = [t for t in (attrs.get("type"), attrs.get("audience")) if t]
        records.append({
            "title": title,
            "topic": attrs.get("topic", ""),
            "channel": attrs.get("channel", "video"),
            "type": attrs.get("type", ""),
            "audience": attrs.get("audience", ""),
            "date": attrs.get("date", ""),
            "status": attrs.get("status", ""),
            "url": url,
            "tags": tags,
        })


# ---------------------------------------------------------------------------
# HTML helpers (shared by marketing / research / repos harvests).
# ---------------------------------------------------------------------------

def _clean_text(s):
    s = _TAGSTRIP_RE.sub("", s)
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    # Drop a trailing site-name suffix like " · Hyperbots …" / " | Hyperbots …".
    s = re.split(r"\s+[·|—-]\s+Hyperbots", s)[0].strip()
    return s


def _page_title(path, fallback):
    """Title from <h1> then <title>, else a prettified fallback. Never raises."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            txt = f.read(20000)
    except OSError:
        return fallback
    for rx in (_H1_TAG_RE, _TITLE_TAG_RE):
        m = rx.search(txt)
        if m:
            t = _clean_text(m.group(1))
            if t:
                return t
    return fallback


def _prettify(slug):
    s = slug
    if s.startswith("hyperapi-"):
        s = s[len("hyperapi-"):]
    s = s.replace("-", " ").strip()
    return (s[:1].upper() + s[1:]) if s else slug


def _date_from(text):
    m = _DATE_RE.search(text)
    return m.group(1) if m else ""


# Files / dirs that are not content pieces themselves.
_SKIP_NAMES = {"index.html", "gate.js"}
_SKIP_DIR_PARTS = {"assets", "_assets", "img", "images", "css", "js", "static"}


def _is_content_html(dirpath, fn):
    if not fn.endswith(".html"):
        return False
    if fn in _SKIP_NAMES:
        return False
    rel = os.path.relpath(dirpath, REPO_ROOT).split(os.sep)
    if any(p in _SKIP_DIR_PARTS for p in rel):
        return False
    return True


def harvest_marketing(records):
    """One record per published/draft marketing HTML page."""
    if not os.path.isdir(MARKETING_DIR):
        return
    for dirpath, _dirs, files in os.walk(MARKETING_DIR):
        for fn in sorted(files):
            if not _is_content_html(dirpath, fn):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, REPO_ROOT).replace(os.sep, "/")
            rell = rel.lower()
            # Channel from filename hints.
            if "linkedin" in fn.lower():
                channel = "linkedin"
            elif "tweet" in fn.lower() or "twitter" in fn.lower():
                channel = "tweet"
            else:
                channel = "blog"
            ctype = "draft" if ("draft" in rell) else "published"
            title = _page_title(path, _prettify(fn[:-5]))
            records.append({
                "title": title,
                "topic": "",
                "channel": channel,
                "type": ctype,
                "audience": "marketing",
                "date": _date_from(rel),
                "status": ctype,
                "url": "/" + rel,
                "tags": [],
            })


def harvest_research(records):
    """One record per research study/leaderboard/paper HTML page."""
    for base in RESEARCH_DIRS:
        if not os.path.isdir(base):
            continue
        for dirpath, _dirs, files in os.walk(base):
            for fn in sorted(files):
                if not _is_content_html(dirpath, fn):
                    continue
                path = os.path.join(dirpath, fn)
                rel = os.path.relpath(path, REPO_ROOT).replace(os.sep, "/")
                title = _page_title(path, _prettify(fn[:-5]))
                records.append({
                    "title": title,
                    "topic": "",
                    "channel": "research",
                    "type": "published",
                    "audience": "research",
                    "date": _date_from(rel),
                    "status": "published",
                    "url": "/" + rel,
                    "tags": [],
                })


def _split_lang(slug):
    """Return (base_concept, is_english). Mirrors build_repos_index.py."""
    for suf in LANG_SUFFIXES:
        if slug.endswith("-" + suf):
            return slug[: -(len(suf) + 1)], False
    return slug, True


def harvest_repos(records):
    """One blog record PER CONCEPT (slugs deduped to base concepts).

    ~1,650 repos/<slug>/blog.html dirs collapse to ~683 base concepts (slug
    minus a trailing language suffix). The English variant's slug + title is
    preferred; url points at that English blog.html.
    """
    if not os.path.isdir(REPOS_DIR):
        return
    concepts = {}  # base -> {"slug":.., "title":.., "english": bool}
    for slug in sorted(os.listdir(REPOS_DIR)):
        d = os.path.join(REPOS_DIR, slug)
        if not os.path.isdir(d):
            continue
        blog = os.path.join(d, "blog.html")
        if not os.path.isfile(blog):
            continue
        base, is_en = _split_lang(slug)
        c = concepts.get(base)
        # Prefer the English variant for both slug (url) and title.
        if c is None:
            concepts[base] = {
                "slug": slug,
                "title": _page_title(blog, _prettify(base)),
                "english": is_en,
            }
        elif is_en and not c["english"]:
            concepts[base] = {
                "slug": slug,
                "title": _page_title(blog, _prettify(base)),
                "english": True,
            }
    for base in sorted(concepts):
        c = concepts[base]
        records.append({
            "title": c["title"],
            "topic": base,
            "channel": "blog",
            "type": "published",
            "audience": "marketing",
            "date": "",
            "status": "published",
            "url": "/repos/{}/blog.html".format(c["slug"]),
            "tags": [],
        })


def main(argv):
    records = []
    harvest_topics(records)
    harvest_videos(records)
    harvest_marketing(records)
    harvest_research(records)
    harvest_repos(records)

    # Dedupe by url (first occurrence wins; topics/videos harvested first).
    seen = set()
    deduped = []
    for r in records:
        u = r.get("url", "")
        if u and u in seen:
            continue
        if u:
            seen.add(u)
        deduped.append(r)
    records = deduped

    # Stable sort: newest date first, then title.
    records.sort(key=lambda r: (r.get("date", ""), r.get("title", "")),
                 reverse=True)

    payload = {
        "generated_by": "tools/build_content_index.py",
        "count": len(records),
        "fields": list(FIELDS),
        "records": records,
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")

    by_channel = {}
    for r in records:
        by_channel[r["channel"]] = by_channel.get(r["channel"], 0) + 1
    by_type = {}
    for r in records:
        by_type[r["type"]] = by_type.get(r["type"], 0) + 1
    print("Wrote {} ({} records)".format(
        os.path.relpath(OUT_PATH, REPO_ROOT), len(records)))
    print("By channel: {}".format(by_channel))
    print("By type: {}".format(by_type))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
