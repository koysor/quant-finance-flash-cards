# Quotient Rule

**Topic:** Calculus
**Tags:** differentiation, quotient rule, calculus, option greeks, sensitivity
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The quotient rule gives the derivative of one differentiable function divided by another. If $h(x) = \frac{f(x)}{g(x)}$ and $g(x) \neq 0$, the derivative is found by differentiating numerator and denominator separately and combining them according to a fixed formula.

## Key Formula

$$\frac{d}{dx}\!\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)\,g(x) - f(x)\,g'(x)}{[g(x)]^2}$$

A useful mnemonic: "low d-high minus high d-low, over low squared."

The quotient rule can also be derived from the product rule by writing $\frac{f}{g} = f \cdot g^{-1}$ and applying the chain rule to $g^{-1}$.

## Example

Differentiate $h(x) = \frac{e^{-rx}}{1 + e^{-rx}}$ where $r = 0.1$ (a logistic-type discounting function).

Set $f(x) = e^{-rx}$ and $g(x) = 1 + e^{-rx}$, so $f'(x) = -r\,e^{-rx}$ and $g'(x) = -r\,e^{-rx}$.

$$h'(x) = \frac{-r\,e^{-rx}(1 + e^{-rx}) - e^{-rx}(-r\,e^{-rx})}{(1 + e^{-rx})^2} = \frac{-r\,e^{-rx}}{(1 + e^{-rx})^2}$$

At $x = 0$: $h'(0) = \frac{-0.1}{4} = -0.025$.

## Remember

The quotient rule appears in finance whenever a ratio of two quantities must be differentiated. The Sharpe ratio $S = \frac{\mu - r_f}{\sigma}$ requires the quotient rule to find how it changes as the portfolio's expected return or volatility shifts. Similarly, computing the sensitivity of a hedge ratio — such as $\Delta = \frac{\partial C}{\partial S}$ where $C$ itself is a ratio — uses the quotient rule. In fixed income, differentiating yield-based price formulae (price as a ratio involving $(1+y)^n$ terms) with respect to yield $y$ underpins duration and convexity calculations.
