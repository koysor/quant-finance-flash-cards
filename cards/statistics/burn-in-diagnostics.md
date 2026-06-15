# Burn-in Diagnostics

**Topic:** Statistics
**Tags:** MCMC, burn-in, Gelman-Rubin, effective sample size, convergence, Bayesian
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

Burn-in diagnostics are statistical tests that assess whether an MCMC chain has converged to its stationary distribution before samples are used for inference. The two standard tools are the **Gelman–Rubin statistic** $\hat{R}$ (comparing multiple parallel chains) and the **effective sample size** (ESS, correcting for autocorrelation within a chain).

## Key Formula

**Gelman–Rubin $\hat{R}$:** run $m$ chains of $n$ steps each. Let $B$ = between-chain variance and $W$ = average within-chain variance. The potential scale reduction factor is:

$$\hat{R} = \sqrt{\frac{\hat{V}}{W}}, \qquad \hat{V} = \frac{n-1}{n}W + \frac{m+1}{mn}B$$

Convergence is accepted when $\hat{R} < 1.1$ for all parameters.

**Effective Sample Size:** for autocorrelations $\rho_k$ at lag $k$ within a chain of length $n$:

$$\text{ESS} = \frac{n}{1 + 2\sum_{k=1}^{\infty} \rho_k}$$

A chain with high autocorrelation (slow mixing) has ESS $\ll n$; 100 effective samples per parameter is a common minimum threshold.

## Example

Calibrating a Heston model via MCMC: four parallel chains of 10,000 steps. For the vol-of-vol parameter $\xi$, $B \gg W$, giving $\hat{R} = 1.38$ — the chains have not mixed. ESS for $\xi$ is only 45. After reparameterising to $\log \xi$ and running 10,000 more steps, $\hat{R}$ drops to 1.02 and ESS rises to 820 — the posterior for $\xi$ is now trustworthy.

## Remember

In Bayesian calibration of derivatives pricing models, an $\hat{R} > 1.1$ means the posterior mean of a parameter depends on where the chain started, not on the data. Publishing implied volatility surface fits from a non-converged chain is the MCMC equivalent of reporting a sample mean from a biased sample: the number looks precise but is systematically wrong. Always report $\hat{R}$ and ESS alongside calibration results.
