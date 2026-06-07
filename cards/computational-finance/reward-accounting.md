# Reward Accounting

**Topic:** Computational Finance
**Tags:** reward function, transaction costs, p&l attribution, reinforcement learning, simulation gap, mark-to-market
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

Reward accounting is the engineering discipline of computing the per-step RL reward so that it captures the **full economics** of each trade — gross P&L, transaction costs, funding charges, and mark-to-market conventions — ensuring that policies learnt in simulation remain valid when deployed live. Errors in reward accounting are the primary cause of the **simulation gap**: strategies that appear profitable in backtests but lose money in production.

## Key Formula

At each step $t$, the correctly accounted net reward for an agent holding weight vector $w_t$ is:

$$R_t = \underbrace{w_t^\top \Delta p_t}_{\text{gross P\&L}} - \underbrace{c\,\lVert w_t - w_{t-1} \rVert_1}_{\text{transaction costs}} - \underbrace{\kappa\,\hat{\sigma}_t^2}_{\text{risk penalty}}$$

where $\Delta p_t$ is the vector of asset price changes, $c$ is proportional cost per unit weight change, and $\kappa\,\hat{\sigma}_t^2$ is an optional variance penalty. The cumulative discounted return over an episode is:

$$G = \sum_{t=0}^{T-1} \gamma^t R_t$$

## Example

An agent holds 60% UK equities and 40% gilts, then rebalances to 50/50. Equities rise 1%, gilts fall 0.2%, transaction cost $c = 0.05\%$ per unit weight change.

Gross P&L: $0.6 \times 1\% + 0.4 \times (-0.2\%) = 0.52\%$  
Weight change: $\lVert \Delta w \rVert_1 = |{-}0.10| + |0.10| = 0.20$  
Transaction cost: $0.05\% \times 0.20 = 0.01\%$  
Net $R_t = 0.52\% - 0.01\% = 0.51\%$

If the simulation omitted transaction costs, the agent would incorrectly record $R_t = 0.52\%$ and learn to overtrade.

## Remember

The most common reward accounting error is **omitting transaction costs** from the training reward: the agent learns that frequent rebalancing is free and develops a high-turnover policy that profits in simulation but bleeds real money on costs. A subtler error is using **close-to-close** price changes when the strategy executes at the open — the reward accounts for returns the strategy never captured. Correct reward accounting is why systematic trading desks spend as much engineering effort on their simulation environment as on their ML models: the reward signal is the only source of truth the agent has, and any gap between simulated and real economics propagates into every weight in the learned policy.
