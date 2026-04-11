# Linear Factor Model (Single-Index Model)

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** factor model, single-index model, beta, idiosyncratic risk, covariance matrix
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

Sharpe's **single-index model** expresses each asset's return as a linear function of the market return plus an idiosyncratic component. It drastically reduces the number of parameters needed for mean-variance optimisation from $O(N^2)$ to $O(N)$.

## Key Formula

$$r_i = \alpha_i + \beta_i r_M + \varepsilon_i, \qquad \varepsilon_i \sim N(0, e_i^2), \quad \varepsilon_i \perp \varepsilon_j$$

The key assumption is that residuals are **uncorrelated across assets** — all co-movement passes through the market index.

**Derived portfolio statistics:**

$$\sigma_C^2 = \beta_C^2\sigma_M^2 + e_C^2 \qquad \text{(portfolio variance)}$$

$$\text{Cov}(r_i, r_j) = \beta_i\beta_j\sigma_M^2 \qquad \text{(asset covariance)}$$

| Approach | Parameters required |
|---|---|
| Full covariance matrix | $N + N(N-1)/2 \approx N^2/2$ |
| Single-index model | $3N + 1$ ($\alpha_i$, $\beta_i$, $e_i^2$ for each asset, plus $\sigma_M^2$) |

For $N = 100$: full matrix needs ~5,000 parameters; factor model needs ~301.

## Example

An analyst is constructing an MVO portfolio of 500 UK equities. The full covariance matrix requires $500 \times 501 / 2 = 125{,}250$ parameter estimates. The single-index model requires $3(500) + 1 = 1{,}501$ — a 98.8% reduction.

## Remember

The single-index model works because it replaces the full covariance matrix with a much simpler structure: every pair of assets co-moves only because they both move with the market. Setting $\text{Cov}(r_i, r_j) = \beta_i\beta_j\sigma_M^2$ makes the covariance matrix a rank-1 matrix (plus diagonal idiosyncratic terms), which is both computationally efficient and far easier to estimate reliably. This is the foundation of all modern factor models.
