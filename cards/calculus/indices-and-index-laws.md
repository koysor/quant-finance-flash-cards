# Indices and Index Laws

**Topic:** Calculus
**Tags:** indices, exponents, powers, fractional exponents, algebraic manipulation
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

An **index** (plural: indices) is the power to which a base number is raised, written $a^n$ where $a$ is the base and $n$ is the index. The **index laws** are a set of algebraic rules that govern how expressions with indices are simplified, combined, and manipulated.

## Key Formula

**Multiplication** — same base, add indices:

$$a^m \times a^n = a^{m+n}$$

**Division** — same base, subtract indices:

$$\frac{a^m}{a^n} = a^{m-n}$$

**Power of a power** — multiply indices:

$$(a^m)^n = a^{mn}$$

**Negative exponent** — reciprocal:

$$a^{-n} = \frac{1}{a^n}$$

**Fractional exponent** — roots:

$$a^{1/n} = \sqrt[n]{a}, \qquad a^{m/n} = \sqrt[n]{a^m} = \left(\sqrt[n]{a}\right)^m$$

**Zero exponent:**

$$a^0 = 1 \quad (a \neq 0)$$

## Example

Simplify $\dfrac{8^{2/3} \times 2^{-1}}{4^{1/2}}$:

$$8^{2/3} = (2^3)^{2/3} = 2^2 = 4$$

$$4^{1/2} = (2^2)^{1/2} = 2^1 = 2$$

$$\frac{4 \times 2^{-1}}{2} = \frac{4 \times \frac{1}{2}}{2} = \frac{2}{2} = 1$$

## Remember

Index laws underpin nearly every quantitative finance formula that involves exponential growth or decay. Continuous compounding uses $e^{rT}$, which is manipulated via the power-of-a-power rule when splitting time periods: $e^{r(T_1 + T_2)} = e^{rT_1} \times e^{rT_2}$. Volatility scales with the square root of time because $\sigma_{T} = \sigma_1 \times T^{1/2}$ — a direct application of fractional exponents. The power rule for differentiation, $\frac{d}{dx}x^n = nx^{n-1}$, relies on fluent index manipulation, especially when $n$ is negative or fractional, as occurs when differentiating option pricing functions with respect to spot price or time.
