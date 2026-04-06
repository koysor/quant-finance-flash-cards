# Addition and Subtraction of Complex Numbers

**Topic:** Calculus
**Tags:** complex numbers, addition, subtraction, real part, imaginary part
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

To add or subtract two complex numbers, combine their real parts and imaginary parts separately. If $z_1 = a + bi$ and $z_2 = c + di$, then addition and subtraction are performed component-wise, treating the real and imaginary parts as independent dimensions.

## Key Formula

$$z_1 + z_2 = (a + c) + (b + d)i$$

$$z_1 - z_2 = (a - c) + (b - d)i$$

Geometrically, addition corresponds to **vector addition** in the complex plane: place $z_2$ tail-to-head after $z_1$.

## Example

Let $z_1 = 3 + 4i$ and $z_2 = 1 - 2i$.

$$z_1 + z_2 = (3 + 1) + (4 + (-2))i = 4 + 2i$$

$$z_1 - z_2 = (3 - 1) + (4 - (-2))i = 2 + 6i$$

Modulus check: $|z_1 + z_2| = \sqrt{4^2 + 2^2} = \sqrt{20} = 2\sqrt{5}$.

## Remember

In quantitative finance, complex number addition arises when combining characteristic functions or when decomposing a Fourier-domain signal into contributions from separate sources. For example, if two independent risk factors have characteristic functions $\varphi_1(u)$ and $\varphi_2(u)$, the characteristic function of their sum is the product $\varphi_1(u)\varphi_2(u)$ — but the exponents (log-characteristic functions) are added component-wise, reducing to complex addition. Understanding how real and imaginary parts combine separately is also essential when interpreting the output of numerical Fourier inversion in the Carr-Madan option pricing framework.
