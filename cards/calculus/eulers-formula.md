# Euler's Formula

**Topic:** Calculus
**Tags:** euler's formula, complex exponential, taylor series, fourier transform, characteristic functions
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Euler's formula** states that for any real number $\theta$, the complex exponential $e^{i\theta}$ equals $\cos\theta + i\sin\theta$. It unifies the exponential function and trigonometry by showing that rotating through angle $\theta$ in the complex plane is the same as multiplying by $e^{i\theta}$, and it is the engine behind the Fourier transform and characteristic functions in probability theory.

## Key Formula

$$e^{i\theta} = \cos\theta + i\sin\theta$$

**Derivation via Taylor series** — expand each function around $0$:

$$e^{i\theta} = 1 + i\theta + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!} + \frac{(i\theta)^4}{4!} + \cdots$$

Using $i^2 = -1,\; i^3 = -i,\; i^4 = 1$ and separating real and imaginary parts:

$$= \underbrace{\left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots\right)}_{\cos\theta} + i\underbrace{\left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \cdots\right)}_{\sin\theta}$$

**Conjugate symmetry** (used constantly when taking real parts):

$$e^{-i\theta} = \cos\theta - i\sin\theta$$

$$\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}, \qquad \sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$$

## Example

Let $\theta = \pi/3$ (60°). Euler's formula gives:

$$e^{i\pi/3} = \cos\frac{\pi}{3} + i\sin\frac{\pi}{3} = \frac{1}{2} + i\frac{\sqrt{3}}{2}$$

The modulus is $\left|e^{i\pi/3}\right| = \sqrt{(1/2)^2 + (\sqrt{3}/2)^2} = \sqrt{1/4 + 3/4} = 1$, confirming that $e^{i\theta}$ always lies on the unit circle regardless of $\theta$.

Squaring: $e^{i2\pi/3} = \cos(2\pi/3) + i\sin(2\pi/3) = -1/2 + i\sqrt{3}/2$. This is simply rotating by another 60°, demonstrating how complex multiplication corresponds to adding angles.

## Remember

The characteristic function of a log-return $X$ is $\varphi_X(u) = E[e^{iuX}]$ — Euler's formula is what makes this integral always converge, because $|e^{iuX}| = 1$ for real $u$ and real $X$, unlike the moment generating function $E[e^{uX}]$ which can diverge for fat-tailed distributions. In the Heston and Variance Gamma models a closed-form $\varphi_{\ln S_T}(u)$ is available; quants apply Euler's formula in reverse when performing the Carr-Madan FFT inversion to price a full strip of European calls, turning a one-line characteristic function into a grid of option prices in milliseconds.
