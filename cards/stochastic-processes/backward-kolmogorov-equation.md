# Backward Kolmogorov Equation

**Topic:** Stochastic Processes
**Tags:** Kolmogorov, PDE, backward equation, trinomial model, Black-Scholes, boundary condition, diffusion

---

## Definition

The **backward Kolmogorov equation** is a partial differential equation that describes the expected value of a function of a stochastic process by conditioning on the **initial state**. Unlike the forward (Fokker-Planck) equation, which evolves a probability density forward in time, the backward equation works in reverse — starting from a known terminal condition and solving backwards to find the value at an earlier time. It is derived from the trinomial model (or any discrete stepping scheme) by conditioning on the state at the first time step and taking the continuous-time limit.

## Key Formula

For a process driven purely by diffusion with coefficient $c$, the backward Kolmogorov equation is:

$$\frac{\partial p}{\partial t} + c^2 \frac{\partial^2 p}{\partial y^2} = 0$$

Note the **positive sign** on the second-order term — this is opposite to the forward equation, reflecting the reversal of the time direction.

The boundary condition is imposed at the **final time** $T$:

$$p(y, T) = f(y)$$

where $f(y)$ is the payoff or terminal condition (e.g. an option payoff at expiry).

When you add a drift term $rS \frac{\partial V}{\partial S}$ and a discounting term $-rV$, the backward Kolmogorov equation becomes the **Black-Scholes PDE**:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

## Example

Consider a simple symmetric random walk on a lattice with spacing $\Delta y$ and time step $\Delta t$. At each step the process moves up, stays, or moves down with equal probability $\tfrac{1}{3}$. The expected value of a terminal payoff $f(y)$ satisfies:

$$p(y, t) = \tfrac{1}{3}\bigl[p(y + \Delta y,\, t + \Delta t) + p(y,\, t + \Delta t) + p(y - \Delta y,\, t + \Delta t)\bigr]$$

Expanding in Taylor series and taking the limit $\Delta t \to 0$ with $(\Delta y)^2 / \Delta t \to c^2$ yields the backward Kolmogorov equation $\frac{\partial p}{\partial t} + c^2 \frac{\partial^2 p}{\partial y^2} = 0$. For a European call with payoff $f(y) = \max(y - K, 0)$ at expiry, solving this PDE backwards from $T$ to $0$ gives the fair price today.

## Remember

The backward Kolmogorov equation is the **skeleton** of the Black-Scholes PDE. In its simplest form it captures only diffusion and a terminal boundary condition. When you add risk-neutral drift ($rS \partial V / \partial S$) and discounting ($-rV$), you recover the full Black-Scholes equation. This is why understanding the backward equation is essential: it reveals that option pricing is fundamentally about solving a backward-in-time diffusion problem, where the boundary condition is the payoff at expiry.
