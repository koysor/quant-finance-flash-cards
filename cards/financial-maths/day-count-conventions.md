# Day-Count Conventions

**Topic:** Financial Mathematics
**Tags:** day count, actual/360, actual/365, 30/360, accrued interest, fixed income, volatility convention
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

A day-count convention is a rule that specifies how to count the number of days between two dates for the purpose of calculating accrued interest, discount factors, or annualised rates. Different asset classes and markets use different conventions, so the same cash flows can produce different quoted rates depending on the convention applied — making cross-market comparisons of yields and volatilities require explicit convention adjustment.

## Key Formula

The year fraction between dates $d_1$ and $d_2$ under convention $X$ is:

$$\tau(d_1, d_2; X) = \frac{\text{Numerator days}(d_1, d_2; X)}{\text{Denominator}(X)}$$

| Convention | Numerator | Denominator | Used in |
|-----------|-----------|-------------|---------|
| Act/360 | Actual calendar days | 360 | USD/EUR money markets, LIBOR |
| Act/365 (fixed) | Actual calendar days | 365 | GBP money markets, equity vol |
| Act/Act (ICMA) | Actual days / coupon period | Coupon periods per year | Government bonds (ICMA) |
| Act/Act (ISDA) | Actual days in each year | 365 or 366 | Derivatives (ISDA) |
| 30/360 | Months × 30 + days (capped at 30) | 360 | US corporate/municipal bonds |

## Example

A bond pays a coupon on 1 March and 1 September. Accrued interest is computed on 15 April (45 actual days after 1 March).

- **Act/360**: $\tau = 45/360 = 0.1250$
- **Act/365**: $\tau = 45/365 = 0.1233$
- **30/360**: Numerator $= (4-3)\times30 + (15-1) = 44$ days; $\tau = 44/360 = 0.1222$

On a £10 million bond with a 5% coupon, these differences produce accrued interest of £6,250, £6,164, and £6,111 respectively — a £139 spread purely from convention choice.

For volatility: a 14% annualised vol quoted under 252 trading days converts to $14\% \times \sqrt{365/252} = 16.8\%$ under a 365-day convention — a 2.8 percentage point difference that is entirely a convention artefact.

## Remember

Day-count conventions are a persistent source of confusion when comparing fixed income yields across markets: a 5% EUR money market rate (Act/360) is not equivalent to a 5% GBP rate (Act/365) — the EUR rate is effectively $5\% \times 365/360 = 5.069\%$ on an Act/365 basis. For volatility, the equity market's 252-day convention and the bond market's 365-day convention mean that quoting a vol estimate without specifying the convention is ambiguous by up to 20% in relative terms. In derivatives documentation, the ISDA Master Agreement always specifies the day-count convention for each rate leg, because mismatched conventions in a swap can cause significant P&L discrepancies at settlement.

