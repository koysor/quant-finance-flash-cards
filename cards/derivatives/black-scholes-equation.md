# Black-Scholes Equation

**Topic:** Derivatives
**Tags:** Black-Scholes, options, PDE, pricing, lognormal
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

The **Black-Scholes model** (1973) gives a closed-form price for European options on a non-dividend-paying stock, assuming the stock price follows Geometric Brownian Motion and markets are frictionless.

## Key Formulae

**European call price:**

$$C = S_0 \, N(d_1) - K e^{-rT} N(d_2)$$

**European put price:**

$$P = K e^{-rT} N(-d_2) - S_0 \, N(-d_1)$$

where:

$$d_1 = \frac{\ln(S_0 / K) + \left(r + \tfrac{\sigma^2}{2}\right)T}{\sigma \sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}$$

| Symbol | Meaning |
|---|---|
| $S_0$ | Current stock price |
| $K$ | Strike price |
| $r$ | Continuously compounded risk-free rate |
| $\sigma$ | Annualised volatility of the stock |
| $T$ | Time to expiry (in years) |
| $N(\cdot)$ | Cumulative standard normal CDF |

The underlying **Black-Scholes PDE** that any derivative price $V(S,t)$ must satisfy is:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

## Example

Price a European call with $S_0 = 100$, $K = 100$, $r = 5\%$, $\sigma = 20\%$, $T = 1$ year.

$$d_1 = \frac{\ln(1) + (0.05 + 0.02)}{0.20} = \frac{0.07}{0.20} = 0.35$$

$$d_2 = 0.35 - 0.20 = 0.15$$

$$C = 100 \cdot N(0.35) - 100 e^{-0.05} \cdot N(0.15) \approx 100(0.637) - 95.12(0.560) \approx \textbf{£10.45}$$

## Remember

- $N(d_2)$ is the risk-neutral probability that the option expires in the money; $N(d_1)$ is the delta-weighted probability used to value the stock component.
- The formula assumes **constant volatility** — a simplification violated in practice. Traders quote options in terms of **implied volatility** (the $\sigma$ that recovers the market price) rather than the raw price.
- The PDE is derived by constructing a **delta-hedged portfolio** that eliminates the stochastic term, leaving a deterministic equation that must earn the risk-free rate.
