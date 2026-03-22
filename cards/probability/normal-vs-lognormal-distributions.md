# Normal vs Lognormal Distributions

**Topic:** Probability
**Tags:** normal distribution, lognormal distribution, returns, asset prices, Black-Scholes
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **normal distribution** is symmetric about its mean, unbounded in both directions, and fully described by $\mu$ and $\sigma$. The **lognormal distribution** applies to a variable whose logarithm is normally distributed — it is positively skewed and bounded below by zero. In quantitative finance, log returns are modelled as normal, which implies that price levels are lognormal. Choosing between the two distributions determines whether a model can produce negative values — a critical distinction for asset prices, interest rates, and option pricing.

## Key Formula

If log returns are normal:

$$\ln \frac{S_T}{S_0} \sim N\!\left(\left(\mu - \tfrac{1}{2}\sigma^2\right)T,\; \sigma^2 T\right)$$

then the price level is lognormal:

$$S_T = S_0 \exp\!\left(\left(\mu - \tfrac{1}{2}\sigma^2\right)T + \sigma\sqrt{T}\,Z\right), \quad Z \sim N(0,1)$$

| Property | Normal | Lognormal |
|---|---|---|
| Support | $(-\infty, +\infty)$ | $(0, +\infty)$ |
| Symmetry | Symmetric | Right-skewed |
| Mean | $\mu$ | $e^{\mu + \sigma^2/2}$ |
| Median | $\mu$ | $e^{\mu}$ |
| Additivity | Sum of normals is normal | Product of lognormals is lognormal |

## Example

A stock at £100 has annualised drift $\mu = 8\%$ and volatility $\sigma = 20\%$.

**Normal model** (applied to price directly): $S_1 \sim N(108, 20^2)$. This gives a 0.27% probability of $S_1 < 0$ — a nonsensical result for a stock price.

**Lognormal model** (applied to log return): $\ln(S_1/100) \sim N(0.06, 0.04)$, so $S_1 > 0$ always. The median price is $100 \times e^{0.06} = £106.18$, below the mean of $100 \times e^{0.08} = £108.33$ — the right skew in action.

## Remember

Black-Scholes assumes lognormal prices (equivalently, normal log returns), which guarantees $S > 0$ and justifies the use of $N(d_1)$ and $N(d_2)$. However, the lognormal assumption breaks down for interest rates (which can be negative, as seen with EUR and JPY rates post-2014) — this is why the Bachelier (normal) model has returned to prominence for rate options. In risk management, the choice matters: normal VaR overestimates the probability of extreme negative prices, while lognormal VaR underestimates the probability of very large positive moves. Neither distribution captures the fat tails observed in practice, but understanding the distinction is the starting point for more realistic models.
