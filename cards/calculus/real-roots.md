# Real Roots

**Topic:** Calculus
**Tags:** real roots, zeros, discriminant, polynomial, break-even, root finding
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A **real root** (or real zero) of a function $f$ is a value $x \in \mathbb{R}$ such that $f(x) = 0$. Geometrically, real roots are the $x$-coordinates where the graph of $f$ crosses or touches the $x$-axis. A polynomial of degree $n$ has at most $n$ real roots; if it has fewer, the remaining roots are complex.

## Key Formula

For a quadratic $ax^2 + bx + c = 0$, the number of real roots is determined by the discriminant:

$$\Delta = b^2 - 4ac$$

$$\Delta > 0 \implies \text{two distinct real roots} \quad x = \frac{-b \pm \sqrt{\Delta}}{2a}$$

$$\Delta = 0 \implies \text{one repeated real root} \quad x = -\frac{b}{2a}$$

$$\Delta < 0 \implies \text{no real roots (two complex conjugate roots)}$$

For a general continuous function, the **Intermediate Value Theorem** guarantees a real root on $[a, b]$ whenever $f(a)$ and $f(b)$ have opposite signs.

## Example

A delta-hedged portfolio has P&L approximately equal to:

$$\Pi = \tfrac{1}{2}\Gamma(\delta S)^2 - \Theta \cdot \delta t$$

Setting $\Pi = 0$ to find the break-even move $\delta S^*$:

$$\tfrac{1}{2}\Gamma(\delta S^*)^2 = \Theta \cdot \delta t \implies \delta S^* = \sqrt{\frac{2\Theta \cdot \delta t}{\Gamma}}$$

With $\Gamma = 0.05$, $\Theta = -2$, $\delta t = 1/252$:

$$\delta S^* = \sqrt{\frac{2 \times 2 \times (1/252)}{0.05}} \approx 0.566$$

This real root is the **break-even move** — if $|\delta S| > \delta S^*$, the gamma profit exceeds the theta decay.

## Remember

Finding real roots is the core of **implied volatility inversion**. Given a market price $C_{\text{mkt}}$, implied vol $\sigma^*$ is the real root of $f(\sigma) = C_{\text{BS}}(\sigma) - C_{\text{mkt}} = 0$. Since Black-Scholes vega is always positive, $f$ is strictly increasing and has exactly one real root — guaranteeing a unique implied vol. The Intermediate Value Theorem confirms it exists (since $C_{\text{BS}}$ ranges from intrinsic value to $S_0$ as $\sigma$ goes from 0 to $\infty$), and Newton-Raphson or bisection finds it numerically.
