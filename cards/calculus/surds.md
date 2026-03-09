# Surds

**Topic:** Calculus
**Tags:** surds, irrational numbers, square roots, simplification, rationalisation
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

A **surd** is an irrational number expressed as the root of a positive integer that cannot be simplified to a rational number — for example $\sqrt{2}$, $\sqrt{3}$, or $\sqrt[3]{5}$. Surds are left in exact root form rather than converted to inexact decimals, preserving precision in algebraic manipulation.

## Key Formula

**Simplification** — factor out perfect squares:

$$\sqrt{ab} = \sqrt{a} \cdot \sqrt{b}, \qquad \sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$$

**Rationalising the denominator:**

$$\frac{1}{\sqrt{a}} = \frac{\sqrt{a}}{a}, \qquad \frac{1}{a + \sqrt{b}} = \frac{a - \sqrt{b}}{a^2 - b}$$

**Fractional exponent form:**

$$\sqrt[n]{a} = a^{1/n}, \qquad \sqrt[n]{a^m} = a^{m/n}$$

## Example

Simplify $\sqrt{72}$:

$$\sqrt{72} = \sqrt{36 \times 2} = 6\sqrt{2}$$

Rationalise $\dfrac{5}{3 + \sqrt{2}}$:

$$\frac{5}{3 + \sqrt{2}} \times \frac{3 - \sqrt{2}}{3 - \sqrt{2}} = \frac{5(3 - \sqrt{2})}{9 - 2} = \frac{15 - 5\sqrt{2}}{7}$$

## Remember

Surds appear throughout quantitative finance whenever exact algebraic expressions involve square roots. The $\sigma\sqrt{T}$ term in the Black-Scholes formula for $d_1$ and $d_2$ is a surd when $T$ is not a perfect square — keeping it in root form avoids rounding error that compounds through option pricing calculations. The square-root rule for scaling volatility ($\sigma_{\text{annual}} = \sigma_{\text{daily}} \times \sqrt{252}$) relies on surd arithmetic, and rationalising denominators is a routine step when simplifying Greeks or solving quadratic equations that arise in calibration problems.
