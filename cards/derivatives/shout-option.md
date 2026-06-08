# Shout Option

**Topic:** Derivatives
**Tags:** shout option, path-dependent, exotic option, lock-in, european call, structured products
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

A **shout option** is a path-dependent exotic option that allows the holder to "shout" once at any time $\tau$ during the option's life, locking in the current intrinsic value as a guaranteed floor on the payoff, whilst retaining the right to benefit from further upside if the asset continues to rise.

## Key Formula

If the holder shouts at time $\tau$ when the asset price is $S_\tau$, the payoff at expiry $T$ is:

$$\Pi = \max(S_T - K,\; S_\tau - K,\; 0)$$

This decomposes into two components:

$$\Pi = \underbrace{\max(S_\tau - K,\; 0)}_{\text{locked-in intrinsic value}} + \underbrace{\max(S_T - S_\tau,\; 0)}_{\text{at-the-money call from } \tau \text{ to } T}$$

The second term is an at-the-money European call on the return from $\tau$ to $T$, priced at the shout time using Black–Scholes.

## Example

A shout call has strike $K = 100$ and expiry in 6 months. The holder shouts at month 3 when $S_\tau = 120$, locking in an intrinsic value of $\max(120 - 100, 0) = 20$.

- If $S_T = 130$: payoff $= \max(130 - 100, 120 - 100, 0) = 30$
- If $S_T = 95$: payoff $= \max(95 - 100, 120 - 100, 0) = 20$ (floor protects)
- If $S_T = 110$: payoff $= \max(110 - 100, 120 - 100, 0) = 20$

Without the shout, the European call would pay only $\max(95 - 100, 0) = 0$ in the second scenario.

## Remember

The optimal shout strategy — analogous to the optimal exercise rule for American options — is solved by dynamic programming: the holder shouts when the current intrinsic value exceeds the value of waiting (the at-the-money call from that moment to expiry). Shout options appear in **structured retail savings products** where clients are guaranteed to crystallise a market gain at their chosen moment, making them more expensive than vanilla calls but cheaper than perfect lookback options.
