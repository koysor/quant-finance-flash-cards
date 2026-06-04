# Finite Difference Method

**Topic:** Computational Finance
**Tags:** finite difference, crank-nicolson, pde, american option, black-scholes pde
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **finite difference method (FDM)** solves PDEs by replacing continuous derivatives with discrete approximations on a grid of asset prices and time steps. Applied to the Black-Scholes PDE, FDM produces a grid of option values $V_{i,j} \approx V(S_i, t_j)$ at each $(S, t)$ node, working backwards from the known terminal payoff to the present. It is the standard numerical method for pricing American options, barrier options, and other derivatives where no closed-form solution exists.

## Key Formula

The **Black-Scholes PDE** for option value $V(S,t)$:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

The **Crank-Nicolson scheme** (second-order accurate in both $S$ and $t$) averages explicit and implicit updates:

$$\frac{V_{i,j+1} - V_{i,j}}{\Delta t} = \frac{1}{2}\left[\mathcal{L}V_{i,j+1} + \mathcal{L}V_{i,j}\right]$$

where $\mathcal{L}$ is the finite-difference discretisation of the spatial operator. At each time step this produces a tridiagonal linear system $A\mathbf{v}_{j} = \mathbf{b}_{j+1}$, solved in $O(N)$ by the Thomas algorithm. **American option** early exercise is enforced at each backward step: $V_{i,j} \leftarrow \max(V_{i,j},\, \text{intrinsic value}_i)$.

## Example

Price an American put with $S_0 = \$100$, $K = \$100$, $r = 5\%$, $\sigma = 20\%$, $T = 1$ year. Grid: $N_S = 200$ asset steps, $N_t = 500$ time steps.

1. Set terminal condition: $V_{i,N_t} = \max(K - S_i, 0)$
2. At each time step backwards, solve the tridiagonal system for $\mathbf{v}_j$
3. Apply early exercise: $V_{i,j} \leftarrow \max(V_{i,j}, K - S_i)$

Result: $V(100, 0) \approx \$6.09$ — versus the European put price of \$5.57 (Black-Scholes). The \$0.52 difference is the early exercise premium that FDM captures and Black-Scholes cannot.

## Remember

The finite difference method is the workhorse of American option pricing on trading desks — Black-Scholes gives no closed form for American options, and Monte Carlo cannot easily enforce early exercise optimally. FDM solves the Black-Scholes PDE backwards on a grid, which naturally accommodates the American constraint (check whether early exercise dominates continuation at each node) and any boundary condition. In practice, Crank-Nicolson is preferred over explicit schemes because it is unconditionally stable — the explicit scheme requires $\Delta t \leq (\Delta S)^2/(\sigma^2 S^2)$ (the CFL condition) which forces prohibitively small time steps. FDM also naturally produces the full $(S, t)$ option value surface in one pass, giving delta and gamma as by-products from the grid differences.
