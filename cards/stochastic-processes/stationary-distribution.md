# Stationary Distribution

**Topic:** Stochastic Processes
**Tags:** stationary distribution, Markov chain, invariant measure, ergodicity, interest rate models, mean reversion
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The stationary distribution $\pi$ of a Markov process is the unique probability distribution that the process leaves unchanged: if the chain starts in $\pi$, it remains in $\pi$ at all future times. For an ergodic Markov chain, the process converges to $\pi$ from any starting state.

## Key Formula

**Discrete (Markov chain):** $\pi$ satisfies the balance equation

$$\pi P = \pi, \quad \sum_i \pi_i = 1$$

where $P$ is the transition matrix. Equivalently, the detailed balance condition (sufficient but not necessary for stationarity):

$$\pi_i P_{ij} = \pi_j P_{ji}$$

**Continuous (diffusion):** $\pi(x)$ is the steady-state density solving the Fokker–Planck equation

$$0 = -\frac{\partial}{\partial x}[\mu(x)\pi(x)] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x)\pi(x)]$$

## Example

The Vasicek short-rate model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ has stationary distribution

$$\pi = \mathcal{N}\!\left(\theta,\, \frac{\sigma^2}{2\kappa}\right)$$

With $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.01$: the long-run rate is $\mathcal{N}(4\%,\, 0.01\%)$, so the short rate spends the vast majority of time between 2% and 6%.

## Remember

Calibrating a mean-reverting interest rate model sets $\theta$ to match the centre of the stationary distribution and $\kappa$ to control how quickly the rate returns to it. A poorly calibrated $\kappa$ misprices long-dated bonds because the model's stationary distribution — the distribution that governs rates in the distant future — is too wide or too narrow relative to market-implied terminal distributions.
