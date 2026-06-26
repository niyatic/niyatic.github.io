# `daily-drafts/` — today + recent (a view, not a copy)

This is **not** a separate store of content. It is a **view** over the channel files in
`_internal/topics/*/` whose `status:` is `drafting` or `review` — surfaced by day so the team
can see what is actively in flight today and who owns it.

- The source of record stays in `topics/<slug>/<channel>.md`. Nothing is duplicated here.
- `index.html` shows "today + recent days," reading the `status:` and `date:` front-matter.
- When a piece moves to `approved`/`scheduled`, it leaves this view; when `published`, it
  graduates to `library/`.

To populate the live view at scale, the future `tools/build_content_index.py` walk feeds the
same front-matter that powers the search index. For now `index.html` lists the currently
in-flight pieces statically.

By Hyperbots. Product accuracy per apis.hyperbots.com.
