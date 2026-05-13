# Robust Optimisation

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** robust optimisation, uncertainty set, maxmin, ambiguity, estimation error, worst-case
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Robust optimisation** constructs portfolios that maximise return under the worst-case realisation of uncertain parameters within a specified uncertainty set. Rather than treating parameter estimates as exact, it explicitly models the range of plausible inputs and optimises against the adversarial extreme.

## Key Formula

The robust mean-variance problem with ellipsoidal uncertainty set $\mathcal{U}$ for expected returns:

$$\max_{\mathbf{w}}\; \min_{\boldsymbol{\mu} \in \mathcal{U}}\; \boldsymbol{\mu}^\top \mathbf{w} - \frac{\gamma}{2}\, \mathbf{w}^\top \hat{\Sigma}\, \mathbf{w}$$

where $\mathcal{U} = \{\boldsymbol{\mu} : (\boldsymbol{\mu} - \hat{\boldsymbol{\mu}})^\top \Theta^{-1} (\boldsymbol{\mu} - \hat{\boldsymbol{\mu}}) \leq \kappa^2\}$ is a confidence ellipsoid of radius $\kappa$ around the estimated mean $\hat{\boldsymbol{\mu}}$ and $\Theta$ is the estimation covariance. The inner minimisation is solved analytically, reducing the robust problem to a standard second-order cone programme.

## Example

A fund estimates the expected return of a stock at $\hat{\mu} = 8\%$ with estimation standard error $\sigma_{\hat{\mu}} = 3\%$. With $\kappa = 1$ (one-sigma uncertainty), the robust optimiser assumes the true return could be as low as $8\% - 3\% = 5\%$. It sizes the position as if the return were 5% rather than 8%, resulting in a smaller weight that is resilient to estimation error. In a 50-asset universe, applying this across all assets simultaneously produces a markedly more diversified portfolio than naive Markowitz.

## Remember

Robust optimisation is the formal solution to the error-maximisation critique of Markowitz: instead of treating $\hat{\boldsymbol{\mu}}$ as the true mean and letting the optimiser exploit noise, it forces the portfolio to be good even when inputs are adversarially wrong within a plausible range. The uncertainty set radius $\kappa$ is the single parameter controlling conservatism — setting $\kappa = 0$ recovers Markowitz, while large $\kappa$ approaches the minimum-variance portfolio that ignores return forecasts entirely. This directly implements ambiguity aversion in a tractable quadratic programme.
