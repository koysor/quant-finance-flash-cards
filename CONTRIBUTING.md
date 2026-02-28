# Contributing

## Adding a flash card

Create a single `.md` file in `cards/<topic>/`. The filename becomes part of the card's permanent ID, so use a short lowercase hyphenated slug (e.g. `black-scholes-equation.md`).

### Required format

Every card must contain all four metadata fields and all four sections, in this exact order:

```markdown
# Concept Name

**Topic:** Derivatives
**Tags:** tag1, tag2, tag3
**Author:** <Your Name or AI model>

---

## Definition

## Key Formula

## Example

## Remember
```

### Metadata rules

**`**Topic:**`** must exactly match one of the keys in `TOPIC_COLOURS` in `app/routes.py`:

| Value | Colour |
|---|---|
| `Calculus` | amber |
| `Derivatives` | blue |
| `Financial Mathematics` | emerald |
| `Linear Algebra` | violet |
| `Probability` | rose |
| `Risk` | red |
| `Statistics` | cyan |
| `Stochastic Processes` | indigo |

A typo here will create a new topic with the default grey colour. To add a genuinely new topic, add an entry to `TOPIC_COLOURS` in `app/routes.py` at the same time.

**`**Tags:**`** is a comma-separated list of lowercase tags used for filtering, e.g. `options, Greeks, delta, gamma`. Tags appear in the filter strip on the index page.

### Section content rules

**Accessibility** — while the subject matter can be advanced, the explanation should remain accessible to a student of A Level mathematics age. Avoid unnecessary jargon and explain technical terms where possible.

**Definition** — one or two sentences. State precisely what the concept is.

**Key Formula** — the central equation(s), using LaTeX delimiters:
- Display maths: `$$...$$` on its own line
- Inline maths: `$...$`

These are passed through to KaTeX in the browser — do not use MathJax or image-based maths.

**Example** — a short worked numerical example. Prefer concrete numbers over abstract symbols.

**Remember** — the key insight. This section must explicitly connect the mathematics to a quantitative finance application. Do not leave it as a pure maths summary.

### Language

Use **British English** throughout: *normalised*, *behaviour*, *recognise*, *colour*, *modelled*, *practise* (verb).

### Tone and length

Cards are intentionally bite-sized — one concept per card, no padding. If you find yourself writing more than a screen's worth of content, split into two cards.

---

## Adding concept relationships

Edit `edges.json` in the project root and restart the server. Each entry is a JSON object with four fields:

```json
{
  "source": "probability/normal-distribution",
  "target": "risk/value-at-risk",
  "label": "used in",
  "description": "The normal distribution underpins the parametric VaR calculation."
}
```

- **`source`** / **`target`** — card IDs (file path minus `cards/` prefix and `.md` suffix)
- **`label`** — short relationship tag, e.g. *derived via*, *used in*, *parameterised by*
- **`description`** — plain-English sentence explaining why the cards are linked; shown in the "See Also" section on the card detail page

Edges can be removed at runtime via the card detail page sidebar, which writes the change back to `edges.json`.

---

## Adding a new topic

1. Create the directory: `cards/<new-topic>/`
2. Add at least one card
3. Add an entry to `TOPIC_COLOURS` in `app/routes.py`:
   ```python
   "New Topic": "#hexcolour",
   ```
4. Restart the server

The colour cascades automatically to card tiles, the graph, content headings, and badges.

---

## Verifying your changes

There are no automated tests. Start the server and check:

```bash
uv run python run.py
```

1. Your card appears on the index page under the correct topic
2. The card detail page renders correctly, including maths
3. `http://127.0.0.1:5000/graph` shows the card as a node
