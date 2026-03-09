# Completing the Square

**Topic:** Calculus
**Tags:** completing the square, quadratic, algebraic manipulation, Gaussian integral, normal distribution
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

Completing the square rewrites a quadratic expression $ax^2 + bx + c$ in the form $a(x - h)^2 + k$, where $h$ and $k$ are constants determined by the original coefficients. This reveals the vertex of the parabola and, crucially, enables integration of Gaussian-type expressions by isolating a perfect square in the exponent.

## Key Formula

Given a general quadratic $ax^2 + bx + c$ with $a \neq 0$:

$$ax^2 + bx + c = a\!\left(x + \frac{b}{2a}\right)^{\!2} + c - \frac{b^2}{4a}$$

The vertex is at:

$$h = -\frac{b}{2a}, \qquad k = c - \frac{b^2}{4a}$$

so the expression becomes $a(x - h)^2 + k$.

## Example

Rewrite $2x^2 + 12x + 7$ in completed-square form.

**Step 1 — Factor out the leading coefficient from the first two terms:**

$$2x^2 + 12x + 7 = 2(x^2 + 6x) + 7$$

**Step 2 — Halve the coefficient of $x$ and square it:** half of $6$ is $3$, and $3^2 = 9$.

**Step 3 — Add and subtract inside the bracket:**

$$= 2(x^2 + 6x + 9 - 9) + 7 = 2\bigl((x + 3)^2 - 9\bigr) + 7$$

**Step 4 — Distribute and simplify:**

$$= 2(x + 3)^2 - 18 + 7 = 2(x + 3)^2 - 11$$

The vertex is at $(-3,\, -11)$ and the minimum value is $-11$.

## Remember

Completing the square is the key algebraic step when evaluating the Gaussian integrals that arise in the **Black-Scholes derivation**. To obtain the closed-form option price, you must compute expectations of the form $\mathbb{E}[S_T \mathbf{1}_{S_T > K}]$ under the lognormal density. The exponent of that density is a quadratic in $\ln S_T$; completing the square in that quadratic lets you absorb extra linear terms into a shifted mean, reducing the integral to a standard normal CDF evaluated at $d_1$ or $d_2$. Every time a quadratic appears in an exponent in option pricing — whether in the Black-Scholes formula, the Bachelier model, or multivariate Gaussian copulas — this technique is what converts the integral into a recognisable closed form.
