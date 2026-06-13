# Strangle

**Topic:** Derivatives
**Tags:** strangle, options strategy, volatility trading, long volatility, OTM options
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A strangle is a long position in an OTM call at strike $K_c > S$ and an OTM put at strike $K_p < S$, both with the same expiry $T$; it is cheaper than a straddle but requires a larger move to profit.

## Key Formula

$$\text{Payoff} = \max(S_T - K_c,\,0) + \max(K_p - S_T,\,0)$$

$$\text{Net cost} = C(K_c) + P(K_p) < C(K) + P(K) \quad \text{(straddle at same } K\text{)}$$

Break-even: $S_T > K_c + \text{premium}$ or $S_T < K_p - \text{premium}$.

## Example

$S = 100$, $K_p = 95$, $K_c = 105$, $T = 1$ month. Put $= 2$, call $= 2$. Total cost $= 4$.
Break-even: $S_T > 109$ or $S_T < 91$. The straddle at $K = 100$ might cost $\$8$ — the strangle is half the price but needs twice the move.

## Remember

Dealers routinely sell short strangles around earnings announcements, collecting premium if the stock stays within the break-even range. The strategy is "short volatility" — it loses if realised volatility exceeds implied. The short strangle was at the heart of Nick Leeson's positions at Barings (1995), where an earthquake triggered losses that exceeded the maximum profit many times over.
