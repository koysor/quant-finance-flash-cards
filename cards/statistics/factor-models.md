# Factor Models

**Topic:** Statistics
**Tags:** factor models, covariance estimation, dimensionality reduction, systematic risk, residual risk
**Author:** Claude Opus 4.6

---

## Definition

A **factor model** explains asset returns as a linear combination of a small number of common factors plus an asset-specific residual. By attributing co-movement to shared factors, the model dramatically reduces the number of parameters needed to describe the covariance structure — from $n(n+1)/2$ pairwise covariances to just $n$ factor loadings and $n$ residual variances.

## Key Formula

**Single-factor model:**

$$r_i = \alpha_i + \beta_i f + \varepsilon_i$$

where $f$ is the common factor return, $\beta_i$ is asset $i$'s loading, and $\varepsilon_i$ is the idiosyncratic residual (uncorrelated across assets).

**Implied covariance matrix:**

$$\Sigma = \beta \beta^\top \sigma_f^2 + D$$

where $\beta$ is the $n \times 1$ vector of factor loadings, $\sigma_f^2$ is the factor variance, and $D$ is the diagonal matrix of residual variances.

**Multi-factor extension** (with $k$ factors and loading matrix $B$):

$$\Sigma = B \, \Sigma_f \, B^\top + D$$

## Example

Three stocks have market betas $\beta_1 = 1.2$, $\beta_2 = 0.8$, $\beta_3 = 0.5$, market variance $\sigma_f^2 = 0.04$, and residual variances $d_1 = 0.01$, $d_2 = 0.005$, $d_3 = 0.008$.

The factor-implied covariance between stocks 1 and 2:

$$\sigma_{12} = \beta_1 \beta_2 \sigma_f^2 = 1.2 \times 0.8 \times 0.04 = 0.0384$$

The variance of stock 1:

$$\sigma_1^2 = \beta_1^2 \sigma_f^2 + d_1 = 1.44 \times 0.04 + 0.01 = 0.0676$$

Instead of estimating 6 covariance parameters directly, the single-factor model uses only 6 parameters (3 betas + 3 residual variances) — and the saving grows dramatically with $n$.

## Remember

Factor models are the practical solution to the curse of dimensionality in covariance estimation. A portfolio of 500 stocks requires estimating 125,250 covariance entries from the sample — far more parameters than most datasets can support. A 5-factor model reduces this to roughly 3,000 parameters. The Fama-French model, Barra risk models, and statistical PCA-based models are all factor models at heart. They decompose portfolio risk into systematic (factor-driven) and idiosyncratic components, enabling risk attribution, stress testing, and more stable portfolio optimisation.
