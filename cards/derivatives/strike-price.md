# Strike Price

**Topic:** Derivatives
**Tags:** options, strike, exercise price, moneyness, contracts
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **strike price** (or **exercise price**), denoted $K$, is the fixed price specified in an option contract at which the holder may buy (for a call) or sell (for a put) the underlying asset upon exercise. It is set when the contract is written and remains constant throughout the option's life.

## Key Formula

The strike price determines the option's payoff at expiration. For a **call option** with underlying price $S_T$ at maturity:

$$\text{Call payoff} = \max(S_T - K,\; 0)$$

For a **put option**:

$$\text{Put payoff} = \max(K - S_T,\; 0)$$

Moneyness is defined relative to $K$:

- **In the money (ITM):** $S > K$ for calls, $S < K$ for puts
- **At the money (ATM):** $S = K$
- **Out of the money (OTM):** $S < K$ for calls, $S > K$ for puts

In the Black-Scholes formula, $K$ appears in the discounted exercise cost:

$$C = S_0\,N(d_1) - K\,e^{-rT}\,N(d_2)$$

## Example

A European call option on a stock has $K = £50$ and expires in three months. At expiration:

- If $S_T = £62$: payoff $= \max(62 - 50,\; 0) = £12$. The option is ITM.
- If $S_T = £50$: payoff $= \max(50 - 50,\; 0) = £0$. The option is ATM.
- If $S_T = £43$: payoff $= \max(43 - 50,\; 0) = £0$. The option is OTM.

A lower strike makes a call more valuable (more likely to finish ITM) and a put less valuable — the opposite holds for a higher strike.

## Remember

The strike price is the anchor of every option's payoff structure. In the Black-Scholes formula, $K$ appears only in the discounted term $K\,e^{-rT}$, which represents the present value of what you would pay on exercise. The entire options market is organised around $K$: volatility surfaces plot implied volatility against strike, option chains list contracts by strike, and the distance between $S$ and $K$ determines whether a position is a conservative hedge or a leveraged bet. Understanding how $K$ interacts with $S$, $T$, and $\sigma$ is essential for pricing, hedging, and constructing strategies.
