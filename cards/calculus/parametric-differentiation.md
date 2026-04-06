# Parametric Differentiation

**Topic:** Calculus
**Tags:** parametric, differentiation, chain rule, gradient, dy/dx, second derivative
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Parametric differentiation** finds the gradient $dy/dx$ of a parametrically defined curve $x = f(t)$, $y = g(t)$ by applying the chain rule. The second derivative $d^2y/dx^2$ is found by differentiating $dy/dx$ with respect to $t$ and again dividing by $dx/dt$.

## Key Formula

**First derivative:**

$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{g'(t)}{f'(t)}, \quad \text{provided } f'(t) \neq 0$$

**Second derivative:**

$$\frac{d^2y}{dx^2} = \frac{d}{dx}\!\left(\frac{dy}{dx}\right) = \frac{\dfrac{d}{dt}\!\left(\dfrac{dy}{dx}\right)}{dx/dt}$$

## Example

A curve is defined by $x = t^2$, $y = t^3 - t$.

$\frac{dx}{dt} = 2t$, $\quad \frac{dy}{dt} = 3t^2 - 1$

$$\frac{dy}{dx} = \frac{3t^2 - 1}{2t}$$

At $t = 1$: gradient $= \frac{3 - 1}{2} = 1$.

Second derivative: $\frac{d}{dt}\!\left(\frac{3t^2-1}{2t}\right) = \frac{3t^2+1}{2t^2}$, so $\frac{d^2y}{dx^2} = \frac{(3t^2+1)/(2t^2)}{2t} = \frac{3t^2+1}{4t^3}$.

## Remember

Parametric differentiation is the chain rule in disguise, and it underpins **Itô's lemma** — the stochastic analogue. When an option price $V(S, t)$ depends on a stock price $S(t)$ that is itself parametrised by time $t$ via a stochastic process, the total derivative $dV$ requires terms from both $\partial V/\partial S$ and $\partial V/\partial t$ — the multi-variable extension of parametric differentiation. The additional $\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\,dt$ term in Itô's lemma is the stochastic counterpart of the second-derivative correction that appears in the parametric formula above.
