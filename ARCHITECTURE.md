# Architecture

## Overview

A Flask web application that reads Markdown flash cards from the filesystem, stores them in a SQLite graph database, and renders them as both a browsable card library and an interactive knowledge graph. The Markdown files in `cards/` are the source of truth; the database is a derived, disposable cache.

```
cards/**/*.md  ──►  SQLite (graph.db)  ──►  Flask  ──►  Browser
  (source)     ↗     (cache + graph)      (server)     (KaTeX + vis.js)
edges.json   ──►
  (source)
```

---

## Layers

### 1. Content layer — `cards/`

Plain Markdown files organised as `cards/<topic>/<slug>.md`. Each file is self-contained: metadata (`**Topic:**`, `**Tags:**`, etc.) is embedded inline using bold-key patterns rather than YAML front-matter. The file path itself encodes the card's permanent ID.

```
cards/derivatives/black-scholes-equation.md
       └─ topic ─┘ └──────── slug ────────┘
```

Card ID: `derivatives/black-scholes-equation` (strip `cards/` prefix and `.md` suffix).

### 2. Loader — `app/loader.py`

Runs once at startup. Scans `cards/**/*.md` with `Path.rglob`, skips any file whose `st_mtime` matches what is stored in the database (incremental reload), and parses changed files with regex:

```
TITLE_RE  ^#\s+(.+)$
TOPIC_RE  ^\*\*Topic:\*\*\s*(.+)$
LEVEL_RE  ^\*\*Level:\*\*\s*(.+)$
TAGS_RE   ^\*\*Tags:\*\*\s*(.+)$
```

`markdown-it-py` renders the full Markdown body to HTML (leaving `$...$` and `$$...$$` delimiters intact for client-side KaTeX). A `ValueError` on any malformed card is intentionally not caught — it aborts startup so broken cards are never silently ignored.

### 3. Database — `app/db.py` + `graph.db`

SQLite with two tables:

```
cards
  id           TEXT PK        "derivatives/black-scholes-equation"
  name         TEXT           "Black-Scholes Equation"
  topic        TEXT           "Derivatives"
  level        TEXT           "A Level Mathematics"
  tags         TEXT           comma-joined: "Black-Scholes,options,PDE,pricing,lognormal"
  html_content TEXT           pre-rendered HTML from markdown-it-py
  file_mtime   REAL           st_mtime used for incremental reload

edges
  source_id    TEXT FK→cards
  target_id    TEXT FK→cards
  label        TEXT           short relationship tag, e.g. "derived via"
  description  TEXT           plain-English explanation of why the cards are linked
  created_at   TEXT           datetime('now')
  PK (source_id, target_id)  — duplicate edges silently ignored via INSERT OR IGNORE
```

`ON DELETE CASCADE` on both edge FK columns means deleting a card automatically removes its edges. Foreign keys are enabled per-connection via `PRAGMA foreign_keys = ON`.

Every function opens its own connection via `get_db()` and closes it at the end of a `with` block. There is no connection pool; this is fine for a single-process dev server.

### 4. Application factory — `app/__init__.py`

`create_app()` wires everything together:

```python
init_db()                # idempotent DDL — safe to call every restart
load_all_cards()         # mtime-checked upserts + stale card removal
load_edges_from_file()   # clears edges table, repopulates from edges.json
app.register_blueprint(bp)
# context_processor → injects topic_colour(), search_data_json, site_stats, csrf_token
```

The context processor runs on every request and queries `get_all_cards()` + `get_site_stats()`. Given 19 cards and SQLite, this is negligible; if the card count grows substantially, results should be cached.

### 5. Routes — `app/routes.py`

Single Flask Blueprint `main`. The remove-link mutation route is POST-only and redirects back to the card detail page (Post/Redirect/Get pattern).

```
GET  /                          index()        — groups cards by topic, ?tag= and ?topic= filtering
GET  /tag/<tag>                 tag_page()     — dedicated page for a single tag
GET  /card/<path:card_id>       card_detail()  — prerequisites, content, see-also, prev/next nav
POST /card/<path:card_id>/remove-link  remove_link() — deletes edge (CSRF), 302 redirect
GET  /graph                     graph_view()   — vis.js with path finding, topic filter, edge weights
GET  /random                    random_card()  — redirects to a random card
```

`<path:card_id>` is Flask's path converter, which allows `/` within the parameter — required because card IDs contain a topic segment (e.g. `derivatives/black-scholes-equation`).

