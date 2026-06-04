# Rough Bergomi Model

**Topic:** Volatility
**Tags:** rough volatility, fractional brownian motion, hurst exponent, bergomi, volatility surface
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **Rough Bergomi model** (Bayer, Friz & Gatheral, 2016) is a stochastic volatility model in which instantaneous variance $V_t$ is driven by a **fractional Brownian motion** with Hurst exponent $H < 1/2$, giving the variance process "rough" sample paths. Unlike classical models (Heston, SABR) where volatility is driven by a standard Brownian motion ($H = 1/2$), rough models reproduce the observed steep short-maturity implied volatility skew and the power-law term structure of ATM skew that classical models cannot fit.

## Key Formula

The variance process under the rough Bergomi model:

$$V_t = V_0 \exp\!\left(\eta \widetilde{W}^H_t - \tfrac{1}{2}\eta^2 t^{2H}\right)$$

where $\widetilde{W}^H_t = \sqrt{2H} \int_0^t (t-s)^{H-1/2}\, dW_s$ is a Riemann–Liouville fractional Brownian motion, $H \in (0, 1/2)$ is the Hurst exponent controlling roughness, and $\eta > 0$ is the volatility of volatility. The asset price satisfies:

$$dS_t = S_t \sqrt{V_t}\left(\rho\, dW_t + \sqrt{1-\rho^2}\, dB_t\right)$$

with $W$ and $B$ independent Brownian motions and $\rho \leq 0$ the leverage correlation. The ATM skew decays as a power law:

$$\text{ATM skew} \sim t^{H - 1/2}, \qquad H \approx 0.1$$

## Example

Calibrating to S&P 500 options: classical Heston gives an ATM skew term structure $\sim t^{-0.1}$ (too slow for short maturities), while rough Bergomi with $H = 0.1$ gives skew $\sim t^{-0.4}$, matching the empirically observed power law. Typical calibrated parameters are $V_0 = 0.04$, $\eta = 1.9$, $\rho = -0.9$. The model prices one-week options with implied vols 3–4 points closer to market than Heston, at the cost of Monte Carlo-only pricing — there is no closed-form characteristic function.

## Remember

The rough Bergomi model is not just a better fit — it is motivated by a striking empirical fact: realised volatility time series estimated from high-frequency equity data exhibit a Hurst exponent $H \approx 0.1$, far rougher than a standard Brownian motion ($H = 0.5$). This roughness directly explains why short-dated S&P 500 options trade at steeper skews than classical models predict, and why the skew explodes as maturity approaches zero. The practical challenge is that simulation requires discretising a fractional integral, making calibration slow — this is a primary motivation for neural network calibration surrogates, which learn the parameter-to-surface mapping offline and then invert it in milliseconds.
