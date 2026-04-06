# Parabola

**Topic:** Calculus
**Tags:** parabola, quadratic, vertex, convexity, optimisation, payoff diagrams
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A **parabola** is the curve traced by a quadratic function $f(x) = ax^2 + bx + c$ with $a \neq 0$. It is symmetric about a vertical axis and has a single turning point called the **vertex**. When $a > 0$ the parabola opens upward (convex) and the vertex is a minimum; when $a < 0$ it opens downward (concave) and the vertex is a maximum.

## Key Formula

**Standard form:**

$$f(x) = ax^2 + bx + c, \qquad a \neq 0$$

**Vertex form** (obtained by completing the square):

$$f(x) = a\!\left(x - h\right)^2 + k$$

where the vertex is at $(h, k)$ with:

$$h = -\frac{b}{2a}, \qquad k = c - \frac{b^2}{4a}$$

**Axis of symmetry:** $x = h = -\dfrac{b}{2a}$

The parabola crosses the $x$-axis at the roots of $ax^2 + bx + c = 0$, given by the quadratic formula. The discriminant $\Delta = b^2 - 4ac$ determines whether there are two real roots ($\Delta > 0$), one repeated root ($\Delta = 0$), or no real roots ($\Delta < 0$).

## Example

A trader's profit from a long straddle (long call + long put, same strike $K = 100$, total premium paid $= 10$) as a function of the underlying price $S_T$ at expiry has a V-shape — but before expiry, the combined option value is approximately parabolic near the strike due to gamma:

$$V \approx V_0 + \Delta \cdot \delta S + \tfrac{1}{2}\Gamma \cdot (\delta S)^2$$

With $\Delta = 0$ (at-the-money straddle) and $\Gamma = 0.04$, a move of $\delta S = 5$:

$$V \approx V_0 + \tfrac{1}{2}(0.04)(25) = V_0 + 0.50$$

This parabolic approximation — opening upward — reflects the convexity (positive gamma) of a long options position.

## Remember

The parabolic shape is the geometric signature of **gamma** in options pricing. A long option position has positive gamma, so its value as a function of the underlying is convex (upward-opening parabola near the strike). The vertex corresponds to the point of zero delta. Every second-order Taylor expansion of an option price is locally a parabola — this is why gamma scalping involves harvesting the area between the parabola and its tangent line as the underlying moves.
