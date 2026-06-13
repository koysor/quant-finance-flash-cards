# Bear Put Spread

**Topic:** Derivatives
**Tags:** bear put spread, vertical spread, options strategy, limited risk, put options, mildly bearish
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A bear put spread buys a put at higher strike $K_1$ and sells a put at lower strike $K_2$ ($K_2 < K_1$) with the same expiry $T$; it profits from a moderate fall in the underlying while capping both profit and loss.

## Key Formula

$$\text{Net cost} = P(K_1) - P(K_2) > 0$$

$$\text{Payoff at }T = \begin{cases} 0 & S_T \ge K_1 \\ K_1 - S_T & K_2 < S_T < K_1 \\ K_1 - K_2 & S_T \le K_2 \end{cases}$$

$$\text{Max profit} = (K_1 - K_2) - \text{net cost}, \qquad \text{Max loss} = \text{net cost}$$

By put–call parity, the bear put spread is equivalent to a bull call spread at the same strikes (same payoff net of interest and dividends).

## Example

$K_1 = 100$, $K_2 = 90$, $P(100) = 7$, $P(90) = 3$. Net cost $= 4$. Max profit $= 10 - 4 = 6$ if $S_T \le 90$. Max loss $= 4$ if $S_T \ge 100$. Break-even: $S_T = 96$.

## Remember

The bear put spread is the natural complement to the bull call spread — both are vertical spreads with bounded risk. The bear put is preferred when skew is steep (OTM puts are expensive relative to OTM calls), because selling the lower-strike put reduces the high cost of the long put hedge. It is the fundamental building block of put-spread collars used by corporate treasuries.
