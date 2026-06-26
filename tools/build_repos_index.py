#!/usr/bin/env python3
"""Build repos/index.html — a navigable, language-grouped index of all repo blogs.

Scans repos/*/blog.html, derives a display title and language per slug, groups
slugs by base-concept (slug minus a trailing language suffix), and emits a
branded, filterable index page. Python 3 stdlib only.
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPOS_DIR = os.path.join(ROOT, "repos")
OUT = os.path.join(REPOS_DIR, "index.html")

# Recognized language suffixes (slug suffix -> display language).
# Order: longest/multi-part first so "-zh-hans" wins over "-zh".
LANGS = [
    ("zh-hans", "Chinese (Simplified)"),
    ("zh-hant", "Chinese (Traditional)"),
    ("pt-br", "Portuguese (BR)"),
    ("ar", "Arabic"),
    ("de", "German"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("hi", "Hindi"),
    ("it", "Italian"),
    ("ja", "Japanese"),
    ("ko", "Korean"),
    ("nl", "Dutch"),
    ("pt", "Portuguese"),
    ("ru", "Russian"),
    ("tr", "Turkish"),
    ("pl", "Polish"),
    ("vi", "Vietnamese"),
    ("th", "Thai"),
    ("id", "Indonesian"),
    ("ms", "Malay"),
    ("sv", "Swedish"),
    ("da", "Danish"),
    ("no", "Norwegian"),
    ("fi", "Finnish"),
    ("cs", "Czech"),
    ("el", "Greek"),
    ("he", "Hebrew"),
    ("uk", "Ukrainian"),
    ("ro", "Romanian"),
    ("hu", "Hungarian"),
    ("zh", "Chinese"),
]
LANG_MAP = dict(LANGS)

TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")


def split_lang(slug):
    """Return (base_concept, lang_display). No suffix -> English."""
    for suf, disp in LANGS:
        if slug.endswith("-" + suf):
            return slug[: -(len(suf) + 1)], disp
    return slug, "English"


def clean_text(s):
    s = TAG_RE.sub("", s)
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    # Drop trailing site-name suffix like " · Hyperbots HyperAPI"
    s = re.split(r"\s+[·|]\s+Hyperbots", s)[0].strip()
    return s


def prettify(slug):
    s = slug
    if s.startswith("hyperapi-"):
        s = s[len("hyperapi-"):]
    s = s.replace("-", " ").strip()
    return s[:1].upper() + s[1:] if s else slug


def extract_title(path, base_slug):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            txt = f.read(20000)
    except OSError:
        return None
    for rx in (H1_RE, TITLE_RE):
        m = rx.search(txt)
        if m:
            t = clean_text(m.group(1))
            if t:
                return t
    return None


def main():
    concepts = {}  # base -> {"title":..., "langs": {lang: slug}}
    total = 0
    if not os.path.isdir(REPOS_DIR):
        print("no repos/ dir", file=sys.stderr)
        return 1
    for slug in sorted(os.listdir(REPOS_DIR)):
        d = os.path.join(REPOS_DIR, slug)
        if not os.path.isdir(d):
            continue
        blog = os.path.join(d, "blog.html")
        if not os.path.isfile(blog):
            continue
        total += 1
        base, lang = split_lang(slug)
        title = extract_title(blog, base)
        c = concepts.get(base)
        if c is None:
            c = {"title": None, "langs": {}}
            concepts[base] = c
        # Store one slug per language (first wins).
        c["langs"].setdefault(lang, slug)
        # Prefer the English variant's title for the concept display.
        if title and (c["title"] is None or lang == "English"):
            if c["title"] is None or lang == "English":
                c["title"] = title
        if c["title"] is None:
            c["title"] = prettify(base)

    rows = []
    for base in sorted(concepts):
        c = concepts[base]
        title = c["title"] or prettify(base)
        # Order languages: English first, then alphabetical.
        langs = sorted(c["langs"].items(), key=lambda kv: (kv[0] != "English", kv[0]))
        links = " ".join(
            '<a class="lang" href="/repos/{slug}/blog.html">{lab}</a>'.format(
                slug=html.escape(s, quote=True), lab=html.escape(lang)
            )
            for lang, s in langs
        )
        haystack = html.escape((title + " " + base).lower(), quote=True)
        rows.append(
            '<div class="row" data-s="{hs}">'
            '<div class="t">{title}</div>'
            '<div class="langs">{links}</div>'
            "</div>".format(hs=haystack, title=html.escape(title), links=links)
        )

    n_concepts = len(concepts)
    page = TEMPLATE.format(
        total=total,
        n_concepts=n_concepts,
        rows="\n".join(rows),
    )
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(page)
    print("Wrote {} : {} blogs, {} concepts".format(OUT, total, n_concepts))
    return 0


TEMPLATE = """<!doctype html><html lang="en"><head>
<script src="/gate.js"></script>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Blog index — Hyperbots HyperAPI</title>
<meta name="description" content="Index of every HyperAPI blog, grouped by concept with available languages.">
<style>
:root {{ --brand-7:#1B7DA7; --brand-8:#047495; --brand-9:#07658D; --brand-2:#EDFAFF; --brand-3:#DEEEF5; --brand-4:#BDDFEE; --grey-2:#F6F9F9; --grey-4:#E2ECEE; --grey-10:#748081; --grey-12:#211F26; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ font:14px/1.55 -apple-system,BlinkMacSystemFont,system-ui,"Segoe UI",Roboto,sans-serif; background:var(--grey-2); color:var(--grey-12); max-width:1080px; margin:0 auto; padding:28px 24px 56px; -webkit-font-smoothing:antialiased; }}
.back {{ color:var(--grey-10); font-size:13px; text-decoration:none; display:inline-block; margin-bottom:16px; }}
.back:hover {{ text-decoration:underline; }}
.header {{ display:flex; align-items:center; gap:14px; padding:18px 22px; background:#fff; border:1px solid var(--grey-4); border-radius:12px; border-left:5px solid var(--brand-7); margin-bottom:18px; box-shadow:0 1px 3px rgba(33,31,38,.06); }}
.header img {{ width:36px; height:37px; }}
h1 {{ font-size:22px; color:var(--grey-12); font-weight:600; margin:0; }}
.sub {{ color:var(--grey-10); font-size:13px; margin-top:4px; }}
.controls {{ display:flex; align-items:center; gap:14px; flex-wrap:wrap; margin-bottom:14px; }}
#filter {{ flex:1; min-width:240px; padding:11px 14px; font:14px inherit; border:1px solid var(--brand-4); border-radius:9px; background:#fff; outline:none; }}
#filter:focus {{ border-color:var(--brand-7); box-shadow:0 0 0 3px var(--brand-3); }}
#count {{ font-size:12.5px; color:var(--grey-10); white-space:nowrap; }}
#count b {{ color:var(--brand-7); }}
.list {{ background:#fff; border:1px solid var(--grey-4); border-radius:10px; overflow:hidden; }}
.row {{ padding:12px 18px; border-bottom:1px solid var(--grey-4); }}
.row:last-child {{ border-bottom:0; }}
.row.hidden {{ display:none; }}
.row .t {{ font-weight:600; color:var(--grey-12); font-size:14.5px; margin-bottom:5px; }}
.langs {{ display:flex; flex-wrap:wrap; gap:6px; }}
a.lang {{ font-size:11.5px; padding:2px 9px; background:var(--brand-2); color:var(--brand-9); border:1px solid var(--brand-4); border-radius:11px; text-decoration:none; font-weight:600; }}
a.lang:hover {{ background:var(--brand-7); color:#fff; border-color:var(--brand-7); }}
.empty {{ padding:24px 18px; color:var(--grey-10); font-size:13px; display:none; }}
.footer {{ margin-top:40px; padding-top:14px; border-top:1px solid var(--grey-4); color:var(--grey-10); font-size:12px; }}
.footer a {{ color:var(--brand-7); text-decoration:none; }}
</style></head><body>

<a class="back" href="/">&larr; back to content hub</a>

<header class="header">
  <img src="/assets/hyperbots-logo.svg" alt="Hyperbots"/>
  <div>
    <h1>HyperAPI blog index</h1>
    <div class="sub">{n_concepts} concepts &middot; {total} blogs across all languages</div>
  </div>
</header>

<div class="controls">
  <input id="filter" type="text" placeholder="Filter by topic or keyword&hellip;" autocomplete="off" aria-label="Filter blogs">
  <span id="count"><b id="shown">{n_concepts}</b> of {n_concepts} concepts</span>
</div>

<div class="list" id="list">
{rows}
</div>
<div class="empty" id="empty">No matching concepts.</div>

<div class="footer">
  Generated by <code>tools/build_repos_index.py</code> &middot; {total} blogs indexed &middot;
  <a href="/">content hub</a>
</div>

<script>
(function(){{
  var q=document.getElementById('filter'),
      rows=Array.prototype.slice.call(document.querySelectorAll('#list .row')),
      shown=document.getElementById('shown'),
      empty=document.getElementById('empty');
  function apply(){{
    var v=q.value.toLowerCase().trim(), n=0;
    for(var i=0;i<rows.length;i++){{
      var hit=!v||rows[i].getAttribute('data-s').indexOf(v)!==-1;
      rows[i].classList.toggle('hidden',!hit);
      if(hit)n++;
    }}
    shown.textContent=n;
    empty.style.display=n?'none':'block';
  }}
  q.addEventListener('input',apply);
}})();
</script>
</body></html>"""


if __name__ == "__main__":
    sys.exit(main())
