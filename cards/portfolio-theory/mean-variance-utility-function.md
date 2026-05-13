# Mean-Variance Utility Function

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** utility function, risk aversion, mean-variance, portfolio optimisation, expected utility
**Created:** 2026-04-20
**Author:** Claude Sonnet 4.6

---

## Definition

The mean-variance utility function is an investor preference model that ranks portfolios by expected return minus a penalty for variance, where the penalty is scaled by the investor's **risk-aversion coefficient** $\lambda$. It provides the theoretical justification for why rational investors prefer the efficient frontier — and specifically which point on it — given their personal tolerance for risk.

## Key Formula

$$U = \mu_p - \frac{\lambda}{2} \sigma_p^2$$

where $\mu_p$ is the portfolio's expected return, $\sigma_p^2$ is its variance, and $\lambda > 0$ is the risk-aversion coefficient. A higher $\lambda$ means the investor penalises variance more heavily. Setting $\frac{\partial U}{\partial \mathbf{w}} = 0$ subject to $\mathbf{w}^\top \mathbf{1} = 1$ gives the optimal weights:

$$\mathbf{w}^* = \frac{1}{\lambda} \Sigma^{-1} \boldsymbol{\mu}$$

## Example

Two portfolios: A has $\mu = 12\%$, $\sigma^2 = 0.04$; B has $\mu = 8\%$, $\sigma^2 = 0.01$.

For a cautious investor with $\lambda = 4$:
- $U_A = 0.12 - \frac{4}{2}(0.04) = 0.12 - 0.08 = 0.04$
- $U_B = 0.08 - \frac{4}{2}(0.01) = 0.08 - 0.02 = 0.06$

B is preferred. For an aggressive investor with $\lambda = 1$:
- $U_A = 0.12 - 0.02 = 0.10$
- $U_B = 0.08 - 0.005 = 0.075$

A is now preferred. The same portfolios rank differently depending solely on risk aversion.

## Remember

In practice, $\lambda$ is rarely observed directly — asset managers infer it from client questionnaires, from the volatility of existing portfolios (reverse-optimisation), or from regulatory suitability categories. The Black-Litterman model uses $\lambda$ calibrated to the market portfolio: the equilibrium expected returns $\boldsymbol{\Pi} = \lambda \Sigma \mathbf{w}_{\text{market}}$ are derived by assuming the market portfolio maximises this utility, which gives a principled starting point for active tilts. Misestimating $\lambda$ leads to portfolios that are either too concentrated (low $\lambda$) or too diluted (high $\lambda$) relative to what the client actually wants.
