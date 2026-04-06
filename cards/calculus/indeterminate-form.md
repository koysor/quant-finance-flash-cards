# Indeterminate Form

**Topic:** Calculus
**Tags:** indeterminate forms, limits, algebraic manipulation, L'Hôpital, asymptotic analysis, continuous compounding
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

An **indeterminate form** arises when a limit produces an expression whose value cannot be determined from the individual component limits alone. The seven standard indeterminate forms are $\frac{0}{0}$, $\frac{\infty}{\infty}$, $0 \cdot \infty$, $\infty - \infty$, $0^0$, $1^\infty$, and $\infty^0$. Unlike a definite form such as $\frac{1}{0}$ (which is clearly undefined), an indeterminate form may evaluate to any finite value, $\pm\infty$, or may not exist — the actual result depends on the relative rates at which the components grow or shrink.

## Key Formula

**The seven indeterminate forms and their standard reductions:**

| Form | Algebraic transformation | Reduces to |
|---|---|---|
| $\dfrac{0}{0}$ | Apply L'Hôpital directly | $\dfrac{0}{0}$ or $\dfrac{\infty}{\infty}$ |
| $\dfrac{\infty}{\infty}$ | Apply L'Hôpital directly | — |
| $0 \cdot \infty$ | Rewrite as $\dfrac{f}{1/g}$ or $\dfrac{g}{1/f}$ | $\dfrac{0}{0}$ or $\dfrac{\infty}{\infty}$ |
| $\infty - \infty$ | Factorise, common denominator, or conjugate | $\dfrac{0}{0}$ |
| $0^0$, $1^\infty$, $\infty^0$ | Write as $e^{g \ln f}$, evaluate exponent | $0 \cdot \infty$ |

**Key continuous-compounding limit** ($1^\infty$ form):

$$\lim_{n \to \infty} \left(1 + \frac{r}{n}\right)^n = e^r$$

Setting $f(n) = \left(1 + \frac{r}{n}\right)^n$, take logarithm: $\ln f = n \ln\!\left(1 + \frac{r}{n}\right) \xrightarrow{} r$ via L'Hôpital, so $f \to e^r$.

## Example

Evaluate the $0 \cdot \infty$ form that arises in bond pricing as yield $y \to 0$:

A zero-coupon bond price is $P = e^{-yT}$. Duration $D$ is defined as minus the logarithmic derivative with respect to $y$: $D = T$. Now consider continuously-compounded annuity factor $A(y, T) = \frac{1 - e^{-yT}}{y}$ as $y \to 0$ — this is a $\frac{0}{0}$ form.

Apply L'Hôpital: differentiate numerator and denominator with respect to $y$:

$$\lim_{y \to 0} \frac{1 - e^{-yT}}{y} = \lim_{y \to 0} \frac{T e^{-yT}}{1} = T$$

So the annuity factor converges to $T$ as rates approach zero, confirming that a string of near-zero-discount cash flows has present value equal to the sum of undiscounted amounts.

## Remember

Indeterminate forms appear throughout quantitative finance wherever a pricing formula reaches a degenerate regime: zero rates, zero volatility, zero time to expiry, or infinite strike. Recognising the form determines the correct algebraic strategy — converting $0 \cdot \infty$ or $1^\infty$ into $\frac{0}{0}$ before applying L'Hôpital prevents incorrect conclusions. The continuous compounding formula $e^r = \lim_{n\to\infty}(1+r/n)^n$ is itself a resolved $1^\infty$ indeterminate form, foundational to all discounted cash flow analysis.
