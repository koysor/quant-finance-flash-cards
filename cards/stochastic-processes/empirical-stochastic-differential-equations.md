# Empirical Stochastic Differential Equations

**Topic:** Stochastic Processes
**Tags:** empirical sde, machine learning, drift, diffusion, non-parametric, calibration, simulation
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

An empirical SDE replaces the parametric drift and diffusion functions of a classical stochastic differential equation with machine-learning models trained on historical data, allowing the dynamics of an asset to be learnt directly from observations rather than assumed.

## Key Formula

The standard SDE for asset price $S_t$ is:

$$dS_t = \mu(S_t, t)\,dt + \sigma(S_t, t)\,dW_t$$

In the empirical approach, $\mu$ and $\sigma$ are replaced by trained ML functions estimated from discrete price increments:

$$\hat{\mu}(S_t, t) \approx \frac{\mathbb{E}[\Delta S_t \mid S_t]}{\Delta t}, \qquad \hat{\sigma}^2(S_t, t) \approx \frac{\mathbb{E}[(\Delta S_t)^2 \mid S_t]}{\Delta t}$$

Once trained, paths are simulated using the Euler-Maruyama scheme: $S_{t+\Delta t} = S_t + \hat{\mu}\,\Delta t + \hat{\sigma}\,\sqrt{\Delta t}\,Z$, where $Z \sim \mathcal{N}(0,1)$.

## Example

A neural network is trained on ten years of daily S&P 500 returns. Instead of assuming constant volatility (Black-Scholes), the network learns that $\hat{\sigma}$ is higher following negative returns (leverage effect) and lower on low-volume days. Simulating 10,000 paths with these empirical functions produces a distribution that exhibits volatility clustering, whereas GBM paths have constant volatility throughout.

## Remember

Classical models impose rigid functional forms on $\mu$ and $\sigma$, which is why Black-Scholes consistently mis-prices far-from-the-money options. Empirical SDEs let the data reveal the leverage effect, mean reversion, and volatility clustering directly, producing simulated paths that better reproduce the stylised facts of real financial markets and more accurate risk estimates.
