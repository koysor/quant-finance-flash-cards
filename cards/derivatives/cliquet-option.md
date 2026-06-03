# Cliquet Option

**Topic:** Derivatives
**Tags:** cliquet, forward-start option, local floor, forward volatility, structured products, reset
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

A **cliquet option** (ratchet option) is a series of forward-start options whose strikes are set at the prevailing spot price on a sequence of reset dates $\{T_0, T_1, \ldots, T_{N-1}\}$. Each sub-period option pays a local return capped and floored, locking in gains periodically. Cliquets are common in structured equity products and capital-guaranteed notes — and they are the canonical instrument that stress-tests a model's **forward volatility** dynamics, since the value depends not just on today's smile but on the smile at every future reset date.

## Key Formula

Each **forward-start caplet** pays $\max(S_{T_{k+1}}/S_{T_k} - 1 - \text{cap}, \text{floor})$ at $T_{k+1}$. The total cliquet payoff is:

$$\Pi = \sum_{k=0}^{N-1} \min\!\left(\max\!\left(\frac{S_{T_{k+1}}}{S_{T_k}} - 1,\; f_k\right),\; c_k\right)$$

where $f_k$ and $c_k$ are the local floor and cap for period $k$. Each sub-option has **reset strike** $K_k = S_{T_k}$ set at the start of period $k$ — it is **at-the-money forward** at $T_k$ and therefore priced using the forward smile at $T_k$, not the current smile.

## Example

A 3-year cliquet with annual resets, local floor $f = 0\%$, local cap $c = 8\%$. At $T_0 = 0$: $S_0 = 100$. At $T_1 = 1$: $S_1 = 107$, return = $+7\%$, contribution = $\min(7\%, 8\%) = 7\%$. At $T_2 = 2$: $S_2 = 95$, return = $-11.2\%$, contribution = $\max(-11.2\%, 0\%) = 0\%$. At $T_3 = 3$: $S_3 = 105$, return = $+10.5\%$, contribution = $\min(10.5\%, 8\%) = 8\%$. Total payoff = $15\%$.

## Remember

Cliquets are notoriously difficult to price because they depend on the **forward smile** — the implied vol surface at future dates — which is not uniquely pinned down by today's market smile. Local volatility (Dupire) and Heston produce very different forward smiles even when calibrated to the same current surface, leading to large pricing disagreements. Rough volatility and SLV produce more realistic forward smiles and are preferred for cliquet pricing. For RL, pricing a cliquet requires the agent to learn the joint distribution of $\{S_{T_1}, S_{T_2}, \ldots, S_{T_N}\}$ given $S_0$ — the state at each reset must include the previous reset level to track the ongoing payoff accumulation, making cliquets the multi-step, multi-state-variable benchmark for RL exotic pricing.
