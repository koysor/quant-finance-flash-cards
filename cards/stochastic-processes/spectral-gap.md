# Spectral Gap

**Topic:** Stochastic Processes
**Tags:** spectral gap, eigenvalue, Markov chain, mixing time, MCMC, convergence
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The spectral gap of a Markov chain with transition matrix $P$ is the difference between its two largest eigenvalues: $\delta = 1 - \lambda_2$, where $\lambda_1 = 1$ is always the leading eigenvalue and $\lambda_2 < 1$ is the second largest. A large spectral gap means fast mixing; a gap near zero means the chain forgets its starting state extremely slowly.

## Key Formula

For an ergodic, reversible Markov chain with eigenvalues $1 = \lambda_1 > \lambda_2 \geq \ldots \geq \lambda_n \geq -1$:

$$\delta = 1 - \lambda_2$$

The mixing time is bounded by the spectral gap:

$$\tau_{\text{mix}}(\varepsilon) \leq \frac{1}{\delta} \ln\!\left(\frac{1}{\varepsilon \,\pi_{\min}}\right)$$

where $\pi_{\min} = \min_i \pi_i$ is the smallest stationary probability. Doubling the spectral gap halves the mixing time.

## Example

An MCMC sampler for Heston model parameters has second eigenvalue $\lambda_2 = 0.97$, giving spectral gap $\delta = 0.03$. With $\pi_{\min} \approx 10^{-3}$ and $\varepsilon = 0.01$:

$$\tau_{\text{mix}} \lesssim \frac{1}{0.03}\ln\!\left(\frac{1}{0.01 \times 10^{-3}}\right) \approx 33 \times 11.5 \approx 380 \text{ steps}$$

After reparameterising (sampling $\log \kappa$ instead of $\kappa$), the second eigenvalue drops to $\lambda_2 = 0.80$ and $\delta = 0.20$, reducing the bound to around 60 steps — a 6× speedup.

## Remember

When calibrating stochastic volatility models via MCMC, a poorly conditioned proposal distribution can collapse the spectral gap to near zero, causing millions of iterations to still reflect the starting point rather than the posterior. Reparameterisation — sampling $\log \sigma$ instead of $\sigma$, or using a centred versus non-centred parameterisation — is the standard fix: it enlarges the spectral gap and makes burn-in tractable.
