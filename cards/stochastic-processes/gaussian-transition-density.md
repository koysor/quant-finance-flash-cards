# Gaussian Transition Density

**Topic:** Stochastic Processes
**Tags:** transition density, Gaussian, Brownian motion, Kolmogorov, Green's function, diffusion

---

## Definition

The **Gaussian transition density** is the fundamental solution to the forward Kolmogorov (Fokker-Planck) equation with a delta-function initial condition. It gives the probability density for a diffusion process to move from position $y$ at time $t$ to position $y'$ at time $t'$. For a pure diffusion with no drift and constant diffusion coefficient $c$, the transition density is a Gaussian whose variance grows linearly in time — a direct consequence of the central limit theorem applied to the accumulation of infinitesimal independent increments.

## Key Formula

The transition density solving $\frac{\partial p}{\partial t'} = c^2 \frac{\partial^2 p}{\partial y'^2}$ with initial condition $p(y, t; y', t) = \delta(y' - y)$ is:

$$p(y, t;\, y', t') = \frac{1}{2c\sqrt{\pi(t'-t)}} \exp\!\left(-\frac{(y'-y)^2}{4c^2(t'-t)}\right)$$

This is a normal distribution with parameters:

- **Mean:** $y$ (no drift, so the expected position stays at the starting point)
- **Variance:** $2c^2(t'-t)$ (grows linearly with the time interval)
- **Standard deviation:** $c\sqrt{2(t'-t)}$

For standard Brownian motion where $c = \frac{1}{\sqrt{2}}$, the variance simplifies to $t'-t$ and the density becomes:

$$p(y, t;\, y', t') = \frac{1}{\sqrt{2\pi(t'-t)}} \exp\!\left(-\frac{(y'-y)^2}{2(t'-t)}\right)$$

## Example

Suppose a particle starts at $y = 0$ and undergoes pure diffusion with $c = 1$ over a time interval $t' - t = 4$. The transition density has variance $2 \times 1^2 \times 4 = 8$ and standard deviation $\sqrt{8} = 2\sqrt{2} \approx 2.83$. To find the probability the particle lies between $-2$ and $2$:

$$P(-2 \le y' \le 2) = \int_{-2}^{2} \frac{1}{2\sqrt{4\pi}} \exp\!\left(-\frac{y'^2}{16}\right) dy' = \text{erf}\!\left(\frac{1}{\sqrt{2}}\right) \approx 0.683$$

This is the familiar 68% rule — the interval $\pm\sigma$ captures about two-thirds of the probability, regardless of the diffusion coefficient or time elapsed, because the shape is always Gaussian.

## Remember

This density is the **Green's function** of the diffusion equation, and its generalisation (modified for drift) is the engine behind option pricing. In the Black-Scholes framework, the price of a European option equals the discounted expectation of the payoff under the risk-neutral measure:

$$V = e^{-r(T-t)} \int_0^{\infty} h(S_T)\, p(S_t, t;\, S_T, T)\, dS_T$$

where $h$ is the payoff function and $p$ is the (lognormal) transition density of the risk-neutral stock price process. Integrating payoff times density gives the option price — making the transition density the single most important object in continuous-time derivatives pricing.
