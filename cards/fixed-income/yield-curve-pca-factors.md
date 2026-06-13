# Yield Curve PCA Factors

**Topic:** Fixed Income
**Tags:** PCA, principal components, yield curve, level, slope, curvature, factor model, hedging
**Created:** 2026-06-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Principal component analysis (PCA)** applied to historical yield curve changes decomposes correlated movements across tenors into uncorrelated factors. Empirically, three factors — **level**, **slope**, and **curvature** — explain more than 99% of total yield variance. This reduction from 10+ correlated tenor points to 3 independent drivers underpins most practical interest rate hedging and stress-testing frameworks.

## Key Formula

Let $\Delta y_\tau$ be the daily change in the yield at tenor $\tau$. PCA finds eigenvectors $v_k$ and eigenvalues $\lambda_k$ of the covariance matrix $\Sigma$ of $(\Delta y_{\tau_1}, \ldots, \Delta y_{\tau_n})$:

$$\Sigma v_k = \lambda_k v_k, \qquad k = 1, 2, 3$$

Cumulative variance explained by $K$ factors: $\sum_{k=1}^{K} \lambda_k \Big/ \sum_{k=1}^{n} \lambda_k$.

| Factor | Loading shape | Typical variance explained |
|---|---|---|
| PC1 — Level | All tenors move in the same direction | 80–90% |
| PC2 — Slope | Short rates move opposite to long rates | 7–12% |
| PC3 — Curvature | Short and long rates move together, mid curve opposite | 2–4% |

A **PC hedge** sets the portfolio's sensitivity to each factor to zero: $\sum_i w_i v_{ki} = 0$ for $k = 1, 2, 3$.

## Example

Using US Treasury data (1990–2020), a PCA across 3m, 6m, 1y, 2y, 5y, 7y, 10y, 30y tenors yields approximately:
- PC1 (level) loading: $[+0.28, +0.31, +0.35, +0.38, +0.38, +0.37, +0.36, +0.33]$ — all positive, largest at 2–5y
- PC2 (slope) loading: $[-0.62, -0.53, -0.33, -0.07, +0.24, +0.31, +0.33, +0.26]$ — negative at short end, positive at long end
- PC3 (curvature) loading: $[+0.51, +0.22, -0.20, -0.50, -0.17, +0.12, +0.35, +0.47]$ — butterfly shape

A bond with DV01 = \$10k at 2y, \$8k at 5y, \$6k at 10y: its slope exposure = $10\text{k} \times (-0.07) + 8\text{k} \times (+0.24) + 6\text{k} \times (+0.33) = 3{,}260$ — indicating substantial slope risk.

## Remember

PCA factors are **empirical**, not model-derived: they tell you what the yield curve has done historically, not what an equilibrium model says it should do. The level factor dominates because central bank policy shifts all rates together. The slope factor captures the business-cycle correlation between short-term policy rates and long-term growth expectations. In practice, a portfolio that is DV01-neutral (level-hedged) can still lose heavily if the yield curve steepens — PC2 risk is invisible to a simple duration hedge. Full factor-neutral hedging requires positions in at least three maturity buckets.
