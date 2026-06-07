# Free Exercise Boundary

**Topic:** Derivatives
**Tags:** free exercise boundary, american option, optimal stopping, smooth pasting, critical stock price, early exercise
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **free exercise boundary** $S^*(t)$ is the critical stock price at time $t$ below which it is optimal to exercise an American put immediately. It divides the $(t, S)$ plane into two regions: the **exercise region** $\{S \leq S^*(t)\}$, where the option value equals its intrinsic value, and the **continuation region** $\{S > S^*(t)\}$, where the Black-Scholes PDE governs the option value. The boundary is "free" because its location is not fixed in advance — it must be solved for simultaneously with the option value.

## Key Formula

Two **boundary conditions** pin down $S^*(t)$ and the option value $V(S, t)$ at the boundary:

$$\underbrace{V(S^*(t),\, t) = K - S^*(t)}_{\text{value matching}}$$

$$\underbrace{\frac{\partial V}{\partial S}\bigg|_{S = S^*(t)} = -1}_{\text{smooth pasting}}$$

**Value matching** says the option value equals its intrinsic payoff exactly at the boundary. **Smooth pasting** says the derivative is continuous across the boundary — if it were not, an arbitrage in an infinitesimal move would exist.

The boundary satisfies a limiting condition at expiry:

$$S^*(T^-) = \min\!\left(K,\; \frac{rK}{q}\right)$$

where $r$ is the risk-free rate and $q$ is the continuous dividend yield; for a non-dividend-paying stock, $S^*(T^-) = K$.

## Example

American put: $K = 100$, $r = 5\%$, $\sigma = 25\%$, $T = 1$ year, no dividends. Using a finite-difference grid, the exercise boundary at selected times:

| Time to expiry $\tau$ | $S^*(\tau)$ |
|---|---|
| 1 year | £74 |
| 6 months | £80 |
| 1 month | £92 |
| At expiry | £100 |

The boundary rises toward $K = 100$ as expiry approaches. Deep in-the-money puts (say $S = 60$, well below $S^*(t)$) are exercised immediately to collect the £40 intrinsic value and invest it at 5%, since the optionality that remains is worth less than the interest forgone.

## Remember

The free exercise boundary is the central object that makes American option pricing harder than European pricing: instead of a single PDE on a fixed domain, you must solve a PDE on a domain whose boundary is itself unknown. In practice, finite-difference methods discretise the smooth-pasting condition numerically, and the Longstaff–Schwartz Monte Carlo algorithm approximates the boundary implicitly by comparing payoffs against regression estimates of the continuation value. Traders use the exercise boundary to build **exercise triggers**: when a risk system reports $S_t < S^*(t)$, an automated alert flags the position for immediate exercise. Mispricing the boundary by even a few points leads to systematic early-exercise errors that compound across a large book of American puts.
