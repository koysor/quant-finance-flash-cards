# Explicit Function

**Topic:** Calculus
**Tags:** explicit function, function definition, differentiation, closed form, option pricing
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A function is **explicit** when the dependent variable is expressed directly in terms of the independent variable: $y = f(x)$. The output is isolated on one side; you can substitute any input and evaluate the output in a single step without solving an equation.

## Key Formula

**General form:**

$$y = f(x)$$

The derivative follows directly from differentiation rules without any further manipulation:

$$\frac{dy}{dx} = f'(x)$$

**Examples of explicit functions:**

$$y = x^2 + 3x - 1 \qquad y = e^{-rt} \qquad y = \ln(S/K)$$

**Black-Scholes call price** is an explicit function of its inputs:

$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$

where $d_1$ and $d_2$ are themselves explicit functions of $S_0, K, r, \sigma, T$.

## Example

The present value of a zero-coupon bond is an explicit function of yield $y$ and maturity $T$:

$$P = e^{-yT}$$

Given $y = 0.05$ and $T = 3$: $P = e^{-0.15} \approx 0.861$.

The duration (sensitivity of price to yield) follows by direct differentiation:

$$\frac{dP}{dy} = -T e^{-yT} = -3 \times 0.861 = -2.583$$

No equation needs to be solved — the explicit form makes evaluation and differentiation immediate.

## Remember

Most closed-form pricing models deliver **explicit** functions: Black-Scholes gives $C$ directly as a function of $(S, K, r, \sigma, T)$. This makes Greeks easy to compute analytically. When a model cannot be solved explicitly — such as American options or calibration problems — the function becomes implicit, and numerical methods (root-finding, PDEs, Monte Carlo) are required instead. Recognising whether a pricing relationship is explicit or implicit determines which computational approach is appropriate.
