# Path Dependence

**Topic:** Derivatives
**Tags:** path dependence, path-independent, weak path dependence, strong path dependence, exotic options, pricing method
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Path dependence** is the property of a derivative payoff that requires knowledge of the underlying price trajectory $\{S_t : 0 \leq t \leq T\}$, not just the terminal value $S_T$. The degree of path dependence determines the appropriate pricing method: path-independent payoffs admit closed-form solutions, weakly path-dependent payoffs can be priced by an augmented PDE, and strongly path-dependent payoffs require Monte Carlo simulation.

## Key Formula

The three-level classification by payoff structure and pricing method:

| Class | Payoff form | Pricing method |
|-------|-------------|----------------|
| Path-independent | $\Pi = f(S_T)$ | Black–Scholes closed form |
| Weakly path-dependent | $\Pi = f(S_T,\, I_T)$, $I_t$ evolves continuously | Augmented PDE on $(S, I, t)$ |
| Strongly path-dependent | $\Pi = f\!\left(\{S_{t_i}\}_{i=1}^{N}\right)$ | Monte Carlo over full paths |

where $I_T$ is a finite-dimensional summary statistic (e.g. running average $\bar{S}$, running maximum $M_T$).

## Example

Three contracts on the same underlying, $S_0 = 100$, $K = 100$, $T = 6$ months:

1. **European call** — payoff $\max(S_T - 100, 0)$: path-independent; Black–Scholes formula runs in microseconds.
2. **Asian call** (3 monthly fixings) — payoff $\max(\bar{S} - 100, 0)$: weakly path-dependent; 2D finite-difference grid on $(S, \bar{S})$.
3. **Range accrual** — pays £1 for each day $S_t \in [90, 110]$: strongly path-dependent; Monte Carlo with 100,000 paths, each recording 252 daily prices.

The three contracts have very different computational costs despite sharing the same underlying, maturity, and approximate strike.

## Remember

Path dependence is the primary practical classification axis on an exotic options desk, because it determines which pricing engine handles the trade. Bank systems route each new exotic into one of three queues at inception: analytical (path-independent), PDE grid (weakly path-dependent), or Monte Carlo (strongly path-dependent). Misclassifying a strongly path-dependent product as weakly path-dependent and trying to price it on a 2D grid produces a systematically wrong price because the PDE cannot capture the full sequence of daily fixings the payoff depends on. Getting this classification right at trade capture — before any Greeks are computed or risk limits are checked — is one of the first things a quant must verify when onboarding a new structured product.
