# MPT in Practice — Drawbacks and Solutions

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** MPT, estimation error, covariance matrix, parameter uncertainty, robust optimisation
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

Modern Portfolio Theory (Markowitz, 1952) is widely adopted — used by 83% of quantitative equity managers — but has two fundamental practical limitations: the **dimensionality problem** and the **parameter estimation problem**. Practitioners have developed two schools of solutions.

## Key Formula

**Parameter count for $N$ assets:**

$$\text{Full covariance matrix} = \frac{N(N+1)}{2} \text{ parameters}$$

For $N = 500$: $\frac{500 \times 501}{2} = 125{,}250$ parameters.

**Sensitivity of optimal weights to input errors:**

Small perturbations in $\boldsymbol{\mu}$ (expected returns) can completely reverse optimal allocations — optimisers are "error maximisers" when inputs are noisy.

| Input | Stability | Estimation problem |
|---|---|---|
| Variances & covariances | Relatively stable | Manageable with 3–5 years of data |
| Expected returns | Highly unstable | Requires hundreds of years for precision |

## Example

With $N = 50$ assets and only 3 years of daily data (~750 observations), the ratio of parameters to observations for the covariance matrix alone is $50 \times 51 / 2 = 1{,}275$ parameters vs 750 data points — the matrix is **rank-deficient** and cannot be inverted reliably without regularisation.

## Remember

**Two schools of solutions:** (1) Improve the 1-period framework — use factor models to reduce dimensionality, Bayesian shrinkage or Black-Litterman to stabilise return estimates, and robust optimisation to make weights less sensitive to input errors. (2) Multi-period stochastic programming — model left-tail scenarios explicitly, use dynamic methods such as Kalman filtering, and accept that the single-period mean-variance framework is a simplification. In practice, most institutional systems use factor models plus some form of regularisation or Bayesian return estimation.
