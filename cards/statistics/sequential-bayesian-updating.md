# Sequential Bayesian Updating

**Topic:** Statistics
**Tags:** sequential bayes, online learning, kalman filter, bayesian updating, real-time, recursive estimation
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Sequential Bayesian updating** processes observations one at a time, treating the current posterior as the prior for the next observation. It produces the same result as batch Bayesian inference but requires storing only the current posterior — not the full dataset — making it efficient for real-time and streaming data.

## Key Formula

At each time step $t$, the posterior after observing $y_t$ becomes the prior for $y_{t+1}$:

$$\underbrace{p(\theta \mid y_1, \ldots, y_t)}_{\text{new prior}} \;\propto\; p(y_t \mid \theta) \times \underbrace{p(\theta \mid y_1, \ldots, y_{t-1})}_{\text{previous posterior}}$$

For a Normal model with known variance $\sigma^2$ and prior $\theta \sim \mathcal{N}(\mu_0, \tau_0^2)$, each observation $y_t$ updates:

$$\mu_t = \frac{\tau_{t-1}^2 \, y_t + \sigma^2 \, \mu_{t-1}}{\tau_{t-1}^2 + \sigma^2}, \qquad \frac{1}{\tau_t^2} = \frac{1}{\tau_{t-1}^2} + \frac{1}{\sigma^2}$$

## Example

A trading algorithm estimates the drift $\mu$ of a mean-reverting spread. At 09:00, prior: $\mu \sim \mathcal{N}(0, 0.01)$. After observing 20 ticks of data, the posterior is $\mathcal{N}(0.003, 0.0002)$ — the algorithm has updated its belief and widened its buy signal. By 15:00, after 500 ticks, the posterior uncertainty has shrunk to $\mathcal{N}(0.0028, 0.00002)$ — the estimate is sharp enough to trade confidently. No data needs to be stored after each tick is processed.

## Remember

Sequential Bayesian updating is the theoretical foundation of the **Kalman filter**, which is its linear Gaussian special case. In quantitative finance, it underpins real-time signal estimation in high-frequency trading (updating alpha estimates tick-by-tick), online parameter estimation in GARCH models (updating volatility forecasts as new returns arrive), and adaptive portfolio rebalancing (adjusting factor exposures as new macro data releases). The key advantage over batch re-estimation is computational: the recursive update is $O(1)$ per observation rather than $O(T)$ for full re-estimation, making it essential wherever latency matters.
