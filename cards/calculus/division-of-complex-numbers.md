# Division of Complex Numbers

**Topic:** Calculus
**Tags:** complex numbers, division, conjugate, modulus, argument, characteristic functions
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

To divide one complex number by another, multiply both numerator and denominator by the **conjugate** of the denominator. This eliminates the imaginary part from the denominator, producing a real divisor and leaving a standard complex number in the result. In polar form, division reduces to dividing moduli and subtracting arguments.

## Key Formula

**Cartesian form** (multiply by conjugate):

$$\frac{z_1}{z_2} = \frac{a_1 + b_1 i}{a_2 + b_2 i} = \frac{(a_1 + b_1 i)(a_2 - b_2 i)}{a_2^2 + b_2^2}$$

which gives:

$$\frac{z_1}{z_2} = \frac{a_1 a_2 + b_1 b_2}{a_2^2 + b_2^2} + \frac{b_1 a_2 - a_1 b_2}{a_2^2 + b_2^2}\,i$$

**Polar form** (divide moduli, subtract arguments):

$$\frac{z_1}{z_2} = \frac{r_1}{r_2}\,e^{i(\theta_1 - \theta_2)}, \qquad r_2 \neq 0$$

## Example

Compute $\dfrac{3 + 4i}{1 + 2i}$.

Multiply numerator and denominator by the conjugate $1 - 2i$:

$$\frac{(3 + 4i)(1 - 2i)}{(1 + 2i)(1 - 2i)} = \frac{3 - 6i + 4i - 8i^2}{1 + 4} = \frac{3 - 2i + 8}{5} = \frac{11 - 2i}{5} = \frac{11}{5} - \frac{2}{5}i$$

**Check using polar form:** $|z_1| = \sqrt{9+16} = 5$, $|z_2| = \sqrt{1+4} = \sqrt{5}$, so $\left|\frac{z_1}{z_2}\right| = \frac{5}{\sqrt{5}} = \sqrt{5}$. Verify: $\left|\frac{11}{5} - \frac{2}{5}i\right| = \frac{1}{5}\sqrt{121 + 4} = \frac{\sqrt{125}}{5} = \sqrt{5}$. ✓

## Remember

Complex division appears in quantitative finance when computing the **Gil-Pelaez Fourier inversion** integral to recover option prices and probability densities from characteristic functions. The integrand contains terms of the form $e^{-iuk}\,\varphi(u) / (iu)$, which is a division of complex exponentials. In polar form this becomes clear: dividing $e^{i\alpha}$ by $e^{i\beta}$ simply subtracts the argument, so multiplying by $e^{-iuk}$ shifts the characteristic function's phase by $-uk$. Understanding conjugate-based division is also essential when extracting the real part of a complex ratio — the key step that converts a complex Fourier integral into a real-valued probability or price.
