# Hamiltonian Monte Carlo

**Topic:** Statistics
**Tags:** hamiltonian monte carlo, HMC, leapfrog, MCMC, gradient, Stan, Bayesian calibration
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

**Hamiltonian Monte Carlo** (HMC) is an MCMC algorithm that augments the parameter space with auxiliary momentum variables and uses gradient information — via simulated Hamiltonian dynamics — to propose large, high-probability moves. This eliminates the random-walk behaviour of Metropolis–Hastings and dramatically increases the spectral gap, making HMC far more efficient in high-dimensional posterior distributions.

## Key Formula

Define the **Hamiltonian** $H(\theta, p) = U(\theta) + K(p)$, where:

- $U(\theta) = -\log \pi(\theta \mid \text{data})$ — potential energy (negative log-posterior)
- $K(p) = \tfrac{1}{2} p^\top M^{-1} p$ — kinetic energy, with momentum $p \sim \mathcal{N}(0, M)$

The **leapfrog integrator** evolves the system for $L$ steps of size $\varepsilon$:

$$p_{t+\varepsilon/2} = p_t - \tfrac{\varepsilon}{2}\nabla_\theta U(\theta_t), \qquad \theta_{t+\varepsilon} = \theta_t + \varepsilon M^{-1} p_{t+\varepsilon/2}$$

The resulting proposal $(\theta^*, p^*)$ is accepted with probability $\min\!\bigl(1,\, e^{H(\theta,p) - H(\theta^*, p^*)}\bigr)$.

## Example

Calibrating a Hull–White model $(\alpha, \sigma)$ to cap prices, a random-walk Metropolis chain may require 50,000 iterations to achieve ESS $\approx 500$ for each parameter. An HMC implementation with $L = 20$ leapfrog steps and step size $\varepsilon = 0.05$ typically achieves the same ESS in around 2,000 iterations — roughly a 25× efficiency gain — because gradient guidance directs proposals to high-probability regions rather than diffusing randomly.

## Remember

Stan and PyMC use the **No-U-Turn Sampler** (NUTS), an adaptive HMC variant that automatically tunes $L$ and $\varepsilon$ during warm-up. In quantitative finance, HMC (via Stan) is the practical tool of choice for Bayesian calibration of multi-factor term structure models such as the ACM model or Wishart affine term structures — settings where the posterior is high-dimensional and sharply curved, exactly the regime where Metropolis–Hastings becomes prohibitively slow. The efficiency advantage of HMC grows with dimension, making it the preferred sampler whenever gradient computations are feasible.
