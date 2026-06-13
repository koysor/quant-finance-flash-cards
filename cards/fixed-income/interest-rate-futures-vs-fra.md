# Interest Rate Futures vs Forward Rate Agreement

**Topic:** Fixed Income
**Tags:** futures, FRA, forward rate agreement, convexity adjustment, daily margining, eurodollar
**Created:** 2026-06-11
**Author:** Claude Sonnet 4.6

---

## Definition

A **forward rate agreement (FRA)** locks in an interest rate for a future period and settles once in cash at the start of the accrual period. An **interest rate futures contract** (e.g. Eurodollar, SOFR futures) achieves the same economic exposure but settles daily via **variation margin**. The daily margining creates a correlation between the daily P&L and the prevailing discount rate, causing the futures rate to systematically differ from the FRA forward rate by the **convexity adjustment**.

## Key Formula

$$\text{Futures rate} = \text{FRA forward rate} + \text{convexity adjustment}$$

Under the Vasicek model with mean-reversion speed $a$ and volatility $\sigma$:

$$\text{Convexity adjustment} = \frac{\sigma^2}{2a^2}\!\left(1 - e^{-a T_1}\right)\!\left(1 - e^{-a T_2}\right)$$

where $T_1$ is the futures expiry and $T_2$ is the end of the underlying accrual period. For a simpler rule of thumb (approximate, for small adjustments):

$$\text{Adjustment} \approx \tfrac{1}{2}\sigma^2 T_1 T_2$$

| Feature | FRA | Eurodollar / SOFR Futures |
|---|---|---|
| Settlement | Single cash payment at accrual start | Daily variation margin throughout life |
| Convexity adjustment | None — futures rate adjusted to FRA equivalent | Yes — futures rate exceeds FRA rate |
| Credit risk | Bilateral counterparty exposure | Exchange-cleared, minimal |
| Liquidity | OTC, bespoke | Exchange-traded, very liquid |

## Example

Eurodollar futures expiry $T_1 = 2$ yr, accrual end $T_2 = 2.25$ yr. Vasicek parameters: $a = 0.1$, $\sigma = 0.01$. Convexity adjustment:

$$\frac{(0.01)^2}{2 \times (0.1)^2}(1-e^{-0.2})(1-e^{-0.225}) = 0.005 \times 0.181 \times 0.201 = 1.8 \text{ bp}$$

If the futures settles at $94.00$ (implying $6\%$), the FRA forward rate is approximately $6\% - 1.8 \text{ bp} = 5.982\%$. This 1.8 bp difference is small but grows quadratically with maturity — a 10-year futures has an adjustment of roughly 50 bp.

## Remember

The convexity adjustment arises because futures P&L is received or paid **immediately** each day, while FRA P&L is received only at settlement. When rates rise (futures loses), the daily loss must be funded at the now-higher rate — a negative carry effect. This asymmetry means the futures holder demands a higher fixed rate than the FRA to compensate, so futures rates always exceed FRA forward rates for a positively-sloped volatility term structure. Ignoring the convexity adjustment when stripping a yield curve from futures prices systematically underestimates forward rates at long maturities — a source of mispricing in interest rate derivatives.
