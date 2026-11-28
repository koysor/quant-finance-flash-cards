# Kolmogorov Equations

**Topic:** Stochastic Processes
**Tags:** kolmogorov, forward equation, backward equation, generator, transition density, pde
**Created:** 2026-11-28
**Author:** Claude Opus 5.5

---

## Definition

The **Kolmogorov equations** are a pair of PDEs satisfied by the transition density $p(x, t;\, y, T)$ of a Markov diffusion. The **backward** equation acts on the starting point $(x, t)$ and evolves expectations backwards from a terminal condition. The **forward** equation (Fokker-Planck) acts on the end point $(y, T)$ and evolves the density forwards from a known start. Both come from one operator, the **generator** $\mathcal{L}$, and its adjoint $\mathcal{L}^*$.

## Key Formula

For the SDE $dX = a(X)\,dt + b(X)\,dW$, the generator is

$$\mathcal{L}f = a(x)\,\frac{\partial f}{\partial x} + \tfrac{1}{2}b(x)^2\,\frac{\partial^2 f}{\partial x^2}$$

**Backward**, in $(x, t)$, with terminal condition $p \to \delta(x - y)$ as $t \to T$:

$$\frac{\partial p}{\partial t} + \mathcal{L}_x\,p = 0$$

**Forward**, in $(y, T)$, with initial condition $p \to \delta(y - x)$ as $T \to t$:

$$\frac{\partial p}{\partial T} = \mathcal{L}^*_y\,p = -\frac{\partial}{\partial y}\bigl[a(y)\,p\bigr] + \frac{1}{2}\frac{\partial^2}{\partial y^2}\bigl[b(y)^2\,p\bigr]$$

The two are linked through the expected payoff $u(x, t) = \mathbb{E}[f(X_T) \mid X_t = x]$:

$$u(x, t) = \int f(y)\,p(x, t;\, y, T)\,dy$$

so $u$ satisfies the backward equation with $u(x, T) = f(x)$.

## Example

Take $dX = 0.05\,dt + 0.2\,dW$ with $X_0 = 0$, and compute $\mathbb{E}[X_1^2]$ both ways.

**Forward:** the density at $T = 1$ is normal with mean $0.05$ and variance $0.2^2 = 0.04$, so
$\mathbb{E}[X_1^2] = 0.04 + 0.05^2 = 0.0425$.

**Backward:** with $\tau = T - t$, try $u(x, t) = (x + 0.05\tau)^2 + 0.04\tau$. Then
$\partial_t u = -0.1(x + 0.05\tau) - 0.04$, $\;0.05\,\partial_x u = 0.1(x + 0.05\tau)$, $\;\tfrac{1}{2}(0.04)\,\partial_{xx}u = 0.04$.
These sum to zero, and $u(x, 1) = x^2$, so $u(0, 0) = 0.0025 + 0.04 = 0.0425$.

Both routes give the same answer.

## Remember

The two equations answer opposite pricing questions. The **backward** equation prices **one payoff from every starting spot**: add discounting and it becomes the Black-Scholes PDE, solved on a grid from expiry back to today. The **forward** equation prices **every payoff from one starting spot**: one forward solve gives the whole terminal distribution, so a desk can value many strikes and maturities at once and calibrate local volatility (Dupire). Choose backward to price one exotic, and forward to fit a vol surface.
