---
name: find-duplicates
description: Find flash cards with significant concept overlap and suggest merges or differentiations
allowed-tools: Read, Glob, Grep
---

Scan the card library for cards that may cover overlapping concepts.

## Step 1 — Build a card index

Glob `cards/**/*.md`. For each card read:
- `# Title` — the concept name
- `**Topic:**` — topic
- `**Tags:**` — tag list
- First sentence of `## Definition` — the concept's core meaning

## Step 2 — Detect overlap candidates

Apply these heuristics to find likely overlaps:

**Title similarity** — pairs of cards whose titles share 2+ significant words (ignoring stop words like "and", "of", "the", "a"). Flag these automatically.

**Tag overlap** — pairs of cards (within the same topic) that share 4 or more tags. High tag overlap in the same topic strongly suggests conceptual duplication.

**Definition overlap** — for title-similar or high-tag-overlap pairs, read both Definitions in full and judge: do they explain the same concept, or genuinely distinct (but related) concepts?

## Step 3 — Classify each pair

For each flagged pair, classify as one of:
- **Likely duplicate** — same concept explained twice; recommend merging or deleting one
- **Partial overlap** — related but distinct; recommend adding a differentiating sentence to each Definition and an edge connecting them
- **False positive** — genuinely different concepts that happen to share words/tags

## Step 4 — Report

For each flagged pair:
```
card-id-1  ←→  card-id-2
Classification: Likely duplicate / Partial overlap / False positive
Reason: <one sentence>
Recommendation: <merge | add edge + clarify | no action>
```

Group by classification. Only report Likely duplicate and Partial overlap pairs — omit false positives.

Offer to create edges for Partial overlap pairs, or to open the cards for manual review.
