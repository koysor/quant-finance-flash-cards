# Rough Volatility

**Topic:** Volatility
**Tags:** rough volatility, fractional brownian motion, hurst exponent, atm skew, vol-of-vol, gatheral
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Rough volatility** models (Gatheral, Jaisson, Rosenbaum, 2018) replace the smooth Brownian diffusion in Heston's variance process with a **fractional Brownian motion** $W^H$ with Hurst exponent $H \approx 0.1$. Because $H < \frac{1}{2}$, the variance path is rougher than standard Brownian motion — it has short-memory anti-persistence — which empirically produces the steep power-law decay of the ATM volatility skew term structure that Heston and other Markovian stochastic vol models cannot match.

## Key Formula

The **Rough Bergomi model** (Bayer, Friz, Gatheral, 2016) specifies log-variance as:

$$\log V_t = \log V_0 + \nu\sqrt{2H}\int_0^t (t - s)^{H - 1/2}\,dW_s^V$$

where $W^V$ is a standard Brownian motion, $\nu > 0$ is the vol-of-vol, and $H \in (0, \tfrac{1}{2})$ is the **Hurst exponent** controlling roughness. The ATM implied volatility skew scales as:

$$\psi(T) \sim \left|\frac{\partial \hat{\sigma}}{\partial \log K}\bigg|_{K=F}\right| \propto T^{H - 1/2}$$

Under Heston ($H = \frac{1}{2}$): $\psi(T) \to \text{constant}$ as $T \to 0$. Under rough vol ($H \approx 0.1$): $\psi(T) \sim T^{-0.4}$ — exploding as $T \to 0$, matching what is observed in SPX options.

## Example

SPX 1-week ATM skew is approximately $-1.5$ vol points per 10-delta shift. Heston (best fit $H = 0.5$) predicts a flat short-term skew of $-0.4$. Rough Bergomi with $H = 0.1$, $\nu = 0.8$, $\rho = -0.9$ fits $-1.4$ — close to the observed level. The difference matters: a dealer hedging a 1-week 10-delta SPX put with the Heston hedge ratio is systematically underhedging by 70% of the true vega exposure.

## Remember

Rough volatility is the most significant development in derivatives modelling since Heston — it explains three empirical stylised facts simultaneously: (1) the steep short-term vol skew, (2) the power-law autocorrelation decay of realised volatility, and (3) the VIX term structure shape. The cost is **non-Markovian dynamics**: because $H < \frac{1}{2}$, the variance process has memory and the $(S_t, V_t)$ state is no longer Markov-sufficient for option pricing. This motivates RL approaches — a Neural SDE with a fractional noise driver can learn rough-vol dynamics from data, and a TDBP agent trained on rough Bergomi paths learns to price options consistently with the observed skew term structure without needing to solve the non-Markovian PDE.
