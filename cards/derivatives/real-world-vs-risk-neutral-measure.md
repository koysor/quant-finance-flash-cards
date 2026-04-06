# Real World vs Risk-Neutral Probability Measure

**Topic:** Derivatives
**Tags:** P measure, Q measure, risk-neutral pricing, Girsanov, change of measure, market price of risk
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **real-world measure** $\mathbb{P}$ (or physical measure) describes probabilities as they actually occur — asset prices drift at their true expected return $\mu$. The **risk-neutral measure** $\mathbb{Q}$ is an equivalent probability measure under which all assets grow at the risk-free rate $r$, making discounted asset prices martingales. Under $\mathbb{Q}$, option prices are simply discounted expectations of their payoffs, with no need to know $\mu$.

## Key Formula

**GBM under the real-world measure $\mathbb{P}$:**

$$dS = \mu S\, dt + \sigma S\, dW^{\mathbb{P}}$$

**GBM under the risk-neutral measure $\mathbb{Q}$:**

$$dS = r S\, dt + \sigma S\, dW^{\mathbb{Q}}$$

The measures are linked via the **market price of risk** $\lambda = \frac{\mu - r}{\sigma}$ and **Girsanov's theorem**:

$$dW^{\mathbb{Q}} = dW^{\mathbb{P}} + \lambda\, dt$$

**Risk-neutral pricing formula:**

$$V_0 = e^{-rT} \, E^{\mathbb{Q}}[V_T]$$

Under $\mathbb{P}$, a correction for risk aversion would be required; under $\mathbb{Q}$, discounting at $r$ suffices.

## Example

A stock has $\mu = 12\%$, $\sigma = 20\%$, $r = 5\%$.

Market price of risk: $\lambda = \frac{0.12 - 0.05}{0.20} = 0.35$

Under $\mathbb{P}$, the stock has a positive drift premium — investors expect 7% above the risk-free rate to compensate for bearing volatility risk.

Under $\mathbb{Q}$, the drift is replaced by $r = 5\%$. A European call is then priced as:

$$C = e^{-rT} E^{\mathbb{Q}}[\max(S_T - K, 0)]$$

The Black-Scholes formula evaluates this expectation exactly. Crucially, $\mu = 12\%$ does not appear anywhere in the price — only $r$, $\sigma$, $S_0$, $K$, and $T$ matter.

## Remember

The $\mathbb{P}$/$\mathbb{Q}$ distinction is one of the most important conceptual divides in quantitative finance. **Derivatives pricing** lives under $\mathbb{Q}$ — use $r$ as the drift, and the market price of risk disappears. **Risk management and portfolio management** live under $\mathbb{P}$ — use the true drift $\mu$ to forecast P&L, compute VaR, or run scenario analyses. Confusing the two measures is a common error: plugging a $\mathbb{Q}$-calibrated volatility surface into a $\mathbb{P}$-based risk model without adjustment implicitly assumes the market price of risk is zero, which is almost never true.
