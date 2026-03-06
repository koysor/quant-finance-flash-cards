# Zomma (Greeks)

**Topic:** Derivatives
**Tags:** zomma, Greeks, sensitivity, options, gamma, volatility
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

**Zomma** (also called **DgammaDvol**) is the third-order Greek that measures the rate of change of Gamma with respect to a change in implied volatility. Formally, $\text{Zomma} = \partial \Gamma / \partial \sigma = \partial^3 V / \partial S^2 \, \partial \sigma$. It captures how the curvature of the option price changes when volatility moves.

## Key Formula

For European options under Black-Scholes:

$$\text{Zomma} = \Gamma \cdot \frac{d_1 d_2 - 1}{\sigma}$$

where $\Gamma = N'(d_1) / (S\sigma\sqrt{T})$.

Key properties:

- When $d_1 d_2 > 1$ (deep ITM or OTM), Zomma is **positive** — rising volatility increases Gamma.
- When $d_1 d_2 < 1$ (near ATM), Zomma is **negative** — rising volatility decreases Gamma by spreading the curvature over a wider price range.
- Zomma is zero when $d_1 d_2 = 1$.

## Example

A European call has $S = 100$, $K = 100$, $\sigma = 20\%$, $T = 0.25$, $\Gamma = 0.0393$, $d_1 = 0.175$, $d_2 = 0.075$.

$$d_1 d_2 = 0.175 \times 0.075 = 0.01313$$

$$\text{Zomma} = 0.0393 \times \frac{0.01313 - 1}{0.20} = 0.0393 \times \frac{-0.9869}{0.20} = \mathbf{-0.1939}$$

If implied volatility rises from 20% to 21%, Gamma changes by approximately $-0.1939 \times 0.01 = -0.00194$, falling from 0.0393 to about 0.0374. The ATM option becomes less convex as volatility increases.

## Remember

Zomma matters when volatility and the underlying move simultaneously — which happens routinely during market stress. A Gamma-hedged portfolio may appear safe under stable volatility, but a volatility spike can shift Gamma via Zomma, leaving the hedger unexpectedly over- or under-hedged. For ATM options (negative Zomma), a volatility spike reduces Gamma, which is actually stabilising — the position becomes less sensitive to further spot moves. For deep OTM options (positive Zomma), a volatility spike increases Gamma, amplifying risk precisely when markets are most turbulent. Exotic desks hedging barrier options and digital options, where Gamma is already extreme, monitor Zomma closely.
