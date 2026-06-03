# RL Option Pricing

**Topic:** Computational Finance
**Tags:** reinforcement learning, option pricing, model-free, bellman equation, deep learning, tdbp
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**RL option pricing** is a data-driven approach in which a reinforcement learning agent learns to estimate derivative fair values by iterating the Bellman equation over simulated or historical price paths, without assuming a specific parametric model for the underlying dynamics. The agent treats pricing as a **conditional expectation estimation** problem at each point in the time–space domain.

## Key Formula

The RL pricing objective at each time step is to minimise the **Bellman residual**:

$$\mathcal{L} = \mathbb{E}\!\left[\Bigl(P_t - e^{-r\Delta t}\,\mathbb{E}[P_{t+1} \mid s_t]\Bigr)^2\right]$$

where $P_t$ is the network's price estimate at state $s_t = (S_t, \tau, \ldots)$. At maturity, the terminal condition $P_T = \text{payoff}(S_T)$ anchors the backward induction. The agent requires only:
- A source of price paths (simulated or historical)
- The terminal payoff function
- The risk-free discount factor $e^{-r\Delta t}$

## Example

A TDBP agent trains on 50,000 GBM paths for a 100-day barrier call (knock-out at 110). Traditional Monte Carlo requires 100,000 new paths per pricing request. After a one-off 30-minute training phase, the RL agent prices any $(S_0, \sigma, T)$ combination in under 1 ms with errors below 0.5% versus the closed-form barrier price.

## Remember

RL option pricing offers three structural advantages over PDE and Monte Carlo methods: (1) **inference speed** — pricing is a single forward pass through the trained network, enabling real-time Greeks and scenario analysis; (2) **model agnosticism** — the same algorithm prices options under GBM, Heston, Merton-Heston, or DPL-constrained dynamics without model-specific solvers; (3) **path-dependent instruments** — barrier, Asian, and lookback payoffs are handled naturally since the agent trains directly on the path distribution.
