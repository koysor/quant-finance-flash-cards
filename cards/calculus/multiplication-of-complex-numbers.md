# Multiplication of Complex Numbers

**Topic:** Calculus
**Tags:** complex numbers, FOIL, modulus, argument, polar form
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

Multiplying two complex numbers combines their magnitudes and rotates their angles. In Cartesian form the product is expanded term by term using the FOIL method and the identity $i^2 = -1$; in polar form the rule is elegantly geometric: multiply the moduli and add the arguments.

## Key Formula

**Cartesian (FOIL) form** — for $z_1 = a + bi$ and $z_2 = c + di$:

$$z_1 z_2 = (a + bi)(c + di) = ac + adi + bci + bdi^2 = (ac - bd) + (ad + bc)i$$

**Polar form** — for $z_1 = r_1 e^{i\theta_1}$ and $z_2 = r_2 e^{i\theta_2}$:

$$z_1 z_2 = r_1 r_2\, e^{i(\theta_1 + \theta_2)}$$

so $|z_1 z_2| = |z_1|\,|z_2|$ and $\arg(z_1 z_2) = \arg(z_1) + \arg(z_2)$.

## Example

Let $z_1 = 3 + 4i$ and $z_2 = 1 + 2i$.

**FOIL:** $z_1 z_2 = (3)(1) + (3)(2i) + (4i)(1) + (4i)(2i) = 3 + 6i + 4i + 8i^2 = 3 + 10i - 8 = -5 + 10i$.

**Polar check:** $|z_1| = 5$, $|z_2| = \sqrt{5}$, so $|z_1 z_2| = 5\sqrt{5}$.
Verify: $|-5 + 10i| = \sqrt{25 + 100} = \sqrt{125} = 5\sqrt{5}$. $\checkmark$

## Remember

Polar multiplication — multiply moduli, add arguments — is the algebraic backbone of the **characteristic function** machinery used in quant finance. When you compute $\varphi_{X+Y}(u) = \varphi_X(u)\,\varphi_Y(u)$ for independent $X$ and $Y$, each factor $\varphi(u) = r e^{i\theta}$ contributes its modulus and argument independently; the product's argument is the sum of the individual arguments, which is exactly why the log-characteristic function (cumulant generating function) adds cumulants across independent assets. This underpins the fast Fourier transform option-pricing methods (Carr-Madan, Lewis) used daily in derivatives desks.
