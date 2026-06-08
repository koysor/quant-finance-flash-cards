# Forward Rate Agreement (FRA)

**Topic:** Fixed Income
**Tags:** fra, forward rate agreement, isda, discounted settlement, single-period swap, money market
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

A **Forward Rate Agreement** is a bilateral contract that locks in an interest rate $K$ for a single future accrual period $[t^{as}, t^{ae}]$. Unlike a swap coupon that settles at the end of the period, an FRA uses **ISDA discounted settlement**: the net cash flow is paid at the fixing date (start of the period) rather than at maturity.

## Key Formula

At the ISDA settlement date $t^p \approx t^{as}$ (fixing + 2 business days), one party pays:

$$\frac{\delta(L^j(\theta) - K)}{1 + \delta L^j(\theta)}$$

| Term | Meaning |
|---|---|
| $\delta$ | Accrual factor for $[t^{as}, t^{ae}]$ |
| $L^j(\theta)$ | IBOR rate fixing at date $\theta$ |
| $K$ | Fixed rate agreed at initiation |
| Denominator | Discounts cash flow from period end back to period start at rate $L$ |

Without the denominator, settlement $\delta(L-K)$ would occur at period end $t^{ae}$. Dividing by $(1 + \delta L)$ moves it to $t^p$.

## Example

3×6 FRA (3-month accrual starting in 3 months), $K = 4\%$, $\delta = 0.5$ (Act/360, 6-month period). At fixing, IBOR sets at $L = 4.5\%$. Settlement paid at $t^p$:

$$\frac{0.5 \times (0.045 - 0.04)}{1 + 0.5 \times 0.045} = \frac{0.0025}{1.0225} = 0.002444 \text{ per unit notional}$$

On a \$10m notional this is \$24,440 — slightly less than the \$25,000 undiscounted amount.

## Remember

The ISDA FRA settlement formula is a **legal term sheet convention**, not a quant pricing formula. The denominator arises purely because market participants agreed to settle at the start of the accrual period rather than the end — it is not derived from any arbitrage argument. FRAs are fundamental building blocks for **curve calibration**: short-dated FRAs pin down forward rates at the near end of the yield curve before liquid swap tenors begin.
