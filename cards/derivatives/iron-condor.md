# Iron Condor

**Topic:** Derivatives
**Tags:** iron condor, options strategy, short volatility, income strategy, defined risk, neutral
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

An iron condor sells an OTM put spread ($K_1$/$K_2$, where $K_1 < K_2 < S$) and an OTM call spread ($K_3$/$K_4$, where $S < K_3 < K_4$); it collects premium if the underlying stays between $K_2$ and $K_3$ at expiry.

## Key Formula

$$\text{Net credit} = [P(K_2) - P(K_1)] + [C(K_3) - C(K_4)] > 0$$

$$\text{Max profit} = \text{net credit} \quad \text{(if } K_2 \le S_T \le K_3\text{)}$$

$$\text{Max loss} = \text{wing width} - \text{net credit} = (K_2 - K_1) - \text{credit} \quad \text{(same for each wing)}$$

Break-even: $S_T = K_2 - \text{credit}$ or $S_T = K_3 + \text{credit}$.

## Example

$S = 100$, $K_1/K_2 = 85/90$, $K_3/K_4 = 110/115$. Sell put spread for \$1.50, sell call spread for \$1.50. Net credit $= \$3$. Max profit $= \$3$, max loss $= \$5 - \$3 = \$2$ per wing. Profitable if $S_T \in [87, 113]$.

## Remember

The iron condor is the most popular retail income strategy — a short strangle with protective wings that limit catastrophic loss. It has positive theta (collects time decay daily) and negative vega (loses if implied vol rises). A spike in the VIX can make an iron condor unprofitable even if the underlying doesn't reach the break-evens, because the short options reprice at higher implied vol before expiry.
