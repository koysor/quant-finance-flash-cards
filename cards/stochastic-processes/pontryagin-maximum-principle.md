# Pontryagin Maximum Principle

**Topic:** Stochastic Processes
**Tags:** pontryagin, maximum principle, optimal control, adjoint variable, costate, hamiltonian
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **Pontryagin Maximum Principle** (PMP, 1956) provides necessary conditions for optimal control by introducing **adjoint (costate) variables** $p_t$ that travel backward in time alongside the forward state trajectory. Where the HJB equation characterises the value function globally as a PDE, the PMP characterises the optimal trajectory locally through a Hamiltonian system — the two are dual formulations of the same problem.

## Key Formula

For a deterministic control problem $\min_u \int_0^T \ell(x_t, u_t)\,dt + \Phi(x_T)$ subject to $\dot{x}_t = f(x_t, u_t)$, define the **Pontryagin Hamiltonian**:

$$\mathcal{H}(x, u, p) = \ell(x, u) + p \cdot f(x, u)$$

The PMP states that along an optimal trajectory $(x^*, u^*)$:

$$\dot{x}^*_t = \frac{\partial \mathcal{H}}{\partial p}\bigg|_{u^*}, \qquad \dot{p}_t = -\frac{\partial \mathcal{H}}{\partial x}\bigg|_{u^*}, \qquad u^*_t = \arg\min_u \mathcal{H}(x^*_t, u, p_t)$$

with **transversality condition** $p_T = \nabla_x \Phi(x_T^*)$. The adjoint variable $p_t$ equals $\partial V/\partial x$ — it is the **sensitivity of the value function** to the state, i.e. the Greek of the control problem.

## Example

Optimal liquidation of a large equity position over $T = 1$ day to minimise market impact. State: remaining inventory $x_t$. Control: trading rate $u_t \le 0$ (selling). Cost: $\ell = \eta u_t^2$ (quadratic impact). The Hamiltonian $\mathcal{H} = \eta u^2 + p \cdot u$ gives optimal rate $u^*_t = -p_t / (2\eta)$. The adjoint equation $\dot{p}_t = 0$ means $p_t$ is constant, so the optimal strategy is **uniform liquidation** — selling at a constant rate throughout the day, recovering the Almgren-Chriss result analytically.

## Remember

The Pontryagin adjoint $p_t = \partial V/\partial x$ is mathematically identical to the **delta** of the value function — it measures how the optimal value changes if the current state is perturbed. In deep hedging, the neural network's gradient $\partial \hat{V}/\partial S$ (computed via autograd) is the finite-sample approximation to the Pontryagin adjoint of the hedging problem. This is why neural network Greeks are not just a computational convenience — they are the adjoint variables of the underlying stochastic control problem, and their correctness is a necessary condition for the hedging strategy to be near-optimal.
