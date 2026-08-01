---
name: bulk-validate
description: Run validate-card checks across all cards or a topic directory and report a summary
allowed-tools: Read, Glob, Grep
---

Validate flash cards in bulk and produce a summary report.

Target: $ARGUMENTS (topic directory name like `financial-maths`, or omit to check all cards)

## Step 1 — Select cards

If a topic is given (e.g. `financial-maths`), glob `cards/<topic>/*.md`. Otherwise glob `cards/**/*.md`.

## Step 2 — Check each card

For each card, run these checks:

1. **Structure** — has `# Title`, `**Topic:**`, `**Tags:**`, `**Created:**`, `**Author:**`, `---`, `## Definition`, `## Key Formula`, `## Example`, `## Remember` in the correct order. Note: `**Level:**` is not a recognised field — flag if present.
2. **Topic** — value exactly matches a key in `TOPIC_COLOURS` in `app/routes.py`
3. **Tags** — comma-separated, 3–6 tags, all lowercase, no empty tags
4. **British English** — flag American spellings: normalized/normalised, color/colour, behavior/behaviour, recognize/recognise, modeling/modelling, center/centre, analyze/analyse
5. **LaTeX** — display maths uses `$$...$$`, inline uses `$...$`; flag `\(...\)`, `\[...\]`, or image-based maths
6. **Remember section** — must connect maths to a quantitative finance application, not just summarise the maths. Flag if it contains no finance-specific term (e.g. no mention of portfolio, hedge, risk, pricing, trader, market, strategy, position)
7. **Length** — flag if any single section exceeds 150 words (cards should be bite-sized)

## Step 3 — Produce report

Summarise results as:

```
Checked N cards — P passed, F had issues

Issues found:
  card-id
    ✗ Check name: specific problem text
  card-id
    ✗ Check name: specific problem text
```

If all cards pass, say so clearly. Do not list passing cards individually — only flag failures.

At the end, offer to fix any of the flagged issues.
