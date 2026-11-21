# Architecture

## Overview

A Flask application that reads Markdown flash cards from the filesystem, stores them in a SQLite graph database, and renders them as both a browsable card library and an interactive knowledge graph. The Markdown files in `cards/` are the source of truth; the database is a derived, disposable cache.

Locally the Flask development server serves the pages. In production nothing runs on the server: the same Flask app renders every page to static HTML at deploy time, and Caddy serves the files (see [Deployment](#deployment)).

```
cards/**/*.md  ──►  SQLite (graph.db)  ──►  Flask ──► Browser (KaTeX + vis.js)     local
  (source)     ↗     (cache + graph)          │
edges.json   ──►                              └──► static_site.py ──► dist/ ──► Caddy ──► Browser   production
notation.json ──►
key-terms.json ──►
resources.json ──►
  (sources)
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
TITLE_RE    ^#\s+(.+)$
TOPIC_RE    ^\*\*Topic:\*\*\s*(.+)$                        required; must be a TOPIC_COLOURS key
TAGS_RE     ^\*\*Tags:\*\*\s*(.+)$                         required
CREATED_RE  ^\*\*Created:\*\*\s*(\d{4}-\d{2}-\d{2})\s*$    optional; falls back to the file mtime
AUTHOR_RE   ^\*\*Author:\*\*\s*(.+)$                       optional; "Unknown" when missing
```

`markdown-it-py` renders the full Markdown body to HTML (leaving `$...$` and `$$...$$` delimiters intact for client-side KaTeX). The loader also records which `notation.json` symbols and `key-terms.json` variables each card's maths uses. A `ValueError` on a malformed card or an unknown topic is intentionally not caught — it aborts startup so broken cards are never silently ignored.

### 3. Database — `app/db.py` + `graph.db`

SQLite with three tables:

```
cards
  id           TEXT PK        "derivatives/black-scholes-equation"
  name         TEXT           "Black-Scholes Equation"
  topic        TEXT           "Derivatives"
  tags         TEXT           comma-joined: "Black-Scholes,options,PDE,pricing,lognormal"
  html_content TEXT           pre-rendered HTML from markdown-it-py
  created_date TEXT           "YYYY-MM-DD 00:00:00" from **Created:**, else the file mtime
  author       TEXT           "Claude Sonnet 4.6" or "Unknown"
  notation     TEXT           JSON list of LaTeX symbol entries used in this card
  key_terms    TEXT           JSON list of plain-text variable entries used in this card
  file_mtime   REAL           st_mtime used for incremental reload

edges
  id          INTEGER PK AUTOINCREMENT
  source_id   TEXT FK→cards
  target_id   TEXT FK→cards
  label       TEXT           short relationship tag, e.g. "derived via"
  description TEXT           plain-English explanation of why the cards are linked
  created_at  TEXT           datetime('now')

meta
  key         TEXT PK        "edge_file_mtime"
  value       TEXT           edges.json mtime, so an unchanged file is not reloaded
```

`ON DELETE CASCADE` on both edge FK columns means deleting a card automatically removes its edges. When `edges.json` is reloaded, entries whose source or target card does not exist are skipped with a warning. Foreign keys are enabled per writable connection via `PRAGMA foreign_keys = ON`.

Functions get their connection from `get_db()`. Inside a request it is one connection per request, stored on `g` and closed at teardown. It is read-only (`mode=ro`, no PRAGMAs) unless edge editing is on, since nothing else writes after startup. During the startup load every call shares one `bulk_connection()` transaction, which takes precedence even if another app's request context is active. There is no connection pool: opening a read-only connection costs under 1 ms. Foreign keys only matter for writes, so `PRAGMA foreign_keys = ON` is set on writable connections only.

### 4. Application factory — `app/__init__.py`

`create_app()` wires everything together:

```python
init_db()  # idempotent DDL — safe to call every restart
# load notation.json  → app.config["NOTATION"]   (LaTeX symbol definitions)
# load key-terms.json → app.config["KEY_TERMS"]  (plain variable definitions)
load_all_cards(
    notation_dict, key_terms_dict
)  # mtime-checked upserts + stale card removal
load_edges_from_file()  # if edges.json changed: clear edges table, repopulate
# load resources.json → app.config["RESOURCES"]  (per-card website/video links)
app.register_blueprint(bp)
# context_processor → injects topic_colour(), topic_slug(), TOPIC_COLOURS, site_stats,
#                     csrf_token, edge_edit_enabled, static_build
# url_defaults      → ?v= content hash on static URLs
```

The context processor runs on every page render; `get_site_stats()` is memoised in a module-level dict, so it costs one SQLite query per process. The CSRF token is only created in edge-edit mode, so ordinary pages never touch the session or set a cookie.

### 5. Routes — `app/routes.py`

Single Flask Blueprint `main`. The remove-link mutation route is POST-only and redirects back to the card detail page (Post/Redirect/Get pattern).

```
GET  /                          index()        — groups cards by topic; ?tag= and ?topic= filtering
GET  /topic/<slug>              topic_page()   — the grid for one topic (same page as ?topic=)
GET  /tag/<path:tag>            tag_page()     — dedicated page for a single tag
GET  /card/<path:card_id>       card_detail()  — prerequisites, content, see-also, prev/next nav
                                                 slug-based redirect/disambiguation if not found verbatim
POST /card/<path:card_id>/remove-link  remove_link() — deletes edge (CSRF), 302 redirect; edit mode only
GET  /path/<path:card_id>       study_path()   — nearest prerequisites (2 levels, at most 30) in learning order
GET  /formulas                  formulas()     — all Key Formula sections aggregated by topic
GET  /quiz                      quiz()         — topic list; ?topic= shows that topic's quiz
GET  /quiz/<slug>               quiz_topic()   — one topic's quiz (same page as ?topic=)
GET  /graph                     graph_view()   — vis.js with path finding, topic filter, edge weights
GET  /recent                    recent()       — newest first by created date; ?start= / ?end=; JSON with ?format=json
GET  /search-data.json          search_data_json_view() — card index for the search overlay
GET  /random                    random_card()  — redirects to a random card
GET  /barbie                    barbie_theme() — sets the theme cookie (easter egg)
```

`<path:...>` is Flask's path converter, which allows `/` within the parameter. Card IDs need it because they contain a topic segment (e.g. `derivatives/black-scholes-equation`). Tags need it too, because some contain a slash (`30/360`, `dy/dx`).

Topic slugs come from `topic_slug()` (`Portfolio Theory & Asset Pricing` → `portfolio-theory-asset-pricing`), and `TOPIC_BY_SLUG` maps them back. Templates link to the path routes rather than `?topic=`, because the static build cannot store a page per query string. With `STATIC_BUILD` set, `/random` and `/barbie` render pages that do their work in the browser instead of redirecting.

`TOPIC_COLOURS` (dict, top of `routes.py`) is the single source of truth for all topic colour identity. It flows into:
- graph node colours (server-side JSON)
- `--tc` CSS custom property (set inline on card tiles, card content panel, badge)
- context processor → `topic_colour()` callable available in every template

### 6. Templates — `app/templates/`

```
base.html         Shared layout: fonts, KaTeX CDN, scroll bar, search overlay,
                  keyboard shortcuts modal, theme/wide-mode toggle, mobile nav, back-to-top
index.html        Card grid grouped by topic (also /topic/<slug>), tag filter strip, stats bar, visited state
tag.html          Dedicated tag page showing all cards for a given tag
quiz.html         Topic list, or one topic's cards with reveal and known/unknown marks (localStorage)
path.html         Study path: prerequisites in learning order
recent.html       Cards newest first; the static build adds a browser-side ?start= / ?end= filter
card.html         Breadcrumb, prerequisites, card content, see-also, prev/next nav,
                  sidebar (notation, key terms, resources)
formulas.html     All Key Formula sections grouped by topic
graph.html        vis.js Network, path finding, topic filter, edge weights, theme-aware
disambiguate.html Disambiguation page shown when multiple cards share a slug
404.html          Branded error page; its script resolves /card/<slug> from the search data
random.html       Static-build stand-in for /random: picks a card in the browser
barbie.html       Static-build stand-in for /barbie: sets the theme cookie in the browser
_legacy_query.html Static-build script sending old ?tag= / ?topic= URLs to the path pages
```

The Spotlight-style search overlay fetches all card metadata once from `/search-data.json` and then searches entirely client-side.

### 7. Frontend — `app/static/`

```
style.css     ~1650 lines — design tokens as CSS custom properties, dark/light/barbie themes
              via [data-theme] attribute, wide mode via [data-wide] attribute,
              per-topic --tc custom property
favicon.svg   SVG monitor icon
```

No frontend build step. All third-party JS/CSS is CDN:

| Library | Version | Purpose |
|---|---|---|
| KaTeX | 0.16.9 | Client-side maths rendering — auto-render scans `$...$` and `$$...$$` |
| vis-network | 9.1.9 | Interactive force-directed graph |
| Google Fonts | — | Sora (display), Inter (body), JetBrains Mono (code) |

---

## Key Design Decisions

**Five committed sources of truth, one disposable cache.** `cards/**/*.md` owns card content; `edges.json` owns relationships (labels + plain-English descriptions); `resources.json` owns per-card learning resources (websites and videos, keyed by card ID); `notation.json` owns LaTeX symbol definitions; `key-terms.json` owns plain-text equation variable definitions (e.g. `dW`, `S`). `graph.db` is derived from all of these and is gitignored — delete it and restart to rebuild completely.

**Card IDs from file paths.** Renaming or moving a card file changes its ID. The cascade delete removes the old ID's edges from the database, and `edges.json` entries that still use it are skipped with a warning at the next reload. Old links to a card that moved to another topic still work through the slug lookup. When you rename or move a card, update its IDs in `edges.json` and `resources.json` in the same commit.

**Metadata parsed with regex, not a Markdown parser.** This keeps the format explicit and strict. If `**Topic:**` is missing or misspelt, startup fails loudly rather than inserting a card with empty metadata.

**HTML pre-rendered at load time, not per request.** `html_content` is stored in the database so each request is a simple SQL query + template render. KaTeX maths rendering happens in the browser, so the server does no maths rendering at all.

**Production is a static build of the same app.** Rather than a second renderer, `app/static_site.py` drives the Flask app through its test client. Local and live pages therefore come from the same templates and views. The few things that need a server (query strings, redirects, cookies) get small browser-side stand-ins in the static build.

**Visited card state is client-only.** Stored in `localStorage` — no server sessions, no user accounts. Clearing browser storage resets progress.

**Theme and wide mode stored in `localStorage`, applied before paint.** A small inline `<script>` in `<head>` reads `localStorage` and sets `data-theme` and `data-wide` on `<html>` before the stylesheet is applied, eliminating any flash on reload. Wide mode removes `max-width` constraints from `.nav`, `.container`, and `.formulas-page` so the layout fills the full viewport.

---

## Startup Sequence

```
FLASK_DEBUG=1 uv run python run.py
  └─ create_app()               refuses to start without SECRET_KEY unless FLASK_DEBUG=1
       ├─ init_db()              CREATE TABLE IF NOT EXISTS … (no-op if already exists)
       ├─ load_all_cards()       rglob cards/**/*.md → mtime check → upsert changed
       │                         also removes stale cards whose files no longer exist
       ├─ load_edges_from_file() if edges.json changed: clear edges table, repopulate
       ├─ register_blueprint(bp)
       ├─ attach context_processor (topic_colour, stats; CSRF token in edit mode only)
       └─ attach static URL versioning (?v= content hash)
  └─ app.run(debug=(DEBUG == "true"), port=PORT or 5000)
```

A fresh `graph.db` takes a few seconds to build; later starts skip unchanged cards. With `DEBUG=true` the reloader watches Python files. **It does not watch `cards/*.md`** — editing a card file requires a manual server restart (or saving any `.py` file to trigger the reloader).

The static build (`scripts/build_static.py`) calls the same `create_app()`, then renders every page into `dist/`.

---

## Rendering and Performance

Nothing changes at runtime (outside edge-edit mode), so every page is a pure function of the files loaded at startup. Production takes that to its end: the whole site is rendered to files at deploy time, and Caddy handles compression, `Cache-Control` and ETags (see [Deployment](#deployment)). The Flask app therefore has no page cache, HTTP caching headers or rate limiting. The dev server renders each request afresh, which is fast enough locally.

What the app still does for the pages it renders:

- **Static asset URLs carry a content hash.** `url_for('static', ...)` appends `?v=<hash>` (`version_static_urls` in `create_app()`). Caddy caches `/static/*` for a year, and a changed file gets a new URL.
- **Shared JavaScript is one file.** The search overlay, theme and wide-mode toggles, mobile menu, random card and keyboard shortcuts live in `app/static/base.js`. It is a plain script loaded at the end of `<body>`, so its top-level names are globals for inline `onclick` handlers and page scripts. `base.html` passes it the server URLs it needs in a small inline `FC_URLS` object. Kept inline, the script added about 8.6 KB to each of the ~7,450 static pages.
- **Templates are dedented.** A Jinja extension strips every template line's indentation at compile time. It cut the index from 2.0 MB to 1.3 MB with identical rendering.
- **Request connections to SQLite are read-only** and skip the PRAGMAs (edit mode keeps a writable one).
- **No cookies.** The CSRF token is only created in edge-edit mode, so ordinary pages never touch the session.

Render times with the Flask test client: `/` about 110 ms, `/card/<id>` about 20 ms, `/path/<id>` about 26 ms. The static build renders every page once, in about 50 s.

## Deployment

Production is static. `scripts/build_static.py` (logic in `app/static_site.py`) requests every page through the Flask test client with `X-Forwarded-Prefix: /flashcards` and writes each response to a file: `/a/b` becomes `a/b.html`, plus `404.html`, the JSON files and `static/`. That's about 7,450 pages. The build fails if any page links to a file it did not write. `create_app()` wraps the app in `ProxyFix`, which turns the header into `SCRIPT_NAME`, so every `url_for` link carries the prefix. Templates must build URLs with `url_for`, never root-relative strings.

A query string cannot select a file, so templates link to path routes (`/topic/<slug>`, `/quiz/<slug>`, `/tag/<path:tag>`). With `STATIC_BUILD` set in the app config, pages carry small scripts that do the server's remaining jobs in the browser:

- forwarding old `?tag=`/`?topic=` URLs;
- filtering `/recent?start=&end=`;
- picking a random card (`/random`) and setting the Barbie theme cookie (`/barbie`);
- resolving `/card/<slug>` on the 404 page.

CI copies the files to the shared EC2 instance as `~/flashcards-site/releases/<sha>` and repoints a `current` symlink, and Caddy from the `quant-finance` repo serves them with `file_server`. The workflow, Caddy configuration and rollback are in [`.github/workflows/DEPLOY-EC2.md`](.github/workflows/DEPLOY-EC2.md).

## Adding Things

**New card:** create `cards/<topic>/<slug>.md`, restart the server. No other changes needed if the topic already exists; the static build picks it up automatically.

**New topic:** add an entry to `TOPIC_COLOURS` in `app/routes.py` first (an unknown topic aborts startup), then create the directory and its cards, and restart. The colour cascades automatically to all UI elements, and the topic gets `/topic/<slug>` and `/quiz/<slug>` pages.

**New edge:** add an entry to `edges.json` and restart the server. Each entry has `source`, `target`, `label`, and `description` fields. With `ALLOW_EDGE_EDIT=1`, the remove-link form on the card detail page can delete edges at runtime (and writes the change back to `edges.json`).

**New learning resource:** add an entry to `resources.json` under the card ID key. Each card can have `websites` and `videos` arrays of `{title, url}` objects. URLs are validated by `scripts/validate_urls.py` on commit.

**New notation symbol:** add an entry to `notation.json` mapping a LaTeX command (e.g. `\\sigma`) to `{symbol, meaning}`. It will appear automatically in the sidebar of every card that uses that command.

**New key term:** add an entry to `key-terms.json` mapping a plain variable name (e.g. `dW`) to `{symbol, meaning}`. It will appear in the sidebar of every card whose LaTeX math blocks contain that variable.

**New route:** add a handler to `app/routes.py` and a template to `app/templates/`. The context processor variables (`topic_colour`, `topic_slug`, `site_stats`, `static_build`) are available in all templates automatically. For the page to exist in production, add its URLs to `page_urls()` in `app/static_site.py`, and don't make its content depend on a query string. The build's link check fails if a page links to a URL it did not render.
