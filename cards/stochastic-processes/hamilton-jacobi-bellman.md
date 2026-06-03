# Hamilton-Jacobi-Bellman Equation

**Topic:** Stochastic Processes
**Tags:** hjb equation, stochastic control, bellman equation, continuous time, optimal control, dynamic programming
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **Hamilton-Jacobi-Bellman (HJB) equation** is the continuous-time version of the Bellman optimality equation, characterising the value function of an optimal stochastic control problem as a second-order PDE. It is the theoretical foundation underlying option pricing, dynamic portfolio optimisation, and the continuous-time limit of RL algorithms such as TDBP.

## Key Formula

For a controlled diffusion $dX_t = f(X_t, a_t)\,dt + \sigma(X_t, a_t)\,dW_t$ with running reward $\ell$ and terminal payoff $g$, the value function $V(t, x) = \sup_a \mathbb{E}[\int_t^T \ell\,ds + g(X_T)]$ satisfies:

$$-\frac{\partial V}{\partial t} = \sup_{a \in \mathcal{A}}\left\{\ell(x, a) + f(x, a)\,\frac{\partial V}{\partial x} + \frac{1}{2}\sigma^2(x, a)\,\frac{\partial^2 V}{\partial x^2}\right\}$$

with terminal condition $V(T, x) = g(x)$. For **option pricing** (no control, $f = rS$, $\sigma = \sigma S$, $\ell = 0$), this collapses to the **Black-Scholes PDE**:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0$$

## Example

A portfolio manager dynamically allocates between a risky asset and cash to maximise expected log-wealth over $T = 1$ year. The HJB equation for log-utility gives the famous **Merton optimal fraction** $\pi^* = (\mu - r)/(\gamma \sigma^2)$, where $\gamma$ is risk aversion. For $\mu = 10\%$, $r = 5\%$, $\sigma = 20\%$, $\gamma = 2$: $\pi^* = 62.5\%$ in the risky asset at every point in time — a constant policy that is optimal regardless of current wealth level.

## Remember

The HJB equation is the continuous-time backbone of both classical derivatives pricing and RL: the Black-Scholes PDE is the HJB equation with no control, while TDBP's discrete Bellman recursion $P_t = e^{-r\Delta t}\mathbb{E}[P_{t+1} | \mathcal{F}_t]$ is a time-discretised numerical solver for the HJB. The neural network at each time step approximates the HJB solution at that time slice, and the Bellman residual loss is the finite-difference discretisation error of the PDE. Feynman-Kac provides the bridge: the solution to the HJB PDE equals the conditional expectation of the discounted reward under the controlled process, which is exactly what RL simulation estimates.
