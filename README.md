# Quantitative Finance Flash Cards

Bite-sized revision flash cards for Quantitative Finance exams and interviews, designed for accessibility and clarity. Each card covers one concept — definition, key formula, worked example, and its finance application.

1687 cards · 16 topics · 5086 concept connections

## Running the app

```bash
uv sync                                  # install dependencies
FLASK_DEBUG=1 uv run python run.py       # http://127.0.0.1:5000
```

`bash launch_app.sh` (or `launch_app.bat` on Windows) does both. `FLASK_DEBUG=1` is required locally: without it, `create_app()` refuses to start unless `SECRET_KEY` is set. Add `DEBUG=true` for the debugger and the reloader.

On first run the app scans `cards/` and loads `edges.json`, building `graph.db` automatically (a few seconds). Later starts skip unchanged cards. Adding or editing a card takes effect on the next server restart.

After cloning, install the git pre-commit hooks so URL validation and README stats run automatically:

```bash
bash scripts/install_hooks.sh
```

## Environment variables

| Variable | Default | Purpose |
|---|---|---|
| `SECRET_KEY` | Required unless `FLASK_DEBUG=1` | Flask session signing key. With `FLASK_DEBUG=1` (local development) a random key is generated and changes on restart; the launch scripts set this. The static build sets a throwaway one. |
| `PORT` | `5000` | Port for the development server. |
| `FLASK_DEBUG` | unset | Set to `1` for local development: lets the app start without `SECRET_KEY` (a random key is generated). |
| `DEBUG` | `false` | Set to `true` to run `run.py` with Flask's debugger and reloader. |
| `ALLOW_EDGE_EDIT` | unset | Set to `1` to enable the card-page "remove link" button, which rewrites `edges.json`. It also turns off page caching and caching headers. Never set it for the static build, which refuses to run with it. |
| `CACHE_THRESHOLD` | `500` | Maximum number of pages the dev server caches in memory. A full cache is about 20–30 MB. |

## Topics

| Topic | Cards | Scope |
|---|---|---|
| Banking Regulation | 57 | FRTB, IRRBB, LCR, NSFR, EVE, EaR, Basel capital rules |
| Calculus | 194 | Differentiation, integration, Taylor series, quadratic techniques, A Level pure maths |
| Computational Finance | 113 | Numerical methods, finite differences, FFT, simulation, ML algorithms |
| Derivatives | 134 | Options, futures, Greeks, pricing models, risk-neutral theory |
| Financial Mathematics | 63 | TVM, compounding, NPV, leverage, hedge funds, execution |
| Fixed Income | 143 | Bonds, yield curves, duration, DV01, credit spreads, swaps, short-rate models, calibration |
| Linear Algebra | 78 | Matrices, vectors, eigenvalues, SVD, decompositions |
| Machine Learning | 282 | ML algorithms (SVM, trees, neural networks), deep learning, training techniques, RL, NLP, generative models, MLOps |
| Mathematical Notation | 62 | Sigma, pi, set theory, logical and summation notation |
| Portfolio Theory & Asset Pricing | 102 | CAPM, efficient frontier, factor models, performance ratios |
| Probability | 106 | Distributions, expectation, Bayes, transform methods |
| Risk | 51 | VaR, CVaR, Monte Carlo, stress testing, EVT, drawdowns |
| Short Selling | 20 | Short mechanics, securities lending, regulation, short squeezes |
| Statistics | 145 | Regression, hypothesis testing, covariance estimation |
| Stochastic Processes | 92 | Brownian motion, GBM, Itô's lemma, SDEs, martingales |
| Volatility | 45 | Implied/realised vol, VIX, vol surface, smile, stochastic vol models |

## Deployment (AWS EC2)

Live at https://koysor.duckdns.org/flashcards/ as a static site. On every push to `main`, GitHub Actions runs the tests, renders every page to HTML with `scripts/build_static.py` (failing on any broken link), and copies the files over SSH to the shared EC2 instance. There, Caddy from the quant-finance repo serves them under `/flashcards/`, and no Python runs on the server. See [`.github/workflows/DEPLOY-EC2.md`](.github/workflows/DEPLOY-EC2.md) for the workflow, the Caddy configuration, rollback and the deploy key.

To build the site locally (Linux or WSL; some tag names are not valid Windows file names):

```bash
uv run python scripts/build_static.py --prefix /flashcards --out dist
```

## Features

