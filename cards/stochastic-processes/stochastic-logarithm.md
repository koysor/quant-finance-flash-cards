# Stochastic Logarithm

**Topic:** Stochastic Processes
**Tags:** stochastic logarithm, semimartingale, doleans exponential, inverse, relative return, stochastic calculus
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

The **stochastic logarithm** of a positive semimartingale $Z$ with $Z_0 > 0$ is the unique semimartingale $M$ satisfying $dM_t = dZ_t / Z_{t-}$, denoted $\mathcal{L}(Z)_t$. It is the left-inverse of the Doléans exponential: $\mathcal{E}(\mathcal{L}(Z)) = Z$.

## Key Formula

For a positive continuous semimartingale $Z$:

$$\mathcal{L}(Z)_t = \ln\frac{Z_t}{Z_0} + \frac{1}{2[Z,Z]_t^c}{}\quad\text{(continuous case)}$$

More precisely, using Itô's lemma applied to $\ln Z$:

$$\mathcal{L}(Z)_t = \ln Z_t - \ln Z_0 + \frac{1}{2}\int_0^t \frac{d[Z,Z]_s^c}{Z_s^2}$$

where $[Z,Z]^c$ is the continuous part of the quadratic variation. For a process with jumps, the formula includes a correction: $-\sum_{s \le t}(\Delta Z_s / Z_{s-} - \ln(1 + \Delta Z_s / Z_{s-}))$.

## Example

Let $Z_t = S_0 e^{\mu t + \sigma W_t}$ (geometric Brownian motion) with $S_0 = 100$, $\mu = 0.05$, $\sigma = 0.2$. Then $dZ = Z(\mu\,dt + \sigma\,dW)$, so:

$$\mathcal{L}(Z)_t = \int_0^t \frac{dZ_s}{Z_s} = \mu t + \sigma W_t$$

At $t = 1$ with $W_1 = 0.5$: $\mathcal{L}(Z)_1 = 0.05 + 0.2 \times 0.5 = 0.15$.

Note this equals $\ln(Z_1/Z_0) + \tfrac{1}{2}\sigma^2 t = (0.05 - 0.02)t + \sigma W_t + 0.02t = 0.15$ ✓

## Remember

The stochastic logarithm captures **instantaneous relative returns**: $dM_t = dZ_t / Z_{t-}$ is the percentage change in $Z$ over an infinitesimal interval. In quantitative finance this arises naturally when decomposing a price process into its multiplicative factors — for instance, computing the log-return process of a self-financing portfolio or expressing the Radon–Nikodým density in terms of the market price of risk. The stochastic logarithm maps multiplicative semimartingale structure back to additive structure, making it the continuous-time analogue of taking logarithms of a product.
