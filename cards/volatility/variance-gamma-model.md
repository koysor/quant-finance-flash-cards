# Variance Gamma Model

**Topic:** Volatility
**Tags:** variance gamma, lévy process, skew, excess kurtosis, option pricing, characteristic function
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

The Variance Gamma (VG) model is a Lévy process model for asset prices that generalises Brownian motion by allowing jumps and controlling skewness and kurtosis independently. It is constructed by time-changing a Brownian motion with drift using a Gamma process, producing return distributions with fatter tails and asymmetry not captured by Black-Scholes.

## Key Formula

The log-price under VG is:

$$\ln S_T = \ln S_0 + (r + \omega)T + \theta \,G_T + \sigma W_{G_T}$$

Where:
- $G_T \sim \text{Gamma}(T/\nu,\, \nu)$ — the Gamma subordinator with variance rate $\nu > 0$
- $W_t$ — standard Brownian motion, independent of $G_T$
- $\theta$ — drift of the subordinated Brownian motion (controls **skewness**)
- $\sigma$ — volatility of the subordinated Brownian motion (controls **kurtosis width**)
- $\omega = \frac{1}{\nu}\ln\!\left(1 - \theta\nu - \tfrac{1}{2}\sigma^2\nu\right)$ — martingale correction

The characteristic function is closed-form:

$$\phi_{VG}(u) = \exp\!\left(iuT(r+\omega)\right) \left(1 - iu\theta\nu + \tfrac{1}{2}\sigma^2\nu u^2\right)^{-T/\nu}$$

## Example

Calibrate VG to S&P 500 options. Black-Scholes requires a different implied vol at each strike (the smile). VG fits the full smile with three parameters: $\sigma = 0.15$, $\theta = -0.14$ (negative skew — left tail fatter than right), $\nu = 0.20$ (excess kurtosis). The closed-form characteristic function feeds directly into the Carr-Madan FFT algorithm to price the entire option strip in milliseconds.

## Remember

The VG model is a practical bridge between Black-Scholes and full jump-diffusion models. Because $\theta$ and $\nu$ directly control skew and excess kurtosis, the model fits equity option smiles with far fewer parameters than local volatility, and its closed-form characteristic function makes it amenable to FFT pricing. It is widely used for equity exotics and credit derivatives where asymmetric fat tails are economically meaningful.
