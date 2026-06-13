# Butterfly Spread

**Topic:** Derivatives
**Tags:** butterfly spread, options strategy, short volatility, convexity, limited risk, neutral strategy
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A long butterfly spread buys one call at $K_1$, sells two calls at $K_2 = \tfrac{K_1+K_3}{2}$, and buys one call at $K_3$; it profits if the underlying remains near $K_2$ at expiry.

## Key Formula

$$\text{Net cost} = C(K_1) - 2C(K_2) + C(K_3) > 0 \quad \text{(by convexity of call prices)}$$

$$\text{Max profit} = (K_2 - K_1) - \text{net cost} \quad \text{at } S_T = K_2$$

$$\text{Max loss} = \text{net cost} \quad \text{(if } S_T \le K_1 \text{ or } S_T \ge K_3\text{)}$$

The spread also has a put version and can be constructed via puts or a combination of verticals.

## Example

$K_1 = 95$, $K_2 = 100$, $K_3 = 105$; calls priced at 8, 5, 2. Net cost $= 8 - 10 + 2 = 0$ (this would be rare; typically small positive). Max profit $= 5 - 0 = 5$ if $S_T = 100$. If bought at net cost $= 1$, max profit $= 4$, max loss $= 1$.

## Remember

A butterfly is a bet that the stock stays near $K_2$ and that implied volatility is overpriced. Because the net cost is small, it offers high reward-to-risk if the pin is correct. Option market-makers use butterflies to assess the risk-neutral density at $K_2$: by Breeden–Litzenberger, the butterfly price is proportional to the risk-neutral probability of $S_T \approx K_2$.
