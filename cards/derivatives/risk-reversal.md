# Risk Reversal

**Topic:** Derivatives
**Tags:** risk reversal, options strategy, skew, FX options, volatility smile, zero cost
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A risk reversal is long an OTM call at strike $K_c$ and short an OTM put at strike $K_p$ ($K_p < S < K_c$), typically structured as approximately zero-cost by choosing strikes such that $C(K_c) \approx P(K_p)$.

## Key Formula

$$\text{RR value} = IV(K_c) - IV(K_p)$$

Positive RR: calls trade at higher implied vol than equi-distant puts (bullish skew — e.g. commodities, some EM FX).

Negative RR: puts trade at higher implied vol than calls (bearish skew — equities, developed-market indices).

25-delta RR: buy 25$\Delta$ call, sell 25$\Delta$ put. Standard FX vol market quote.

## Example

EUR/USD 1-month 25-delta RR = $-0.5\%$: the 25$\Delta$ put has implied vol 0.5% higher than the 25$\Delta$ call. This means the market assigns higher probability to EUR falling sharply than rising sharply. A long RR profits if EUR rallies strongly.

## Remember

In FX, the risk reversal is one of the three standard vol market quotes (alongside ATM vol and the butterfly/strangle). Its sign and magnitude tell you the direction and size of the vol skew. In equity markets the RR is always negative — out-of-the-money puts are persistently expensive because of crash-insurance demand — and the steepness of the put skew is a direct measure of investor fear.
