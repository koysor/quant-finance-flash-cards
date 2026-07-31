# Breeden-Litzenberger Formula

**Topic:** Derivatives
**Tags:** risk-neutral density, butterfly spread, option prices, implied distribution, state prices, model-free
**Created:** 2026-07-31
**Author:** Claude Opus 5

---

## Definition

The Breeden-Litzenberger formula states that the second derivative of the European call price with respect to strike recovers the risk-neutral probability density of the underlying at expiry. It is a model-free result: no dynamics are assumed, only that a continuum of call prices $C(K, T)$ is observable and arbitrage-free.

## Key Formula

$$f_{S_T}(K) = e^{rT}\,\frac{\partial^2 C(K, T)}{\partial K^2}$$

The first derivative gives the discounted risk-neutral survival probability:

$$\frac{\partial C}{\partial K} = -e^{-rT}\,\mathbb{P}^{\mathbb{Q}}(S_T > K)$$

Discretely, the density is read off a **butterfly spread** — buy one call at $K - h$, sell two at $K$, buy one at $K + h$:

$$f_{S_T}(K) \approx e^{rT}\,\frac{C(K-h) - 2C(K) + C(K+h)}{h^2}$$

Because a butterfly has a non-negative payoff, its price must be non-negative, so $\partial_{KK} C \ge 0$ — the no-butterfly-arbitrage condition is exactly the statement that the implied density is non-negative.

## Example

SPX calls expiring in one year, $r = 4\%$, quoted at £5 strike spacing:

| $K$ | $C(K)$ |
|---|---|
| 4995 | 210.00 |
| 5000 | 206.20 |
| 5005 | 202.55 |

Second difference: $210.00 - 2(206.20) + 202.55 = 0.15$.

$$f_{S_T}(5000) \approx e^{0.04}\times\frac{0.15}{5^2} = 1.0408 \times 0.0060 = 0.00625$$

So the risk-neutral probability that $S_T$ lands within £5 of 5000 is roughly $0.00625 \times 5 \approx 3.1\%$.

## Remember

This is the mechanism by which an options desk reads the market's own forecast distribution rather than imposing one. Two immediate uses: it prices any European payoff by numerical integration $V_0 = e^{-rT}\int \Pi(K)\,f_{S_T}(K)\,dK$ without a model, and it supplies the denominator $\tfrac{1}{2}K^2 \partial_{KK}C$ of Dupire's local volatility formula — which is why a noisy or non-convex price surface makes local volatility blow up. In practice the second difference is a brutal amplifier of quote noise: a £0.05 bid-ask error on a £200 call swings the estimated density by tens of percent, so strikes must be smoothed or the surface fitted in total-variance space before differentiating twice.
