# Embargo Period

**Topic:** Computational Finance
**Tags:** cross-validation, look-ahead bias, autocorrelation, financial machine learning, backtesting, time series
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

An **embargo period** is a fixed gap appended immediately after each purged training fold in time series cross-validation, removing a further $h$ observations from the end of the training set to prevent autocorrelated features from carrying information about the test period into the model.

## Key Formula

Let $T_1$ be the start of the test fold. After purging, the embargo additionally removes all training observations in the window $[T_1 - h,\; T_1)$, where $h$ is the embargo length, typically set equal to the label formation horizon $\Delta$ or the feature autocorrelation length. The combined purge-and-embargo constraint removes any training observation $t'$ satisfying:

$$t' > T_1 - \Delta - h$$

The total number of observations dropped near each test boundary is $\Delta + h$. Across $K$ folds the total data loss is approximately $K(\Delta + h)$ observations.

## Example

A portfolio signal uses 5-day forward returns as labels ($\Delta = 5$) and a 10-day moving average as a feature. Test fold begins at day 201. Purging removes days 197–200 (label windows overlap the test). Embargo of $h = 10$ further removes days 191–196, because the moving average for day 196 uses prices from days 187–196, which still share data with the test window. The training set is therefore cut off at day 190.

## Remember

Purging alone is insufficient when features are constructed from windows that extend further back in time than the label horizon. A 20-day momentum signal computed on day $t$ uses prices from $t-19$ to $t$; even if day $t$'s label does not overlap the test period, the feature still carries information correlated with test-period prices. In Lopez de Prado's *Advances in Financial Machine Learning* (2018) purging and embargo are always applied together — skipping the embargo is a common practitioner error that leaves a residual autocorrelation channel open, inflating cross-validation Sharpe ratios even when purging is nominally applied.
