# Tangency Portfolio

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** tangency portfolio, Sharpe ratio, optimal risky portfolio, efficient frontier, mean-variance
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **tangency portfolio** $T$ is the unique risky portfolio where the line drawn from the risk-free rate $R$ is **tangent** to the efficient frontier of risky assets. It is the single best risky portfolio to hold when borrowing or lending at $R$ is possible — it maximises the Sharpe ratio among all risky portfolios.

## Key Formula

The weight of asset $A$ in the tangency portfolio (two-asset case):

$$w_A^T = \frac{(\mu_A - R)\sigma_B^2 - (\mu_B - R)\rho_{AB}\sigma_A\sigma_B}{(\mu_A - R)\sigma_B^2 + (\mu_B - R)\sigma_A^2 - (\mu_A + \mu_B - 2R)\rho_{AB}\sigma_A\sigma_B}$$

Any blend of $T$ and the risk-free asset lies on the CML:

$$\mu_\Pi = R + w_t(\mu_T - R), \qquad \sigma_\Pi = w_t\sigma_T, \qquad S_T = \frac{\mu_T - R}{\sigma_T}$$

## Example

$\mu_A = 12\%$, $\sigma_A = 20\%$; $\mu_B = 7\%$, $\sigma_B = 12\%$; $\rho = 0.3$; $R = 4\%$.

Numerator: $(8)(0.0144) - (3)(0.3)(0.20)(0.12) = 0.1152 - 0.0216 = 0.0936$

Denominator: $(8)(0.0144) + (3)(0.04) - (11)(0.3)(0.024) = 0.1152 + 0.12 - 0.0792 = 0.156$

$$w_A^T = \frac{0.0936}{0.156} = 60\%, \qquad w_B^T = 40\%$$

## Remember

The tangency portfolio is the "optimal risky portfolio" — once a risk-free asset is available, every rational investor holds some mix of $T$ and the risk-free asset. Their risk appetite determines the split, but the risky allocation is always $T$. Under CAPM, the tangency portfolio equals the market portfolio, which is why index funds are theoretically optimal.
