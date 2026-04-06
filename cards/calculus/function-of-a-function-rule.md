# Function of a Function Rule

**Topic:** Calculus
**Tags:** chain rule, composite functions, substitution, differentiation, change of variable
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The function of a function rule (also called the chain rule) states that when one function is nested inside another — a **composite function** — its derivative is found by multiplying the derivative of the outer function (evaluated at the inner function) by the derivative of the inner function. The key technique is to name the inner function $u$, differentiate each layer separately, then multiply.

## Key Formula

If $y = f(u)$ where $u = g(x)$, the composite is $y = f(g(x))$ and:

$$\frac{dy}{dx} = f'(u) \cdot g'(x) = \frac{dy}{du} \cdot \frac{du}{dx}$$

**Substitution for integration** (the reverse direction):

$$\int f\bigl(g(x)\bigr)\,g'(x)\,dx = \int f(u)\,du, \qquad u = g(x)$$

The two steps of the substitution method:
1. Let $u = g(x)$, compute $du = g'(x)\,dx$, rewrite the integral entirely in $u$.
2. Integrate in $u$, then substitute back $u = g(x)$.

## Example

Differentiate $y = e^{-\frac{1}{2}x^2}$ — the kernel of the normal density.

Let $u = -\tfrac{1}{2}x^2$, so $y = e^u$.

$$\frac{dy}{du} = e^u, \qquad \frac{du}{dx} = -x$$

$$\frac{dy}{dx} = e^u \cdot (-x) = -x\,e^{-\frac{1}{2}x^2}$$

This result confirms that the standard normal density $\phi(x) = \tfrac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}x^2}$ satisfies $\phi'(x) = -x\,\phi(x)$, which is used when differentiating option prices with respect to the strike.

## Remember

The substitution technique is the engine behind computing **option prices and Greeks from first principles**. The Black-Scholes call price involves integrating $e^{-\frac{1}{2}u^2}$ after a change of variable that converts the lognormal payoff integral into a standard normal integral. Every time a quant shifts variables — from log-returns to prices, from real to risk-neutral measure, from $d_1$ to $d_2$ — they are applying the function of a function rule. Recognising the inner function $u$ in a compound expression is the single most useful algebraic habit in quantitative finance.
