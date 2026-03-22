# Jump-Diffusion Models

**Topic:** Stochastic Processes
**Tags:** jump-diffusion, Merton, Poisson, fat tails, option pricing, stochastic processes
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A **jump-diffusion model** augments the standard continuous diffusion (such as Geometric Brownian Motion) with sudden, discrete jumps that arrive randomly according to a Poisson process. The most widely used version is the **Merton (1976) jump-diffusion model**, which adds lognormally distributed jumps to GBM in order to capture the large, sudden price moves observed in real markets but absent from pure diffusion models.

## Key Formula

**Merton jump-diffusion SDE:**

$$\frac{dS}{S} = (\mu - \lambda \bar{k})\,dt + \sigma\,dW + J\,dN$$

where:

| Symbol | Meaning |
|---|---|
| $\mu$ | Drift rate of the underlying |
| $\sigma$ | Diffusion volatility (continuous component) |
| $dW$ | Brownian motion increment |
| $dN$ | Poisson process increment ($dN = 1$ with probability $\lambda\,dt$, else $0$) |
| $\lambda$ | Average number of jumps per year (jump intensity) |
| $J$ | Random jump size, with $\ln(1 + J) \sim \mathcal{N}(\mu_J, \sigma_J^2)$ |
| $\bar{k}$ | $E[J] = e^{\mu_J + \sigma_J^2/2} - 1$, the compensator that keeps the drift correct |

## Example

Suppose a stock at $S_0 = £100$ follows a jump-diffusion with $\sigma = 20\%$, $\lambda = 1$ jump per year, $\mu_J = -5\%$, and $\sigma_J = 10\%$.

Over a small interval $dt = 1/252$ (one trading day), the continuous part behaves like standard GBM. With probability $\lambda\,dt \approx 0.004$, a jump occurs. If a jump fires, the stock multiplies by $e^J$ where $\ln(1+J) \sim \mathcal{N}(-0.05,\, 0.01)$. A typical jump realisation might be $J = -8\%$, sending the price from £100 to roughly £92 in a single day — a move that pure GBM with $\sigma = 20\%$ would treat as a roughly 6-standard-deviation event.

## Remember

Jump-diffusion models were introduced specifically to explain the **volatility smile**: Black-Scholes assumes continuous paths and produces flat implied volatility across strikes, but market option prices consistently show higher implied volatility for out-of-the-money puts. By adding jumps — typically skewed downward — Merton's model generates the excess kurtosis and negative skewness seen in equity returns, producing a smile-like pattern in implied volatility without abandoning the analytical tractability of the Black-Scholes framework entirely. In practice, jump-diffusion is the simplest extension that captures crash risk, making it a natural stepping stone between pure GBM and the fully stochastic volatility models used on modern trading desks.
