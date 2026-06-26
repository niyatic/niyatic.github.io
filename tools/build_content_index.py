#!/usr/bin/env python3
"""Build the faceted content search index for the Hyperbots content hub.

Implements §3 of CONTENT-HUB-IA-PLAN-v3. Walks the repo (stdlib only),
emits library/content-index.json — one record per content piece:
  {title, topic, channel, type, audience, date, status, url, tags}

Harvest sources:
  - _internal/topics/**/*.md  -- YAML front-matter blocks
  - library/videos/index.html -- per-card data-* attributes (channel=video)
  - repos/                    -- SKIPPED by default (see REPOS note below): the
                                 repo holds ~1,650 blog dirs, which would dwarf
                                 the index. Light per-concept harvest is opt-in
                                 via --include-repos (capped).

Robust: skips files without front-matter; never crashes on a malformed block.
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
OUT_PATH = os.path.join(REPO_ROOT, "library", "content-index.json")

# Cap for the optional repos harvest so it can never bloat the index.
REPOS_CAP = 60

FIELDS = ("title", "topic", "channel", "type", "audience", "date", "status",
          "url", "tags")


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


def harvest_repos(records):
    """OPTIONAL/light: one blog record per repo concept, capped.

    Off by default (see REPOS note in the module docstring). Enable with
    --include-repos. Capped at REPOS_CAP to keep the index from bloating.
    """
    if not os.path.isdir(REPOS_DIR):
        return
    count = 0
    for name in sorted(os.listdir(REPOS_DIR)):
        if count >= REPOS_CAP:
            break
        d = os.path.join(REPOS_DIR, name)
        if not os.path.isdir(d):
            continue
        blog = os.path.join(d, "blog.html")
        if not os.path.isfile(blog):
            continue
        records.append({
            "title": name.replace("-", " ").strip(),
            "topic": name,
            "channel": "blog",
            "type": "published",
            "audience": "developer",
            "date": "",
            "status": "published",
            "url": "/repos/{}/blog.html".format(name),
            "tags": [],
        })
        count += 1


def main(argv):
    include_repos = "--include-repos" in argv
    records = []
    harvest_topics(records)
    harvest_videos(records)
    if include_repos:
        harvest_repos(records)

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
    print("Wrote {} ({} records)".format(
        os.path.relpath(OUT_PATH, REPO_ROOT), len(records)))
    print("By channel: {}".format(by_channel))
    if not include_repos:
        print("Note: repos/ harvest skipped (would bloat index with ~1,650 "
              "blogs); pass --include-repos for a capped sample.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
