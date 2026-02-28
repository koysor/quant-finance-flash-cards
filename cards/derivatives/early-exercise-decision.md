# Early Exercise Decision

**Topic:** Derivatives
**Tags:** early exercise, American options, optimal stopping, intrinsic value, time value, dividends
**Created:** 2026-02-28 20:46:20
**Author:** Unknown

---

## Definition

The **early exercise decision** is the problem of determining whether the holder of an American option should exercise now or continue to hold. Exercise is optimal only when the intrinsic value received today (plus interest earned on the proceeds) exceeds the option's continuation value — the expected discounted payoff from holding further. This is an **optimal stopping problem**: at every point in time, the holder compares exercising immediately against waiting.

## Key Formula

Exercise early when the intrinsic value exceeds the continuation value:

$$\text{Exercise if: intrinsic value} > \text{continuation value}$$

$$\max(K - S_t, \, 0) \;>\; e^{-r \, \delta t} \, \mathbb{E}^{\mathbb{Q}}\!\left[V(S_{t+\delta t}, \, t+\delta t)\right]$$

Two key results for non-dividend-paying stocks:

$$\text{American call: never exercise early} \quad (C_A = C_E)$$

$$\text{American put: exercise when } S_t \leq S^*(t)$$

where $S^*(t)$ is the critical stock price boundary. For a call on a dividend-paying stock, exercise may be optimal just before the ex-dividend date if:

$$D > K\bigl(1 - e^{-r\tau}\bigr)$$

where $D$ is the dividend and $\tau$ is the time remaining after the ex-dividend date.

## Example

An American put has $K = 100$ and $r = 5\%$. The stock drops to $S = 70$.

Intrinsic value if exercised now: $100 - 70 = £30$. Investing £30 at 5% for the remaining 6 months earns $30 \times (e^{0.025} - 1) \approx £0.76$ in interest.

The continuation value (from a binomial tree) is £28.50. Since £30 > £28.50, **exercise now** — the interest earned on £30 in hand outweighs the chance of a larger payoff later.

If instead $S = 90$: intrinsic value = £10, but continuation value = £11.20. **Do not exercise** — the option's time value still exceeds the interest benefit.

## Remember

In practice, the early exercise decision matters most in two situations: **deep in-the-money puts**, where locking in cash to earn interest dominates the remaining optionality, and **calls just before an ex-dividend date**, where capturing the dividend outweighs the time value sacrificed. Traders monitor the exercise boundary $S^*(t)$ daily — crossing it triggers immediate exercise. Getting this wrong means leaving money on the table, which is why American option models (binomial trees, finite differences) must evaluate the exercise condition at every node.
