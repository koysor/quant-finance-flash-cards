# LIBOR in Arrears Swap

**Topic:** Fixed Income
**Tags:** in-arrears, LIBOR, convexity adjustment, forward measure, swap, timing mismatch
**Created:** 2026-06-12
**Author:** Claude Sonnet 4.6

---

## Definition

In a standard floating swap, the LIBOR rate fixes at the **start** of the accrual period $T_i$ and is paid at the **end** $T_{i+1}$. In a **LIBOR in arrears swap**, the rate fixes and is paid on the same date $T_{i+1}$ — eliminating the delay between observation and payment. This timing change introduces a **convexity adjustment** because the payment date no longer matches the measure under which the forward rate is defined.

## Key Formula

The in-arrears rate exceeds the standard forward LIBOR rate $F$ by a positive convexity adjustment. Under the lognormal model with volatility $\sigma$:

$$\text{In-arrears rate} = F + \frac{\delta \sigma^2 F^2}{1 + \delta F}$$

where $\delta = T_{i+1} - T_i$ is the accrual fraction. Under the normal model with absolute volatility $\sigma_N$:

$$\text{In-arrears adjustment} = \frac{\delta \sigma_N^2}{1 + \delta F}$$

| Feature | Standard swap | In-arrears swap |
|---|---|---|
| Fixing date | $T_i$ (start of period) | $T_{i+1}$ (end of period) |
| Payment date | $T_{i+1}$ | $T_{i+1}$ |
| Natural measure | $T_{i+1}$-forward (payment = maturity) | $T_i$-forward, but paid at $T_{i+1}$ |
| Convexity adjustment | None | Positive |

## Example

3-month LIBOR in arrears swap. $\delta = 0.25$ yr, forward rate $F = 5\%$, lognormal vol $\sigma = 25\%$.

$$\text{Adjustment} = \frac{0.25 \times (0.25)^2 \times (0.05)^2}{1 + 0.25 \times 0.05} = \frac{0.25 \times 0.0625 \times 0.0025}{1.0125} = \frac{0.0000391}{1.0125} \approx 3.9 \text{ bp}$$

The in-arrears coupon is approximately $5\% + 3.9 \text{ bp} = 5.039\%$. This grows quadratically with forward vol — at $\sigma = 50\%$ the adjustment is 16 bp.

## Remember

The in-arrears adjustment is always **positive** because fixing later (at the end of the period) creates a favourable correlation: when rates are high, the in-arrears payment is higher, and high rates coincide with a lower present value of the payment — the holder receives more precisely when discounting is cheapest. This is the same asymmetry that drives the Eurodollar futures convexity adjustment, but for a single coupon date rather than daily margining. In practice, in-arrears swaps are used by structured note issuers to match funding profiles, and their pricing requires explicit convexity adjustment — failing to apply it causes systematic underpricing of the floating leg.
