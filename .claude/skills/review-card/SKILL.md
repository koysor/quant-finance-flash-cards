---
name: review-card
description: Review an existing card for content quality and suggest or apply targeted improvements
allowed-tools: Read, Edit, Glob
---

Review and improve the card at: $ARGUMENTS

This skill is about **content quality**, not structural conformance (use `validate-card` for that).

## Step 1 — Read the card

Read the full `.md` file. Also read a few related cards (find them via `edges.json`) to understand the topic context and the standard of nearby cards.

## Step 2 — Assess quality

Evaluate each section against these standards:

**Definition**
- Is it precise enough to distinguish this concept from similar ones?
- Does it avoid vague phrases like "is a method used to" or "is an important concept in"?
- Is it one or two sentences maximum?

**Key Formula**
- Is the central equation clearly presented with `$$...$$`?
- Are all variables defined inline (either in the formula block or immediately after)?
- Is the formula the *most important* one for this concept, not a secondary result?

**Example**
- Does it use concrete numbers, not just abstract symbols?
- Is the worked example complete enough to follow without prior knowledge?
- Does it match the formula shown?

**Remember**
- Does it name a specific quantitative finance use case (not just "used in finance")?
- Does it give the reader a mental hook — a reason *why* this matters in practice?
- Is it distinct from just restating the Definition?

## Step 3 — Propose improvements

For each section that falls short, write an improved version. Clearly show:
```
CURRENT:
<original text>

SUGGESTED:
<improved text>

REASON: <one sentence explaining what was weak>
```

If a section is already strong, say so and skip it.

## Step 4 — Apply changes

Ask the user which improvements to apply. Apply only the approved ones using Edit, preserving all other content exactly.

Maintain British English throughout. Do not change the card's structure, metadata, or LaTeX delimiters.
