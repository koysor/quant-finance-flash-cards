# Dupire's Formula

**Topic:** Volatility
**Tags:** Dupire formula, local volatility, implied volatility, Breeden-Litzenberger, smile-consistent, arbitrage-free
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

Dupire's formula (1994) extracts the unique local volatility function $\sigma_{\text{loc}}(K, T)$ consistent with all observed European call prices $C(K, T)$, producing an arbitrage-free model that exactly fits the market volatility smile.

## Key Formula

$$\sigma_{\text{loc}}^2(K,T) = \frac{\dfrac{\partial C}{\partial T} + r K \dfrac{\partial C}{\partial K}}{\dfrac{1}{2}K^2 \dfrac{\partial^2 C}{\partial K^2}}$$

Denominator uses the Breeden–Litzenberger result: the risk-neutral density of $S_T$ is

$$q(K) = e^{rT}\frac{\partial^2 C}{\partial K^2}$$

In terms of implied volatility $\Sigma(K,T)$, the formula becomes more complex but remains closed-form.

## Example

If the implied vol surface has a steep put skew ($\partial \Sigma/\partial K < 0$), Dupire gives a local vol surface that slopes steeply in $K$, producing a heavier left tail in the risk-neutral distribution than a flat lognormal. The surface is calibrated by interpolating market quotes and differentiating numerically.

## Remember

Dupire's formula is theoretically exact but practically fragile: it requires a smooth, arbitrage-free call-price surface to compute second derivatives numerically. The resulting local vol surface tends to predict a flattening of the forward smile for longer maturities, making it systematically poor at pricing forward-start products (cliquets, autocallables) compared with stochastic volatility models such as Heston or SABR.
