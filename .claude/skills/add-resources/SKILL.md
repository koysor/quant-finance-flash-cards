---
name: add-resources
description: Find cards missing from resources.json and add curated website and video links
allowed-tools: Read, Edit, Glob, Grep, WebSearch
---

Find flash cards that have no entry in `resources.json` and add learning resources for each.

## Step 1 — Find cards without resources

Read `resources.json` to get all card IDs that already have entries. Glob `cards/**/*.md` to get all card IDs (strip `cards/` prefix and `.md` suffix). The difference is the set of cards needing resources.

If `$ARGUMENTS` is provided, restrict to that topic directory (e.g. `financial-maths`) or a single card ID.

## Step 2 — Generate resources for each missing card

For each card without resources:

1. Read the card's `.md` file to understand the concept, topic, and tags.
2. Identify 2 good **website** sources. Prefer in this order:
   - Investopedia (for finance concepts)
   - Corporate Finance Institute
   - Khan Academy (for maths foundations)
   - Wikipedia (for formal definitions)
   - Paul's Online Math Notes (for calculus/maths)
   - Brilliant.org
3. Identify 2 good **video** sources. Prefer well-known educational channels:
   - Khan Academy YouTube
   - 3Blue1Brown (for maths intuition)
   - StatQuest with Josh Starmer (for statistics/ML)
   - Investopedia YouTube
   - MIT OpenCourseWare
   - The Organic Chemistry Tutor (for maths mechanics)

Only include URLs you are confident exist. Do not guess video URLs — use search if unsure.

## Step 3 — Write to resources.json

Read the full `resources.json`. For each card, insert a new entry under the card ID key, keeping the object sorted alphabetically by key. Each entry must follow this structure:

```json
"topic/card-slug": {
  "websites": [
    { "title": "Source Name — Page Title", "url": "https://..." },
    { "title": "Source Name — Page Title", "url": "https://..." }
  ],
  "videos": [
    { "title": "Channel — Video Title", "url": "https://www.youtube.com/watch?v=..." },
    { "title": "Channel — Video Title", "url": "https://www.youtube.com/watch?v=..." }
  ]
}
```

Preserve 2-space indent and trailing newline. Write back with Edit (or Write if large).

## Step 4 — Report

Print a table of cards processed and the number of resources added per card.
