# Delivery Option Value

**Topic:** Fixed Income
**Tags:** delivery option value, bond futures, quality option, timing option, wild card, embedded option
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

Delivery option value is the economic worth of the bond futures short's right to choose which bond to deliver (quality option) and when within the delivery month to deliver it (timing options including the wild card), causing actual futures prices to trade below the theoretical no-delivery-option forward price of the CTD.

## Key Formula

The theoretical futures price assuming the CTD is fixed and delivery occurs at expiry is:

$$F^* = \frac{(P_{\text{CTD}} + AI_t)(1 + r_{\text{repo}})^{T-t} - c_{\text{CTD}} \cdot \Delta t - AI_T}{CF_{\text{CTD}}}$$

The actual futures price embeds the delivery option discount:

$$F = F^* - \frac{\text{DOV}}{CF_{\text{CTD}}}$$

where DOV (delivery option value) $> 0$ increases with:
- **Rate volatility** $\sigma_r$: larger yield moves create more CTD-switching probability
- **Basket breadth**: more eligible bonds means more quality option value
- **Time to expiry**: longer optionality window increases timing option value

Empirically, DOV $\approx 0.10$–$0.50$ per £100 nominal for standard government bond futures.

## Example

US 10-year note futures: theoretical price based on fixed CTD forward = 109.22. Actual futures price = 109.06. DOV contribution to price discount = $109.22 - 109.06 = 0.16$ (approximately 5 ticks of $\frac{1}{32}$). During the 2022 rate volatility spike ($\sigma_r$ doubled), the DOV on the same contract widened to 0.38 — over 12 ticks — because large yield moves made multiple bonds competitive for CTD status, increasing the quality option's value significantly.

## Remember

Delivery option value is why basis traders can earn a consistent (though small) risk premium by being long the basis — long cash CTD, short futures. They are selling the short's delivery optionality and earning the net basis as compensation. The strategy's risk is that a large rate move causes an unexpected CTD switch: the bond they are long ceases to be CTD, the futures price adjusts to reflect the new CTD, and the basis collapses. Understanding and monitoring the DOV is therefore essential for any cash-futures arbitrage strategy or for accurately pricing the fair value of bond futures contracts.
