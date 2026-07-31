# Yield Curve Fitting

**Topic:** Fixed Income
**Tags:** yield curve, least squares, nelson-siegel, curve construction, interpolation, term structure
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

Yield curve fitting is the process of estimating a smooth, continuous function of interest rates across maturities by minimising the discrepancy between model-implied yields and a set of observed market rates or bond prices.

## Key Formula

The fitting objective minimises a weighted sum of squared residuals across $N$ instruments:

$$\min_{\boldsymbol{\theta}} \sum_{i=1}^{N} w_i \left[y_i^{\text{obs}} - y(\tau_i;\, \boldsymbol{\theta})\right]^2$$

where $y_i^{\text{obs}}$ is the observed yield at tenor $\tau_i$, $y(\tau_i;\boldsymbol{\theta})$ is the parametric model yield, $w_i$ is a weight (often the DV01 of the instrument), and $\boldsymbol{\theta}$ is the parameter vector — e.g. Nelson-Siegel's $(\beta_0, \beta_1, \beta_2, \lambda)$.

With $\lambda$ fixed, the problem is linear in $(\beta_0, \beta_1, \beta_2)$:

$$\min_{\boldsymbol{\beta}} \| \mathbf{X}\boldsymbol{\beta} - \mathbf{y}^{\text{obs}} \|^2 \implies \hat{\boldsymbol{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \mathbf{y}^{\text{obs}}$$

where each row of $\mathbf{X}$ contains the three Nelson-Siegel loading factors evaluated at the corresponding tenor.

## Example

Observed par yields: 2Y = 3.0%, 5Y = 3.5%, 10Y = 4.0%. Fixing $\lambda = 2$ and solving the linear least-squares system yields $\hat{\beta}_0 = 4.3\%$, $\hat{\beta}_1 = -1.8\%$, $\hat{\beta}_2 = 0.7\%$. The fitted curve implies a 7-year rate of 3.9% — a tenor not directly quoted by any input instrument, enabling pricing of off-the-run bonds at that maturity.

## Remember

Central banks (ECB, Bank of England, Federal Reserve) publish official fitted yield curves using Nelson-Siegel or Svensson — these smooth parametric curves, not raw bond yields, are the benchmark rates used to price off-the-run government bonds, estimate term premia, and set hurdle rates for fixed-income relative value strategies. A gap between a bond's observed yield and the fitted curve is a signal of cheapness or richness exploited by relative value traders.
