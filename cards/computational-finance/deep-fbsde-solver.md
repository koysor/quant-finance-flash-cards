# Deep FBSDE Solver

**Topic:** Computational Finance
**Tags:** fbsde, deep learning, pde, option pricing, high-dimensional
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **Deep FBSDE solver** (Han, Jentzen & E, 2018) uses deep neural networks to solve **forward-backward stochastic differential equations (FBSDEs)** — and by extension, high-dimensional parabolic PDEs — that are intractable by classical finite difference or tree methods. It reformulates the PDE as a stochastic control problem, parameterising the unknown gradient of the solution with a neural network trained by minimising a terminal condition loss.

## Key Formula

A parabolic PDE $\frac{\partial u}{\partial t} + \mathcal{L}u + f = 0$ with terminal condition $u(T,x) = g(x)$ is equivalent (by the Feynman-Kac formula) to the FBSDE system:

$$dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t \quad \text{(forward SDE)}$$

$$dY_t = -f(X_t, Y_t, Z_t)\,dt + Z_t^\top dW_t \quad \text{(backward SDE)}$$

where $Y_t = u(t, X_t)$ is the PDE solution and $Z_t = \sigma^\top \nabla_x u$ is its gradient. The deep FBSDE method parameterises $Z_t \approx \mathcal{N}_\theta(t, X_t)$ with a neural network and minimises:

$$\mathcal{L}(\theta) = \mathbb{E}\!\left[\lvert Y_T - g(X_T) \rvert^2\right]$$

via stochastic gradient descent over simulated forward paths.

## Example

Pricing a **100-dimensional basket option** with correlated underlyings — a problem where the curse of dimensionality makes grids infeasible ($10^{100}$ grid points for a 100-dimensional grid). The forward SDE simulates 100-dimensional GBM paths; the neural network $\mathcal{N}_\theta$ outputs a 100-dimensional gradient (the delta vector) at each time step; training minimises the discrepancy between the network's terminal payoff prediction and the actual payoff $g(X_T) = \max(\bar{X}_T - K, 0)$. Convergence is achieved in minutes on a GPU versus years for a grid-based solver.

## Remember

The deep FBSDE solver is one of the landmark results showing that deep learning can overcome the curse of dimensionality in quantitative finance. Classical PDE methods (finite differences, trinomial trees) scale exponentially with the number of risk factors — making them useless for portfolios of correlated assets or XVA calculations that depend on dozens of market factors simultaneously. Deep FBSDE solvers scale polynomially: the network width grows modestly with dimension. The same framework solves CVA, FVA, and optimal hedging problems in high dimensions, and is actively used in research at major banks for pricing exotic derivatives with many underlyings.
