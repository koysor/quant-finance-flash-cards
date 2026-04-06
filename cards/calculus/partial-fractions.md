# Partial Fractions

**Topic:** Calculus
**Tags:** calculus, integration, rational-functions, algebra, laplace-transform, bond-pricing
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

Partial fraction decomposition rewrites a rational function — a ratio of two polynomials — as a sum of simpler fractions whose denominators are factors of the original denominator. This reduces a complex integral into a sum of standard, easily integrable terms.

## Key Formula

For a proper rational function with distinct linear factors:

$$\frac{P(x)}{(x - a)(x - b)} = \frac{A}{x - a} + \frac{B}{x - b}$$

where the constants $A$ and $B$ are found by multiplying both sides by the denominator and substituting $x = a$ and $x = b$ respectively:

$$A = \frac{P(a)}{a - b}, \qquad B = \frac{P(b)}{b - a}$$

For a repeated linear factor $(x - a)^2$:

$$\frac{P(x)}{(x - a)^2} = \frac{A}{x - a} + \frac{B}{(x - a)^2}$$

## Example

Integrate $\displaystyle\int \frac{1}{(x-1)(x+3)}\, dx$.

Decompose: $\dfrac{1}{(x-1)(x+3)} = \dfrac{A}{x-1} + \dfrac{B}{x+3}$

Setting $x = 1$: $A = \tfrac{1}{4}$. Setting $x = -3$: $B = -\tfrac{1}{4}$.

$$\int \frac{1}{(x-1)(x+3)}\, dx = \frac{1}{4}\ln|x-1| - \frac{1}{4}\ln|x+3| + C = \frac{1}{4}\ln\left|\frac{x-1}{x+3}\right| + C$$

## Remember

In fixed income, the present value of a bond's cash flows involves summing discounted payments — but when pricing bonds or solving term-structure ODEs algebraically, rational functions of the discount factor arise naturally. Partial fractions convert these into logarithmic or power-law terms, enabling closed-form integration. The technique is also essential when inverting Laplace transforms, which appear in the analytical solution of the Black-Scholes PDE after the heat-equation transformation.
