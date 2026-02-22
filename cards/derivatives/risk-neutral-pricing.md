# Risk-Neutral Pricing

**Topic:** Derivatives
**Level:** A Level Mathematics
**Tags:** risk-neutral measure, Q measure, no-arbitrage, martingale, derivatives pricing

---

## Definition

**Risk-neutral pricing** is a no-arbitrage valuation technique in which we price derivatives by replacing the real-world drift $\mu$ with the risk-free rate $r$, and computing a discounted expected payoff. The resulting probability measure is called the **risk-neutral measure** $\mathbb{Q}$.

Under $\mathbb{Q}$, all traded assets grow at rate $r$ on average — investors are neither rewarded nor penalised for taking risk. This is not a description of reality; it is a mathematical device that ensures prices are free of arbitrage.

## Key Formula

The fundamental pricing equation under $\mathbb{Q}$:

$$V_0 = e^{-rT} \, \mathbb{E}^{\mathbb{Q}}\!\left[V_T\right]$$

For a European call with payoff $V_T = \max(S_T - K,\, 0)$:

$$C = e^{-rT} \, \mathbb{E}^{\mathbb{Q}}\!\left[\max(S_T - K,\, 0)\right]$$

Under $\mathbb{Q}$, the stock price satisfies:

$$dS_t = r S_t \, dt + \sigma S_t \, d\widetilde{W}_t$$

where $\widetilde{W}_t$ is Brownian motion under $\mathbb{Q}$. Evaluating the expectation analytically recovers the **Black-Scholes formula**.

## Example

Suppose a stock is £100 today. In one period it goes to £120 (up) or £80 (down). $r = 5\%$.

Find the risk-neutral probability $q$ of the up move:

$$100 \cdot e^{0.05} = 120q + 80(1-q) \implies q = \frac{105.13 - 80}{40} \approx 0.628$$

Price a call with $K = 100$:

$$C = e^{-0.05}\left(0.628 \times 20 + 0.372 \times 0\right) \approx \textbf{£11.96}$$

## Remember

- Risk-neutral pricing does **not** assume investors are indifferent to risk — it is a change of probability measure (Girsanov's theorem) that makes discounted prices **martingales**.
- The risk-neutral measure is the foundation of modern derivatives pricing: Black-Scholes, binomial trees, and Monte Carlo methods all operate under $\mathbb{Q}$.
- Only the risk-free rate $r$ enters the pricing formula, not the actual expected return $\mu$ — the latter cancels out when hedging is possible.
