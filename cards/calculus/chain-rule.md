# Chain Rule

**Topic:** Calculus
**Tags:** chain rule, differentiation, composite functions, total derivative, Itô

---

## Definition

The chain rule gives the derivative of a composite function — a function applied to another function. In the single-variable case, if $y = f(g(x))$, then the derivative is the product of the outer and inner derivatives. The multivariate extension (total derivative) accounts for all paths through which the independent variable affects the output.

## Key Formula

Single variable — if $y = f(u)$ and $u = g(x)$:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

Multivariate — if $f = f(x, y)$ where $x = x(t)$ and $y = y(t)$:

$$\frac{df}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$$

## Example

Let $y = (3x + 1)^5$. Set $u = 3x + 1$, so $y = u^5$.

$$\frac{dy}{dx} = 5u^4 \cdot 3 = 15(3x + 1)^4$$

At $x = 1$: $\frac{dy}{dx} = 15 \times 4^4 = 15 \times 256 = 3{,}840$.

## Remember

The chain rule is the deterministic version of **Itô's Lemma**. In ordinary calculus, if $V = f(S, t)$ then $dV = \frac{\partial f}{\partial S}dS + \frac{\partial f}{\partial t}dt$. But when $S$ follows a stochastic process, the chain rule acquires an extra correction term: $\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 f}{\partial S^2}dt$. This Itô correction is what produces the Gamma term in options pricing. Every Greek is computed via the chain rule — Delta, Gamma, Theta, and Vega are all partial derivatives of the option price function, and understanding how they compose through the chain rule is essential for hedging multi-leg positions.
