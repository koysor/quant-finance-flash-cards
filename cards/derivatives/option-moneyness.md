# Option Moneyness

**Topic:** Derivatives
**Tags:** options, moneyness, in-the-money, at-the-money, out-of-the-money, strike price
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Moneyness** describes the relationship between an option's strike price $K$ and the current price of the underlying asset $S$. It determines how much intrinsic value an option has and strongly influences its delta, time value, and likelihood of expiring in the money.

## Key Formula

For a **call option**:

| State | Condition | Intrinsic value |
|---|---|---|
| In the money (ITM) | $S > K$ | $S - K > 0$ |
| At the money (ATM) | $S = K$ | $0$ |
| Out of the money (OTM) | $S < K$ | $0$ |

For a **put option**:

| State | Condition | Intrinsic value |
|---|---|---|
| In the money (ITM) | $S < K$ | $K - S > 0$ |
| At the money (ATM) | $S = K$ | $0$ |
| Out of the money (OTM) | $S > K$ | $0$ |

A common quantitative measure of moneyness is the **log-moneyness**:

$$m = \ln\!\left(\frac{S}{K}\right)$$

where $m > 0$ means the call is ITM (put is OTM), $m = 0$ is ATM, and $m < 0$ means the call is OTM (put is ITM).

## Example

A stock trades at £105. Consider a call with $K = £100$ and a put with $K = £100$.

- **Call**: $S > K$, so the call is **in the money** with intrinsic value = £5
- **Put**: $S > K$, so the put is **out of the money** with intrinsic value = £0
- **Log-moneyness**: $\ln(105/100) = 0.049$ — slightly positive, confirming the call is ITM

## Remember

Moneyness is the single most important driver of an option's risk profile. Deep ITM options behave like the underlying (delta near $\pm 1$, mostly intrinsic value), while deep OTM options are cheap, highly leveraged bets with delta near zero. ATM options have the highest time value, the largest gamma, and the greatest sensitivity to volatility — this is why ATM implied volatility is the benchmark quote in options markets.
