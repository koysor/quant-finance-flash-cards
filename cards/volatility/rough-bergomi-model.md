# Rough Bergomi Model

**Topic:** Volatility
**Tags:** rough volatility, bergomi model, stochastic volatility, fractional brownian motion, volatility smile
**Created:** 2026-06-03
**Author:** Gemini CLI

---

## Definition

The **Rough Bergomi (rBergomi)** model (Bayer et al., 2016) is a non-Markovian stochastic volatility model that replaces the standard Brownian motion in the Bergomi variance process with a **fractional Brownian motion** with Hurst exponent $H < 1/2$. This modification allows the model to capture the "rough" paths of realised volatility and the extreme steepness (power-law decay) of the volatility smile for short maturities observed in market data.

## Key Formula

The variance process $\xi_t(T)$ for a maturity $T$ is modelled as:

$$v_t = \xi_0(t) \exp \left( \eta \sqrt{2H} \int_0^t (t-s)^{H-1/2} dW_s - \frac{1}{2} \eta^2 t^{2H} \right)$$

where $\eta$ is the "vol-of-vol" and $H \in (0, 0.5)$ is the **Hurst exponent**. The integral represents a **Riemann-Liouville** fractional Brownian motion. When $H=0.5$, the model collapses to the standard Markovian Bergomi model.

## Example

An equity desk is pricing a 1-week expiry ATM call option on the S&P 500. A standard Heston model, even with high vol-of-vol, produces a volatility smile that is too flat compared to market quotes. By using a Rough Bergomi model with $H \approx 0.1$, the desk can match the "at-the-money skew" $\lvert \frac{\partial \sigma_{imp}}{\partial K} \rvert$ which grows like $T^{H-1/2}$ as $T \to 0$. The rBergomi model correctly predicts the very high price for short-dated out-of-the-money puts that standard models consistently underprice.

## Remember

The Rough Bergomi model is currently the most popular "physically consistent" model for the volatility surface. While its non-Markovian nature makes it difficult to price via standard PDEs (requiring expensive Monte Carlo), it is the primary use-case for **Neural Network Model Calibration**, where deep learning is used to learn the rBergomi pricing map to allow for real-time calibration on the trading floor.
