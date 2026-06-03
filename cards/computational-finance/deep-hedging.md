# Deep Hedging

**Topic:** Computational Finance
**Tags:** deep hedging, convex risk measure, hedging strategy, neural network, transaction costs, incomplete markets
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Deep Hedging** (Buehler et al., 2019) is a framework that casts derivatives hedging as a constrained optimisation problem: find the admissible trading strategy $\pi$ that minimises a **convex risk measure** of the hedging P&L at expiry. A recurrent neural network parameterises $\pi$, taking market features as inputs at each step, and the network is trained end-to-end by gradient descent through the risk measure objective.

## Key Formula

The deep hedging objective is:

$$\pi^* = \arg\min_{\pi \in \mathcal{A}}\; \rho\!\left(Z - V_T(\pi)\right)$$

where $Z$ is the derivative payoff at expiry $T$, $V_T(\pi)$ is the terminal wealth of the hedging portfolio under strategy $\pi$, and $\rho$ is a convex risk measure. For **CVaR** at level $\alpha$:

$$\text{CVaR}_\alpha(X) = \min_{z \in \mathbb{R}}\left\{z + \frac{1}{1-\alpha}\,\mathbb{E}\!\left[\max(-X - z,\, 0)\right]\right\}$$

Transaction costs enter the portfolio dynamics directly: $V_{t+1}(\pi) = V_t(\pi) + \pi_t\,\Delta S_t - C(\Delta\pi_t, S_t)$, where $C$ is the cost function.

## Example

A market maker hedges a short straddle on FTSE 100 (short call + short put, $K = 7000$, $T = 30$ days). Under Black-Scholes delta hedging with daily rebalancing: CVaR$_{95\%}$ of the hedging loss = £420. Under deep hedging trained with CVaR$_{95\%}$ objective (proportional cost $c = 0.05\%$, 10,000 training paths): CVaR$_{95\%}$ = £310 — a 26% reduction — because the agent learns to hedge gamma more aggressively in the final week while reducing trades when gamma is low, saving costs that would have been wasted on delta adjustments far from expiry.

## Remember

Deep hedging is the formal union of RL dynamic hedging and risk management theory: by replacing the ad-hoc variance penalty of plain RL with a coherent convex risk measure (CVaR, Expected Shortfall), the framework produces strategies that are directly interpretable in terms of the desk's regulatory capital requirements. The key insight is that in **incomplete markets** — where transaction costs, discrete trading, or jumps prevent perfect replication — the "correct" hedge is not the replicating portfolio (which may not exist) but the risk-minimising feasible strategy, and a neural network is the most powerful function class for learning it.
