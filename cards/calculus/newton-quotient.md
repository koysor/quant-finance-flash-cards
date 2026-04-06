# Newton Quotient

**Topic:** Calculus
**Tags:** calculus, differentiation, limits, first principles, rate of change
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **Newton quotient** (also called the **difference quotient**) is the expression used to define the derivative of a function from first principles. It measures the average rate of change of $f$ over an interval of width $h$, and the derivative is obtained by taking the limit as $h \to 0$.

## Key Formula

$$\frac{f(x+h) - f(x)}{h}$$

The derivative is defined as the limit of the Newton quotient:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

provided this limit exists. When the limit exists at $x$, the function is said to be **differentiable** at $x$.

## Example

Find the derivative of $f(x) = x^2$ from first principles.

$$\frac{f(x+h) - f(x)}{h} = \frac{(x+h)^2 - x^2}{h} = \frac{x^2 + 2xh + h^2 - x^2}{h} = \frac{2xh + h^2}{h} = 2x + h$$

Taking the limit: $f'(x) = \lim_{h \to 0} (2x + h) = 2x$.

So the instantaneous rate of change of $x^2$ at $x = 3$ is $f'(3) = 6$.

## Remember

In quantitative finance, **Delta** ($\Delta$) is often approximated numerically using a finite difference — a direct application of the Newton quotient with a small but non-zero $h$:

$$\Delta \approx \frac{V(S + h) - V(S)}{h}$$

This is how option sensitivities are computed in practice when no closed-form formula for the Greek exists. The Newton quotient is also the basis of **finite-difference methods** for solving the Black-Scholes PDE on a grid, where derivatives are replaced by discrete approximations.
