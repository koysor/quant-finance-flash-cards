# Differentiation

**Topic:** Calculus
**Tags:** differentiation, derivative, rate of change, gradient, first principles
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Differentiation** is the process of finding the instantaneous rate of change of a function at a point. The derivative $f'(x)$ gives the gradient of the tangent to the curve $y = f(x)$ at $x$, defined as the limit of the gradient of a chord as the chord length shrinks to zero. A function is **differentiable** at a point if this limit exists and is finite.

## Key Formula

**Definition from first principles:**

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

**Leibniz notation** for the same concept:

$$\frac{dy}{dx} = \lim_{\delta x \to 0} \frac{\delta y}{\delta x}$$

**Second derivative** (rate of change of the rate of change):

$$f''(x) = \frac{d^2 y}{dx^2} = \lim_{h \to 0} \frac{f'(x + h) - f'(x)}{h}$$

## Example

Find the derivative of $f(x) = x^2$ from first principles.

$$f'(x) = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h} = \lim_{h \to 0} \frac{2xh + h^2}{h} = \lim_{h \to 0} (2x + h) = 2x$$

At $x = 3$: $f'(3) = 6$. The tangent to $y = x^2$ at the point $(3, 9)$ has gradient $6$.

## Remember

Every option sensitivity (Greek) is a derivative in this sense. Delta $\Delta = \partial V / \partial S$ is the instantaneous rate of change of the option price $V$ with respect to the underlying price $S$ — it tells a trader how much the option value moves for an infinitesimally small move in the underlying. In delta-hedging, a trader holds $-\Delta$ units of the underlying to offset this sensitivity; as $S$ changes, $\Delta$ changes (because of Gamma), requiring continuous rebalancing. The entire Greeks framework is built on the first-principles definition of the derivative.
