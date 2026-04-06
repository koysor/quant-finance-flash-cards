# Stochastic Calculus

**Topic:** Stochastic Processes
**Tags:** stochastic calculus, Itô calculus, Brownian motion, SDE, quadratic variation
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Stochastic calculus** is the branch of mathematics that extends ordinary calculus to functions of random processes. The key departure from classical calculus is that Brownian motion paths are nowhere differentiable and have non-zero quadratic variation, so Taylor expansions retain a second-order term that would vanish in the deterministic setting. The central results are the construction of the **Itô integral** and **Itô's lemma**.

## Key Formula

For a stochastic process $X_t$ satisfying $dX_t = \mu\,dt + \sigma\,dW_t$, the Itô integral of an adapted process $H_t$ is defined as:

$$\int_0^t H_s\,dW_s = \lim_{n \to \infty} \sum_{i=0}^{n-1} H_{t_i}\bigl(W_{t_{i+1}} - W_{t_i}\bigr)$$

The critical identity that drives everything is the **quadratic variation rule**:

$$(dW_t)^2 = dt, \qquad dW_t\,dt = 0, \qquad (dt)^2 = 0$$

This means a twice-differentiable function $f(t, X_t)$ satisfies **Itô's lemma**:

$$df = \frac{\partial f}{\partial t}\,dt + \frac{\partial f}{\partial x}\,dX_t + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\sigma^2\,dt$$

The extra $\tfrac{1}{2}\sigma^2 f_{xx}\,dt$ term — the **Itô correction** — has no counterpart in ordinary calculus.

## Example

Apply stochastic calculus to derive the GBM log-price. Let $S_t$ satisfy $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ and set $f = \ln S_t$. The ordinary chain rule would give $d(\ln S_t) = dS_t / S_t$, but Itô's lemma adds a correction:

$$d(\ln S_t) = \frac{1}{S_t}\,dS_t - \frac{1}{2}\cdot\frac{1}{S_t^2}\cdot\sigma^2 S_t^2\,dt = \mu\,dt + \sigma\,dW_t - \frac{\sigma^2}{2}\,dt$$

$$d(\ln S_t) = \left(\mu - \frac{\sigma^2}{2}\right)dt + \sigma\,dW_t$$

With $\mu = 0.08$ and $\sigma = 0.20$, the log-price grows at $0.08 - 0.02 = 0.06$ per year plus random noise — the $-0.02$ is the **volatility drag** that cannot be seen by ordinary differentiation.

## Remember

Stochastic calculus is the mathematical engine of quantitative finance. Itô's lemma transforms the GBM SDE into the Black-Scholes PDE; Itô integrals model the P&L of a delta-hedging strategy; and the zero-expectation property of Itô integrals ($\mathbb{E}[\int H\,dW] = 0$) is the rigorous foundation of risk-neutral pricing. Without stochastic calculus, continuous-time derivative pricing would not be possible.
