# Yield Curve Bootstrapping

**Topic:** Fixed Income
**Level:** A Level Mathematics
**Tags:** bootstrapping, yield curve, zero rate, discount factor, swap rate, fixed income
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Yield curve bootstrapping is the sequential process of extracting zero-coupon (spot) rates and discount factors from observed market instrument prices — typically deposit rates for the short end, futures or FRAs for the middle, and swap rates for the long end. Starting from the shortest maturity, each instrument is used to solve for the next unknown discount factor, building the curve one point at a time. The resulting zero curve is the foundation for pricing all fixed-income instruments and derivatives.

## Key Formula

Given par swap rates $c_1, c_2, \ldots, c_n$ and previously bootstrapped discount factors $d_1, \ldots, d_{k-1}$, the next discount factor $d_k$ is:

$$d_k = \frac{1 - c_k \sum_{i=1}^{k-1} d_i}{1 + c_k}$$

The **zero rate** at maturity $t_k$ is:

$$r_k = -\frac{\ln d_k}{t_k}$$

The **forward rate** between $t_{k-1}$ and $t_k$:

$$f_{k-1,k} = \frac{\ln d_{k-1} - \ln d_k}{t_k - t_{k-1}}$$

## Example

Market quotes (annual payment, act/365):

| Instrument | Maturity | Rate |
|-----------|----------|------|
| Deposit | 1y | 4.50% |
| Swap | 2y | 4.80% |
| Swap | 3y | 5.00% |

**Step 1** — 1-year discount factor from the deposit rate:

$$d_1 = \frac{1}{1.045} = 0.9569$$

**Step 2** — 2-year discount factor from the 2y swap ($c_2 = 4.80\%$):

$$d_2 = \frac{1 - 0.048 \times 0.9569}{1 + 0.048} = \frac{1 - 0.04593}{1.048} = \frac{0.95407}{1.048} = 0.9104$$

**Step 3** — 3-year discount factor from the 3y swap ($c_3 = 5.00\%$):

$$d_3 = \frac{1 - 0.05 \times (0.9569 + 0.9104)}{1 + 0.05} = \frac{1 - 0.09337}{1.05} = \frac{0.90663}{1.05} = 0.8635$$

Zero rates: $r_1 = 4.50\%$, $r_2 = -\frac{\ln 0.9104}{2} = 4.69\%$, $r_3 = -\frac{\ln 0.8635}{3} = 4.89\%$.

## Remember

Bootstrapping is the first task a quant developer performs on a rates desk — every morning, the curve is rebuilt from fresh market quotes, and every instrument on the book is revalued against it. The bootstrapped zero curve is the single most important object in fixed-income pricing: it determines discount factors for cash flow valuation, forward rates for floating-leg projections, and swap rates for mark-to-market. Post-LIBOR, dual-curve bootstrapping (separate projection and discounting curves) is standard — one curve for forecasting SOFR/SONIA forwards, another (OIS-based) for discounting. Understanding bootstrapping deeply — including the choice of interpolation method between knots, the handling of turn-of-year effects, and the propagation of input sensitivities — is essential because errors in the curve propagate to every price on the desk.
