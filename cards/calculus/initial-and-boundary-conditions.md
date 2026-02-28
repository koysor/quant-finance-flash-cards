# Initial and Boundary Conditions

**Topic:** Calculus
**Tags:** calculus, PDE, boundary conditions, initial conditions, Black-Scholes, option pricing
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

A partial differential equation (PDE) typically admits infinitely many solutions. **Initial conditions** (ICs) and **boundary conditions** (BCs) are the additional constraints that select the unique, physically meaningful solution.

An **initial condition** specifies the state of the system at a particular moment in time. For the forward Kolmogorov (Fokker-Planck) equation, the IC is a Dirac delta function $p(y, t; y', t) = \delta(y' - y)$, concentrating all probability at the starting point.

A **boundary condition** constrains the solution along the edges of the spatial domain for all time. The three standard types are:

- **Dirichlet** — the value of the solution is specified on the boundary, e.g. $V(0, t) = 0$.
- **Neumann** — the derivative (flux) of the solution is specified on the boundary, e.g. $\frac{\partial V}{\partial S}\big|_{S \to \infty} = 1$.
- **Mixed (Robin)** — a linear combination of the value and its derivative is specified.

For backward-in-time equations such as the backward Kolmogorov equation and the Black-Scholes PDE, the "initial" condition is actually a **terminal condition** — it specifies the solution at the final time $T$, and the equation is solved backwards to earlier times.

## Key Formula

**Black-Scholes PDE** (the same equation for every European option):

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

**Terminal condition** (European call):

$$V(S, T) = \max(S - K, 0)$$

**Boundary conditions** (European call):

$$V(0, t) = 0 \qquad \text{(Dirichlet at } S = 0\text{)}$$

$$V(S, t) \sim S - K e^{-r(T-t)} \quad \text{as } S \to \infty \qquad \text{(asymptotic Dirichlet)}$$

**Forward Kolmogorov initial condition:**

$$p(y, t; y', t) = \delta(y' - y)$$

## Example

Consider pricing a European put under Black-Scholes. The PDE is identical to the call case. Only the conditions change:

**Terminal condition:**

$$V(S, T) = \max(K - S, 0)$$

**Boundary conditions:**

$$V(0, t) = K e^{-r(T-t)} \qquad \text{(at } S = 0 \text{, the put is worth the discounted strike)}$$

$$V(S, t) \to 0 \quad \text{as } S \to \infty \qquad \text{(deep out-of-the-money put is worthless)}$$

For a **down-and-out barrier call** with barrier $B < K$:

$$V(B, t) = 0 \qquad \text{(knock-out Dirichlet condition at the barrier)}$$

$$V(S, T) = \max(S - K, 0) \qquad \text{(same terminal payoff as a vanilla call)}$$

The barrier introduces an additional Dirichlet condition that "kills" the option value when the underlying hits $B$.

## Remember

In quantitative finance, the payoff function **is** the boundary condition. The Black-Scholes PDE is universal — it is the same second-order parabolic equation regardless of the option type. What distinguishes a call from a put, a barrier option from a digital, or an American from a European is entirely the set of initial/terminal and boundary conditions imposed on that PDE.

This means that once you can solve the Black-Scholes PDE for one set of boundary conditions, pricing a different derivative is "merely" a matter of changing the conditions:

- **European call:** $V(S, T) = \max(S - K, 0)$
- **European put:** $V(S, T) = \max(K - S, 0)$
- **Digital (binary) call:** $V(S, T) = \mathbf{1}_{S > K}$
- **Barrier option:** adds a Dirichlet condition $V(B, t) = 0$ at the barrier

Understanding initial and boundary conditions is therefore not an abstract mathematical exercise — it is the mechanism by which every exotic payoff is translated into a well-posed pricing problem.
