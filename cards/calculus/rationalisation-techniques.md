# Rationalisation Techniques

**Topic:** Calculus
**Tags:** rationalisation, surds, conjugate, simplification, algebraic manipulation
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

Rationalisation is the process of eliminating surds (irrational numbers) from the denominator of a fraction by multiplying both the numerator and denominator by an appropriate expression — effectively multiplying by a clever form of 1. For single-term denominators one multiplies by the surd itself; for two-term denominators one multiplies by the conjugate, exploiting the difference-of-squares identity.

## Key Formula

**Single-term denominator** — multiply by $\frac{\sqrt{a}}{\sqrt{a}}$:

$$\frac{1}{\sqrt{a}} = \frac{1}{\sqrt{a}} \times \frac{\sqrt{a}}{\sqrt{a}} = \frac{\sqrt{a}}{a}$$

**Two-term (conjugate) denominator** — multiply by $\frac{a - \sqrt{b}}{a - \sqrt{b}}$:

$$\frac{1}{a + \sqrt{b}} = \frac{1}{a + \sqrt{b}} \times \frac{a - \sqrt{b}}{a - \sqrt{b}} = \frac{a - \sqrt{b}}{a^2 - b}$$

**Underpinning identity** — the difference of squares:

$$(a + \sqrt{b})(a - \sqrt{b}) = a^2 - (\sqrt{b})^2 = a^2 - b$$

## Example

**Example 1 — single-term denominator:**

$$\frac{5}{\sqrt{3}} = \frac{5}{\sqrt{3}} \times \frac{\sqrt{3}}{\sqrt{3}} = \frac{5\sqrt{3}}{3}$$

**Example 2 — conjugate method:**

$$\frac{4}{3 - \sqrt{2}} = \frac{4}{3 - \sqrt{2}} \times \frac{3 + \sqrt{2}}{3 + \sqrt{2}} = \frac{4(3 + \sqrt{2})}{9 - 2} = \frac{12 + 4\sqrt{2}}{7}$$

## Remember

Rationalisation is a routine algebraic step when simplifying closed-form expressions in quantitative finance. The Black–Scholes terms $d_1$ and $d_2$ contain $\sigma\sqrt{T}$ in the denominator; rationalising or restructuring such expressions makes differentiation cleaner when deriving Greeks like Vega and Gamma. In calibration and numerical work, rewriting expressions to remove surds from denominators can also improve numerical stability and reduce floating-point cancellation errors.
