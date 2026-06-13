# Ho–Lee Bond Price Formula

**Topic:** Fixed Income
**Tags:** Ho-Lee, bond pricing, exponential affine, convexity correction, A function
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

Under the Ho–Lee model the zero-coupon bond price is **exponential-affine in the current spot rate** $r$, with a deterministic function $A(t;T)$ that encodes the history of the calibrated drift $\eta(t)$ and a convexity correction from rate uncertainty.

## Key Formula

$$Z(r,t;T) = \exp\!\Bigl(A(t;T) - r(T-t)\Bigr)$$

$$A(t;T) = -\int_t^T \eta(s)(T-s)\,ds + \frac{1}{6}c^2(T-t)^3$$

| Term | Meaning |
|---|---|
| $r(T-t)$ | Pure discounting at the current spot rate over time to maturity |
| $-\int_t^T \eta(s)(T-s)\,ds$ | Effect of the time-varying drift on future rates |
| $\tfrac{1}{6}c^2(T-t)^3$ | Convexity correction — Jensen's inequality adjustment for rate uncertainty |

The implied **continuously compounded yield** is:

$$Y(r,t;T) = r - \frac{A(t;T)}{T-t} = r + \frac{1}{T-t}\int_t^T \eta(s)(T-s)\,ds - \frac{c^2(T-t)^2}{6}$$

## Example

With $c = 1\%$, $\eta(s) = 0.003$ (constant for simplicity), $r = 4\%$, and $T - t = 5$ years: $A = -0.003 \times \tfrac{5^2}{2} + \tfrac{(0.01)^2 \times 5^3}{6} = -0.0375 + 0.0000208 \approx -0.0375$. Bond price $= e^{-0.0375 - 0.04 \times 5} = e^{-0.2375} = 0.788$.

## Remember

The cubic term $\tfrac{1}{6}c^2(T-t)^3$ is the signature of **no mean reversion**: without mean reversion, rate uncertainty grows without bound and the convexity correction grows as the cube of maturity. In the Hull–White model the equivalent term is smaller because mean reversion dampens long-run uncertainty. This difference means Ho–Lee systematically overprices convexity for long-maturity bonds relative to Hull–White.
