# `_internal/` — Content-ops pipeline (by Hyperbots)

This is the **content-ops / pipeline** section of the Hyperbots content hub. It is the
team's working tree: where every piece of content is conceived, drafted, reviewed, and
scheduled **before** it graduates to the published `library/`. It is gated (soft-gate via
`/gate.js`) and internal-facing.

Owned by: **Content ops**. Other teams own `research/`, `library/` (incl. `library/videos/`),
`abm/`, and the root index — do not edit those from here.

> Note: this repo ships `.nojekyll`, so an underscore-prefixed directory like `_internal/`
> **is** served (Jekyll's `_`-skip does not apply). Every `.html` here therefore carries the
> gate.

---

## The topic model (one line)

A **topic** is the unit of work. Each topic spawns up to **7 channel pieces**:

> **blog · post (linkedin) · tweet · huggingface · hackernews · video · reddit**

Pieces are *drafted* in `_internal/` (daily), *scheduled* via the weekly plan, and
*graduate* to `library/` when published. A topic lives as a folder:

```
_internal/topics/<topic-slug>/
  topic.md          ← brief + per-channel status board (the 7 channels & their state)
  blog.md
  linkedin.md       ← "post"
  tweet.md
  huggingface.md    ← HF strategy (model/dataset-card angle)
  hackernews.md     ← HN title + Show-HN / comment angle
  video.md          ← script + link to the rendered video in library/videos/
  reddit.md         ← subreddit targets + compliant comment/post
```

Every channel file carries the front-matter schema (below). A topic that does not use a
channel marks it `status: n/a` — so the 7-slot grid is always visible and gaps are obvious.

Copy `topics/_TEMPLATE/` to start a new topic.

---

## Lifecycle (status flows; location follows status)

```
idea → drafting → review → approved → scheduled → published
```

- Lifecycle is tracked by the `status:` field — **never** by `-DRAFT` filename suffixes.
- On **published**, the piece graduates: published blogs/posts/videos surface in `library/`
  (and the search index); the draft stays in `_internal/topics/` as the source of record.
- `daily-drafts/` is a **view** over topics whose channels are in `drafting`/`review`.
- `weekly-plan/` is the publishing queue: which topic ships on which channel on which day.

---

## Metadata front-matter schema

Every content `.md` gets this YAML block at the top (authored once per file — it powers the
status boards, the daily/weekly views, and the future search index). Schema is copied
verbatim from the Content Hub Master Plan v3 §4:

```yaml
---
title: "…"
topic: parse-intent-edge        # the topic-slug it belongs to
channel: blog                   # blog|linkedin|tweet|huggingface|hackernews|video|reddit
type: published                 # draft|published|strategy|asset
audience: marketing             # research|marketing|sales|developer|cfo
date: 2026-06-16
status: published               # idea|drafting|review|approved|scheduled|published
tags: [savior-bench, ocr, honest-benchmark]
---
```

---

## Brand & accuracy guardrails

- All content is **by Hyperbots**. No competitor / vendor product names in product framing;
  foundation-model names appear only as labeled benchmark baselines (the scientific artifact).
- Product accuracy is referenced only "per apis.hyperbots.com." No fabricated GAAP/IFRS cites,
  customer names, or benchmark numbers.
- Open-source framing: "open-source fine-tuned by Hyperbots (Hyperbots IP)" — never claim
  closed-source ownership of open weights.

---

## Directory map

```
_internal/
  README.md                 ← this file
  topics/
    index.html              ← gated topic list + client-side filter
    _TEMPLATE/              ← copyable 7-channel skeleton
    parse-intent-edge/      ← migrated worked example (C-01)
    bank-statement-extract/ ← migrated worked example (BFSI)
  weekly-plan/
    index.html              ← gated list of weeks
    _TEMPLATE-week.md
    2026-W25.md             ← current week
  daily-drafts/
    index.html              ← gated "today + recent" view over drafting/review
    README.md
```
