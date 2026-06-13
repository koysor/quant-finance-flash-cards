# Straddle

**Topic:** Derivatives
**Tags:** straddle, options strategy, volatility trading, long volatility, gamma, vega
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A straddle is an options strategy consisting of a long call and a long put with the same strike $K$ and expiry $T$ on the same underlying; it profits from a large move in either direction.

## Key Formula

$$\text{Payoff} = \lvert S_T - K \rvert = \max(S_T - K,\,0) + \max(K - S_T,\,0)$$

$$\text{Net cost} = C(K,T) + P(K,T)$$

Break-even at expiry: $S_T > K + \text{premium}$ or $S_T < K - \text{premium}$.

ATM straddle price approximation (at-the-money, small $T$):

$$C + P \approx S \cdot \sigma \sqrt{\frac{2T}{\pi}} \approx 0.8 \cdot S \cdot \sigma \sqrt{T}$$

## Example

$S = 100$, $K = 100$, $\sigma = 20\%$, $T = 1$ year. Call $= 10$, put $= 10$ (approximately, put–call parity). Total premium $= 20$. Break-even: $S_T < 80$ or $S_T > 120$. If the stock moves ±25, the straddle gains approximately \$5 net.

## Remember

The ATM straddle is the most direct way to trade implied volatility: its price is proportional to $\sigma\sqrt{T}$. Buying a straddle and delta-hedging daily converts implied vol into realised vol P&L — the strategy profits if realised $\sigma$ exceeds implied $\sigma$ paid at entry.
