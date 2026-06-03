# Double Barrier Option

**Topic:** Derivatives
**Tags:** double barrier, knock-out, knock-in, path-dependent, state augmentation, exotic option
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

A **double barrier option** is knocked out (or in) when the underlying price touches either of two barriers — an upper barrier $B_U$ and a lower barrier $B_L$ — at any point during the option's life. The product pays its vanilla payoff only if the price stays within the corridor $[B_L, B_U]$ throughout (double knock-out) or exits it at some point (double knock-in). They are cheaper than single-barrier options and are common in FX structured products where both upside and downside risk need to be bounded.

## Key Formula

Under GBM with continuous monitoring, the double knock-out call price is expressed via an infinite series of image terms using the **reflection principle**:

$$C_\text{DKO} = \sum_{n=-\infty}^{\infty}\left[C_\text{BS}(S_0 \lambda^{2n}, K) - \left(\frac{B_L}{S_0}\right)^{2\mu}\!C_\text{BS}\!\left(\frac{B_L^2}{S_0}\lambda^{2n}, K\right)\right]$$

where $\lambda = B_U/B_L$, $\mu = r/\sigma^2 - \tfrac{1}{2}$. In practice, 5–10 terms suffice.

For RL pricing with **discrete monitoring**, the Markov-sufficient state is:

$$s_t = \left(S_t,\; \mathbf{1}[\text{hit } B_U],\; \mathbf{1}[\text{hit } B_L],\; \tau\right)$$

— two binary hit-indicators, one per barrier.

## Example

A double knock-out call on EUR/USD: $S_0 = 1.10$, $K = 1.10$ (ATM), $B_L = 1.05$, $B_U = 1.18$, $T = 3$ months, $\sigma = 8\%$, $r = 3\%$. The vanilla ATM call costs 1.2 USD cents. The double knock-out costs 0.65 cents — 46% cheaper because both the profitable (above 1.18) and loss-truncating (below 1.05) scenarios are removed. A corporate hedger buying this saves 0.55 cents of premium while accepting that the hedge disappears if EUR/USD moves sharply in either direction.

## Remember

The double barrier is the natural extension to stress-test **multi-constraint RL state design**: where a single barrier adds one binary bit to the state, a double barrier adds two independent bits — one for each boundary. The state space grows by a factor of 4 (alive, upper hit, lower hit, both hit — though "both hit" is impossible for a standard product, so effectively 3 states). An RL pricer that omits either hit-indicator will systematically misprice the product near the boundaries. In the context of daily price limits (DPL), the double barrier is mathematically equivalent — the DPL corridor $[L_n, U_n]$ acts as a daily double-barrier reset, making the DPL pricing problem a repeated double-barrier problem with state reset at each session open.
