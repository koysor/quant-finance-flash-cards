# Bull Call Spread

**Topic:** Derivatives
**Tags:** bull call spread, vertical spread, options strategy, limited risk, call options, mildly bullish
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A bull call spread buys a call at strike $K_1$ and sells a call at higher strike $K_2$ ($K_2 > K_1$) with the same expiry $T$; it profits from a moderate rise in the underlying while capping both profit and loss.

## Key Formula

$$\text{Net cost} = C(K_1) - C(K_2) > 0$$

$$\text{Payoff at }T = \begin{cases} 0 & S_T \le K_1 \\ S_T - K_1 & K_1 < S_T < K_2 \\ K_2 - K_1 & S_T \ge K_2 \end{cases}$$

$$\text{Max profit} = (K_2 - K_1) - \text{net cost}, \qquad \text{Max loss} = \text{net cost}$$

## Example

$K_1 = 100$, $K_2 = 110$, $C(100) = 8$, $C(110) = 3$. Net cost $= 5$. Max profit $= 10 - 5 = 5$ if $S_T \ge 110$. Max loss $= 5$ if $S_T \le 100$. Break-even: $S_T = 105$.

## Remember

A bull call spread reduces cost versus a naked long call by selling upside above $K_2$. This simultaneously caps vega exposure — making it more suitable when implied volatility is high (and calls expensive). The short call at $K_2$ acts like a built-in profit target: the strategy is designed for "mildly bullish, not strongly bullish" views.
