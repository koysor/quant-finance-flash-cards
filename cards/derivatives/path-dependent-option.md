# Path-Dependent Option

**Topic:** Derivatives
**Tags:** path dependent, asian option, barrier option, lookback, exotic options, monte carlo
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

A **path-dependent option** is a derivative whose payoff depends on the entire history of the underlying asset price $\{S_t : 0 \leq t \leq T\}$, not just the terminal value $S_T$. This contrasts with **path-independent** (vanilla) options such as European calls, whose payoff $\max(S_T - K, 0)$ depends only on where the price ends up, not on how it got there.

## Key Formula

Path-independent payoff (European call):

$$\Pi_{\text{PI}} = \max(S_T - K,\; 0)$$

Path-dependent payoffs (examples):

$$\Pi_{\text{Asian}} = \max\!\left(\bar{S} - K,\; 0\right), \quad \bar{S} = \frac{1}{n}\sum_{i=1}^{n} S_{t_i}$$

$$\Pi_{\text{Barrier}} = \max(S_T - K,\; 0) \cdot \mathbf{1}\!\left\{\max_{0 \leq t \leq T} S_t < B\right\}$$

where $B$ is the barrier level and $\mathbf{1}\{\cdot\}$ is the indicator function.

## Example

A discretely-monitored Asian call on an equity index with $K = 4{,}000$, $n = 12$ monthly fixings, and realised fixings averaging $\bar{S} = 4{,}150$ pays:

$$\Pi = \max(4{,}150 - 4{,}000,\; 0) = 150 \text{ index points}$$

A European call with the same $K$ and terminal price $S_T = 3{,}900$ pays $\max(3{,}900 - 4{,}000, 0) = 0$, even though the index spent most of the year above the strike. The Asian investor profits; the European call expires worthless.

## Remember

Path-dependent options generally cannot be priced by the Black–Scholes closed-form formula and instead require **Monte Carlo simulation**: simulate thousands of full price paths, compute the payoff on each path, then discount the average. This makes path-dependent options significantly more expensive to price and hedge than vanilla options — delta changes continuously as the path accumulates, requiring frequent rebalancing. In practice, Asian options are widely used in commodity and FX markets precisely because path-averaging reduces the cost of this hedge.
