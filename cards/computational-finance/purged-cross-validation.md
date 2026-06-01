# Purged Cross-Validation

**Topic:** Computational Finance
**Tags:** cross-validation, look-ahead bias, label overlap, financial machine learning, backtesting, overfitting
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**Purged cross-validation** is a variant of $k$-fold cross-validation for financial time series that removes ("purges") training observations whose label formation window overlaps with the test fold, eliminating the information leakage introduced when consecutive samples share overlapping prices or returns.

## Key Formula

For a test fold spanning $[t_1, t_2]$ and labels formed over a look-forward window of length $\Delta$, a training observation at time $t'$ is purged if:

$$t' + \Delta > t_1$$

The purged cross-validation score over $K$ folds is:

$$\text{CV}_{\text{purged}} = \frac{1}{K}\sum_{k=1}^{K} \mathcal{L}\!\left(\hat{f}^{(k)}_{\text{purged}},\, \mathcal{D}^{(k)}_{\text{test}}\right)$$

where $\hat{f}^{(k)}_{\text{purged}}$ is the model trained on the $k$-th fold with overlapping observations removed.

## Example

A classifier predicts whether a 5-day forward return will be positive ($\Delta = 5$ days). Test fold covers trading days 101–120. A training observation at day 97 has label window $[97, 102]$, which overlaps with the test period, so it is purged. Days 96 and earlier are safe. With daily sampling, only the 4 observations immediately before each test fold boundary are removed — a small cost for eliminating systematic contamination.

## Remember

Standard $k$-fold and even simple walk-forward validation miss a subtle look-ahead bias: when labels are built from overlapping windows — 5-day returns, 20-day moving averages, momentum signals — adjacent training and test observations share underlying prices. The training label for day $t$ literally uses the same price data as the test label for day $t+1$. This inflates cross-validation scores in ways that vanish in live trading, producing the characteristic backtest-to-live performance gap. Purged CV was formalised by Marcos Lopez de Prado in *Advances in Financial Machine Learning* (2018) and is the required validation standard for any financial ML model built on rolling-window features.
