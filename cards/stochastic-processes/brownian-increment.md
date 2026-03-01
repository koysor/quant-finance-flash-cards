# Brownian Increment

**Topic:** Stochastic Processes
**Tags:** Brownian motion, increment, stochastic calculus, dW, Wiener process
**Author:** Claude Opus 4.6

---

## Definition

The **Brownian increment** $dW$ (or $dX$) is the infinitesimal change in Brownian motion over a time step $dt$. It is the fundamental building block of stochastic calculus — every SDE is driven by this random increment.

The increment is normally distributed with mean zero and variance $dt$:

$$dW \sim \mathcal{N}(0, \, dt)$$

Its standard deviation is $\sqrt{dt}$, which is **much larger** than $dt$ for small time steps. This asymmetry between the size of the random increment ($\sqrt{dt}$) and the deterministic time step ($dt$) is the root cause of the Itô correction.

## Key Formula

**Distribution:**

$$dW \sim \mathcal{N}(0, \, dt), \qquad E[dW] = 0, \qquad E[dW^2] = dt$$

**Order of magnitude:**

$$dW \sim O(\sqrt{dt}) \gg O(dt)$$

**Simulation form** (useful for Monte Carlo):

$$dW = \phi \sqrt{dt}, \qquad \phi \sim \mathcal{N}(0, 1)$$

**Multiplication rules** (used in Itô calculus):

$$dW^2 = dt, \qquad dt \cdot dW = 0, \qquad (dt)^2 = 0$$

## Example

If $dt = 0.0001$ (roughly one hour of trading in a year):

- The deterministic step: $dt = 0.0001$
- The random step: $\sqrt{dt} = 0.01$ — **one hundred times larger**

This means the random fluctuations completely dominate at short time scales. For a stock with $\sigma = 0.20$ and $S = 100$:

- Drift contribution: $\mu S \, dt = 0.10 \times 100 \times 0.0001 = £0.001$
- Diffusion contribution (typical): $\sigma S \sqrt{dt} = 0.20 \times 100 \times 0.01 = \textbf{£0.20}$

The random move is 200 times the drift.

## Remember

- The $\sqrt{dt}$ scaling of $dW$ means **noise dominates signal at short time scales** — this is why high-frequency returns look almost purely random, while drift only becomes visible over longer horizons.
- Because $dW \sim O(\sqrt{dt})$, the term $dW^2$ is $O(dt)$ — too large to ignore in a Taylor expansion. This is precisely why ordinary calculus fails and the Itô correction term appears.
- In Monte Carlo simulation, each time step uses $dW = \phi\sqrt{dt}$ with a fresh standard normal draw $\phi$ — this single random number drives the entire path dynamics.
