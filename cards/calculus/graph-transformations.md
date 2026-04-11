# Graph Transformations

**Topic:** Calculus
**Tags:** graph transformations, translation, stretch, reflection, f(x), functions
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **graph transformation** changes the position or shape of the graph $y = f(x)$ by modifying either the input $x$ or the output $f(x)$. Transformations applied **inside** the function (to $x$) act horizontally and opposite to the sign; transformations applied **outside** (to $f$) act vertically and as expected. The six standard transformations are translation, stretch, and reflection in both directions.

## Key Formula

| Transformation | Equation | Effect |
|---|---|---|
| Horizontal translation by $a$ | $y = f(x - a)$ | Right by $a$ (left if $a < 0$) |
| Vertical translation by $b$ | $y = f(x) + b$ | Up by $b$ (down if $b < 0$) |
| Horizontal stretch, factor $\frac{1}{a}$ | $y = f(ax)$ | Squash by factor $a$ toward $y$-axis |
| Vertical stretch, factor $a$ | $y = af(x)$ | Stretch from $x$-axis by factor $a$ |
| Reflection in $y$-axis | $y = f(-x)$ | Flip left–right |
| Reflection in $x$-axis | $y = -f(x)$ | Flip up–down |

**Combined:** $y = af(bx + c) + d$ applies in order: horizontal shift, horizontal stretch, vertical stretch, vertical shift.

## Example

Starting from $y = \sin x$: the graph of $y = 3\sin(2x - \pi) + 1$.

Rewrite as $y = 3\sin\!\left(2\left(x - \frac{\pi}{2}\right)\right) + 1$:
- $f(2x)$: horizontal squash by factor 2 (period $\pi$)
- $f(2(x - \pi/2))$: translate right by $\pi/2$
- $3f(\cdot)$: vertical stretch by 3 (amplitude 3)
- $+1$: translate up by 1

## Remember

Graph transformations are the foundation of **volatility smile calibration**. The Black-Scholes implied volatility surface $\sigma(K, T)$ as a function of strike is a transformed version of a base curve — the risk-reversal shifts the smile left/right (translation), the butterfly adjusts its width (stretch), and the at-the-money level shifts it up/down. Understanding transformations also clarifies **standardisation**: replacing $X$ with $(X - \mu)/\sigma$ is a horizontal translation and stretch that maps any normal distribution to the standard normal — the fundamental tool in all z-score and VaR calculations.
