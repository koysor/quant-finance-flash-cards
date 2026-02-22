---
name: validate-card
description: Validate a flash card's structure, metadata, spelling, and finance relevance
allowed-tools: Read, Grep, Glob
---

Validate the card at the given path (or all cards if no path given). Check each of these strictly:

1. **Structure** — has exactly these sections in order: `# Title`, `**Topic:**`, `**Level:**`, `**Tags:**`, `---`, `## Definition`, `## Key Formula`, `## Example`, `## Remember`
2. **Topic** — value matches a key in `TOPIC_COLOURS` in `app/routes.py` exactly (case-sensitive)
3. **Level** — is `A Level Mathematics` verbatim
4. **Tags** — comma-separated, no empty tags
5. **British English** — flag any American spellings (e.g. "normalized" → "normalised", "color" → "colour", "behavior" → "behaviour", "recognize" → "recognise", "modeling" → "modelling")
6. **LaTeX** — display maths uses `$$...$$`, inline uses `$...$`, no MathJax or image-based maths
7. **Remember section** — must explicitly connect the mathematics to a quantitative finance application, not just summarise the maths
8. **Length** — flag if any section is excessively long (cards should be bite-sized, one concept)

Report results as a checklist with pass/fail for each item. Quote the specific text for any failures.
