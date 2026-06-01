# pyfolio

**Topic:** Computational Finance
**Tags:** portfolio analytics, tear sheet, backtesting, sharpe ratio, drawdown, performance attribution
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**pyfolio** is an open-source Python library (developed by Quantopian) that generates standardised **tear sheets** — multi-page visual performance reports — from a daily return series, computing rolling and aggregate risk-adjusted metrics, drawdown analysis, and factor exposure automatically.

## Key Formula

The core input is a pandas Series of daily returns $r_t$. pyfolio annualises the Sharpe ratio assuming 252 trading days:

$$SR_{\text{ann}} = \frac{\bar{r}}{\hat{\sigma}} \times \sqrt{252}$$

and computes the **max drawdown** from the cumulative wealth index $W_t = \prod_{s=1}^{t}(1 + r_s)$:

$$\text{MDD} = \min_{t} \left(\frac{W_t}{\max_{s \leq t} W_s} - 1\right)$$

A full tear sheet also reports the Sortino ratio (penalises only downside volatility), Calmar ratio ($SR_{\text{ann}} / \lvert\text{MDD}\rvert$), alpha and beta vs. a benchmark, and a rolling 6-month Sharpe ribbon.

## Example

```python
import pyfolio as pf

pf.create_full_tear_sheet(
    returns,                     # daily return Series
    benchmark_rets=spy_returns   # optional benchmark
)
```

For a strategy with annualised return 12\%, volatility 8\%, the tear sheet reports $SR = 12/8 = 1.5$. If the largest peak-to-trough decline was $-18\%$, the Calmar ratio is $12/18 = 0.67$. The rolling Sharpe plot reveals whether that 1.5 was stable or driven by a single good year.

## Remember

A single headline Sharpe ratio hides almost everything that matters about a strategy. pyfolio's tear sheet forces you to look at the full distribution of monthly returns, the time-clustering of drawdowns, and the rolling evolution of risk-adjusted performance — all the dimensions that determine whether a strategy is deployable. The standard use case in a quant team is to run `create_full_tear_sheet` as the first step after any backtest: if the rolling Sharpe shows that all the alpha was earned in 2020–2021 and the strategy has been flat since, a static 3-year Sharpe of 1.0 is misleading, and the tear sheet makes this immediately visible.
