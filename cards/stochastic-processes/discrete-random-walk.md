# Discrete Random Walk Model

**Topic:** Stochastic Processes
**Level:** A Level Mathematics
**Tags:** random walk, discrete, simulation, price model, GBM

---

## Definition

The **discrete random walk model** is a step-by-step formula for generating asset price paths. At each time step, the price changes by a deterministic drift component plus a random shock drawn from a standard normal distribution, both scaled proportionally to the current price.

## Key Formula

$$S_{i+1} = S_i \left(1 + \mu \, \delta t + \sigma \, \phi \sqrt{\delta t}\right)$$

where:
- $\mu$ is the annualised drift
- $\sigma$ is the annualised volatility
- $\delta t$ is the time step as a fraction of a year
- $\phi \sim N(0, 1)$ is a fresh random draw at each step

## Example

With $S_0 = 100$, $\mu = 0.08$, $\sigma = 0.2$, $\delta t = 1/252$ (one trading day), and $\phi = 0.5$:

$$S_1 = 100 \left(1 + 0.08 \times \frac{1}{252} + 0.2 \times 0.5 \times \sqrt{\frac{1}{252}}\right)$$

$$S_1 = 100 \left(1 + 0.000317 + 0.006299\right) = 100.66$$

The drift contribution (£0.03) is tiny compared to the random shock (£0.63).

## Remember

This discrete model is the foundation of Monte Carlo simulation — run it thousands of times with different random draws to build a distribution of future prices. It is also the stepping stone to the continuous-time SDE $dS = \mu S \, dt + \sigma S \, dX$ that underpins Black-Scholes.
