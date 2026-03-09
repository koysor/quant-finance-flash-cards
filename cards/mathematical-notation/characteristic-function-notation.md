# Characteristic Function Notation

**Topic:** Mathematical Notation
**Tags:** characteristic function, Fourier transform, Lévy processes, option pricing, FFT
**Created:** 2026-03-09
**Author:** Claude Sonnet 4.6

---

## Definition

The **characteristic function** of a random variable $X$ is its Fourier transform of the probability density. Unlike the moment generating function (MGF), it always exists for any distribution — including fat-tailed distributions where the MGF diverges. This makes it the preferred tool for pricing options under Lévy processes (jump-diffusion, variance gamma, CGMY models).

| Symbol | Read as | Meaning |
|---|---|---|
| $\varphi_X(u)$ | "phi sub X of u" | Characteristic function of $X$ evaluated at frequency $u$ |
| $E[e^{iuX}]$ | "expectation of e to the i u X" | Definition of $\varphi_X(u)$; $i = \sqrt{-1}$ |
| $i$ | "i" | Imaginary unit, $i^2 = -1$; makes the integral always converge |
| $\hat{f}(u)$ | "f-hat" | Fourier transform of the density $f$ — same as $\varphi_X(u)$ |
| $\varphi_X(u) = e^{\psi(u)}$ | "cumulant generating form" | $\psi(u)$ is the **characteristic exponent**; additive for independent increments |

## Key Formula

**Definition:**

$$\varphi_X(u) = E\!\left[e^{iuX}\right] = \int_{-\infty}^{\infty} e^{iux} f_X(x) \, dx$$

**Inversion formula** (recover the density from $\varphi_X$):

$$f_X(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-iux} \varphi_X(u) \, du$$

**Carr-Madan formula** for European call option pricing via FFT:

$$C(K) = \frac{e^{-\alpha \ln K}}{\pi} \int_0^{\infty} e^{-iv \ln K} \frac{e^{-rT} \varphi_{\ln S_T}(v - (\alpha+1)i)}{\alpha^2 + \alpha - v^2 + i(2\alpha+1)v} \, dv$$

## Example

For $X \sim \mathcal{N}(\mu, \sigma^2)$, the characteristic function is:

$$\varphi_X(u) = \exp\!\left(i\mu u - \tfrac{1}{2}\sigma^2 u^2\right)$$

For a sum of two independent normals $X + Y$ with $Y \sim \mathcal{N}(\nu, \tau^2)$:

$$\varphi_{X+Y}(u) = \varphi_X(u) \cdot \varphi_Y(u) = \exp\!\left(i(\mu+\nu)u - \tfrac{1}{2}(\sigma^2+\tau^2)u^2\right)$$

This recovers $X + Y \sim \mathcal{N}(\mu+\nu, \sigma^2+\tau^2)$ without computing a convolution integral.

## Remember

In the Heston model and other stochastic volatility models, the risk-neutral log-price $\ln S_T$ does not have a closed-form density — but it *does* have a closed-form characteristic function. The **Carr-Madan FFT method** uses this: evaluate $\varphi_{\ln S_T}(u)$ analytically, then numerically invert via a fast Fourier transform to obtain option prices across a grid of strikes in milliseconds. This is why quants learn characteristic functions — they unlock analytical tractability for models where the density is intractable.
