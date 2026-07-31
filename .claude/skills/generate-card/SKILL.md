---
name: generate-card
description: Generate a new flash card and its edges from a concept name
allowed-tools: Read, Write, Glob, Edit, Bash, WebFetch, WebSearch
---

Generate a flash card for the concept: $ARGUMENTS

## Step 1 — Determine topic and check for duplicates

Read `app/routes.py` to get the current `TOPIC_COLOURS` keys. Pick the most appropriate topic. Glob `cards/**/*.md` to check no existing card already covers this concept.

## Step 2 — Write the card

Write the card to `cards/<topic-slug>/<concept-slug>.md` using this exact structure:

```
# Concept Name

**Topic:** <must exactly match a TOPIC_COLOURS key>
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

## Step 5 — Validate resource URLs

Run the URL validator against only the new card's resources to catch broken links before they enter the repository:

```bash
uv run python scripts/validate_urls.py --force
```

If any URLs fail validation:
1. Remove the broken entry from `resources.json`
2. Search the web for a working replacement from the same source category (well-known educational sites for websites, established YouTube channels for videos)
3. Add the replacement URL and re-run the validator
4. Repeat until all URLs pass

Do **not** proceed to the next step until validation passes with zero failures.

## Step 6 — Restart the app

Delete `graph.db` and restart the Flask dev server so the new card and edges are loaded.

`FLASK_DEBUG=1` is **required**: `create_app()` raises `RuntimeError` unless either `SECRET_KEY` is set in the environment or debug mode is on. Without it the server dies immediately, and because it is backgrounded the failure is silent — a stale `app.log` or an already-running instance can make it look as though the restart succeeded.

```bash
lsof -ti tcp:5000 | xargs -r kill 2>/dev/null
rm -f graph.db app.log
FLASK_DEBUG=1 uv run python run.py > app.log 2>&1 &
```

Stop the old server **by port, not by `pkill -f`**. Any `pkill -f` pattern that matches `run.py` also matches the shell executing this block — the launch line two rows down contains that literal string in its own command line — so `pkill` kills the caller and the whole restart aborts with exit code 144 before the server is ever started. Bracket tricks like `[r]un\.py` do not help, because it is the *launch* line being matched, not the pattern.

Then confirm the server actually came up before reporting success. Poll rather than using a fixed `sleep` — startup rebuilds `graph.db` by parsing every card, which takes well over ten seconds once the collection is large, so a short fixed wait reports a false failure on a healthy server:

```bash
for i in $(seq 1 30); do
  code=$(curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:5000/card/<new-card-id>")
  [ "$code" = "200" ] && break
  sleep 2
done
if [ "$code" != "200" ]; then echo "FAILED ($code)"; tail -30 app.log; else echo "OK"; fi
```

A genuine `FAILED` means the loader rejected something: a malformed card, a `**Topic:**` that is not a `TOPIC_COLOURS` key, or a card ID in `edges.json` that does not exist. The traceback in `app.log` names the offending file. Fix it and repeat until the card returns 200 — do **not** report the card as created while this check is failing.

If the tool you use to background the server terminates it when the call returns, launch it as a background task instead of with `&`, then poll with the same `curl` check.

## Step 7 — Summary

Report what was created: the card path, and a table of new edges (source → target, label, description).

## Step 8 — Suggest related cards

Suggest 3-5 related concepts that would make good future flash cards. These should be concepts that:
- Are closely related to the newly created card
- Do **not** already exist in `cards/**/*.md`
- Are relevant to quantitative finance at A Level mathematics standard

Present them as a bulleted list with a one-line description of each, e.g.:

> **Suggested next cards:**
> - **Concept Name** — brief description of what the card would cover and why it connects
