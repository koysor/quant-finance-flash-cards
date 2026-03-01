# Continuous-Time Limit

**Topic:** Derivatives
**Tags:** binomial model, Black-Scholes, PDE, Taylor expansion, convergence, CQF

---

## Definition

The **continuous-time limit** is the process by which the discrete binomial option-pricing model converges to the Black-Scholes PDE as the time step $\delta t \to 0$ (equivalently, the number of steps $N \to \infty$). Starting from the one-step risk-neutral pricing formula, a Taylor expansion in powers of $\delta t$ is applied to the option value. Terms of order $\delta t^2$ and higher vanish in the limit, and — crucially — the real-world drift $\mu$ cancels out entirely. Only the volatility $\sigma$ and the risk-free rate $r$ survive, yielding a deterministic partial differential equation for the option price.

## Key Formula

Begin with a one-step binomial tree. The option value at a node satisfies:

$$V = e^{-r\,\delta t}\bigl[q\,V^{+} + (1-q)\,V^{-}\bigr]$$

where $q$ is the risk-neutral up-probability. Expand $V^{+}$ and $V^{-}$ using Taylor series about the current stock price $S$, collect terms in $\delta t$, and let $\delta t \to 0$. The result is the **Black-Scholes PDE**:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

Key observations from the expansion:

| Order | Contribution |
|---|---|
| $O(1)$ | Identically satisfied |
| $O(\delta t)$ | Produces the PDE above |
| $O(\delta t^2)$ | Vanishes as $\delta t \to 0$ |

The drift $\mu$ drops out because the risk-neutral probability $q$ is constructed so that the expected stock return equals $r$, not $\mu$.

## Example

Consider a binomial tree with $S = 100$, $\sigma = 0.20$, $r = 0.05$, and $N$ steps over $T = 1$ year, so $\delta t = 1/N$.

The CRR (Cox-Ross-Rubinstein) parameters are:

$$u = e^{\sigma\sqrt{\delta t}}, \quad d = e^{-\sigma\sqrt{\delta t}}, \quad q = \frac{e^{r\,\delta t} - d}{u - d}$$

| $N$ | $\delta t$ | Call price ($K=100$) |
|---|---|---|
| 10 | 0.100 | £10.37 |
| 100 | 0.010 | £10.44 |
| 1000 | 0.001 | £10.45 |
| $\infty$ | $\to 0$ | **£10.45** (Black-Scholes) |

As $N$ increases, the binomial price converges to the closed-form Black-Scholes value, confirming the continuous-time limit.

## Remember

- The drift $\mu$ vanishing is not a coincidence — it is a consequence of **risk-neutral pricing**. Because we can delta-hedge, the option price depends only on the hedging cost (driven by $\sigma$) and the financing cost (driven by $r$), never on where the stock is expected to go.
- This limit argument is central to CQF Module 1: it bridges the intuitive discrete binomial world with the continuous PDE framework used in production pricing libraries.
- In practice, the convergence is slow ($O(1/\sqrt{N})$ for vanilla options), which motivates Richardson extrapolation and other acceleration techniques when using trees for numerical pricing.
