# bt (Backtesting Framework)

**Topic:** Computational Finance
**Tags:** backtesting, portfolio rebalancing, tree-of-algos, python, strategy composition, algorithmic trading
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**bt** is a lightweight Python backtesting library in which strategies are built by composing small, reusable **algo** objects into a tree structure — separating the *when to rebalance*, *which assets to select*, and *how to weight* decisions — making it easy to prototype and compare portfolio strategy variants without writing event-driven callbacks.

## Key Formula

Each `bt.algos.Rebalance()` call computes the trades needed to reach the target weights $\mathbf{w}^*$:

$$\Delta n_{i,t} = \frac{w^*_{i,t} \cdot V_t - V_{i,t}}{p_{i,t}}$$

where $V_t$ is the portfolio value, $V_{i,t}$ is the current value held in asset $i$, and $p_{i,t}$ is the price. Positive $\Delta n$ buys shares; negative sells. The algo pipeline is evaluated sequentially:

$$\text{RunMonthly} \to \text{SelectMomentum}(n) \to \text{WeighEqually} \to \text{Rebalance}$$

only executing the rebalance step when the scheduling algo signals `True`.

## Example

```python
import bt
import pandas as pd

# Equal-weight monthly rebalance across 3 ETFs
strategy = bt.Strategy('EW-Monthly', [
    bt.algos.RunMonthly(),
    bt.algos.SelectAll(),
    bt.algos.WeighEqually(),
    bt.algos.Rebalance()
])

backtest = bt.Backtest(strategy, prices)   # prices: DataFrame of daily closes
result = bt.run(backtest)
result.display()   # prints Sharpe, CAGR, max drawdown
result.plot()      # plots cumulative returns
```

Swapping `WeighEqually()` for `WeighMeanVar()` reruns the same backtest with mean-variance weights in two lines, enabling rapid strategy comparison.

## Remember

bt's tree-of-algos model is designed for **portfolio-level** strategies — monthly or quarterly rebalancing of multi-asset or factor-based portfolios — rather than the bar-by-bar execution that Zipline handles. The key insight is that strategy research is mostly about comparing many weight-scheme and selection-rule combinations quickly; bt makes this a matter of swapping a single algo object, whereas Zipline would require rewriting the `handle_data` function each time. bt is the appropriate choice for long-only factor portfolios (momentum, value, quality) where the rebalancing granularity is daily or lower frequency, and Zipline is warranted only when intraday execution logic or complex order management is needed.
