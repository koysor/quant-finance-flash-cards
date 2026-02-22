# Brownian Motion

**Topic:** Stochastic Processes
**Level:** A Level Mathematics
**Tags:** stochastic processes, Brownian motion, Wiener process, random walk

---

## Definition

**Standard Brownian motion** (or Wiener process) W(t) is a continuous-time stochastic process that models random movement. It is the mathematical foundation of most asset price models in finance.

## Key Properties

Let W(t) denote standard Brownian motion:

1. **W(0) = 0** — starts at zero.
2. **Independent increments** — W(t) − W(s) is independent of all information up to time s.
3. **Normally distributed increments** — W(t) − W(s) ~ N(0, t − s) for t > s.
4. **Continuous paths** — W(t) is continuous (but not differentiable) everywhere.

A key result:

$$dW \sim N(0, dt) \quad \Rightarrow \quad (dW)^2 = dt$$

## Geometric Brownian Motion (GBM)

Asset prices are typically modelled using **Geometric Brownian Motion**, which ensures prices remain positive:

$$dS = \mu S \, dt + \sigma S \, dW$$

- **μ** — drift (expected return)
- **σ** — volatility
- **dW** — Brownian increment

The solution is:

$$S(T) = S(0) \exp\!\left(\left(\mu - \tfrac{\sigma^2}{2}\right)T + \sigma W(T)\right)$$

## Remember

- The (dW)² = dt result is crucial — it means that at the second order, the randomness is actually **deterministic**. This is what makes Itô's lemma tractable.
- GBM implies that **log returns** are normally distributed, which is why the Black-Scholes model leads to a lognormal stock price distribution.
- GBM does **not** capture: fat tails, volatility clustering, or jumps — real limitations of the Black-Scholes model.
