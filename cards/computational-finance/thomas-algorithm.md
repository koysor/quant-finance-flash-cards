# Thomas Algorithm

**Topic:** Computational Finance
**Tags:** tridiagonal solver, crank-nicolson, linear systems, pde pricing, computational complexity, numerical methods
**Created:** 2026-07-31
**Author:** Claude Opus 5

---

## Definition

The Thomas algorithm is a specialised form of Gaussian elimination that solves a tridiagonal linear system $A\mathbf{x} = \mathbf{d}$ in $O(N)$ operations instead of the $O(N^3)$ of general elimination. It is the standard solver inside implicit and Crank-Nicolson finite-difference option pricers, where each time step produces exactly such a system.

## Key Formula

For the system with sub-diagonal $a_i$, diagonal $b_i$ and super-diagonal $c_i$:

$$a_i x_{i-1} + b_i x_i + c_i x_{i+1} = d_i, \qquad i = 1, \dots, N$$

**Forward sweep** (eliminate the sub-diagonal):

$$c'_1 = \frac{c_1}{b_1}, \qquad c'_i = \frac{c_i}{b_i - a_i c'_{i-1}}$$

$$d'_1 = \frac{d_1}{b_1}, \qquad d'_i = \frac{d_i - a_i d'_{i-1}}{b_i - a_i c'_{i-1}}$$

**Back substitution:**

$$x_N = d'_N, \qquad x_i = d'_i - c'_i x_{i+1}$$

The algorithm is numerically stable without pivoting whenever the matrix is diagonally dominant, $\lvert b_i\rvert > \lvert a_i\rvert + \lvert c_i\rvert$, which the Black-Scholes discretisation satisfies for sensible grid ratios.

## Example

Crank-Nicolson pricing of an American put on a grid of $N = 200$ asset steps and 500 time steps.

- **General elimination:** $\approx N^3/3 = 2.7$ million operations per step, $1.3 \times 10^9$ in total.
- **Thomas:** $\approx 8N = 1{,}600$ operations per step, $8 \times 10^5$ in total.

A speed-up of roughly 1,600×, turning a solve that would take minutes into one that takes milliseconds — and the matrix only needs its coefficients rebuilt if the grid or volatility changes.

## Remember

This is why PDE pricing is viable in production at all. A local volatility validation study reprices hundreds of vanillas on refining grids to demonstrate convergence in space and time, and each refinement doubles $N$ — with an $O(N^3)$ solver the cost would grow eightfold per refinement, but with Thomas it merely doubles, so a full convergence table is cheap. The one caveat is that the linear structure breaks when early exercise is enforced: American options need the free-boundary constraint applied after each solve (projected SOR or a policy-iteration wrapper), because the payoff constraint is not a tridiagonal relation.
