# Polynomial Functions

**Topic:** Calculus
**Tags:** polynomial, degree, coefficients, roots, Taylor series, payoff approximation
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A **polynomial function** is a sum of non-negative integer powers of the variable, each multiplied by a constant coefficient:

$$p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0, \qquad a_n \neq 0$$

The **degree** is $n$ (the highest power present). Polynomials are defined for all $x \in \mathbb{R}$, are infinitely differentiable, and have at most $n$ real roots.

## Key Formula

**Fundamental Theorem of Algebra:** every degree-$n$ polynomial has exactly $n$ roots in $\mathbb{C}$ (counting multiplicity). Real coefficients imply complex roots come in conjugate pairs.

**Differentiation** is term-by-term:

$$p'(x) = n a_n x^{n-1} + (n-1)a_{n-1} x^{n-2} + \cdots + a_1$$

**Taylor's theorem** expresses any smooth function locally as a polynomial:

$$f(x) \approx f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n$$

## Example

A trader approximates an option's value near the current spot $S_0 = 100$ using a second-degree polynomial (delta-gamma approximation):

$$V(S) \approx V_0 + \Delta \cdot (S - S_0) + \tfrac{1}{2}\Gamma \cdot (S - S_0)^2$$

With $V_0 = 5$, $\Delta = 0.4$, $\Gamma = 0.03$ and $S = 105$:

$$V(105) \approx 5 + 0.4(5) + \tfrac{1}{2}(0.03)(25) = 5 + 2 + 0.375 = 7.375$$

This degree-2 polynomial approximation captures both the linear (delta) and curvature (gamma) components of the option's price movement.

## Remember

Polynomials are the building blocks of local approximation in quantitative finance. Every Taylor expansion truncated at degree $n$ is a polynomial — the delta-gamma approximation is degree 2, and higher-order Greeks (speed, colour) add degree-3 and degree-4 terms. Polynomial regression is also used in the Longstaff-Schwartz algorithm for American option pricing, where the continuation value is estimated as a polynomial function of the underlying state variables at each exercise date.
