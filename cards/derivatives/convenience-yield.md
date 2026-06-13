# Convenience Yield

**Topic:** Derivatives
**Tags:** convenience yield, commodity futures, cost of carry, backwardation, contango, storage costs
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The convenience yield $y$ is the non-monetary benefit of holding a physical commodity rather than a futures contract — it reflects the value of immediate access to the commodity for production or to meet unexpected demand.

## Key Formula

$$F = S \cdot e^{(r + u - y)T}$$

where $r$ = risk-free rate, $u$ = storage cost rate (continuous), $y$ = convenience yield.

Implied convenience yield from futures:

$$y = r + u - \frac{1}{T}\ln\!\left(\frac{F}{S}\right)$$

Backwardation ($F < S$): $y > r + u$. Contango ($F > S$): $y < r + u$.

## Example

Crude oil: $S = \$80$/bbl, $r = 5\%$, $u = 3\%$, $T = 1$yr. If $F = \$78$: implied $y = 5\% + 3\% - \ln(78/80) = 8\% + 2.5\% = 10.5\%$. High $y$ reflects refiners' willingness to pay a premium to hold physical inventory.

## Remember

Unlike financial assets, commodities have convenience yield $> 0$ because running out of crude oil or natural gas shuts down operations — inventory has option-like value. This is why oil frequently trades in backwardation even though pure cost-of-carry would imply contango. Commodities futures curves are the market's implied signal about near-term physical tightness.
