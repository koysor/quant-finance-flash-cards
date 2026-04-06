# Trigonometric Functions

**Topic:** Calculus
**Tags:** trigonometry, sine, cosine, tangent, periodicity, Fourier, derivatives
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **trigonometric functions** sin, cos, and tan are defined in a right-angled triangle as ratios of sides relative to an angle $\theta$:

$$\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}}, \qquad \cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}}, \qquad \tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{\text{opposite}}{\text{adjacent}}$$

Extended to all real angles via the unit circle, they become periodic functions with period $2\pi$.

## Key Formula

**Pythagorean identity:**

$$\sin^2\theta + \cos^2\theta = 1$$

**Derivatives:**

$$\frac{d}{d\theta}\sin\theta = \cos\theta, \qquad \frac{d}{d\theta}\cos\theta = -\sin\theta, \qquad \frac{d}{d\theta}\tan\theta = \sec^2\theta$$

**Euler's formula** — the bridge to complex exponentials:

$$e^{i\theta} = \cos\theta + i\sin\theta$$

Extracting real and imaginary parts:

$$\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}, \qquad \sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$$

**Small angle approximations** (for $\theta \ll 1$ radians):

$$\sin\theta \approx \theta, \qquad \cos\theta \approx 1 - \frac{\theta^2}{2}, \qquad \tan\theta \approx \theta$$

## Example

The Fourier transform of a function $f(t)$ decomposes it into sinusoidal components:

$$\hat{f}(\omega) = \int_{-\infty}^{\infty} f(t)\, e^{-i\omega t}\, dt = \int_{-\infty}^{\infty} f(t)[\cos(\omega t) - i\sin(\omega t)]\, dt$$

The real part of the integrand involves $\cos(\omega t)$ — symmetric oscillations — and the imaginary part involves $\sin(\omega t)$ — antisymmetric oscillations. This is why even functions (like the normal PDF) have purely real Fourier transforms: the $\sin$ terms vanish.

## Remember

Trigonometric functions appear in quantitative finance primarily through **Fourier transforms and characteristic functions**. The characteristic function $\varphi_X(u) = E[e^{iuX}] = E[\cos(uX)] + i\,E[\sin(uX)]$ is a complex sinusoidal average of the distribution. The Carr-Madan FFT option pricing method evaluates an integral involving $e^{-iuk}$ — a complex exponential that is a linear combination of $\cos(uk)$ and $\sin(uk)$. Without fluency with trigonometric functions and their relationship to complex exponentials via Euler's formula, Fourier-based pricing methods are impenetrable.
