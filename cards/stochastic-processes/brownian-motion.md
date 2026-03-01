# Brownian Motion

**Topic:** Stochastic Processes
**Tags:** stochastic processes, Brownian motion, Wiener process, random walk

---

## Definition

**Standard Brownian motion** (or Wiener process) $W(t)$ is a continuous-time stochastic process that models random movement. It satisfies four properties: $W(0) = 0$, independent increments, normally distributed increments $W(t) - W(s) \sim N(0, t - s)$, and continuous (but nowhere differentiable) paths. It is the mathematical foundation of most asset price models in finance.

## Key Formula

The increment over an infinitesimal time step:

$$dW \sim N(0, dt) \qquad \Rightarrow \qquad (dW)^2 = dt$$

Geometric Brownian Motion (GBM) uses Brownian motion to model asset prices:

$$dS = \mu S \, dt + \sigma S \, dW$$

with solution:

$$S(T) = S(0) \exp\!\left(\left(\mu - \tfrac{\sigma^2}{2}\right)T + \sigma W(T)\right)$$

## Example

Simulate one step of Brownian motion with $\delta t = 0.01$.

Draw $Z \sim N(0, 1)$. The Brownian increment is $\Delta W = Z \sqrt{\delta t} = Z \times 0.1$.

If $Z = 1.5$, then $\Delta W = 0.15$. Starting from $W(0) = 0$, we get $W(0.01) = 0.15$.

For GBM with $S_0 = 100$, $\mu = 0.08$, $\sigma = 0.2$, $\delta t = 0.01$:

$$S(0.01) = 100 \times \exp\!\left((0.08 - 0.02) \times 0.01 + 0.2 \times 0.15\right) = 100 \times e^{0.0306} \approx £103.11$$

## Remember

- The $(dW)^2 = dt$ result is crucial — it means that at the second order, the randomness is actually **deterministic**. This is what makes Itô's lemma tractable.
- GBM implies that **log-returns** are normally distributed, which is why the Black-Scholes model leads to a lognormal stock price distribution.
- GBM does **not** capture: fat tails, volatility clustering, or jumps — real limitations of the Black-Scholes model.
