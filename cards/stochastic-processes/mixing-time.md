# Mixing Time

**Topic:** Stochastic Processes
**Tags:** mixing time, Markov chain, MCMC, burn-in, convergence, Monte Carlo
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The mixing time of a Markov chain is the minimum number of steps needed for the chain's distribution to come within a specified tolerance $\varepsilon$ of its stationary distribution, regardless of the starting state. It governs how long a burn-in period is required before MCMC samples can be trusted.

## Key Formula

$$\tau_{\text{mix}}(\varepsilon) = \min\!\left\{t : \max_{x}\, \lVert P^t(x, \cdot) - \pi \rVert_{\text{TV}} \leq \varepsilon\right\}$$

where $\lVert \mu - \nu \rVert_{\text{TV}} = \frac{1}{2}\sum_i \lvert \mu_i - \nu_i \rvert$ is the total variation distance. The standard choice is $\varepsilon = \tfrac{1}{4}$.

Mixing time is bounded by the **spectral gap** $\delta = 1 - \lambda_2$, where $\lambda_2$ is the second-largest eigenvalue of $P$:

$$\tau_{\text{mix}}(\varepsilon) \leq \frac{1}{\delta}\ln\!\left(\frac{1}{\varepsilon \pi_{\min}}\right)$$

## Example

An MCMC sampler explores a posterior distribution for stochastic volatility model parameters. The chain starts far from the high-probability region. With spectral gap $\delta = 0.02$ and $\pi_{\min} \approx 10^{-4}$ at $\varepsilon = 0.01$, the mixing-time bound gives roughly $\frac{1}{0.02}\ln(10^6) \approx 690$ steps. The practitioner discards the first 1,000 draws as burn-in to be safe.

## Remember

In Bayesian calibration of derivatives pricing models (e.g. using MCMC to fit Heston or SABR parameters to option prices), ignoring mixing time leads to biased parameter estimates: the early samples are anchored near the arbitrary starting point rather than the true posterior. A short burn-in on a slowly mixing chain is a common source of model mis-calibration.
