# Longstaff-Schwartz (Least-Squares Monte Carlo)

**Topic:** Computational Finance
**Tags:** american options, monte carlo, regression, optimal stopping, least squares, continuation value
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **Longstaff-Schwartz algorithm** (also called **Least-Squares Monte Carlo, LSM**) prices American options by estimating the continuation value at each exercise date via **ordinary least-squares regression** across Monte Carlo paths. At each time step, paths where the immediate payoff exceeds the estimated continuation value are flagged as early-exercise points; the option value is then computed by averaging the appropriately discounted payoffs.

## Key Formula

At time step $t_k$ (working backward from maturity $T$), the continuation value for paths that are in the money is estimated by regressing the discounted future cash flows $Y_i$ on a vector of basis functions $\mathbf{L}(S_{t_k})$:

$$\hat{C}(S_{t_k}) = \sum_{j=1}^{M} a_j\,L_j(S_{t_k})$$

where coefficients $\mathbf{a}$ minimise $\sum_i \bigl(Y_i - \hat{C}(S_{t_k,i})\bigr)^2$.

The exercise rule at $t_k$: exercise if $g(S_{t_k}) \ge \hat{C}(S_{t_k})$, i.e. immediate payoff $\ge$ estimated continuation value.

## Example

American put, $K = 1.10$, $r = 6\%$, $T = 3$ years, using 3 paths (from the original Longstaff-Schwartz paper):

| Path | $t=1$ | $t=2$ | $t=3$ |
|------|-------|-------|-------|
| 1 | 1.09 | 1.08 | 1.34 |
| 2 | 1.16 | 1.26 | 1.54 |
| 3 | 1.22 | 1.07 | 1.03 |

At $t = 2$, only paths 1 and 3 are in the money (payoffs £0.02 and £0.03). Regressing discounted $t=3$ payoffs on $[1, S, S^2]$ gives estimated continuation values. Path 3 has continuation £0.016 < payoff £0.03, so it exercises early. Working back to $t=1$ refines the boundary further. The average discounted payoff across paths gives the American put price.

## Remember

Longstaff-Schwartz is the industry-standard algorithm for American exotic option pricing on equity desks because it handles high-dimensional state spaces (multiple underlyings, stochastic vol) by adding more regressors without changing the algorithmic structure. Its main weakness — sensitivity to the choice of basis functions — is precisely what motivates RL alternatives such as OST-TDBP, which replaces the hand-chosen polynomial basis with a neural network that learns the optimal continuation value representation directly from the data.
