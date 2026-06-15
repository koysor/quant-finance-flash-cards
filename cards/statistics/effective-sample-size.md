# Effective Sample Size

**Topic:** Statistics
**Tags:** effective sample size, MCMC, autocorrelation, spectral gap, convergence, Bayesian
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **effective sample size** (ESS) measures how many independent draws a correlated MCMC chain of length $n$ is equivalent to. Because successive MCMC samples are autocorrelated, $n$ raw draws carry less information than $n$ independent draws; ESS quantifies the information loss due to serial dependence.

## Key Formula

$$\text{ESS} = \frac{n}{1 + 2\displaystyle\sum_{k=1}^{\infty} \rho_k}$$

where $\rho_k$ is the autocorrelation of the chain at lag $k$. The denominator is the **integrated autocorrelation time** $\tau = 1 + 2\sum_{k=1}^{\infty}\rho_k$, so $\text{ESS} = n/\tau$.

The spectral gap $\delta = 1 - |\lambda_2|$ of the transition kernel controls how quickly autocorrelations decay, with $\tau$ approximately bounded by $1/\delta$: a larger spectral gap gives a smaller $\tau$ and a larger ESS per iteration.

## Example

A Metropolis–Hastings chain calibrating a Vasicek model runs for $n = 10{,}000$ iterations. Sample autocorrelations of the mean-reversion parameter $\kappa$ decay geometrically: $\rho_k \approx 0.8^k$.

$$\tau \approx 1 + 2 \cdot \frac{0.8}{1 - 0.8} = 1 + 8 = 9 \qquad \Rightarrow \qquad \text{ESS} \approx \frac{10{,}000}{9} \approx 1{,}111$$

Despite 10,000 raw iterations, only about 1,111 effectively independent samples of $\kappa$ are obtained. A chain with $\rho_k \approx 0.2^k$ would give $\tau \approx 1.5$ and ESS $\approx 6{,}700$ — more than a 6× gain from better mixing.

## Remember

Burn-in diagnostics (e.g. the Gelman–Rubin $\hat{R}$) confirm that the chain has converged; ESS confirms that enough post-convergence samples have been collected to make inference reliable. A practical rule of thumb for Bayesian model calibration is ESS $\geq 400$ per parameter to obtain stable 95% credible intervals. If ESS is low, running the chain for longer helps linearly, but switching to Hamiltonian Monte Carlo typically increases the spectral gap and ESS by an order of magnitude — the better fix when the chain is inherently slow to mix.
