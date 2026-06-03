# RL Dynamic Hedging

**Topic:** Computational Finance
**Tags:** reinforcement learning, dynamic hedging, delta hedging, hedge ratio, p&l variance, transaction costs
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**RL dynamic hedging** trains a reinforcement learning agent to learn hedge ratios directly from simulated or historical paths by minimising a risk objective — typically the variance of the hedged P&L or a risk-adjusted cost. Unlike Black-Scholes delta hedging, the RL agent jointly optimises the hedge ratio and the rebalancing frequency, accounting for transaction costs and discrete trading in the reward function.

## Key Formula

The agent selects a hedge ratio $\delta_t$ (units of underlying held) at each step to minimise the expected hedged P&L risk. The per-step reward penalises both residual risk and transaction cost:

$$r_t = -\frac{1}{2}\lambda\,\text{Var}(\Delta \Pi_t) - c\,\lvert \delta_t - \delta_{t-1} \rvert$$

where $\Delta \Pi_t = \Delta V_t - \delta_t \Delta S_t$ is the hedging P&L, $\lambda$ is risk aversion, and $c$ is the proportional transaction cost. The agent maximises:

$$G = \mathbb{E}\!\left[\sum_{t=0}^{T} r_t\right]$$

## Example

An RL agent hedges a short ATM call on a £100 stock with $\sigma = 20\%$, $T = 30$ days, transaction cost $c = 0.01\%$ per £ traded. Black-Scholes delta hedging (daily rebalance) produces a hedging error standard deviation of £0.42 and £1.20 in total transaction costs. The RL agent, trained with $\lambda = 1$, learns to rebalance less frequently when gamma is low (far from expiry, far from strike) and more frequently near expiry — achieving £0.38 hedging error std and £0.85 transaction costs, a Pareto improvement on both dimensions.

## Remember

RL dynamic hedging naturally solves the **rebalancing frequency trade-off** that Black-Scholes delta hedging ignores: it learns to hedge aggressively when gamma is high (near-the-money, near-expiry) and loosely when gamma is low, internalising transaction costs into the objective. It also extends naturally to higher-order hedging — by adding the underlying's volatility or a second option as hedging instruments, the agent can learn to neutralise gamma and vega exposure simultaneously, a task that requires manual intervention in classical Greeks-based hedging frameworks.
