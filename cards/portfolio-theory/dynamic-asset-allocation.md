# Dynamic Asset Allocation

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** dynamic allocation, tactical allocation, cppi, rebalancing, constant-mix, lifecycle investing
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

Dynamic asset allocation adjusts a portfolio's asset-class weights over time in response to changing market conditions, return expectations, or investor circumstances — as distinct from static mean-variance optimisation, which solves once and never adapts. Three canonical strategies span the space: **buy-and-hold** (let drift dictate weights), **constant-mix** (rebalance to fixed target weights), and **CPPI** (protect a floor by scaling risky exposure to available cushion).

## Key Formula

**Constant Proportion Portfolio Insurance (CPPI):**

$$E_t = m \cdot \max(V_t - F,\; 0)$$

where $V_t$ is portfolio value, $F$ is the **floor** (minimum acceptable value), $m > 1$ is the **multiplier**, and $E_t$ is the £ amount allocated to the risky asset. The bond allocation absorbs the remainder: $B_t = V_t - E_t$.

**Cushion:** $C_t = V_t - F$. The risky weight is:

$$w_t^{\text{risky}} = \frac{m \cdot C_t}{V_t} = m\!\left(1 - \frac{F}{V_t}\right)$$

As $V_t \to F$ the cushion collapses, risky exposure $\to 0$, and the portfolio locks in the floor. As $V_t$ grows, the cushion expands and risky exposure rises.

## Example

Portfolio value $V = \text{\pounds}1{,}000{,}000$, floor $F = \text{\pounds}800{,}000$, multiplier $m = 4$.

Initial cushion: $C = 1{,}000{,}000 - 800{,}000 = \text{\pounds}200{,}000$.  
Equity allocation: $E = 4 \times 200{,}000 = \text{\pounds}800{,}000$ (80%).  
Bond allocation: $B = \text{\pounds}200{,}000$ (20%).

Equities now fall 20%: equity position drops to £640,000; $V' = 640{,}000 + 200{,}000 = \text{\pounds}840{,}000$.  
New cushion: $C' = 840{,}000 - 800{,}000 = \text{\pounds}40{,}000$.  
New equity: $E' = 4 \times 40{,}000 = \text{\pounds}160{,}000$ (19%) — CPPI has automatically de-risked.

## Remember

The three strategies have opposite convexity profiles: **constant-mix** is concave (buys dips, sells rallies — a contrarian, mean-reversion bet), while **CPPI** is convex (buys rallies, sells dips — a trend-following, momentum bet). The correct choice depends on market regime: constant-mix outperforms in oscillating markets, CPPI outperforms in trending ones. Pension funds and insurance companies use CPPI-style mechanisms to build **capital-guaranteed products** and **target-date funds** (glide paths), where protecting the floor represents the present value of the liability.
