# Fourier Transform

**Topic:** Calculus
**Tags:** fourier transform, frequency domain, complex exponential, signal analysis, characteristic functions
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The Fourier transform decomposes a function $f(x)$ into a continuous superposition of complex sinusoids $e^{i\omega x}$, each weighted by a frequency amplitude $\hat{f}(\omega)$. The result lives in the **frequency domain**, revealing which oscillatory components are present — and at what strength — rather than how the function behaves through time or space. The inverse transform reconstructs $f$ exactly from its frequency-domain representation.

## Key Formula

**Forward transform** (time/space domain → frequency domain):

$$\hat{f}(\omega) = \int_{-\infty}^{\infty} f(x)\, e^{-i\omega x}\, dx$$

**Inverse transform** (frequency domain → time/space domain):

$$f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \hat{f}(\omega)\, e^{i\omega x}\, d\omega$$

**Parseval's theorem** (energy is preserved under the transform):

$$\int_{-\infty}^{\infty} |f(x)|^2\, dx = \frac{1}{2\pi} \int_{-\infty}^{\infty} |\hat{f}(\omega)|^2\, d\omega$$

**Convolution theorem** (convolution in one domain = multiplication in the other):

$$\widehat{f * g}(\omega) = \hat{f}(\omega)\cdot \hat{g}(\omega)$$

## Example

Let $f(x) = e^{-a|x|}$ for $a > 0$. Its Fourier transform is:

$$\hat{f}(\omega) = \int_{-\infty}^{\infty} e^{-a|x|} e^{-i\omega x}\, dx = \frac{2a}{a^2 + \omega^2}$$

Setting $a = 1$: $\hat{f}(\omega) = \dfrac{2}{1 + \omega^2}$.

This is a Lorentzian (Cauchy) shape — the original exponential decay has most of its "energy" concentrated at low frequencies, with the transform decaying as $1/\omega^2$ for large $\omega$, confirming that sharp features in the time domain correspond to high-frequency content.

## Remember

The characteristic function of a random variable $X$ is precisely the Fourier transform of its probability density: $\varphi_X(u) = E[e^{iuX}] = \hat{f}_X(u)$. This connection is the bridge between classical analysis and probability theory, and it is what makes the Carr-Madan FFT option-pricing method work. Models such as Heston, Variance Gamma, and CGMY have analytically tractable characteristic functions (i.e. tractable Fourier transforms of their log-price densities) even when the density itself has no closed form. Quants invert these transforms numerically — via the fast Fourier transform — to recover option prices across a full strike grid in milliseconds. Understanding the Fourier transform is therefore a prerequisite for any serious study of option pricing under non-Black-Scholes dynamics.
