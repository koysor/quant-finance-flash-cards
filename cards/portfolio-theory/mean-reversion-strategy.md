# Mean Reversion Strategy

**Topic:** Portfolio Theory & Asset Pricing
**Level:** A Level Mathematics
**Tags:** mean reversion, contrarian, value, overreaction, pairs trading
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A mean reversion strategy profits from the tendency of asset prices or returns to revert towards a historical average or fundamental value after deviating from it. The trader buys assets that have underperformed (expecting a bounce) and sells or shorts assets that have outperformed (expecting a pullback). Mean reversion is the contrarian counterpart to momentum — it works best at very short horizons (intraday to a few days) or very long horizons (3–5 years), while momentum dominates at intermediate horizons (3–12 months).

## Key Formula

A simple **z-score signal** for a mean reversion trade on asset $i$:

$$z_i = \frac{P_i - \mu_i}{\sigma_i}$$

where $\mu_i$ is the rolling mean price and $\sigma_i$ is the rolling standard deviation. The strategy goes long when $z_i < -z^*$ and short when $z_i > z^*$, where $z^*$ is a threshold (commonly 1.5 or 2).

The **expected profit** per round trip:

$$E[\text{P\&L}] = 2 \times z^* \times \sigma_i - C_{\text{transaction}}$$

## Example

A stock has a 60-day rolling mean of £50.00 and rolling standard deviation of £3.00. The current price is £44.50:

$$z = \frac{£44.50 - £50.00}{£3.00} = -1.83$$

Since $z < -1.5$, the strategy enters a long position. If the price reverts to the mean at £50.00, the gross profit is £5.50 per share. With transaction costs of £0.10 per share (round trip), the net profit is £5.40, a return of:

$$R = \frac{£5.40}{£44.50} = 12.1\%$$

However, if the price decline reflects a genuine fundamental shift rather than a temporary overreaction, the stock may not revert and losses can mount.

## Remember

Mean reversion strategies exploit the behavioural tendency of markets to overreact to news in the short term and correct over time. In quantitative finance, the key challenge is distinguishing temporary dislocations from permanent regime changes — a stock that has fallen 30% may be cheap (mean-reverting) or may be in structural decline (trending). Pairs trading, statistical arbitrage, and convergence trades are all applications of mean reversion. The strategy is the natural complement to momentum: many multi-factor portfolios blend both to diversify across market regimes, since mean reversion tends to perform well when momentum crashes.
