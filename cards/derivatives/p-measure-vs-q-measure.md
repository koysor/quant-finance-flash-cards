# Physical Measure vs Risk-Neutral Measure

**Topic:** Derivatives
**Tags:** probability measure, risk-neutral, physical measure, P measure, Q measure, pricing
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **physical measure** $\mathbb{P}$ (also called the real-world measure) assigns probabilities that reflect how events actually occur in the real world. The **risk-neutral measure** $\mathbb{Q}$ is an artificial probability measure under which all assets earn the risk-free rate on average, so that derivative prices equal discounted expected payoffs. The two measures agree on which events are possible but assign different probabilities to them.

## Key Formula

Under $\mathbb{P}$ (real world), a stock has drift $\mu$:

$$dS = \mu S\,dt + \sigma S\,dW_t^{\mathbb{P}}$$

Under $\mathbb{Q}$ (risk-neutral), the same stock has drift $r$:

$$dS = rS\,dt + \sigma S\,dW_t^{\mathbb{Q}}$$

The volatility $\sigma$ is the **same** under both measures — only the drift changes.

**Derivative pricing** uses $\mathbb{Q}$:

$$V_0 = E^{\mathbb{Q}}\!\left[e^{-rT}\,\text{payoff}(S_T)\right]$$

**Risk forecasting** uses $\mathbb{P}$:

$$\text{VaR}_\alpha = -\inf\{x : P^{\mathbb{P}}(\text{loss} \leq x) \geq \alpha\}$$

| | $\mathbb{P}$ (Physical) | $\mathbb{Q}$ (Risk-Neutral) |
|---|---|---|
| **Drift** | Real-world $\mu$ | Risk-free rate $r$ |
| **Volatility** | $\sigma$ | $\sigma$ (unchanged) |
| **Used for** | Forecasting, VaR, simulation | Pricing derivatives |
| **Probabilities** | Reflect actual likelihoods | Adjusted for risk aversion |

## Example

A stock has $\mu = 12\%$, $r = 5\%$, $\sigma = 20\%$. Consider a 1-year binary call paying £100 if $S_T > S_0$.

Under $\mathbb{P}$ (real world): $\;d_2^{\mathbb{P}} = \frac{(\mu - \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}} = \frac{(0.12 - 0.02) \times 1}{0.20} = 0.50$

$$P^{\mathbb{P}}(S_T > S_0) = \Phi(0.50) = 61.5\%$$

Under $\mathbb{Q}$ (risk-neutral): $\;d_2^{\mathbb{Q}} = \frac{(r - \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}} = \frac{(0.05 - 0.02) \times 1}{0.20} = 0.15$

$$P^{\mathbb{Q}}(S_T > S_0) = \Phi(0.15) = 55.96\%$$

$$\text{Price} = e^{-0.05} \times 100 \times 0.5596 = \text{£}53.24$$

The real-world probability of payout is 61.5%, but the price is based on the risk-neutral probability of 55.96%. The difference reflects the market price of risk.

## Remember

The $\mathbb{P}$ vs $\mathbb{Q}$ distinction is the single most important conceptual divide in quantitative finance. **Pricing** lives in $\mathbb{Q}$: Girsanov's theorem replaces the unknown drift $\mu$ with the observable rate $r$, which is why the Black–Scholes formula does not depend on $\mu$. **Risk management** lives in $\mathbb{P}$: VaR, expected shortfall, and scenario analysis all require real-world probabilities because they ask "what will actually happen?" not "what is the fair price?". Confusing the two measures is a common and costly error — using $\mathbb{Q}$ for risk forecasting understates tail probabilities (since $\mathbb{Q}$ downweights good outcomes), while using $\mathbb{P}$ for pricing ignores risk aversion and produces prices no one would trade at.
