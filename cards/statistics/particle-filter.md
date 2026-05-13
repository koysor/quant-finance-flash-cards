# Particle Filter

**Topic:** Statistics
**Tags:** particle filter, sequential monte carlo, non-linear, bayesian filtering, stochastic volatility, hidden state
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

A **particle filter** (sequential Monte Carlo) approximates the posterior distribution of a hidden state using a set of weighted random samples called particles. It is the non-linear, non-Gaussian generalisation of the Kalman filter: where the Kalman filter requires linear dynamics and Normal noise, the particle filter handles arbitrary distributions by representing them empirically.

## Key Formula

At each time step $t$, $N$ particles $\{\theta^{(i)}_t\}_{i=1}^N$ approximate the filtering distribution. The importance weights are updated by the likelihood of the new observation:

$$w_t^{(i)} \propto w_{t-1}^{(i)} \cdot p(y_t \mid \theta_t^{(i)})$$

After reweighting, **resampling** draws $N$ new particles with replacement proportional to $w_t^{(i)}$, preventing weight degeneracy. The posterior mean is estimated as $\hat{\theta}_t = \sum_i w_t^{(i)} \theta_t^{(i)}$.

## Example

A quant filters the latent volatility $\sigma_t$ of an equity from a Heston model, where:

$$dS = \mu S\, dt + \sqrt{\sigma_t}\, S\, dW_1, \qquad d\sigma_t = \kappa(\bar{\sigma} - \sigma_t)\, dt + \xi\sqrt{\sigma_t}\, dW_2$$

With 1,000 particles, each propagated through the Heston dynamics and weighted by the likelihood of observed option prices, the particle filter tracks $\sigma_t$ in real time as new quotes arrive — producing a distribution over $\sigma_t$ rather than a single estimate, directly quantifying filtering uncertainty.

## Remember

The particle filter solves the problem that the Kalman filter cannot: when asset price dynamics are non-linear (jump-diffusion, stochastic volatility) or the observation equation is non-Normal (option implied vols are non-linearly related to the latent state), sequential Bayesian updating has no analytic form. The particle filter approximates it by brute-force Monte Carlo. In practice, it is used for real-time inference of hidden market states — latent volatility regimes, stochastic interest rate factors, and credit intensity processes — anywhere the state-space model is too complex for a Kalman filter.
