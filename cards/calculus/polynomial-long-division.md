# Polynomial Long Division

**Topic:** Calculus
**Tags:** polynomial division, long division, quotient, remainder, rational function, oblique asymptote
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Polynomial long division** divides a polynomial $f(x)$ of degree $n$ by a divisor $d(x)$ of degree $m \leq n$ to produce a quotient $q(x)$ and remainder $r(x)$, where $\deg r < \deg d$:

$$f(x) = d(x)\,q(x) + r(x)$$

The algorithm mirrors numerical long division: divide the leading term, multiply back, subtract, and repeat with the reduced polynomial. It is used to simplify improper rational functions (where degree of numerator $\geq$ degree of denominator) before integration or partial fraction decomposition.

## Key Formula

**Division algorithm for polynomials:**

$$\frac{f(x)}{d(x)} = q(x) + \frac{r(x)}{d(x)}, \quad \deg r < \deg d$$

**Steps:**
1. Divide leading term of dividend by leading term of divisor.
2. Multiply result by full divisor; subtract from dividend.
3. Repeat with the remainder until degree of remainder $<$ degree of divisor.

**Oblique asymptote** of $y = f(x)/d(x)$: if $\deg f = \deg d + 1$, the quotient $q(x)$ is a linear oblique asymptote.

## Example

Divide $x^3 + 2x^2 - x + 3$ by $(x - 1)$:

$$x^3 + 2x^2 - x + 3 = (x-1)(x^2 + 3x + 2) + 5$$

Check via Remainder Theorem: $f(1) = 1 + 2 - 1 + 3 = 5$ ✓

Rational function: $\dfrac{x^2 + 1}{x - 2} = x + 2 + \dfrac{5}{x-2}$ (oblique asymptote $y = x + 2$).

## Remember

Polynomial long division is the algebraic operation underlying **duration and convexity approximations** in fixed income. A bond price as a function of yield $P(y)$ is not a polynomial, but its Taylor expansion around the current yield $y_0$ performs exactly the role of polynomial division — decomposing a complex function into a linear term (duration), a quadratic correction (convexity), and higher-order remainder. Polynomial division is also used in **partial fractions** (prerequisite to the cover-up rule for rational function integration), and in simplifying **z-transform expressions** in digital signal processing and filter design used in algorithmic trading systems.
