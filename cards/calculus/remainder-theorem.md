# Remainder Theorem

**Topic:** Calculus
**Tags:** remainder theorem, polynomial division, factor theorem, roots
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Remainder Theorem** states that when a polynomial $f(x)$ is divided by the linear factor $(x - a)$, the **remainder is $f(a)$**. This follows from the division algorithm: $f(x) = (x-a)q(x) + r$, and setting $x = a$ gives $f(a) = r$. The **Factor Theorem** is the special case: if $f(a) = 0$, then $(x - a)$ is a factor (remainder = 0).

## Key Formula

**Remainder Theorem:**

$$f(x) \div (x - a) \implies \text{remainder} = f(a)$$

**Division algorithm:**

$$f(x) = (x - a)\,q(x) + f(a)$$

**Factor Theorem** (special case $f(a) = 0$):

$$f(a) = 0 \iff (x-a) \text{ is a factor of } f(x)$$

**For divisor $(ax - b)$:** remainder $= f(b/a)$.

## Example

Find the remainder when $f(x) = 2x^3 - 3x^2 + x - 5$ is divided by $(x - 2)$.

$$f(2) = 2(8) - 3(4) + 2 - 5 = 16 - 12 + 2 - 5 = 1$$

Remainder $= 1$.

Check: is $(x + 1)$ a factor? $f(-1) = 2(-1) - 3(1) + (-1) - 5 = -2 - 3 - 1 - 5 = -11 \neq 0$. Not a factor.

Is $(x - 1)$ a factor? $f(1) = 2 - 3 + 1 - 5 = -5 \neq 0$. Not a factor.

## Remember

The Remainder Theorem and Factor Theorem underpin **polynomial model evaluation and root-finding** in quantitative finance. The **characteristic polynomial** of a matrix (e.g. covariance matrix) evaluated at its eigenvalues equals zero — exactly the Factor Theorem. In **Newton-Raphson root-finding** (used to solve yield equations, implied volatility, etc.), checking $f(a) = 0$ verifies a root, and polynomial division via the Remainder Theorem allows deflation — removing known roots to reduce degree and find remaining roots efficiently.
