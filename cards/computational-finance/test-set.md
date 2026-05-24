# Test Set

**Topic:** Computational Finance
**Tags:** test set, holdout set, out-of-sample, model evaluation, backtest overfitting, multiple comparisons
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

The **test set** (holdout set) is the portion of data reserved exclusively for final model evaluation after all training and hyperparameter decisions are complete. It must be examined only once: re-using the same test set to compare multiple models is equivalent to performing covert hyperparameter tuning on it, inflating apparent performance.

## Key Formula

**Estimated generalisation error** on the test set $\mathcal{D}_\text{test}$ of size $m$:

$$\hat{\varepsilon}_\text{test} = \frac{1}{m} \sum_{i \in \mathcal{D}_\text{test}} \mathcal{L}\!\left(y_i,\; f(\mathbf{x}_i;\,\hat{\boldsymbol{\theta}})\right)$$

**Multiple-comparison inflation:** if $K$ models are evaluated against the same test set and the best is selected, the expected maximum test score inflates approximately as $\mathbb{E}[\max_k S_k] \approx \mu + \sigma\,\Phi^{-1}\!\left(\tfrac{K}{K+1}\right)$, meaning performance is overstated even without explicit data leakage.

## Example

A credit default model is trained on 2015–2022 loan data, tuned on a 2022–2023 validation set, then evaluated once on 2023–2024 holdout data: test AUC = 0.81. If instead a team evaluated 20 candidate models against this same holdout period and reported the best AUC of 0.88, the reported figure is misleading — the holdout has effectively become a second validation set.

## Remember

In systematic trading the test set is the **out-of-sample period**: historical dates the strategy never touched during development. A large gap between backtest (in-sample) Sharpe and out-of-sample Sharpe is the most common failure mode in quantitative finance — often caused not by deliberate cheating but by implicitly evaluating dozens of parameter configurations against the same out-of-sample window. The discipline of reserving and touching the test set only once is what separates credible research from backtest overfitting.
