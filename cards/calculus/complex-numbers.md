# Complex Numbers

**Topic:** Calculus
**Tags:** complex numbers, imaginary unit, Euler's formula, Fourier transform, characteristic functions
**Author:** Claude Sonnet 4.6

---

## Definition

A **complex number** $z$ is a number of the form $z = a + bi$, where $a, b \in \mathbb{R}$ and $i$ is the imaginary unit satisfying $i^2 = -1$. The real part is $\text{Re}(z) = a$ and the imaginary part is $\text{Im}(z) = b$; the number can equally be represented in polar form as $z = r e^{i\theta}$, where $r = |z|$ is the modulus and $\theta = \arg(z)$ is the argument.

## Key Formula

**Cartesian and polar forms:**

$$z = a + bi = r(\cos\theta + i\sin\theta) = r e^{i\theta}$$

where $r = \sqrt{a^2 + b^2}$ and $\theta = \arctan(b/a)$.

**Euler's formula** (the bridge between the two forms):

$$e^{i\theta} = \cos\theta + i\sin\theta$$

**Complex conjugate** $\bar{z} = a - bi$, so $z\bar{z} = r^2 = a^2 + b^2$.

**Multiplication in polar form:**

$$z_1 z_2 = r_1 r_2\, e^{i(\theta_1 + \theta_2)}$$

## Example

Let $z_1 = 1 + i$ and $z_2 = 1 - i$.

- Modulus: $|z_1| = \sqrt{1^2 + 1^2} = \sqrt{2}$; argument: $\theta = \arctan(1/1) = \pi/4$.
- Product: $z_1 z_2 = (1+i)(1-i) = 1 - i^2 = 1 + 1 = 2$. In polar form: $\sqrt{2}\cdot\sqrt{2}\cdot e^{i(\pi/4 - \pi/4)} = 2 e^{0} = 2$. ✓
- Euler: $e^{i\pi} = \cos\pi + i\sin\pi = -1$, giving the famous identity $e^{i\pi} + 1 = 0$.

## Remember

The imaginary unit $i$ is the gateway to characteristic functions in quantitative finance. The characteristic function of a random variable $X$ is $\varphi_X(u) = E[e^{iuX}]$ — the expectation of $e^{iuX}$ always exists (the modulus $|e^{iuX}| = 1$), unlike the moment generating function which can diverge for fat-tailed distributions. The Carr-Madan FFT option-pricing method exploits this: a closed-form $\varphi_{\ln S_T}(u)$ (available in the Heston model) is numerically inverted via a fast Fourier transform to price a whole strip of European calls simultaneously.
