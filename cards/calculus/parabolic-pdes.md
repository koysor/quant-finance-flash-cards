# Parabolic Partial Differential Equations

**Topic:** Calculus
**Tags:** PDE, parabolic, heat equation, diffusion, Black-Scholes, classification
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

A **second-order linear PDE** in two variables has the general form

$$A\,u_{xx} + B\,u_{xy} + C\,u_{yy} + D\,u_x + E\,u_y + F\,u = G$$

where $A$, $B$, $C$ may depend on $x$ and $y$. The PDE is classified by the **discriminant** $\Delta = B^2 - 4AC$, evaluated at each point:

- **Elliptic:** $B^2 - 4AC < 0$ (e.g. Laplace's equation)
- **Parabolic:** $B^2 - 4AC = 0$ (e.g. the heat equation)
- **Hyperbolic:** $B^2 - 4AC > 0$ (e.g. the wave equation)

A **parabolic PDE** sits on the boundary between elliptic and hyperbolic. Its defining properties are:

1. **Smoothing** — sharp or discontinuous initial conditions become smooth instantly for $t > 0$.
2. **Infinite speed of propagation** — information from the initial condition influences the solution everywhere immediately, though the effect decays rapidly with distance.
3. **Uniqueness** — solutions are uniquely determined by an initial condition (IC) and appropriate boundary conditions (BC).
4. **Irreversibility** — the smoothing effect means information is lost; the equation describes irreversible diffusion processes and is ill-posed when run backwards in time.

The prototype is the **heat equation**:

$$\frac{\partial u}{\partial t} = \kappa \frac{\partial^2 u}{\partial x^2}$$

Here $A = \kappa$, $B = 0$, $C = 0$, so $B^2 - 4AC = 0$ — confirming the parabolic classification.

## Key Formula

**General classification criterion** for $A\,u_{xx} + B\,u_{xy} + C\,u_{yy} + \ldots = 0$:

$$B^2 - 4AC = 0 \quad \Longleftrightarrow \quad \text{parabolic}$$

**Heat equation** (prototype parabolic PDE):

$$\frac{\partial u}{\partial t} = \kappa \frac{\partial^2 u}{\partial x^2}$$

**Black-Scholes PDE** (parabolic, with $A = \tfrac{1}{2}\sigma^2 S^2$, $B = 0$, $C = 0$):

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

**Kolmogorov forward equation** (Fokker-Planck, also parabolic):

$$\frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}\bigl[\mu(x)\,p\bigr] + \frac{1}{2}\frac{\partial^2}{\partial x^2}\bigl[\sigma^2(x)\,p\bigr]$$

## Example

Consider the heat equation on a rod with an initial step function:

$$u(x, 0) = \begin{cases} 1 & \text{if } x \ge 0 \\ 0 & \text{if } x < 0 \end{cases}$$

The solution for $t > 0$ is

$$u(x, t) = \frac{1}{2}\left[1 + \operatorname{erf}\!\left(\frac{x}{2\sqrt{\kappa t}}\right)\right]$$

where $\operatorname{erf}$ is the error function. The sharp jump at $x = 0$ is **immediately smoothed** into a continuous curve for any $t > 0$, no matter how small. This is the hallmark of parabolic behaviour: discontinuities in initial data are erased instantly.

Verify the classification: writing $u_t = \kappa\,u_{xx}$ as $\kappa\,u_{xx} - u_t = 0$, identify $A = \kappa$, $B = 0$, $C = 0$ (there is no $u_{tt}$ term). Then $B^2 - 4AC = 0$, confirming the equation is parabolic.

## Remember

The Black-Scholes PDE and both Kolmogorov equations (forward and backward) are **parabolic**. This is not a coincidence — they all describe the time evolution of quantities governed by diffusion processes.

The practical consequence is the **smoothing property**. A European call payoff $\max(S - K, 0)$ has a sharp kink at $S = K$, yet the option price $V(S, t)$ is a perfectly smooth function for any $t < T$. The parabolic PDE smooths the terminal payoff the instant you step back from expiry, just as the heat equation smooths a step function. This is why option price curves are smooth even though payoff diagrams have corners.

Smoothing also explains why the Greeks exist and are well-behaved: because $V$ is smooth, all its partial derivatives (Delta, Gamma, Theta) are continuous functions. If the pricing PDE were hyperbolic instead of parabolic, the payoff kink would propagate through time and the Greeks would be undefined at the strike.
