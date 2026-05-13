# Expected Portfolio Return

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** expected return, portfolio weights, weighted average, mean-variance, asset allocation
**Created:** 2026-04-20
**Author:** Claude Sonnet 4.6

---

## Definition

The expected return of a portfolio is the **weighted average** of the expected returns of its constituent assets, where the weights are the portfolio's allocation fractions. Unlike portfolio variance, expected return is linear in the weights — doubling the allocation to an asset doubles its contribution to portfolio return.

## Key Formula

For a portfolio of $n$ assets with weight vector $\mathbf{w} = (w_1, w_2, \ldots, w_n)^\top$ and expected return vector $\boldsymbol{\mu} = (\mu_1, \mu_2, \ldots, \mu_n)^\top$:

$$\mu_p = \mathbf{w}^\top \boldsymbol{\mu} = \sum_{i=1}^{n} w_i \mu_i$$

subject to $\sum_{i=1}^n w_i = 1$ (fully invested). The linearity means $\mu_p$ is determined entirely by the individual asset returns and allocations — correlations between assets play no role in expected return, only in risk.

## Example

A three-asset portfolio: Equities ($w = 0.6$, $\mu = 10\%$), Bonds ($w = 0.3$, $\mu = 4\%$), Cash ($w = 0.1$, $\mu = 1\%$).

$$\mu_p = 0.6 \times 10 + 0.3 \times 4 + 0.1 \times 1 = 6.0 + 1.2 + 0.1 = 7.3\%$$

Shifting 10% from Bonds to Equities (new weights 0.7, 0.2, 0.1):

$$\mu_p = 0.7 \times 10 + 0.2 \times 4 + 0.1 \times 1 = 7.0 + 0.8 + 0.1 = 7.9\%$$

The 0.6% increase equals $0.10 \times (10\% - 4\%)$ — the weight shift times the return differential.

## Remember

The linearity of expected portfolio return is what makes the mean-variance optimisation problem tractable: the return constraint $\mathbf{w}^\top \boldsymbol{\mu} = \mu^*$ is a hyperplane in weight space, and the variance objective $\mathbf{w}^\top \Sigma \mathbf{w}$ is quadratic — together they form a convex quadratic programme with a unique solution. In practice, estimating $\boldsymbol{\mu}$ is harder than estimating $\Sigma$: expected returns are notoriously noisy (signal-to-noise ratio of roughly 1:10 in monthly data), which is why the Black-Litterman framework and shrinkage estimators focus primarily on stabilising the return inputs rather than the covariance matrix.
