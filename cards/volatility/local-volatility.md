# Local Volatility

**Topic:** Volatility
**Level:** A Level Mathematics
**Tags:** local volatility, dupire, volatility surface, smile-consistent, exotic pricing
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Local volatility is a model in which the instantaneous volatility of the underlying asset is a deterministic function of the current asset price and time: $\sigma = \sigma(S, t)$. Introduced by Dupire (1994) and Derman-Kani (1994), the local volatility surface is uniquely determined by the market prices of European options across all strikes and expiries. It is the simplest model that is perfectly consistent with the observed volatility smile, making it the standard benchmark for pricing exotic derivatives.

## Key Formula

The **Dupire equation** extracts local volatility from European call prices $C(K, T)$:

$$\sigma_{\text{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + r K \frac{\partial C}{\partial K} + \frac{1}{2} q K^2 \frac{\partial^2 C}{\partial K^2} - q C}{\frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2}}$$

where $r$ is the risk-free rate and $q$ is the dividend yield.

The **local volatility SDE**:

$$dS = (r - q) S \, dt + \sigma_{\text{loc}}(S, t) \, S \, dW$$

## Example

From the market, a call option with $K = £100$, $T = 0.5$ years has:

- $\frac{\partial C}{\partial T} = 3.2$, $\frac{\partial C}{\partial K} = -0.45$, $\frac{\partial^2 C}{\partial K^2} = 0.018$
- $r = 5\%$, $q = 2\%$, $C = £6.50$

$$\sigma_{\text{loc}}^2 = \frac{3.2 + 0.05 \times 100 \times (-0.45) + 0.5 \times 0.02 \times 100^2 \times 0.018 - 0.02 \times 6.50}{0.5 \times 100^2 \times 0.018}$$

$$= \frac{3.2 - 2.25 + 1.80 - 0.13}{90} = \frac{2.62}{90} = 0.0291$$

$$\sigma_{\text{loc}} = \sqrt{0.0291} = 17.1\%$$

## Remember

Local volatility is the first model a quant developer learns beyond Black-Scholes and the one most frequently used for pricing barrier options, autocallables, and other path-dependent exotics. Its great strength is exact calibration to the vanilla surface — it reprices every European option by construction. Its weakness is that the dynamics of the smile are wrong: local vol predicts that the smile flattens as the spot moves (sticky-strike behaviour), when empirically the smile tends to follow the spot (sticky-delta). This is why stochastic volatility models (Heston, SABR) and stochastic-local volatility hybrids exist. Understanding local vol's limitations is as important as understanding the model itself — it tells you when the benchmark is reliable and when you need something more sophisticated.
