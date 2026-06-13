# Market Price of Risk from Yield-Curve Slope

**Topic:** Fixed Income
**Tags:** market price of risk, yield curve slope, short end, lambda estimation, empirical, interest rate
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **market price of interest rate risk** $\lambda(r)$ is invisible in spot-rate time-series data — it only affects instruments with non-zero maturity. The slope of the yield curve at the short end provides the sole empirical window onto $\lambda$: a short-maturity bond's yield equals the spot rate plus a correction proportional to $(u - \lambda w)/2$ times the time to maturity.

## Key Formula

Expanding the bond price $Z(r,t;T)$ for small time to maturity $\tau = T - t$ via the pricing PDE:

$$-\frac{\ln Z}{\tau} \approx r + \frac{u(r) - \lambda(r)w(r)}{2}\,\tau + O(\tau^2)$$

Since $u(r)$ and $w(r)$ are already estimated from historical rate data (stages 1 and 2), observing the **empirical yield–maturity slope** at the short end extracts $u - \lambda w$, and hence:

$$\lambda(r) = \frac{u(r) - 2\,\text{slope}(r)}{w(r)}$$

## Example

Suppose $u(r) = 0.01$ at $r = 5\%$, $w(r) = 0.006$, and the empirical short-end yield slope is $0.008$ (8 bp per year). Then $u - \lambda w = 2 \times 0.008 = 0.016$, giving $\lambda = (0.01 - 0.016)/0.006 = -1.0$. This negative value means investors accept a lower yield than expected — they are paying for the protection bonds provide in bad economic states.

## Remember

In practice, $\lambda(r)$ extracted from US Treasury yield-curve data is **extremely noisy** — fluctuating between approximately $-25$ and $+15$ across the 1986–1995 sample. This is not a data problem; it reflects a genuine information limit. The slope of the short end of the yield curve is simultaneously affected by expectations, term premium, liquidity, and supply/demand — making $\lambda$ very hard to isolate. This empirical messiness propagates directly into the prices of all interest rate derivatives, which is a fundamental source of model risk.
