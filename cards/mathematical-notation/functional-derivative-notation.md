# Functional Derivative Notation

**Topic:** Mathematical Notation
**Tags:** functional derivative, Fréchet derivative, calculus of variations, optimal control, HJB
**Created:** 2026-03-09
**Author:** Claude Sonnet 4.6

---

## Definition

A **functional** $F[f]$ maps an entire function $f$ to a real number. The **functional derivative** $\frac{\delta F}{\delta f(x)}$ measures how $F$ changes when $f$ is perturbed by a tiny spike at $x$ — it is the infinite-dimensional analogue of a partial derivative. In finance, functionals appear in optimal portfolio problems and the Hamilton-Jacobi-Bellman (HJB) equation.

| Symbol | Read as | Meaning |
|---|---|---|
| $F[f]$ | "F of f" | A functional: takes a function $f$ as input, returns a number |
| $\frac{\delta F}{\delta f(x)}$ | "functional derivative of F with respect to f at x" | Rate of change of $F$ when $f$ is perturbed at point $x$ |
| $\delta f$ | "delta f" | An infinitesimal perturbation of the function $f$ |
| $V(x, t)$ | "value function" | In HJB: the optimal expected reward from state $x$ at time $t$ |
| $\frac{\partial V}{\partial t} + \sup_u \mathcal{H}$ | "HJB equation" | PDE whose solution gives the optimal control policy |

## Key Formula

The **definition** of the functional derivative via perturbation:

$$F[f + \varepsilon \delta_y] - F[f] \approx \varepsilon \int \frac{\delta F}{\delta f(x)} \, \delta_y(x) \, dx = \varepsilon \frac{\delta F}{\delta f(y)}$$

where $\delta_y$ is a Dirac delta spike at $y$.

The **Hamilton-Jacobi-Bellman equation** for optimal control:

$$\frac{\partial V}{\partial t}(x,t) + \sup_{u \in \mathcal{U}} \left[\mu(x,u)\frac{\partial V}{\partial x} + \tfrac{1}{2}\sigma^2(x,u)\frac{\partial^2 V}{\partial x^2}\right] = 0$$

## Example

An investor maximises expected utility $F[\pi] = E\!\left[\int_0^T u(\pi_t) \, dt\right]$ over all portfolio weight functions $\pi(\cdot)$. Taking the functional derivative $\frac{\delta F}{\delta \pi(t)} = 0$ gives the first-order condition $E[u'(\pi_t) \cdot r_t] = 0$ — the Euler-Lagrange equation that characterises the optimal portfolio. For log utility $u(w) = \ln w$, this recovers the Kelly criterion.

## Remember

The HJB equation is the stochastic-calculus generalisation of the Euler-Lagrange equations of classical mechanics. In a continuous-time portfolio problem, the **value function** $V(w, t)$ — the maximum expected utility achievable from wealth $w$ at time $t$ — satisfies the HJB equation. Solving it (analytically or numerically) yields the optimal trading strategy as a function of current wealth and time. The functional derivative $\frac{\delta F}{\delta \pi}$ is the formal tool; in practice, quants solve the HJB PDE directly using finite-difference methods.
