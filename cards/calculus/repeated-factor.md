# Repeated Factor

**Topic:** Calculus
**Tags:** calculus, partial-fractions, integration, rational-functions, higher-order-poles, laplace-transform
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

A **repeated factor** (or repeated linear factor) in a denominator is a factor $(x - a)^n$ with $n \geq 2$. When decomposing a rational function using partial fractions, a repeated factor of order $n$ contributes $n$ separate terms — one for each power from 1 up to $n$ — because the cover-up rule alone is insufficient to determine all the constants in that case.

## Key Formula

For a proper rational function with a repeated linear factor $(x - a)^n$:

$$\frac{P(x)}{(x - a)^n \cdot Q(x)} = \frac{A_1}{x - a} + \frac{A_2}{(x - a)^2} + \cdots + \frac{A_n}{(x - a)^n} + \text{(terms from } Q(x)\text{)}$$

The constant $A_n$ (highest power only) can be found by the cover-up rule: multiply both sides by $(x - a)^n$ and set $x = a$. The remaining constants $A_1, \ldots, A_{n-1}$ are found by equating coefficients or substituting convenient values of $x$.

Integrating a repeated-factor term uses the power rule for negative exponents:

$$\int \frac{A_k}{(x-a)^k}\, dx = \frac{-A_k}{(k-1)(x-a)^{k-1}} + C, \qquad k \geq 2$$

## Example

Decompose and integrate $\displaystyle\int \frac{1}{(x-2)^2(x+1)}\, dx$.

Write $\dfrac{1}{(x-2)^2(x+1)} = \dfrac{A}{x-2} + \dfrac{B}{(x-2)^2} + \dfrac{C}{x+1}$.

**Finding $B$** (cover-up, $x = 2$): $B = \dfrac{1}{2+1} = \dfrac{1}{3}$.

**Finding $C$** (cover-up, $x = -1$): $C = \dfrac{1}{(-1-2)^2} = \dfrac{1}{9}$.

**Finding $A$** (set $x = 0$): $\dfrac{1}{4} = \dfrac{A}{-2} + \dfrac{1/3}{4} + \dfrac{1/9}{1}$, giving $A = -\dfrac{1}{9}$.

$$\int \frac{dx}{(x-2)^2(x+1)} = -\frac{1}{9}\ln|x-2| - \frac{1}{3(x-2)} + \frac{1}{9}\ln|x+1| + C$$

## Remember

In the Laplace-transform solution of pricing PDEs (e.g. the Black-Scholes PDE after the standard heat-equation substitution), the transform variable $s$ enters the denominator as a polynomial. A **repeated root** of that polynomial corresponds to a higher-order pole — mathematically a repeated factor — and signals critical damping or resonance in the time-domain solution. When inverting the transform back to the time domain, the repeated factor yields not just an exponential term but an exponential multiplied by a polynomial in $t$ (e.g. $t e^{at}$). Recognising repeated factors is therefore essential for obtaining the correct closed-form option price in models where the characteristic equation has degenerate roots.
