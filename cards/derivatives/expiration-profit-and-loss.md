# Expiration Profit and Loss

**Topic:** Derivatives
**Tags:** options, profit and loss, expiration, break-even, premium, strategy
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Expiration profit and loss** is the net gain or loss on an option position measured at expiry, equal to the payoff received minus the premium paid (for a long position) or the premium received minus the payoff owed (for a short position). Unlike the payoff alone, expiration P&L accounts for the initial cost of entering the trade and is the figure that determines whether the position was profitable.

## Key Formula

**Long call** expiration P&L:

$$P\&L = \max(S_T - K, \; 0) - C_0$$

**Short call** expiration P&L:

$$P\&L = C_0 - \max(S_T - K, \; 0)$$

**Long put** expiration P&L:

$$P\&L = \max(K - S_T, \; 0) - P_0$$

**Short put** expiration P&L:

$$P\&L = P_0 - \max(K - S_T, \; 0)$$

**Break-even** (where $P\&L = 0$):

- Call: $S_T^* = K + C_0$
- Put: $S_T^* = K - P_0$

## Example

A trader sells (writes) a put with $K = £50$ for a premium of $P_0 = £3$.

| $S_T$ | Payoff owed | P&L |
|---|---|---|
| £55 | £0 | +£3 (keep full premium) |
| £50 | £0 | +£3 |
| £47 | £3 | £0 (break-even) |
| £40 | £10 | $-$£7 |

The short put is profitable when $S_T > K - P_0 = £47$. Below that, losses grow pound-for-pound with the falling stock price, reaching a theoretical maximum loss of $K - P_0 = £47$ if the stock falls to zero.

## Remember

Expiration P&L is the starting point for evaluating any options strategy. Multi-leg structures — bull spreads, iron condors, butterflies — are analysed by summing the expiration P&L of each individual leg across all possible values of $S_T$. The break-even price is particularly important: it tells a trader exactly how far the underlying must move to justify the premium paid. In practice, most options are closed before expiry, so the actual P&L includes the mark-to-market change in the option's price (influenced by Greeks, time decay, and volatility shifts), but expiration P&L provides the baseline scenario against which all earlier exit decisions are measured.
