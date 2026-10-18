# Term Spread and Net Interest Margin

**Topic:** Financial Mathematics
**Tags:** net interest margin, term spread, yield curve, maturity transformation, flat curve, inverted curve
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

Banks earn a **term spread** by borrowing short and lending long: the difference between the long-term rate earned on assets and the short-term rate paid on funding. The shape of the yield curve therefore drives net interest margin; a steep curve widens it, a flat curve compresses it, and an inverted curve can make maturity transformation lose money.

## Key Formula

For a mismatched book of notional $N$ lending at long rate $r_L$ and funded at short rate $r_S$:

$$\text{NII} \approx N\,(r_L - r_S), \qquad \text{NIM} \approx \frac{N\,(r_L - r_S)}{\text{Earning assets}}$$

The term spread $s = r_L - r_S$ is the slope of the curve between the two maturities.

## Example

A bank lends £10bn at the five-year rate and funds it at the three-month rate.

| Curve | $r_L$ | $r_S$ | Spread | Annual NII |
|---|---|---|---|---|
| Steep | 4.5% | 3.5% | 1.0% | £100m |
| Flat | 4.0% | 3.8% | 0.2% | £20m |
| Inverted | 3.5% | 4.0% | $-0.5\%$ | $-£50\text{m}$ |

## Remember

The same book that is profitable on a steep curve loses money when short rates overtake long rates, which is the classic way a rate-hiking cycle squeezes a liability-sensitive bank. This is also why a bank watches the slope rather than just the level of rates: a parallel rise leaves the spread unchanged, but a flattener cuts the margin. A flattener is also one of the six prescribed IRRBB shock scenarios.
