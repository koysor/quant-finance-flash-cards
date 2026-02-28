---
name: generate-card
description: Generate a new flash card and its edges from a concept name
allowed-tools: Read, Write, Glob, Edit, Bash
---

Generate a flash card for the concept: $ARGUMENTS

## Step 1 — Determine topic and check for duplicates

Read `app/routes.py` to get the current `TOPIC_COLOURS` keys. Pick the most appropriate topic. Glob `cards/**/*.md` to check no existing card already covers this concept.

## Step 2 — Write the card

Write the card to `cards/<topic-slug>/<concept-slug>.md` using this exact structure:

```
# Concept Name

**Topic:** <must exactly match a TOPIC_COLOURS key>
**Level:** A Level Mathematics
**Tags:** <3-6 lowercase comma-separated tags relevant to quant finance>
**Created:** <today's date in YYYY-MM-DD>
**Author:** <model name, e.g. Claude Opus 4.6>

---

## Definition

<One or two sentences. State precisely what the concept is.>

## Key Formula

<Central equation(s) using $$...$$ for display maths and $...$ for inline.>

## Example

<Short worked numerical example with concrete numbers, not abstract symbols.>

## Remember

<Key insight connecting the mathematics to a specific quantitative finance application. This must not be a pure maths summary.>
```

Rules:
- British English throughout (normalised, behaviour, colour, recognise, modelled)
- One concept per card, no padding
- Pitched at A Level mathematics standard — accessible but rigorous
- The Remember section is the most important: it must make a concrete finance connection

## Step 3 — Generate edges

Read `edges.json` and scan the existing cards (glob `cards/**/*.md`, read their `# Title` and `**Tags:**` lines) to find 2-4 cards that are conceptually related to the new card.

For each related card, create a directed edge (pick whichever direction makes more sense — the new card can be source or target). Each edge needs:
- **`source`** / **`target`** — card IDs (e.g. `derivatives/black-scholes-equation`)
- **`label`** — short relationship tag (2-3 words), e.g. *derived via*, *used in*, *parameterised by*, *extends*, *constrains*, *feeds into*
- **`description`** — one plain-English sentence explaining *why* these concepts are linked in quantitative finance. Match the quality and specificity of existing descriptions in `edges.json`.

Append the new edges to `edges.json`, keeping the array sorted by `source_id` then `target_id`. Preserve the existing formatting (2-space indent, trailing newline).

## Step 4 — Generate learning resources

Read `resources.json`. Add an entry for the new card with:
- **`websites`** — 2 objects, each with `title` and `url`. Use well-known, beginner-friendly sources (Khan Academy, Investopedia, Wikipedia, Brilliant, Paul's Online Math Notes, Corporate Finance Institute, etc.).
- **`videos`** — 2 objects, each with `title` and `url`. Use well-known educational YouTube channels (3Blue1Brown, Khan Academy, StatQuest, The Organic Chemistry Tutor, MIT OpenCourseWare, etc.). Only use URLs you are confident exist.

Write the updated `resources.json` back, keeping the object sorted by card ID. Preserve 2-space indent formatting and trailing newline.

## Step 5 — Restart the app

Delete `graph.db` and restart the Flask dev server so the new card and edges are loaded:

```bash
pkill -f "python run.py" 2>/dev/null; rm -f graph.db; uv run python run.py &
```

Wait a couple of seconds, then verify the server is running by curling the new card's URL.

## Step 6 — Summary

Report what was created: the card path, and a table of new edges (source → target, label, description).

## Step 7 — Suggest related cards

Suggest 3-5 related concepts that would make good future flash cards. These should be concepts that:
- Are closely related to the newly created card
- Do **not** already exist in `cards/**/*.md`
- Are relevant to quantitative finance at A Level mathematics standard

Present them as a bulleted list with a one-line description of each, e.g.:

> **Suggested next cards:**
> - **Concept Name** — brief description of what the card would cover and why it connects
