# Transaction Cost Models

**Topic:** Computational Finance
**Tags:** transaction costs, proportional costs, market impact, rl hedging, spread, reward function
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Transaction cost models** quantify the cost of changing a hedge position and are embedded directly into the reward function of RL hedging agents. Three canonical forms are used: **proportional** (cost scales with trade size), **fixed** (flat cost per trade regardless of size), and **quadratic/market-impact** (cost scales with the square of trade size, reflecting price impact). The choice of model determines the shape of the optimal hedging strategy the agent learns.

## Key Formula

For a position change $\Delta\delta_t = \delta_t - \delta_{t-1}$ (units of underlying) at stock price $S_t$, the three cost components are:

$$C_t = \underbrace{c_p\,\lvert\Delta\delta_t\rvert\,S_t}_{\text{proportional spread}} + \underbrace{c_f\,\mathbf{1}_{\{\Delta\delta_t \neq 0\}}}_{\text{fixed fee}} + \underbrace{c_q\,(\Delta\delta_t\,S_t)^2}_{\text{quadratic impact}}$$

The RL agent's per-step reward is then:

$$r_t = \underbrace{(\delta_t - \delta_{t-1})\,\Delta S_t - C_t}_{\text{hedge P\&L minus cost}} - \frac{\lambda}{2}\,\text{Var}(\delta_t\,\Delta S_{t+1})$$

where $\lambda$ is the risk-aversion parameter.

## Example

An RL agent hedges a 30-day ATM call on a £100 stock. Three cost regimes:

| Model | Parameter | Optimal rebalancing | P&L std |
|---|---|---|---|
| Proportional only | $c_p = 0.02\%$ | Near-continuous near expiry | £0.41 |
| Fixed only | $c_f = £0.50$ | Infrequent, threshold-based | £0.58 |
| Quadratic only | $c_q = 0.001$ | Gradual, small trades | £0.37 |

Fixed costs force the agent to batch trades above a minimum threshold; quadratic costs spread trades across time; proportional costs encourage lazy hedging when moves are small.

## Remember

The transaction cost model shapes the **entire character** of the learned hedging strategy: proportional costs produce a dead-band around the target delta (the agent ignores small drift), fixed costs produce a pulse-based strategy (trade only when delta deviation exceeds a break-even threshold), and quadratic costs produce a smooth execution schedule (as in Almgren-Chriss optimal liquidation). In real markets all three are present simultaneously, making the combined model essential for training RL agents whose behaviour will match live trading conditions.
