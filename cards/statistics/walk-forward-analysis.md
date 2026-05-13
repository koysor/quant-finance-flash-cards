# Walk-Forward Analysis

**Topic:** Statistics
**Tags:** backtesting, walk-forward, out-of-sample, overfitting, rolling window, strategy validation
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

Walk-forward analysis is a backtesting methodology that simulates how a strategy would be deployed in practice: the model is repeatedly trained on a historical in-sample window, then tested on the immediately following out-of-sample period, and the window rolls forward. Performance is evaluated only on the out-of-sample segments, preventing look-ahead bias and detecting overfitting.

## Key Formula

For a dataset of $T$ observations with in-sample window $w$ and out-of-sample step $s$:

$$\text{Fold } k: \quad \underbrace{[1,\; w + (k-1)s]}_{\text{in-sample (train)}} \;\Big|\; \underbrace{[w + (k-1)s + 1,\; w + ks]}_{\text{out-of-sample (test)}}$$

For $K = \lfloor(T - w)/s\rfloor$ folds. Two variants exist:

- **Expanding window** — in-sample grows each fold (more data, but older data may be less relevant)
- **Rolling window** — in-sample stays fixed length, slides forward (more stationary, but discards early data)

**Out-of-sample Sharpe** — the key metric:

$$SR_{\text{OOS}} = \frac{\bar{r}_{\text{OOS}}}{\sigma_{\text{OOS}}} \times \sqrt{252}$$

Computed only on the concatenated out-of-sample return segments.

## Example

A momentum strategy is tested on 10 years of daily data (2,520 days). Walk-forward setup: in-sample $= 504$ days (2 years), step $= 63$ days (1 quarter), giving $K = 32$ folds. The strategy achieves:

| Metric | In-sample | Out-of-sample |
|---|---|---|
| Sharpe ratio | 1.8 | 0.6 |
| Win rate | 58% | 51% |
| Max drawdown | −12% | −24% |

The large gap between in-sample and out-of-sample performance — the **Sharpe decay** from 1.8 to 0.6 — reveals that the strategy is overfit. A well-generalising strategy would show modest Sharpe decay (e.g. 1.2 → 0.9).

## Remember

Walk-forward analysis is the practitioner's standard for strategy validation because it mimics the actual deployment environment. The ratio $SR_{\text{OOS}} / SR_{\text{IS}}$ (out-of-sample to in-sample Sharpe) is known as the **deflation ratio** — values below 0.5 indicate severe overfitting. The permutation test can be applied to the out-of-sample returns to confirm that the residual OOS Sharpe is statistically significant and not a lucky streak, combining walk-forward and permutation testing into a robust validation framework.
