# Outright Curve

**Topic:** Fixed Income
**Tags:** yield curve, interest rates, fixed income, term structure, government bonds, swaps
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **outright curve** is the yield curve for a specific instrument — such as government bonds or interest rate swaps — quoted in absolute yield terms (e.g. 4.25% for the 10-year gilt). It shows the actual level of rates at each maturity, as opposed to a **spread curve**, which expresses yields relative to a benchmark (e.g. gilts + 80 basis points). Outright curves are the raw material from which spread curves and relative-value measures are derived.

## Key Formula

For a zero-coupon government bond of maturity $T$, the **outright yield** $y(T)$ is the single constant rate that discounts the par payment back to the current price $P(T)$:

$$P(T) = \frac{1}{(1 + y(T))^T} \quad \Longrightarrow \quad y(T) = P(T)^{-1/T} - 1$$

The **outright curve** is the function $T \mapsto y(T)$ observed across a set of benchmark maturities (e.g. 2Y, 5Y, 10Y, 30Y).

## Example

On a given day, the UK gilt outright curve shows:

| Maturity | Outright Yield |
|----------|---------------|
| 2Y       | 4.10%         |
| 5Y       | 4.30%         |
| 10Y      | 4.55%         |
| 30Y      | 4.80%         |

A trader considering a 10-year gilt knows immediately that the absolute yield on offer is 4.55%. If the same trader then compares the 10-year swap rate of 4.80%, the 25 basis-point difference is the swap spread — a relative measure derived from the outright curves of both instruments.

## Remember

In rates markets, traders always distinguish between **outright risk** (exposure to the absolute level of yields) and **spread risk** (exposure to the difference between two curves). A position in 10-year gilts is primarily an outright trade — if the entire outright curve shifts up by 10 basis points, the position loses money regardless of what corporate or swap curves do. Understanding which curve is being quoted in outright terms is essential before sizing any fixed-income position, because duration and DV01 (dollar value of a basis point) are calculated against the outright yield, not against a spread.
