# Statistical Arbitrage

**Topic:** Financial Mathematics
**Tags:** statistical arbitrage, pairs trading, mean reversion, market neutral, quantitative strategy
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Statistical arbitrage (stat arb) is a class of quantitative trading strategies that exploit temporary statistical mispricings across large numbers of securities. Unlike classical arbitrage, which guarantees a risk-free profit, stat arb relies on the law of large numbers — individual trades carry risk, but across hundreds or thousands of positions the expected profit is positive with high probability.

## Key Formula

The **expected portfolio return** for $N$ independent pairs, each with expected profit $\mu_i$ and variance $\sigma_i^2$:

$$E[R_p] = \frac{1}{N} \sum_{i=1}^{N} \mu_i$$

$$\sigma_p = \frac{1}{N} \sqrt{\sum_{i=1}^{N} \sigma_i^2}$$

The **portfolio Sharpe ratio** scales with the square root of the number of independent bets:

$$\text{SR}_p \approx \text{SR}_{\text{single}} \times \sqrt{N}$$

This is the **fundamental law of active management** applied to stat arb.

## Example

A stat arb fund runs 200 independent pairs trades, each with an expected return of 0.5% per month and a standard deviation of 3%.

$$E[R_p] = 0.5\%$$

$$\sigma_p = \frac{3\%}{\sqrt{200}} = 0.21\%$$

$$\text{SR}_{\text{monthly}} = \frac{0.5\%}{0.21\%} = 2.4$$

The single-trade Sharpe ratio is only $0.5/3 = 0.17$, but diversification across 200 trades lifts the portfolio Sharpe to 2.4. This illustrates why stat arb funds trade large numbers of positions — the strategy only works at scale.

## Remember

Statistical arbitrage is the industrial-scale extension of pairs trading. While a single pairs trade is risky, running hundreds simultaneously diversifies away idiosyncratic risk, leaving only systematic exposures (which are hedged separately). The strategy's profitability depends on three factors: the **breadth** (number of independent bets), the **information coefficient** (accuracy of the signal), and **transaction costs** (which erode alpha on high-frequency rebalancing). Academic research shows that stat arb profits have declined over time as more capital has entered the space — a phenomenon known as alpha decay — making execution speed, cost management, and signal innovation increasingly important.
