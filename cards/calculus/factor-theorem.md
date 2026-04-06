# Factor Theorem

**Topic:** Calculus
**Tags:** polynomial, roots, factorisation, algebra, partial fractions
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Factor Theorem** states that for a polynomial $p(x)$, the expression $(x - a)$ is a factor of $p(x)$ if and only if $p(a) = 0$. It is a special case of the Remainder Theorem, which states that the remainder when $p(x)$ is divided by $(x - a)$ equals $p(a)$.

## Key Formula

$$p(a) = 0 \iff (x - a) \text{ is a factor of } p(x)$$

**Remainder Theorem:** when $p(x)$ is divided by $(x - a)$:

$$p(x) = (x - a)\,q(x) + p(a)$$

where $q(x)$ is the quotient polynomial of degree one less than $p(x)$.

## Example

Find the roots of $p(x) = x^3 - 6x^2 + 11x - 6$.

Test $x = 1$: $p(1) = 1 - 6 + 11 - 6 = 0$, so $(x - 1)$ is a factor.

Dividing out: $p(x) = (x - 1)(x^2 - 5x + 6) = (x - 1)(x - 2)(x - 3)$.

The roots are $x = 1, 2, 3$.

## Remember

The Factor Theorem is the foundation of **partial fraction decomposition**. When pricing bonds or inverting Laplace transforms in term-structure models, the denominator of the rational transfer function must first be factorised into linear (and irreducible quadratic) terms. Each linear factor $(x - a)$ found via the Factor Theorem yields a partial fraction term whose inverse transform is a known exponential — the building block of every exponential decay curve in fixed-income pricing.
