# Reduction Formula

**Topic:** Calculus
**Tags:** calculus, integration, recursion, integration-by-parts, probability, moments
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

A reduction formula is a recursive identity that expresses an integral involving a parameter $n$ in terms of the same integral with a smaller value of $n$. By applying the formula repeatedly, a complex integral is reduced step by step until a base case that can be evaluated directly is reached. Reduction formulas are typically derived using integration by parts.

## Key Formula

The standard reduction formula for $I_n = \displaystyle\int_0^\infty x^n e^{-x} \, dx$ (the gamma integral):

$$I_n = n \, I_{n-1}, \qquad I_0 = 1$$

which gives $I_n = n!$ for non-negative integer $n$.

For $J_n = \displaystyle\int \sin^n x \, dx$, integration by parts yields:

$$J_n = -\frac{\sin^{n-1} x \cos x}{n} + \frac{n-1}{n} J_{n-2}$$

with base cases $J_0 = x + C$ and $J_1 = -\cos x + C$.

## Example

Find $I_3 = \displaystyle\int_0^\infty x^3 e^{-x} \, dx$ using the reduction formula.

**Apply recursively:**

$$I_3 = 3 \cdot I_2 = 3 \cdot 2 \cdot I_1 = 3 \cdot 2 \cdot 1 \cdot I_0 = 6 \cdot 1 = 6$$

**Verify the base case:** $I_0 = \displaystyle\int_0^\infty e^{-x} \, dx = 1$. So $I_3 = 3! = 6$.

This is the third raw moment $\mathbb{E}[X^3]$ of an exponential distribution with rate $\lambda = 1$.

## Remember

The gamma reduction formula $I_n = n \, I_{n-1}$ is the foundation of the **gamma function** $\Gamma(n+1) = n!$, which appears throughout quantitative finance. It is used to compute moments of the gamma and chi-squared distributions — both central to volatility modelling and risk measurement. In particular, $\mathbb{E}[X^n]$ for a gamma-distributed random variable can be evaluated by reduction, enabling closed-form expressions for the higher moments of realised variance and the moments of chi-squared test statistics used in the Jarque-Bera test for normality.
