# Barrier Option

**Topic:** Derivatives
**Tags:** barrier option, knock-out, knock-in, path-dependent, exotic option, rebate
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

A **barrier option** is a path-dependent derivative whose existence or activation depends on whether the underlying price crosses a predetermined barrier $B$ during the option's life. A **knock-out** option expires worthless if the barrier is hit; a **knock-in** option only becomes active if the barrier is hit. They are cheaper than vanilla options because the payout can be eliminated (or withheld), and are widely used in structured products and FX hedging.

## Key Formula

For an **up-and-out call** (barrier $B > S_0 > K$, knocked out if $S_t \ge B$), the closed-form price under GBM uses the reflection principle:

$$C_\text{UOC} = C_\text{BS}(S_0, K, \sigma, r, T) - \left(\frac{B}{S_0}\right)^{2\lambda} C_\text{BS}\!\left(\frac{B^2}{S_0}, K, \sigma, r, T\right)$$

where $\lambda = (r + \tfrac{1}{2}\sigma^2)/\sigma^2$. The **in-out parity** holds for any barrier type:

$$C_\text{knock-in} + C_\text{knock-out} = C_\text{vanilla}$$

For RL pricing with **discrete monitoring** at dates $\{t_1, \ldots, t_N\}$, the Markov-sufficient state is:

$$s_t = (S_t,\; \mathbf{1}[\text{barrier hit}],\; \tau)$$

## Example

An up-and-out call with $S_0 = 100$, $K = 100$, $B = 115$, $\sigma = 20\%$, $r = 5\%$, $T = 3$ months. The vanilla call costs £3.84. The up-and-out call costs £1.62 — cheaper because all paths that would have generated large payoffs by rising above £115 are knocked out. A structured product issuer sells this to the client at £2.50, pocketing the £0.88 spread.

## Remember

Barrier options demonstrate the central advantage of RL pricing over analytical formulas: the closed-form solution only exists for continuous monitoring under GBM, while practically all barrier options are **discretely monitored** (daily or weekly). Discrete monitoring adds path dependence that breaks the closed-form, requiring Monte Carlo or PDE methods. A TDBP agent trained on discretely monitored paths handles this naturally — the binary barrier-hit indicator in the state vector tells the network at each step whether the option is still alive, and the pricing surface it learns automatically reflects the discrete monitoring premium.
