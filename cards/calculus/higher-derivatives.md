# Higher Derivatives

**Topic:** Calculus
**Tags:** higher derivatives, second derivative, gamma, speed, convexity, calculus
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

A **higher derivative** is obtained by differentiating a function more than once. The $n$th derivative $f^{(n)}(x)$ measures the rate of change of the $(n{-}1)$th derivative. Second derivatives measure curvature; third derivatives measure the rate of change of curvature.

## Key Formula

In Leibniz notation, successive derivatives of $y = f(x)$ are written:

$$\frac{d^2 y}{dx^2} = \frac{d}{dx}\!\left(\frac{dy}{dx}\right), \qquad \frac{d^3 y}{dx^3} = \frac{d}{dx}\!\left(\frac{d^2 y}{dx^2}\right)$$

For a power function $f(x) = x^n$:

$$f^{(k)}(x) = \frac{n!}{(n-k)!}\, x^{n-k}$$

In option pricing, the higher derivatives of the option price $V$ with respect to underlying price $S$ define the **higher-order Greeks**:

$$\Gamma = \frac{\partial^2 V}{\partial S^2}, \qquad \text{Speed} = \frac{\partial^3 V}{\partial S^3}, \qquad \text{Colour} = \frac{\partial^3 V}{\partial S^2\, \partial t}$$

## Example

Let $f(x) = x^4 - 3x^3 + 2x$.

$$f'(x) = 4x^3 - 9x^2 + 2$$
$$f''(x) = 12x^2 - 18x$$
$$f'''(x) = 24x - 18$$

At $x = 1$: $f''(1) = 12 - 18 = -6$ (concave down), $f'''(1) = 6$ (curvature is increasing).

## Remember

In options trading, **Gamma** ($\Gamma$) is the second derivative of the option price with respect to the underlying — it tells a delta-hedger how quickly their hedge ratio is drifting and therefore how often they must rebalance. **Speed** (the third derivative) measures how fast Gamma itself changes, which matters when hedging a large book against a sudden gap in the underlying. **Colour** (the mixed third derivative) measures the daily decay of Gamma, helping risk managers forecast how their Gamma exposure will evolve overnight — a practical concern for options desks carrying large short-dated books.
