# Time Subscript and Index Notation

**Topic:** Mathematical Notation
**Tags:** notation, subscript, time index, continuous time, discrete time, stochastic process
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

In finance, subscripts encode **time** and **asset** indices, which must be read carefully to avoid confusing a fixed parameter with a time-varying quantity:

| Convention | Example | Meaning |
|---|---|---|
| Continuous-time subscript | $S_t$, $W_t$, $r_t$ | Value of the process at time $t \in [0, T]$ |
| Discrete-time subscript | $S_n$, $r_n$, $X_n$ | Value at step $n \in \{0, 1, 2, \ldots, N\}$ |
| Terminal value | $S_T$, $V_T$ | Value at maturity $T$ |
| Initial value | $S_0$, $V_0$ | Value at time 0 (today) |
| Asset index | $S_i$, $\sigma_i$, $\mu_i$ | Quantity for the $i$-th asset |
| Double index | $\sigma_{ij}$, $\rho_{ij}$ | Quantity relating asset $i$ and asset $j$ |
| State and time | $V(S, t)$ or $V_t(S)$ | Option value as function of spot and time |

## Key Formula

**Geometric Brownian motion** (continuous-time):

$$S_t = S_0 \exp\!\left(\left(\mu - \tfrac{1}{2}\sigma^2\right)t + \sigma W_t\right)$$

**Discrete-time return:**

$$r_n = \frac{S_n - S_{n-1}}{S_{n-1}}, \qquad n = 1, 2, \ldots, N$$

**Covariance matrix entry:**

$$\Sigma_{ij} = \operatorname{Cov}(R_i, R_j) = \rho_{ij}\sigma_i\sigma_j$$

## Example

Reading $V(S_t, t)$ carefully: $S_t$ is the **current spot price** (random, changes with time), $t$ is **calendar time** (deterministic parameter). In code, this maps to a function `V(S, t)` taking two arguments. When $t = T$, $V(S_T, T) = (S_T - K)^+$ is the payoff — the function value is determined entirely by where spot ends up, not by any further discounting.

By contrast, $V_0 = V(S_0, 0)$ is today's option price — a number, not a random variable, because $S_0$ is known.

## Remember

The subscript $t$ in $S_t$, $W_t$, $\mathcal{F}_t$, and $V_t$ consistently signals a **time-indexed stochastic process**. This is the dominant convention in continuous-time finance (Black-Scholes, Heston, etc.) and must be distinguished from the notation used in discrete time (econometrics, GARCH), where the subscript is typically $t$ for calendar time or $n$ for step number. The value $S_0$ is always a **known constant**, while $S_t$ for $t > 0$ is **random** — any pricing calculation that mistakes $S_t$ for a constant will produce wrong hedges and wrong sensitivities.
