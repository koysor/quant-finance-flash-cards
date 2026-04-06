# Imaginary Unit

**Topic:** Mathematical Notation
**Tags:** imaginary unit, complex numbers, fourier transform, characteristic functions, euler's formula
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **imaginary unit** $i$ is defined as the number satisfying $i^2 = -1$, extending the real number line to the complex plane. It is not a real number — no point on the real line squares to $-1$ — but it obeys all ordinary arithmetic rules once this single identity is accepted. Every complex number $z = a + bi$ is built from $i$, where $a, b \in \mathbb{R}$.

## Key Formula

**Defining identity and cyclic powers:**

$$i^2 = -1, \qquad i^3 = -i, \qquad i^4 = 1, \qquad i^{n+4} = i^n$$

**Euler's formula** (the most important consequence):

$$e^{i\theta} = \cos\theta + i\sin\theta, \qquad \theta \in \mathbb{R}$$

**Modulus of a complex exponential:**

$$\left|e^{i\theta}\right| = \sqrt{\cos^2\theta + \sin^2\theta} = 1$$

The modulus is always 1, regardless of $\theta$ — a fact that makes integrals involving $e^{iuX}$ always converge.

## Example

Evaluate $i^{17}$:

$$i^{17} = i^{4 \times 4 + 1} = (i^4)^4 \cdot i^1 = 1^4 \cdot i = i$$

Now compute $|e^{i\pi/3}|$ and verify Euler's formula:

$$e^{i\pi/3} = \cos\tfrac{\pi}{3} + i\sin\tfrac{\pi}{3} = \tfrac{1}{2} + i\tfrac{\sqrt{3}}{2}$$

$$\left|\tfrac{1}{2} + i\tfrac{\sqrt{3}}{2}\right| = \sqrt{\tfrac{1}{4} + \tfrac{3}{4}} = \sqrt{1} = 1 \checkmark$$

## Remember

The property $|e^{iuX}| = 1$ for any real $u$ and $X$ is what makes the **characteristic function** $\varphi_X(u) = E[e^{iuX}]$ always exist — even for fat-tailed distributions where the moment generating function $E[e^{uX}]$ diverges. Quants exploit this in the **Carr-Madan FFT method**: replace the intractable density of $\ln S_T$ with its characteristic function (analytically available in Heston, VG, NIG models), then numerically invert via a fast Fourier transform to price European options across a full strike grid. The imaginary unit is therefore the key that unlocks analytical option pricing beyond Black-Scholes.
