# Complex Conjugate

**Topic:** Calculus
**Tags:** complex conjugate, complex numbers, modulus, characteristic function, Fourier transform
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **complex conjugate** of a complex number $z = a + bi$ is $\bar{z} = a - bi$ — the imaginary part is negated while the real part is unchanged. Conjugation reflects the number across the real axis in the complex plane.

## Key Formula

For $z = a + bi = r e^{i\theta}$:

$$\bar{z} = a - bi = r e^{-i\theta}$$

**Key properties:**

$$z \bar{z} = a^2 + b^2 = |z|^2 = r^2$$

$$z + \bar{z} = 2a = 2\,\text{Re}(z), \qquad z - \bar{z} = 2bi = 2i\,\text{Im}(z)$$

$$\overline{z_1 + z_2} = \bar{z}_1 + \bar{z}_2, \qquad \overline{z_1 z_2} = \bar{z}_1 \bar{z}_2$$

**Polynomials with real coefficients:** if $z = a + bi$ is a root, then $\bar{z} = a - bi$ is also a root. Complex roots always occur in **conjugate pairs**.

**Real part extraction:**

$$\text{Re}(z) = \frac{z + \bar{z}}{2}, \qquad |z|^2 = z\bar{z}$$

## Example

The characteristic function of a random variable $X$ is $\varphi(u) = E[e^{iuX}]$. For a standard normal $X \sim \mathcal{N}(0,1)$:

$$\varphi(u) = e^{-u^2/2}$$

This is real-valued, which reflects the fact that $X$ is symmetric: $\varphi(-u) = \overline{\varphi(u)}$ (the characteristic function of a real random variable always satisfies this conjugate symmetry). The option price recovered via Fourier inversion uses:

$$\text{Re}\!\left[\int_0^\infty e^{-iuk} \varphi(u)\, du\right]$$

Taking only the real part (using $\text{Re}(z) = \frac{z + \bar{z}}{2}$) halves the numerical integration domain.

## Remember

The conjugate symmetry $\varphi(-u) = \overline{\varphi(u)}$ of characteristic functions — a direct consequence of complex conjugation — is exploited in the Carr-Madan FFT option pricing method to halve the integration range. When computing the Fourier inversion numerically, the integrand for $u < 0$ is just the conjugate of the integrand for $u > 0$, so only positive frequencies need be evaluated. This symmetry also explains why polynomial roots come in conjugate pairs: if you find one complex root of a characteristic equation (e.g. in an affine term structure model), its conjugate is automatically the other.
