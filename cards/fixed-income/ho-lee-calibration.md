# Ho–Lee Calibration Formula

**Topic:** Fixed Income
**Tags:** Ho-Lee, calibration, double differentiation, forward rate, drift recovery
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **Ho–Lee calibration formula** gives the exact time-dependent drift $\eta^*(t)$ that makes the model reproduce today's entire market yield curve. It is derived by differentiating the bond-price integral equation twice with respect to maturity $T$, using Leibniz's rule to peel off the integral.

## Key Formula

Starting from the integral equation (setting model = market price):

$$\int_{t^*}^T \eta^*(s)(T-s)\,ds = -\log Z_M(t^*;T) - r^*(T-t^*) + \tfrac{1}{6}c^2(T-t^*)^3$$

Differentiating **twice** with respect to $T$ via Leibniz's rule:

$$\frac{d}{dT}: \quad \int_{t^*}^T \eta^*(s)\,ds = \frac{\partial}{\partial T}\!\Bigl[-\log Z_M + \cdots\Bigr]$$

$$\frac{d^2}{dT^2}: \quad \eta^*(T) = c^2(T - t^*) - \frac{\partial^2}{\partial T^2}\log Z_M(t^*;T)$$

| Term | Financial meaning |
|---|---|
| $c^2(T-t^*)$ | Contribution from the convexity correction in $A(t^*;T)$ |
| $-\partial^2_{TT}\log Z_M$ | Curvature of the log discount factor = second derivative of the forward rate curve |

## Example

If the log market discount factor is $\log Z_M(0;T) = -0.035T - 0.0008T^2$, then $\partial^2_{TT}\log Z_M = -0.0016$ (constant). With $c = 1\%$: $\eta^*(T) = (0.01)^2 \times T - (-0.0016) = 0.0001T + 0.0016$. The drift increases linearly with $T$, encoding the upward-sloping forward rate curve.

## Remember

The double-differentiation trick transforms an integral equation into an **explicit formula** — no numerical inversion required. The key insight is that the second derivative of the log discount factor is directly proportional to the second derivative of the forward rate curve (its curvature). A steeply humped forward rate curve requires a drift $\eta^*(t)$ that rises and then falls. In practice, numerical differentiation of market discount factors amplifies noise, making the calibrated drift sensitive to the smoothing assumptions applied to raw bond price data.
