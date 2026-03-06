# Veta (Greeks)

**Topic:** Derivatives
**Tags:** veta, Greeks, sensitivity, options, vega, time decay
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

**Veta** (also called **DvegaDtime**) is the second-order Greek that measures the rate of change of Vega with respect to the passage of time. Formally, $\text{Veta} = \partial \nu / \partial t = \partial^2 V / \partial \sigma \, \partial t$. It tells a trader how their volatility exposure will decay as time passes, even if implied volatility and the underlying remain unchanged.

## Key Formula

For European options under Black-Scholes:

$$\text{Veta} = -S \, N'(d_1)\sqrt{T}\left[\frac{q + (r - q)d_1}{\sigma\sqrt{T}} - \frac{1 + d_1 d_2}{2T}\right]$$

For a non-dividend-paying stock ($q = 0$):

$$\text{Veta} = -S \, N'(d_1)\sqrt{T}\left[\frac{r \, d_1}{\sigma\sqrt{T}} - \frac{1 + d_1 d_2}{2T}\right]$$

Key properties:

- Veta is typically **negative** for ATM options — Vega decreases as expiry approaches (shorter-dated options are less sensitive to volatility).
- Long-dated ATM options have the largest Vega, so their Veta (rate of Vega decay) is most significant in absolute terms.
- Veta can be positive for deep ITM/OTM options under certain conditions.

## Example

A trader holds a calendar spread: long a 6-month ATM call ($\nu = 28.0$) and short a 1-month ATM call ($\nu = 12.5$). Net Vega: $+15.5$.

The 1-month option has $\text{Veta} \approx -55$ per year, while the 6-month option has $\text{Veta} \approx -22$ per year.

Over one week ($\Delta t = 7/365 = 0.0192$):

- Short leg Vega decay: $-(-55) \times 0.0192 = +1.05$ (the short Vega shrinks, helping the position)
- Long leg Vega decay: $-22 \times 0.0192 = -0.42$ (the long Vega shrinks, hurting the position)

Net effect: the spread's Vega advantage increases by about $+0.63$ per week. This is why calendar spreads benefit from the differential rate of Vega decay between the two legs.

## Remember

Veta is essential for managing **calendar spreads** and **diagonal spreads**, where the trader is long one expiry and short another. The profitability of these strategies depends on the front-month Vega decaying faster than the back-month — and Veta quantifies exactly how fast each leg's volatility sensitivity is eroding. Term-structure traders also monitor Veta across their book to understand how their aggregate Vega profile will shift day-by-day, ensuring they do not drift into unintended volatility exposure as time passes. Together with Charm (Delta decay) and Colour (Gamma decay), Veta completes the set of time-decay Greeks for the three primary risk dimensions.
