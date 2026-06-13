# Reward Normalisation

**Topic:** Machine Learning
**Tags:** reward normalisation, reward scaling, rl training, gradient stability, financial rl
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

Reward normalisation is the practice of standardising the reward signal received by a reinforcement learning agent — typically to zero mean and unit standard deviation — so that gradient magnitudes remain stable regardless of the absolute scale of financial returns. Without normalisation, reward magnitudes that differ across assets or market regimes cause erratic gradient steps and prevent the critic from learning a stable value function.

## Key Formula

**Running standardisation** (online, using Welford's algorithm):

$$\hat{r}_t = \frac{r_t - \hat{\mu}_t}{\hat{\sigma}_t + \varepsilon}$$

where $\hat{\mu}_t$ and $\hat{\sigma}_t$ are the running mean and standard deviation of all rewards seen so far, and $\varepsilon \approx 10^{-8}$ prevents division by zero. An alternative uses a **fixed window** (e.g. the last 1,000 rewards) or **exponential moving average** statistics:

$$\hat{\mu}_t = (1-\alpha)\hat{\mu}_{t-1} + \alpha r_t, \qquad \hat{\sigma}_t = \sqrt{(1-\alpha)\hat{\sigma}_{t-1}^2 + \alpha(r_t - \hat{\mu}_t)^2}$$

**Reward clipping** (simpler alternative):

$$\hat{r}_t = \text{clip}(r_t,\, -c,\, +c)$$

with $c$ typically 1 or 5, used in Atari DRL but less common in finance.

## Example

An RL agent learns to trade two assets simultaneously: an equity futures contract with daily P&L ranging from −\$50,000 to +\$50,000, and a bond futures contract ranging from −\$500 to +\$500. Without normalisation, the equity reward dominates gradients 100:1. The actor learns to trade equities aggressively while ignoring bonds entirely. With running standardisation, both streams are scaled to unit variance before the gradient computation — the agent learns both strategies simultaneously with comparable gradient contributions.

## Remember

Reward normalisation is the financial RL equivalent of feature scaling in supervised learning: raw financial rewards carry information about absolute magnitude (a \$1 million P&L is better than \$1,000) but gradient-based optimisation needs rewards in a consistent scale to make reliable step-size decisions. The choice of normalisation window matters: too long a window makes the agent slow to adapt when volatility regimes shift (the running std lags the new regime), while too short a window destroys information about the relative scale of different strategies. In practice, a separate reward normaliser per asset class or strategy, with an EMA half-life of 1,000–10,000 steps, is the standard approach in multi-asset RL systems.

