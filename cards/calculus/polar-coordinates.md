# Polar Co-ordinates

**Topic:** Calculus
**Tags:** polar coordinates, complex numbers, Fourier transform, coordinate systems, trigonometry
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

Polar co-ordinates describe a point in the plane by its distance $r$ from the origin (the **modulus**) and the angle $\theta$ it makes with the positive real axis (the **argument**), rather than by its horizontal and vertical displacements. Any Cartesian point $(x, y)$ has a unique polar representation $(r, \theta)$ with $r \geq 0$ and $\theta \in (-\pi, \pi]$.

## Key Formula

**Cartesian to polar:**

$$r = \sqrt{x^2 + y^2}, \qquad \theta = \arctan\!\left(\frac{y}{x}\right)$$

**Polar to Cartesian:**

$$x = r\cos\theta, \qquad y = r\sin\theta$$

**Complex number in polar form:**

$$z = x + iy = r\,e^{i\theta} = r(\cos\theta + i\sin\theta)$$

**Multiplication rule** (moduli multiply, arguments add):

$$z_1 z_2 = r_1 r_2\, e^{i(\theta_1 + \theta_2)}$$

**De Moivre's theorem:**

$$z^n = r^n e^{in\theta} = r^n(\cos n\theta + i\sin n\theta)$$

## Example

Let $z = 1 + i\sqrt{3}$.

- Modulus: $r = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{4} = 2$
- Argument: $\theta = \arctan(\sqrt{3}/1) = \pi/3$
- Polar form: $z = 2\,e^{i\pi/3}$

Squaring: $z^2 = 4\,e^{i \cdot 2\pi/3} = 4\!\left(\cos\tfrac{2\pi}{3} + i\sin\tfrac{2\pi}{3}\right) = 4\!\left(-\tfrac{1}{2} + i\tfrac{\sqrt{3}}{2}\right) = -2 + 2i\sqrt{3}$.

Verify directly: $(1 + i\sqrt{3})^2 = 1 + 2i\sqrt{3} - 3 = -2 + 2i\sqrt{3}$. ✓

## Remember

The polar form of a complex number is the natural language of the Fourier transform in quantitative finance. The characteristic function $\varphi_X(u) = E[e^{iuX}]$ of a log-price is a complex number; at each frequency $u$ it has a modulus (how much amplitude remains at that frequency) and an argument (the phase shift). When the Carr-Madan method integrates $e^{-iuk}\,\varphi_X(u)$ to recover option prices, it is rotating complex exponentials in the polar plane. The multiplication rule $r_1 r_2\,e^{i(\theta_1+\theta_2)}$ also underlies the convolution theorem: multiplying characteristic functions (i.e. summing independent random variables) is modular arithmetic on moduli and arguments.
