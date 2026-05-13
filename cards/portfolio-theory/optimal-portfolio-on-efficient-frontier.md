# Optimal Portfolio on the Efficient Frontier

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** optimal portfolio, efficient frontier, indifference curves, risk aversion, utility maximisation
**Created:** 2026-04-20
**Author:** Claude Sonnet 4.6

---

## Definition

The optimal portfolio is the single point on the efficient frontier where an investor's highest attainable **indifference curve** is tangent to the frontier. It is unique to each investor: a more risk-averse investor's indifference curves are steeper, pushing their optimal point leftward (lower risk, lower return); a less risk-averse investor's curves are flatter, pushing it rightward.

## Key Formula

An investor with mean-variance utility $U = \mu_p - \tfrac{\lambda}{2}\sigma_p^2$ maximises over all frontier portfolios. The optimal portfolio satisfies:

$$\frac{d\mu_p}{d\sigma_p}\bigg|_{\text{frontier}} = \lambda \, \sigma_p^*$$

where the left side is the local slope of the efficient frontier (the marginal return per unit of additional risk) and the right side is the slope of the investor's indifference curve at their chosen risk level. At the optimum, these slopes are equal — the frontier and the indifference curve are tangent.

Equivalently, the optimal weights solve:

$$\mathbf{w}^* = \frac{1}{\lambda} \Sigma^{-1} \boldsymbol{\mu}$$

(normalised to sum to 1).

## Example

Suppose the efficient frontier offers return-risk combinations $(6\%, 10\%)$ and $(10\%, 18\%)$. An investor with $\lambda = 4$:

- At $(6\%, 10\%)$: $U = 0.06 - 2 \times 0.01 = 0.04$
- At $(10\%, 18\%)$: $U = 0.10 - 2 \times 0.0324 = 0.035$

The lower-risk portfolio gives higher utility — this investor's optimal point is near or below $(6\%, 10\%)$. An investor with $\lambda = 1$:

- At $(6\%, 10\%)$: $U = 0.06 - 0.005 = 0.055$
- At $(10\%, 18\%)$: $U = 0.10 - 0.0162 = 0.084$

This investor prefers the higher-return portfolio — their optimal point is at higher risk.

## Remember

In practice, the optimal portfolio on the frontier is never implemented directly — the weights from $\mathbf{w}^* = \frac{1}{\lambda}\Sigma^{-1}\boldsymbol{\mu}$ are extremely sensitive to errors in $\boldsymbol{\mu}$, producing wildly concentrated positions. Real allocations use this framework conceptually (to justify holding diversified portfolios) but stabilise it with Black-Litterman return priors, shrinkage covariance estimates, or simple constraints. The Two-Fund Separation Theorem simplifies the problem further: every investor merely combines the risk-free asset and the tangency portfolio in proportions determined by $\lambda$, so finding the optimal frontier point reduces to choosing a single blend ratio.
