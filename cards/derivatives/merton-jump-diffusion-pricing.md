# Merton's Jump-Diffusion Option Pricing

**Topic:** Derivatives
**Tags:** jump-diffusion, Merton, option pricing, Poisson, volatility smile
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Merton's jump-diffusion option pricing formula** (1976) gives the European option price as an infinite weighted sum of Black-Scholes prices. Each term in the series corresponds to a scenario in which exactly $n$ jumps occur during the option's life, weighted by the Poisson probability of $n$ jumps. Because the jump sizes are lognormally distributed, each conditional sub-problem is itself a Black-Scholes pricing problem with adjusted volatility and risk-free rate.

## Key Formula

$$C = \sum_{n=0}^{\infty} \frac{e^{-\lambda' T}(\lambda' T)^n}{n!} \; C_{\text{BS}}(S,\, K,\, r_n,\, \sigma_n,\, T)$$

where:

| Symbol | Meaning |
|---|---|
| $\lambda' = \lambda(1 + \bar{k})$ | Risk-neutral jump intensity, with $\bar{k} = e^{\mu_J + \sigma_J^2/2} - 1$ |
| $r_n = r - \lambda \bar{k} + n \ln(1 + \bar{k}) / T$ | Adjusted risk-free rate for the $n$-jump scenario |
| $\sigma_n = \sqrt{\sigma^2 + n \sigma_J^2 / T}$ | Total volatility combining diffusion and $n$ jump contributions |
| $C_{\text{BS}}$ | Standard Black-Scholes call price with inputs $(S, K, r_n, \sigma_n, T)$ |
| $\lambda$ | Physical jump intensity (average jumps per year) |
| $\mu_J,\, \sigma_J$ | Mean and standard deviation of $\ln(1 + J)$ |

## Example

Price a European call with $S = 100$, $K = 100$, $r = 5\%$, $\sigma = 20\%$, $T = 1$, $\lambda = 1$, $\mu_J = -5\%$, $\sigma_J = 10\%$.

First compute $\bar{k} = e^{-0.05 + 0.005} - 1 \approx -0.0440$ and $\lambda' = 1 \times 0.956 = 0.956$.

**$n = 0$ term** (no jumps): $r_0 = 0.05 - 1(-0.044) + 0 = 0.094$, $\sigma_0 = 0.20$. Weight $= e^{-0.956} \approx 0.384$. $C_{\text{BS}}(100, 100, 0.094, 0.20, 1) \approx 13.07$. Contribution $\approx 0.384 \times 13.07 = 5.02$.

**$n = 1$ term** (one jump): $r_1 = 0.094 + \ln(0.956) = 0.094 - 0.045 = 0.049$, $\sigma_1 = \sqrt{0.04 + 0.01} = 0.2236$. Weight $= e^{-0.956} \times 0.956 \approx 0.367$. $C_{\text{BS}}(100, 100, 0.049, 0.2236, 1) \approx 10.83$. Contribution $\approx 0.367 \times 10.83 = 3.97$.

**$n = 2$ term**: Weight $\approx 0.176$. $\sigma_2 = \sqrt{0.04 + 0.02} = 0.2449$, $r_2 \approx 0.004$. $C_{\text{BS}} \approx 9.09$. Contribution $\approx 0.176 \times 9.09 = 1.60$.

Summing the first three terms gives $C \approx 5.02 + 3.97 + 1.60 = 10.59$. Higher-order terms contribute progressively less; in practice truncating at $n = 10$--$15$ is sufficient.

## Remember

- When $\lambda = 0$ (no jumps), the series collapses to the single $n = 0$ term and recovers the standard **Black-Scholes price** exactly — so Black-Scholes is nested as a special case.
- The formula produces a **volatility smile** because the jump component adds extra kurtosis: deep out-of-the-money options gain value from the possibility of large jumps, raising their implied volatility relative to at-the-money options.
- In practice the infinite series converges rapidly because the Poisson weights $e^{-\lambda' T}(\lambda' T)^n / n!$ shrink factorially. Truncating at 10--15 terms gives machine-precision accuracy for typical parameters.
- Merton's formula is analytically tractable — each term is a standard Black-Scholes evaluation — making it far cheaper to compute than Monte Carlo and a natural first extension when constant-volatility pricing is inadequate.
