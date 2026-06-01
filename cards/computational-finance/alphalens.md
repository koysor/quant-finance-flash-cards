# Alphalens

**Topic:** Computational Finance
**Tags:** factor analysis, information coefficient, quantile returns, alpha signal, backtesting, turnover
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**Alphalens** (maintained as `alphalens-reloaded`) is an open-source Python library for performance analysis of predictive equity factors (alpha signals) that produces quantile return tear sheets, Information Coefficient decay plots, and turnover diagnostics before a full backtest is run.

## Key Formula

The core output is the **forward-return by quantile**: stocks are ranked into $Q$ bins by their factor value at time $t$, and the mean forward return over horizon $h$ is computed per bin:

$$\bar{r}_q(h) = \frac{1}{T}\sum_{t=1}^{T} \frac{1}{\lvert \mathcal{I}_{q,t} \rvert} \sum_{i \in \mathcal{I}_{q,t}} r_{i, t+h}$$

The **IC** at each period and the rolling **ICIR** summarise predictive power:

$$IC_t = \rho_s\!\left(\text{factor}_{i,t},\; r_{i,t+h}\right), \qquad \text{ICIR} = \frac{\mu_{IC}}{\sigma_{IC}}$$

A factor is considered useful if Q5 − Q1 (top minus bottom quintile return) is positive and the ICIR exceeds 0.3.

## Example

```python
import alphalens as al

factor_data = al.utils.get_clean_factor_and_forward_returns(
    factor,           # pd.Series indexed by (date, asset)
    prices,           # pd.DataFrame of daily prices
    quantiles=5,
    periods=(1, 5, 10)
)
al.tears.create_full_tear_sheet(factor_data)
```

A 12-month momentum factor tested on 500 large-cap equities: Q5 − Q1 spread = 0.8\% per month at the 1-month horizon, decaying to 0.3\% at 10 months (IC decay plot shows the signal half-life is ~3 months). Daily turnover in Q5 is 15\%, implying 3× annual transaction cost pressure that must be weighed against the 0.8\% gross edge.

## Remember

Running Alphalens is the step that comes *before* zipline or any event-driven backtest: it tells you whether a factor has predictive power and, critically, at what holding horizon and with what turnover. A factor with ICIR = 0.5 but 50\% daily turnover may be unprofitable after costs; a factor with ICIR = 0.2 but 5\% daily turnover may be highly profitable net. Alphalens surfaces this cost-signal interaction explicitly, preventing quants from spending weeks building a full backtest around a signal that was never going to survive transaction costs.
