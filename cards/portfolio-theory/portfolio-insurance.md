# Portfolio Insurance

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** portfolio insurance, protective put, cppi, gap risk, capital guarantee, structured products
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

Portfolio insurance is any strategy that guarantees a minimum portfolio value (the **floor**) at a specified horizon while retaining upside participation. The two main implementations are **option-based** (buy a protective put, transferring gap risk to the option seller at a known premium) and **CPPI** (synthetically replicate the put by dynamically scaling equity exposure to the available cushion, with no upfront option cost but residual gap risk).

## Key Formula

**Option-based floor:** Holding the risky asset $S$ and a European put with strike $K = F$:

$$V_T = S_T + \max(F - S_T,\; 0) = \max(S_T,\; F)$$

The put premium (cost of insurance) from Black-Scholes:

$$P_0 = F e^{-rT} N(-d_2) - S_0 N(-d_1)$$

**CPPI alternative (from the dynamic asset allocation card):**

$$E_t = m \cdot \max(V_t - F,\; 0), \qquad m > 1$$

where $m$ is the multiplier. CPPI requires no premium but carries **gap risk**: a sudden market fall past the floor before rebalancing breaches the guarantee.

## Example

A \£10m fund guarantees \£9m at year-end ($F = \text{\pounds}9\text{m}$):

**Option-based:** Buy a 1-year put with $S_0 = \text{\pounds}10\text{m}$, $K = \text{\pounds}9\text{m}$, $\sigma = 20\%$, $r = 4\%$. Using Black-Scholes, $P_0 \approx \text{\pounds}0.38\text{m}$. Invest £9.62m in equities + put. Floor is unconditionally guaranteed.

**CPPI:** Cushion $= \text{\pounds}1\text{m}$, $m = 5$: invest £5m in equities, £5m in bonds. No upfront cost. But if equities fall 25% overnight before rebalancing: equity value drops to £3.75m; $V = \text{\pounds}8.75\text{m} < F$ — floor breached.

## Remember

Portfolio insurance became infamous in the **1987 crash**: large US institutions ran CPPI-style dynamic hedging that required selling equities as markets fell. The cascade of sell orders amplified the decline, and when markets gapped down faster than portfolios could rebalance, many funds breached their floors — the very outcome the strategy was designed to prevent. This is why **option-based portfolio insurance is now preferred** for hard capital guarantees: the risk is transferred to a bank or derivatives dealer at a known, upfront cost. CPPI remains in widespread use for pension **liability-driven investment (LDI)** and structured notes where the floor is soft and the gap risk is accepted as the price of avoiding the option premium.
