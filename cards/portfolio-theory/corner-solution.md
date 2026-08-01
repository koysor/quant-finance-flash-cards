# Corner Solution

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** mean-variance optimisation, estimation error, constraints, concentration, black-litterman, robustness
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

A corner solution is the outcome of an unconstrained mean-variance optimisation that concentrates the entire portfolio in one or two assets, typically the highest expected-return holding. It arises because the optimiser treats estimated inputs as if they were known exactly, and is a symptom of estimation error rather than of genuine investment insight.

## Key Formula

The unconstrained problem has an analytical solution linear in the estimated mean:

$$\max_{\mathbf{w}}\ \left\{\mathbf{w}'\hat{\boldsymbol{\mu}} - \lambda\,\mathbf{w}'\Sigma\mathbf{w}\right\} \quad\Longrightarrow\quad \mathbf{w}^* = \frac{1}{2\lambda}\Sigma^{-1}\hat{\boldsymbol{\mu}}$$

Two mechanisms drive the weights to extremes. The estimated mean carries standard error $\sigma/\sqrt{T}$, so any asset whose return is overstated by chance is loaded up; and $\Sigma^{-1}$ amplifies the smallest eigenvalues of the covariance matrix, which are precisely the directions estimated least reliably.

The standard remedies are a budget and long-only constraint, forcing numerical rather than analytical solution:

$$\mathbf{w}'\mathbf{1} = 1, \qquad w_i \ge 0$$

## Example

Ten assets with volatilities ranked from 5% to 40% and expected returns set proportional to volatility, so asset 10 has $\mu = 9.55\%$ and $\sigma = 40\%$, with $\rho = 0.3$ throughout.

Optimising on the true inputs already concentrates heavily in asset 10 as the risk budget rises. Now draw $T = 256$ observations from that same known distribution and re-estimate. The sampling error in the means is under half a percentage point — $\tau = 1/T = 0.0039$ — yet the efficient frontier computed from the estimates sits visibly away from the true one, and the allocations differ substantially. Both frontiers describe the *same* market; only estimation noise separates them.

## Remember

This is why the equally weighted $1/N$ portfolio is so hard to beat out of sample, and why Cochrane could call naive mean-variance "a terrible guide to investing". Two responses are standard on a desk. Constrain the problem — long-only and position limits cost some theoretical efficiency but buy large robustness gains, at the price of losing the closed form. Or fix the inputs, which is the Black-Litterman route: replace the sample mean with equilibrium returns implied by index weights, then tilt them only where you hold a view, so the posterior stays anchored near the market portfolio and produces a gentle twist to the frontier rather than a corner. The ordering matters when deciding where to spend effort — errors in the mean are roughly twenty times more damaging to a mean-variance optimiser than errors in the covariance matrix, so the return estimate is where robustness must be bought first.
