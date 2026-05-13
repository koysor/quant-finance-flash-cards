# Time Series Cross-Validation

**Topic:** Computational Finance
**Tags:** time series cross-validation, forward chaining, walk-forward, look-ahead bias, backtesting, overfitting
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Time series cross-validation** (walk-forward or forward-chaining validation) is a model evaluation technique that respects the temporal ordering of data by always training on past observations and testing on future ones. It prevents the look-ahead bias that standard $k$-fold cross-validation introduces when applied naively to sequential financial data.

## Key Formula

**Expanding window** — training set grows over time:

$$\text{Train on } [1, T_k],\quad \text{Test on } [T_k+1, T_k+h], \quad k = 1, \ldots, K$$

**Rolling window** — fixed training window of size $W$ moves forward:

$$\text{Train on } [T_k - W + 1, T_k],\quad \text{Test on } [T_k+1, T_k+h]$$

$$\text{CV score} = \frac{1}{K}\sum_{k=1}^{K} \mathcal{L}\!\left(\hat{f}^{(k)},\, \mathbf{y}_{T_k+1:T_k+h}\right)$$

**Expanding window** is preferred when the full history is informative; **rolling window** when the data-generating process may be non-stationary and recent data is more relevant.

## Example

Ten years of daily equity returns (2,520 observations). Expanding window with annual test periods: train 2015, test 2016; train 2015–2016, test 2017; …; train 2015–2023, test 2024. The model is retrained 9 times, each test period is genuinely out-of-sample, and the average test Sharpe ratio is the honest estimate of live performance.

## Remember

Look-ahead bias is the most common and damaging error in quantitative backtesting. Standard $k$-fold CV randomly shuffles and splits, allowing "future" information to leak into training — producing backtest Sharpe ratios that collapse to near zero in live deployment. Time series cross-validation simulates exactly how a strategy would have been deployed historically, making it the only methodologically sound validation framework for financial signals. The rolling-vs-expanding choice matters too: expanding window assumes the full market history is relevant; rolling window acknowledges that a model fit on 1990s data may not apply to post-2008 markets.
