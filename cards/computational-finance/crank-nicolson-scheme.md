# Crank-Nicolson Scheme

**Topic:** Computational Finance
**Tags:** crank-nicolson, theta scheme, von neumann stability, pde pricing, rannacher start-up, finite difference
**Created:** 2026-07-31
**Author:** Claude Opus 5

---

## Definition

The Crank-Nicolson scheme is the time-stepping method that averages the explicit and implicit finite-difference updates, giving second-order accuracy in both space and time while remaining unconditionally stable. It is the middle member of the one-parameter $\theta$-scheme family that also contains the explicit and fully implicit methods.

## Key Formula

The $\theta$-scheme for a PDE $\partial_t V = \mathcal{L}V$ discretised on a grid:

$$\frac{V^{n+1} - V^{n}}{\Delta t} = \theta\,\mathcal{L}V^{n} + (1-\theta)\,\mathcal{L}V^{n+1}$$

| $\theta$ | Scheme | Accuracy in time | Stability |
|---|---|---|---|
| $0$ | Fully implicit | $O(\Delta t)$ | Unconditional |
| $\tfrac{1}{2}$ | Crank-Nicolson | $O(\Delta t^2)$ | Unconditional |
| $1$ | Explicit | $O(\Delta t)$ | $\alpha \le \tfrac{1}{2}$ only |

Von Neumann analysis of the diffusion equation with $\alpha = D\,\Delta t/\Delta x^2$ gives the amplification factor per step for a Fourier mode of wavenumber $k$:

$$g(k) = \frac{1 - 4(1-\theta)\,\alpha\,\sin^2\!\left(\tfrac{k\Delta x}{2}\right)}{1 + 4\theta\,\alpha\,\sin^2\!\left(\tfrac{k\Delta x}{2}\right)}$$

Stability requires $\lvert g\rvert \le 1$ for every mode, which holds for all $\alpha$ when $\theta \ge \tfrac{1}{2}$.

## Example

Price a European put in log-spot coordinates with $\sigma = 20\%$, so the diffusion coefficient is $D = \sigma^2/2 = 0.02$. Take $\Delta x = 0.005$ and $\Delta t = 1/500 = 0.002$:

$$\alpha = \frac{0.02 \times 0.002}{0.005^2} = 1.6$$

The explicit scheme needs $\alpha \le 0.5$, so it would require $\Delta t \le 6.25\times 10^{-4}$ — over 1,600 time steps for a one-year option. Crank-Nicolson runs at 500 steps with no stability constraint.

But check its highest-frequency mode, $k\Delta x = \pi$, where $\sin^2 = 1$ and $\theta = \tfrac12$:

$$g = \frac{1 - 2(1.6)}{1 + 2(1.6)} = \frac{-2.2}{4.2} = -0.524$$

Negative $g$ means that mode flips sign every step. Starting from a payoff with a kink at the strike, this shows up as saw-tooth oscillation in gamma near $K$ for the first several steps.

## Remember

Crank-Nicolson is the default PDE pricer on a derivatives desk, but its one weakness bites exactly where option payoffs live. A vanilla payoff has a discontinuous first derivative at the strike, which excites those high-frequency modes, and because $g \to -1$ rather than $0$ as $\alpha$ grows, the oscillation is barely damped — the price may look fine while delta and gamma near the strike are visibly wrong, which matters more than the price for a hedging book. The standard fix is **Rannacher start-up**: run the first two time steps fully implicit ($\theta = 0$, where $g$ is small and positive for high modes) to crush the kink, then switch to Crank-Nicolson for the rest. This restores clean Greeks while keeping second-order convergence overall.
