# Polar Form

**Topic:** Calculus
**Tags:** polar form, complex numbers, Euler's formula, modulus, argument
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **polar form** of a complex number expresses $z$ by its distance from the origin $r = |z|$ (the **modulus**) and the angle $\theta$ it makes with the positive real axis (the **argument**), rather than by its Cartesian coordinates $a + bi$. The two representations are linked by Euler's formula: $e^{i\theta} = \cos\theta + i\sin\theta$.

## Key Formula

$$z = a + bi = r(\cos\theta + i\sin\theta) = r\,e^{i\theta}$$

where

$$r = |z| = \sqrt{a^2 + b^2}, \qquad \theta = \arg(z) = \arctan\!\left(\frac{b}{a}\right)$$

**Multiplication in polar form** — moduli multiply and arguments add:

$$z_1 z_2 = r_1 r_2\,e^{i(\theta_1+\theta_2)}$$

**De Moivre's theorem** — powers and roots become trivial:

$$z^n = r^n e^{in\theta} = r^n(\cos n\theta + i\sin n\theta)$$

## Example

Let $z = 1 + i\sqrt{3}$.

- Modulus: $r = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{4} = 2$.
- Argument: $\theta = \arctan(\sqrt{3}/1) = \pi/3$.
- Polar form: $z = 2\,e^{i\pi/3}$.
- Cube: $z^3 = 2^3 e^{i\cdot 3\cdot\pi/3} = 8\,e^{i\pi} = 8(\cos\pi + i\sin\pi) = -8$.

Verification: $(1+i\sqrt{3})^3 = 1 + 3(i\sqrt{3}) + 3(i\sqrt{3})^2 + (i\sqrt{3})^3 = 1 + 3i\sqrt{3} - 9 - 3i\sqrt{3} = -8$. ✓

## Remember

In the Carr-Madan FFT option-pricing method, the log-price density $f(\ln S_T)$ is priced by inverting its characteristic function $\varphi(u) = E[e^{iu\ln S_T}]$. Each evaluation of $\varphi$ at a frequency grid point $u_k$ produces a complex number; the polar form $r_k e^{i\theta_k}$ makes it immediately visible that $|\varphi(u)| \leq 1$ always (the modulus stays on or inside the unit circle), which guarantees the numerical inversion is stable. Models such as Heston give closed-form $\varphi(u)$ in polar-friendly exponential form, so polar arithmetic — multiply moduli, add arguments — is the natural language for manipulating these expressions.
