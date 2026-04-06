# Nth Derivative

**Topic:** Calculus
**Tags:** calculus, differentiation, nth derivative, Taylor series, higher-order Greeks
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **nth derivative** of a function $f(x)$, written $f^{(n)}(x)$ or $\frac{d^n f}{dx^n}$, is the result of differentiating $f$ exactly $n$ times in succession. It generalises the familiar first derivative $f'(x)$ and second derivative $f''(x)$ to arbitrarily high orders. A function must be $n$ times differentiable for $f^{(n)}(x)$ to exist.

## Key Formula

**General power rule** — the nth derivative of $x^k$ (for integer $k \geq n$):

$$\frac{d^n}{dx^n}\!\left(x^k\right) = \frac{k!}{(k - n)!}\, x^{k-n}$$

**Nth derivative in a Taylor series** — the coefficient of the $(x - a)^n$ term:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n$$

so that:

$$f^{(n)}(a) = n! \times \text{(coefficient of } (x-a)^n \text{ in the Taylor expansion)}$$

**Leibniz notation:**

$$f^{(n)}(x) = \frac{d^n f}{dx^n}$$

## Example

Find the first four derivatives of $f(x) = e^{2x}$:

$$f'(x) = 2e^{2x}, \quad f''(x) = 4e^{2x}, \quad f'''(x) = 8e^{2x}, \quad f^{(4)}(x) = 16e^{2x}$$

The pattern is $f^{(n)}(x) = 2^n e^{2x}$.

Using the power rule on $f(x) = x^5$ at $n = 3$:

$$\frac{d^3}{dx^3}(x^5) = \frac{5!}{(5-3)!}\,x^{5-3} = \frac{120}{2}\,x^2 = 60x^2$$

## Remember

Higher-order derivatives appear directly in quantitative finance through the **higher-order Greeks**. Delta ($\Delta$) is the first derivative of the option price $V$ with respect to the underlying $S$; Gamma ($\Gamma$) is the second derivative; **Speed** is the third derivative $\partial^3 V / \partial S^3$, measuring how Gamma changes with $S$. A large Speed means Gamma hedges require frequent rebalancing as the underlying moves. The Taylor series connection is equally important: the delta-gamma P&L approximation $\Delta V \approx \Delta \cdot \delta S + \frac{1}{2}\Gamma \cdot (\delta S)^2$ is just the first two non-zero terms of the Taylor expansion — adding the Speed term $\frac{1}{6} \cdot \frac{\partial^3 V}{\partial S^3} \cdot (\delta S)^3$ improves accuracy for large moves.
