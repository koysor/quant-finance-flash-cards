# Option Dimensionality

**Topic:** Derivatives
**Tags:** dimensionality, multi-asset, basket option, spread option, correlation, monte carlo
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **dimensionality** of an option pricing problem is the number of independent stochastic processes driving the payoff. A single-asset European call is one-dimensional ($d=1$), a spread option on two assets is two-dimensional ($d=2$), and a basket option on $n$ assets is $n$-dimensional. Dimensionality is the primary factor determining whether PDE finite-difference methods (efficient for $d \leq 2$) or Monte Carlo simulation (preferred for $d \geq 3$) is used.

## Key Formula

The multi-asset Black–Scholes PDE for $d$ correlated underlyings:

$$\frac{\partial V}{\partial t} + r\sum_{i=1}^{d} S_i \frac{\partial V}{\partial S_i} + \frac{1}{2}\sum_{i=1}^{d}\sum_{j=1}^{d} \rho_{ij}\sigma_i\sigma_j S_i S_j \frac{\partial^2 V}{\partial S_i \partial S_j} - rV = 0$$

A PDE grid with $M$ nodes per dimension requires $M^d$ total nodes and $O(M^{2d})$ operations per time step, so computational cost grows **exponentially** with dimension $d$.

## Example

A bank prices a basket call on three equity indices with $M = 50$ grid points per dimension. PDE grid: $50^3 = 125{,}000$ nodes — feasible. For a basket on 10 indices: $50^{10} \approx 10^{17}$ nodes — completely infeasible. Monte Carlo with $M = 200{,}000$ paths on 10 assets draws 10 correlated Gaussians per step per path and runs in under a minute, independent of $d$. For $d = 1$ or $2$, the PDE grid is faster and gives Greeks at every node; for $d \geq 3$, Monte Carlo wins on both speed and scalability.

## Remember

Correlation is the hidden extra dimension in multi-asset options. A spread option on oil price and refinery margin appears to be 2D, but if the correlation $\rho_{12}$ is itself stochastic, the problem is effectively 3D — and correlation risk (sensitivity of the option price to $\rho$) is often the dominant and hardest-to-hedge exposure. On structured products desks, building a book of basket options means carrying substantial **correlation vega** that cannot be offset by vanilla options on individual assets, because single-asset implied vols carry no information about the joint distribution. Managing this exposure typically requires cross-gamma positions in pairs of underlying options.
