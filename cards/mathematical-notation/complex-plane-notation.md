# Complex Plane Notation

**Topic:** Mathematical Notation
**Tags:** notation, complex numbers, real part, imaginary part, modulus, argument, complex plane
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

The **complex plane** (Argand plane) uses standard notation to decompose, visualise, and manipulate complex numbers. Each complex number $z \in \mathbb{C}$ corresponds to a point in the plane:

| Symbol | Read as | Meaning |
|---|---|---|
| $\mathbb{C}$ | "the complex numbers" | Set of all $z = a + bi$, $a, b \in \mathbb{R}$ |
| $\operatorname{Re}(z)$ | "real part of $z$" | $a$ (horizontal axis coordinate) |
| $\operatorname{Im}(z)$ | "imaginary part of $z$" | $b$ (vertical axis coordinate) |
| $\lvert z \rvert$ | "modulus of $z$" | $\sqrt{a^2 + b^2}$ (distance from origin) |
| $\arg(z)$ | "argument of $z$" | $\theta = \arctan(b/a)$ (angle from positive real axis) |
| $\bar{z}$ or $z^*$ | "conjugate of $z$" | $a - bi$ (reflection in real axis) |
| $i$ | imaginary unit | $i^2 = -1$ |

## Key Formula

**Polar form (Euler's formula):**

$$z = \lvert z \rvert e^{i\theta} = \lvert z \rvert (\cos\theta + i\sin\theta)$$

**Modulus and conjugate:**

$$\lvert z \rvert^2 = z \bar{z}, \qquad \operatorname{Re}(z) = \frac{z + \bar{z}}{2}, \qquad \operatorname{Im}(z) = \frac{z - \bar{z}}{2i}$$

**Characteristic function** (using complex notation):

$$\varphi_X(u) = E\!\left[e^{iuX}\right] = \int_{-\infty}^{\infty} e^{iux} f_X(x) \, dx, \quad u \in \mathbb{R}$$

## Example

The characteristic function of the standard normal $N(0,1)$ is:

$$\varphi_X(u) = e^{-u^2/2}$$

This is a real-valued function of $u$, but intermediate steps involve $\operatorname{Re}$ and $\operatorname{Im}$ of complex exponentials. The **Gil-Palaez inversion formula** recovers the CDF from the characteristic function:

$$F(x) = \frac{1}{2} - \frac{1}{\pi}\int_0^\infty \operatorname{Re}\!\left(\frac{e^{-iux}\varphi_X(u)}{iu}\right) du$$

The $\operatorname{Re}(\cdot)$ operator discards the imaginary part of the integrand, yielding a real-valued CDF.

## Remember

The complex plane is the natural home for **characteristic functions**, which are used to price derivatives under Lévy processes (Heston, VG, NIG models). The Lewis-Lipton formula expresses European option prices as integrals over the complex plane, exploiting the fact that the characteristic function is entire (analytic everywhere) for most finance models. Numerically, the integral is evaluated along a contour in $\mathbb{C}$, making $\operatorname{Re}(z)$ and $\operatorname{Im}(z)$ not just notation but actual computed quantities in every FFT-based option pricer.