`TOPIC_COLOURS` (dict, top of `routes.py`) is the single source of truth for all topic colour identity. It flows into:
- graph node colours (server-side JSON)
- `--tc` CSS custom property (set inline on card tiles, card content panel, badge)
- context processor → `topic_colour()` callable available in every template

### 6. Templates — `app/templates/`

```
base.html     Shared layout: fonts, KaTeX CDN, scroll bar, search overlay,
              keyboard shortcuts modal, theme toggle, mobile nav, back-to-top
index.html    Card grid grouped by topic, tag filter strip, stats bar, visited state
tag.html      Dedicated tag page showing all cards for a given tag
card.html     Breadcrumb, prerequisites, card content, see-also, prev/next nav, sidebar
graph.html    vis.js Network, path finding, topic filter, edge weights, theme-aware
404.html      Branded error page
```

`base.html` embeds all card metadata as `ALL_CARDS` JSON (from the context processor's `search_data_json`) so the Spotlight-style search overlay works entirely client-side with no additional requests.

### 7. Frontend — `app/static/`

```
style.css     ~1100 lines — design tokens as CSS custom properties, dark/light themes
              via [data-theme] attribute, per-topic --tc custom property, View Transitions
favicon.svg   SVG monitor icon
```

No build step. All third-party JS/CSS is CDN:

| Library | Version | Purpose |
|---|---|---|
| KaTeX | 0.16.9 | Client-side maths rendering — auto-render scans `$...$` and `$$...$$` |
| vis-network | 9.1.9 | Interactive force-directed graph |
| Google Fonts | — | Sora (display), Inter (body), JetBrains Mono (code) |

---

## Key Design Decisions

**Two committed sources of truth, one disposable cache.** `cards/**/*.md` owns card content; `edges.json` owns relationships (labels + plain-English descriptions). `graph.db` is derived from both and is gitignored — delete it and restart to rebuild completely.

**Card IDs from file paths.** Renaming or moving a card file changes its ID. The cascade delete removes the orphaned edges from the DB, and the next mutation (add/remove link) writes the updated state back to `edges.json`. If you rename a card with important edges, update `edges.json` manually before committing.

**Metadata parsed with regex, not a Markdown parser.** This keeps the format explicit and strict. If `**Topic:**` is missing or misspelt, startup fails loudly rather than inserting a card with empty metadata.

**HTML pre-rendered at load time, not per request.** `html_content` is stored in the database so each request is a simple SQL query + template render. KaTeX maths rendering happens in the browser, keeping the server completely stateless with respect to maths.

**Visited card state is client-only.** Stored in `localStorage` — no server sessions, no user accounts. Clearing browser storage resets progress.

**Theme stored in `localStorage`, applied before paint.** A small inline `<script>` in `<head>` reads `localStorage` and sets `data-theme` on `<html>` before the stylesheet is applied, eliminating the flash-of-unstyled-content on reload.

---

## Startup Sequence

```
uv run python run.py
  └─ create_app()
       ├─ init_db()              CREATE TABLE IF NOT EXISTS … (no-op if already exists)
       ├─ load_all_cards()       rglob cards/**/*.md → mtime check → upsert changed
       │                         also removes stale cards whose files no longer exist
       ├─ load_edges_from_file() clears edges table, repopulates from edges.json
       ├─ register_blueprint(bp)
       └─ attach context_processor (CSRF token, topic_colour, search data, stats)
  └─ app.run(debug=True)        reloader active — file changes restart the server
                                 card changes are picked up on next restart
```

The Flask debug reloader watches Python files. **It does not watch `cards/*.md`** — editing a card file requires a manual server restart (or saving any `.py` file to trigger the reloader).

---

## Adding Things

**New card:** create `cards/<topic>/<slug>.md`, restart the server. No other changes needed if the topic already exists.

**New topic:** create the directory, add a card, add an entry to `TOPIC_COLOURS` in `app/routes.py`, restart. The colour cascades automatically to all UI elements.

**New edge:** add an entry to `edges.json` and restart the server. Each entry has `source`, `target`, `label`, and `description` fields. The remove-link form on the card detail page can delete edges at runtime (and writes the change back to `edges.json`).

**New route:** add a handler to `app/routes.py` and a template to `app/templates/`. The context processor variables (`topic_colour`, `search_data_json`, `site_stats`) are available in all templates automatically.
