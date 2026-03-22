# Protective Put Strategy

**Topic:** Derivatives
**Tags:** options, protective put, hedging, portfolio insurance, risk management
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A **protective put** (or "married put") is a hedging strategy in which an investor holds a long position in an asset and buys a put option on the same asset. The put acts as insurance: it sets a floor on the portfolio's value at the strike price $K$, while preserving unlimited upside. The cost of this protection is the put premium $P_0$.

## Key Formula

The combined position at expiry:

$$V_T = S_T + \max(K - S_T, \; 0) - P_0$$

This simplifies to:

$$V_T = \begin{cases} K - P_0 & \text{if } S_T \le K \\[4pt] S_T - P_0 & \text{if } S_T > K \end{cases}$$

The **maximum loss** is capped at:

$$\text{Max loss} = S_0 - K + P_0$$

The **break-even** price is:

$$S_T^* = S_0 + P_0$$

## Example

An investor holds shares bought at $S_0 = £100$ and buys a put with $K = £95$ for $P_0 = £3$.

| $S_T$ | Stock P&L | Put payoff | Net profit |
|---|---|---|---|
| £80 | $-$£20 | £15 | $-$£8 |
| £95 | $-$£5 | £0 | $-$£8 |
| £100 | £0 | £0 | $-$£3 |
| £103 | £3 | £0 | £0 (break-even) |
| £115 | £15 | £0 | £12 |

The worst outcome is $-$£8 (= £100 − £95 + £3), no matter how far the stock falls.

## Remember

The protective put is economically equivalent to a long call (by put–call parity: $S + P = C + K e^{-rT}$), which is why its payoff diagram looks like a shifted call. In quantitative finance, protective puts are the simplest form of portfolio insurance — institutional investors use them around earnings, macro events, or to lock in gains. The trade-off is explicit: the put premium is the cost of eliminating tail risk. Choosing the strike involves balancing the level of protection against the premium cost — lower strikes are cheaper but leave a larger unprotected gap.
