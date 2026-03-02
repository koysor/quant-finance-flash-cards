# Euler-Maruyama Method

**Topic:** Stochastic Processes
**Tags:** Euler-Maruyama, SDE, simulation, discretisation, Monte Carlo, numerical methods
**Author:** Claude Opus 4.6

---

## Definition

The **Euler-Maruyama method** is the simplest numerical scheme for simulating stochastic differential equations. It converts a continuous-time SDE into a discrete time-stepping rule by replacing infinitesimal increments with finite ones. It is the stochastic analogue of the Euler method for ordinary differential equations.

## Key Formula

For the general SDE $dS = a(S, t) \, dt + b(S, t) \, dW$, the Euler-Maruyama discretisation is:

$$S_{i+1} = S_i + a(S_i, t_i) \, \delta t + b(S_i, t_i) \, \phi \sqrt{\delta t}$$

where $\phi \sim \mathcal{N}(0, 1)$ is a fresh independent draw at each step.

| Continuous | Discrete replacement |
|---|---|
| $dt$ | $\delta t$ (fixed time step) |
| $dW$ | $\phi \sqrt{\delta t}$, with $\phi \sim \mathcal{N}(0,1)$ |
| $dS$ | $S_{i+1} - S_i$ |

For GBM ($a = \mu S$, $b = \sigma S$):

$$S_{i+1} = S_i \left(1 + \mu \, \delta t + \sigma \, \phi \sqrt{\delta t}\right)$$

For the Vasicek model ($a = \gamma(\bar{r} - r)$, $b = \sigma$):

$$r_{i+1} = r_i + \gamma(\bar{r} - r_i) \, \delta t + \sigma \, \phi \sqrt{\delta t}$$

## Example

Simulate one step of GBM with $S_0 = 100$, $\mu = 0.05$, $\sigma = 0.20$, $\delta t = 0.01$, and a random draw $\phi = 0.73$:

$$S_1 = 100 \left(1 + 0.05 \times 0.01 + 0.20 \times 0.73 \times \sqrt{0.01}\right) = 100(1 + 0.0005 + 0.0146) = \textbf{101.51}$$

## Remember

The Euler-Maruyama method works for any SDE, which is its main advantage over exact solutions that exist only for special cases like GBM. The approximation improves as $\delta t \to 0$, and for mean-reverting models one should keep $\gamma \, \delta t < 1$ to avoid numerical instability. For GBM specifically, the exact exponential formula $S_{i+1} = S_i \exp[(\mu - \frac{1}{2}\sigma^2)\delta t + \sigma \phi \sqrt{\delta t}]$ avoids discretisation error entirely.
