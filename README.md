# Quantitative Finance Flash Cards

Bite-sized revision flash cards for Quantitative Finance exams and interviews, designed for accessibility and clarity. Each card covers one concept — definition, key formula, worked example, and its finance application.

711 cards · 15 topics · 2056 concept connections

## Running the app

```bash
uv sync                      # install dependencies
uv run python run.py         # http://127.0.0.1:5000
```

On first run the app scans `cards/` and loads `edges.json`, building `graph.db` automatically. Adding or editing a card takes effect on the next server restart.

## Topics

| Topic | Cards | Scope |
|---|---|---|
| Banking Regulation | 15 | FRTB, IRRBB, LCR, NSFR, EVE, EaR, Basel capital rules |
| Calculus | 154 | Differentiation, integration, Taylor series, quadratic techniques, A Level pure maths |
| Computational Finance | 15 | Numerical methods, finite differences, FFT, simulation |
| Derivatives | 75 | Options, futures, Greeks, pricing models, risk-neutral theory |
| Financial Mathematics | 49 | TVM, compounding, NPV, leverage, hedge funds, execution |
| Fixed Income | 18 | Bonds, yield curves, duration, DV01, credit spreads, swaps |
| Linear Algebra | 67 | Matrices, vectors, eigenvalues, SVD, decompositions |
| Mathematical Notation | 44 | Sigma, pi, set theory, logical and summation notation |
| Portfolio Theory & Asset Pricing | 37 | CAPM, efficient frontier, factor models, performance ratios |
| Probability | 62 | Distributions, expectation, Bayes, transform methods |
| Risk | 22 | VaR, CVaR, Monte Carlo, stress testing, EVT, drawdowns |
| Short Selling | 18 | Short mechanics, securities lending, regulation, short squeezes |
| Statistics | 59 | Regression, hypothesis testing, covariance estimation |
| Stochastic Processes | 52 | Brownian motion, GBM, Itô's lemma, SDEs, martingales |
| Volatility | 22 | Implied/realised vol, VIX, vol surface, smile, stochastic vol models |

## Features

- **Card library** — browse all cards grouped by topic, filter by tag or topic
- **Tag pages** — dedicated `/tag/<tag>` pages listing all cards for a given tag
- **Prerequisites & See Also** — incoming edges shown as prerequisites above card content; outgoing edges shown as "See Also" below
- **Knowledge graph** — interactive force-directed network with topic filtering, shortest-path highlighting between any two nodes, and edge weights based on shared tags
- **Spotlight search** — press `/` for fuzzy search across all cards by name or tag
- **Keyboard navigation** — `←`/`→` for prev/next card in topic, `j`/`k` for card list, `r` for random, `g` for graph, `w` for wide mode, `?` for shortcuts
- **Dark / Light theme** — persisted across sessions
- **Wide mode** — toggle full-viewport-width layout via the expand button or `w` key; persisted across sessions
- **Notation & Key Terms sidebar** — every card shows the LaTeX symbols and plain-text equation variables used, drawn from `notation.json` and `key-terms.json`
- **Concept links** — directed relationships between cards with plain-English descriptions, stored in `edges.json`
- **Formula sheet** — all Key Formula sections aggregated on a single `/formulas` page
- **Learning resources** — curated website and video links per card, stored in `resources.json`
- **Visited tracking** — cards you have read are marked in the browser
- **Slug-based redirect** — if a card URL is not found verbatim, the app resolves by slug across all topics: one match redirects (301), multiple matches show a disambiguation page

## Stack

| Layer | Technology |
|---|---|
| Server | Python 3.12, Flask 3 |
| Database | SQLite (via `sqlite3` stdlib) |
| Maths rendering | KaTeX 0.16.9 (client-side, CDN) |
| Graph visualisation | vis-network 9.1.9 (CDN) |
| Fonts | Sora · Inter · JetBrains Mono (Google Fonts) |
| Package management | uv |

No npm, no build step, no Docker.

## Project layout

```
cards/          Markdown source files — card content source of truth
edges.json      Concept relationships — edge source of truth
resources.json  Per-card learning resources (websites, videos)
app/            Flask application package
  __init__.py   Application factory (create_app)
  db.py         SQLite schema and all query functions
  loader.py     Scans cards/, parses metadata, upserts to DB
  routes.py     All routes + topic colour map
  templates/    Jinja2 templates
  static/       CSS and favicon
run.py          Development server entry point
graph.db        Runtime only — gitignored, fully regenerable
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for a full explanation of how the layers fit together.

## Note

The flash cards in this repository are generated with [Claude Opus](https://www.anthropic.com/claude) for learning and revision purposes. While care has been taken to ensure accuracy, they should be used as study aids alongside primary course materials, not as a sole reference.

## Adding a card

Create a `.md` file in the appropriate `cards/<topic>/` directory and restart the server. See [CONTRIBUTING.md](CONTRIBUTING.md) for the required format and content rules.
