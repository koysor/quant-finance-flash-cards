# Optional Stopping Theorem

**Topic:** Stochastic Processes
**Tags:** martingale, stopping time, barrier option, optimal exercise, expected value
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **optional stopping theorem** (Doob's optional stopping) states that the expected value of a martingale at a stopping time $\tau$ equals its initial value, provided certain regularity conditions are satisfied. In other words, you cannot gain an expected advantage by choosing a clever time to stop observing a martingale — the "fair game" property is preserved at random stopping times.

## Key Formula

If $M_t$ is a martingale and $\tau$ is a stopping time satisfying appropriate conditions (e.g. $\tau$ is bounded, or $M$ is uniformly integrable), then:

$$E[M_\tau] = E[M_0]$$

For a **bounded** stopping time $\tau \leq T$:

$$E[M_\tau] = M_0$$

**Key conditions** (any one suffices):
1. $\tau \leq T$ for some constant $T$ (bounded stopping time)
2. $E[\tau] < \infty$ and $|M_{t+1} - M_t|$ is bounded (bounded increments)
3. $M_t$ is uniformly integrable

## Example

A stock follows $S_t = 100 + W_t$ (arithmetic Brownian motion, which is a martingale). A trader buys and decides to sell the first time the price hits £110 or £90 — i.e. $\tau = \inf\{t : S_t = 110 \text{ or } S_t = 90\}$.

By the optional stopping theorem: $E[S_\tau] = S_0 = 100$.

Since $S_\tau \in \{110, 90\}$, let $p = P(S_\tau = 110)$:

$$110p + 90(1-p) = 100 \implies p = 0.5$$

The probability of hitting 110 before 90 is exactly 50% — the martingale property ensures the "fair game" even with a clever stopping rule. No amount of timing skill can create expected profit from a driftless process.

## Remember

The optional stopping theorem has direct applications in pricing barrier options and analysing optimal exercise strategies. For a **knock-out barrier option**, the payoff depends on whether the stock hits a barrier before expiry — the pricing requires computing expectations at the stopping time (first hitting time). For **American options**, the holder chooses when to exercise (a stopping time), and the option price is the supremum over all stopping times of the discounted expected payoff: $V_0 = \sup_\tau E^{\mathbb{Q}}[e^{-r\tau}\text{payoff}(S_\tau)]$. The theorem also explains why no trading strategy based on timing alone can beat a fair market — if discounted prices are martingales under $\mathbb{Q}$, then $E^{\mathbb{Q}}[e^{-r\tau}S_\tau] = S_0$ regardless of the stopping rule, ruling out timing-based arbitrage.
