# Quantitative Finance Flash Cards

Bite-sized revision flash cards for Quantitative Finance exams and interviews, designed for accessibility and clarity. Each card covers one concept — definition, key formula, worked example, and its finance application.

53 cards · 8 topics · 99 concept connections

## Running the app

```bash
uv sync                      # install dependencies
uv run python run.py         # http://127.0.0.1:5000
```

On first run the app scans `cards/` and loads `edges.json`, building `graph.db` automatically. Adding or editing a card takes effect on the next server restart.

## Topics

| Topic | Cards |
|---|---|
| Calculus | Differentiation Rules, Lemma, Taylor Series |
| Derivatives | American Option Pricing, American vs European Options, Black-Scholes Equation, Delta Hedging, Early Exercise Decision, European Option Pricing, Heston Model, Implied Volatility, Option Greeks, Put-Call Parity, Risk-Neutral Pricing |
| Financial Mathematics | Return on Investment, Time Value of Money, Yield Curve |
| Linear Algebra | Cholesky Decomposition, Determinant, Eigenvalues & Eigenvectors, Matrix Inverse, Matrix Multiplication, Systems of Linear Equations, Transpose & Symmetric Matrices |
| Probability | Bayes' Theorem, Binomial Distribution, Chi-Squared Distribution, CDF, Expected Value, Exponential Distribution, Lognormal Distribution, Normal Distribution, PDF, Poisson Distribution, Student's t-Distribution, Uniform Distribution |
| Risk | Model Limitations, Monte Carlo Simulation, Value at Risk (VaR) |
| Statistics | Correlation, Estimating Parameters, Scaling Mean with Time, Square-Root Rule, Statistical Properties of Returns, Variance & Std Dev |
| Stochastic Processes | Brownian Motion, Discrete Random Walk, Drift & Volatility, GBM, Growth vs Volatility Timescales, Itô's Lemma, Martingales, SDE |

## Features

- **Card library** — browse all cards grouped by topic, filter by tag or topic
- **Tag pages** — dedicated `/tag/<tag>` pages listing all cards for a given tag
- **Prerequisites & See Also** — incoming edges shown as prerequisites above card content; outgoing edges shown as "See Also" below
- **Knowledge graph** — interactive force-directed network with topic filtering, shortest-path highlighting between any two nodes, and edge weights based on shared tags
- **Spotlight search** — press `/` for fuzzy search across all cards by name or tag
- **Keyboard navigation** — `←`/`→` for prev/next card in topic, `j`/`k` for card list, `r` for random, `g` for graph, `?` for shortcuts
- **Dark / Light theme** — persisted across sessions
- **Concept links** — directed relationships between cards with plain-English descriptions, stored in `edges.json`
- **Formula sheet** — all Key Formula sections aggregated on a single `/formulas` page
- **Learning resources** — curated website and video links per card, stored in `resources.json`
- **Visited tracking** — cards you have read are marked in the browser

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
