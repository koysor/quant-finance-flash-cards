# Beta Estimation

**Topic:** Statistics
**Tags:** beta, regression, systematic risk, estimation, CAPM
**Created:** 2026-03-01
**Author:** Claude Opus 4.6

---

## Definition

**Beta estimation** is the process of measuring an asset's sensitivity to market movements using historical return data. The standard approach regresses the asset's excess returns on the market's excess returns using ordinary least squares (OLS). The slope coefficient of this regression is the estimated beta.

## Key Formula

The regression model:

$$R_i - R_f = \alpha + \beta (R_m - R_f) + \varepsilon$$

The OLS estimator for beta:

$$\hat{\beta} = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)} = \rho_{i,m} \cdot \frac{\sigma_i}{\sigma_m}$$

The **Blume adjustment** corrects for mean reversion of beta towards 1:

$$\beta_{\text{adjusted}} = \tfrac{2}{3} \hat{\beta} + \tfrac{1}{3} \times 1$$

## Example

Over the past 60 months, a stock's returns have $\sigma_i = 30\%$, the market has $\sigma_m = 18\%$, and their correlation is $\rho = 0.72$.

$$\hat{\beta} = 0.72 \times \frac{0.30}{0.18} = 0.72 \times 1.667 = 1.20$$

Applying the Blume adjustment:

$$\beta_{\text{adjusted}} = \tfrac{2}{3} \times 1.20 + \tfrac{1}{3} \times 1 = 0.80 + 0.33 = 1.13$$

The raw beta of 1.20 is shrunk towards 1, reflecting the empirical tendency of extreme betas to moderate over time.

## Remember

Beta estimation is where CAPM theory meets market data, and every practical choice matters: the market index (S&P 500 vs FTSE 100), return frequency (daily vs monthly), and estimation window (2 years vs 5 years) all affect the result. Bloomberg's default convention uses 2 years of weekly returns with a Blume adjustment. Because beta is estimated with uncertainty, practitioners often report confidence intervals — a stock with $\hat{\beta} = 1.2 \pm 0.3$ could plausibly have a true beta anywhere from 0.9 to 1.5.
