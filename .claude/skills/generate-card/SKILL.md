---
name: generate-card
description: Generate a new flash card and its edges from a concept name
allowed-tools: Read, Write, Glob, Edit
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

## Step 4 — Summary

Report what was created: the card path, and a table of new edges (source → target, label, description).
