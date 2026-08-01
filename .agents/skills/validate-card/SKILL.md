---
name: validate-card
description: Validate a flash card's structure, metadata, spelling, and finance relevance
allowed-tools: Read, Grep, Glob
---

Validate the card at the given path (or all cards if no path given). Check each of these strictly:

1. **Structure** — has exactly these sections in order: `# Title`, `**Topic:**`, `**Tags:**`, `---`, `## Definition`, `## Key Formula`, `## Example`, `## Remember`. Note: `**Level:**` is **not** a recognised metadata field — flag if present.
2. **Topic** — value matches a key in `TOPIC_COLOURS` in `app/routes.py` exactly (case-sensitive)
3. **Tags** — comma-separated, no empty tags
4. **British English** — flag any American spellings (e.g. "normalized" → "normalised", "color" → "colour", "behavior" → "behaviour", "recognize" → "recognise", "modeling" → "modelling")
5. **LaTeX** — display maths uses `$$...$$`, inline uses `$...$`, no MathJax or image-based maths. Additionally check for patterns that break KaTeX rendering:
   - **Bare `|` in table cells:** any `$...|...$` on a line starting with `|` where the `|` inside the formula is not `\lvert`, `\rvert`, `\vert`, `\mid`, `\middle\vert`, or `\|`. Absolute value must use `\lvert...\rvert`; conditional expectation bars must use `\middle\vert`.
   - **`\begin{...}` in table cells:** any `\begin{` inside inline `$...$` on a table row — the `\\` line-break is processed as an escaped backslash by Markdown. Move to a `$$...$$` display block outside the table.
   - **Bare `$` currency in prose:** any unescaped `$` followed by a number or currency amount (e.g. `$6 bn`, `$4.58`) in prose text, especially when other `$...$` LaTeX appears later in the same card. Must be escaped as `\$`.
6. **Remember section** — must explicitly connect the mathematics to a quantitative finance application, not just summarise the maths
7. **Length** — flag if any section is excessively long (cards should be bite-sized, one concept)

Report results as a checklist with pass/fail for each item. Quote the specific text for any failures.