- **Card library** — browse all cards grouped by topic, with a tag strip and a page per topic (`/topic/<slug>`)
- **Tag pages** — dedicated `/tag/<tag>` pages listing all cards for a given tag
- **Prerequisites & See Also** — incoming edges shown as prerequisites above card content; outgoing edges shown as "See Also" below
- **Knowledge graph** — interactive force-directed network with topic filtering, shortest-path highlighting between any two nodes, and edge weights based on shared tags
- **Spotlight search** — press `/` for fuzzy search across all cards by name or tag
- **Keyboard navigation** — `←`/`→` for prev/next card in topic, `j`/`k` for card list, `r` for random, `g` for graph, `f` for formulas, `c` for all cards, `w` for wide mode, `?` for shortcuts
- **Dark / Light theme** — persisted across sessions
- **Wide mode** — toggle full-viewport-width layout via the expand button or `w` key; persisted across sessions
- **Notation & Key Terms sidebar** — every card shows the LaTeX symbols and plain-text equation variables used, drawn from `notation.json` and `key-terms.json`
- **Concept links** — directed relationships between cards with plain-English descriptions, stored in `edges.json`
- **Formula sheet** — all Key Formula sections aggregated on a single `/formulas` page
- **Quiz** — `/quiz/<topic>` shows each card's name, reveals its definition and key formula on demand, and remembers which you marked known
- **Study path** — `/path/<card>` lists a card's nearest prerequisites in learning order
- **Recent cards** — `/recent` lists cards newest first, grouped by date (`?start=` / `?end=` to narrow it; `recent.json` on the live site)
- **Learning resources** — curated website and video links per card, stored in `resources.json`
- **Visited tracking** — cards you have read are marked in the browser
- **Slug-based redirect** — if a card URL is not found verbatim, it is resolved by slug across all topics: one match redirects, multiple matches show a choice. The Flask app does this on the server (301 / 300); the static site does it in the browser from its 404 page

## Stack

| Layer | Technology |
|---|---|
| Server | Python 3.14, Flask 3 |
| Database | SQLite (via `sqlite3` stdlib) |
| Maths rendering | KaTeX 0.16.9 (client-side, CDN) |
| Graph visualisation | vis-network 9.1.9 (CDN) |
| Fonts | Sora · Inter · JetBrains Mono (Google Fonts) |
| Package management | uv |

No npm and no frontend build step. Production is a static build of the Flask app's pages, with no Python running on the server.

## Project layout

```
cards/          Markdown source files — card content source of truth
edges.json      Concept relationships — edge source of truth
resources.json  Per-card learning resources (websites, videos)
notation.json   LaTeX symbol meanings for the Notation sidebar and hover tooltips
key-terms.json  Plain variable meanings (dW, S, …) for the Key Terms sidebar
app/            Flask application package
  __init__.py   Application factory (create_app)
  db.py         SQLite schema and all query functions
  extensions.py Page cache, rate limiter, edit-mode switch
  loader.py     Scans cards/, parses metadata, upserts to DB
  routes.py     All routes + topic colour map
  static_site.py Renders every page to static files for production
  templates/    Jinja2 templates
  static/       CSS and favicon
scripts/        Static build, README stats, URL validation, git hook installer
tests/          pytest suite
run.py          Development server entry point
graph.db        Runtime only — gitignored, fully regenerable
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for a full explanation of how the layers fit together.

## Scripts & git hooks

| Script | Purpose |
|---|---|
| `scripts/build_static.py` | Renders the site to `dist/` for production (`--prefix /flashcards --out dist`). Fails on any broken link. Linux or WSL only. CI runs it. |
| `scripts/validate_urls.py` | Validates every URL in `resources.json` with async HEAD requests. Runs automatically on commit when `resources.json` is staged. Run manually with `uv run python scripts/validate_urls.py --force`. |
| `scripts/update_readme_stats.py` | Recounts cards, topics, and edges, then updates the stats line in `README.md`. Runs automatically on commit when `cards/` or `edges.json` is staged. |
| `scripts/install_hooks.sh` | Installs the pre-commit hook into `.git/hooks/`. Run once after cloning: `bash scripts/install_hooks.sh`. |

## Troubleshooting

**`ValueError` on startup** — a card file has missing or misspelt metadata (e.g. `**Topic:**` not found). The error message shows which file is broken. Fix the card and restart.

**`graph.db` corrupted or out of sync** — delete `graph.db` and restart the server. The database is a disposable cache rebuilt entirely from the Markdown files and JSON sources.

**Card edits not showing up** — cards are loaded at startup, and the reloader (`DEBUG=true`) watches `.py` files only, not `.md` files. After editing a card, restart the server, or save any `.py` file when the reloader is on.

**`ValueError: Unknown topic` on startup** — every card's `**Topic:**` must be a key of `TOPIC_COLOURS` in `app/routes.py`. To add a topic, add its entry (name and colour) there first, then create its cards in a new `cards/<topic>/` directory.

## Note

The flash cards in this repository are generated with [Claude Opus](https://www.anthropic.com/claude) for learning and revision purposes. While care has been taken to ensure accuracy, they should be used as study aids alongside primary course materials, not as a sole reference.

## Adding a card

Create a `.md` file in the appropriate `cards/<topic>/` directory and restart the server. It goes live on the next push to `main`. See [CONTRIBUTING.md](CONTRIBUTING.md) for the required format and content rules.
