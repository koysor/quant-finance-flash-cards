# BayesSearchCV

**Topic:** Computational Finance
**Tags:** hyperparameter tuning, bayesian optimisation, scikit-optimize, model selection, gaussian process, machine learning
**Created:** 2026-05-24
**Author:** Claude Sonnet 4.6

---

## Definition

`BayesSearchCV` is a class from the `scikit-optimize` library (`skopt`) that provides a drop-in replacement for scikit-learn's `RandomizedSearchCV`, directing hyperparameter trials toward promising regions using a Gaussian Process surrogate model rather than sampling uniformly at random. It uses an acquisition function to balance exploring unknown regions against exploiting configurations already known to be good.

## Key Formula

After $n$ evaluations, the surrogate GP posterior at an untested point $\boldsymbol{\lambda}$ is:

$$f(\boldsymbol{\lambda}) \mid \mathcal{D}_n \sim \mathcal{N}\!\left(\mu_n(\boldsymbol{\lambda}),\; \sigma_n^2(\boldsymbol{\lambda})\right)$$

The next trial point is chosen by maximising the **Expected Improvement (EI)** acquisition function:

$$\boldsymbol{\lambda}_{n+1} = \underset{\boldsymbol{\lambda}}{\arg\max}\;\text{EI}(\boldsymbol{\lambda}) = \underset{\boldsymbol{\lambda}}{\arg\max}\;\mathbb{E}\!\left[\max\!\left(f^* - f(\boldsymbol{\lambda}),\;0\right)\right]$$

where $f^* = \min_{i \leq n} \text{CV}(\boldsymbol{\lambda}_i)$ is the best CV loss observed so far. This steers compute toward configurations where either the mean is good (exploitation) or the uncertainty is high (exploration).

## Example

Tuning an XGBoost credit model — same task as `RandomizedSearchCV` but with fewer trials:

```python
from skopt import BayesSearchCV
from skopt.space import Real, Integer

search_spaces = {
    "learning_rate": Real(0.01, 0.3, prior="log-uniform"),
    "max_depth":     Integer(3, 9),
    "reg_lambda":    Real(0.1, 10, prior="log-uniform"),
    "n_estimators":  Integer(100, 500),
}

search = BayesSearchCV(
    xgb_model, search_spaces,
    n_iter=30,                          # vs 60 for RandomizedSearchCV
    cv=TimeSeriesSplit(n_splits=5),
    scoring="roc_auc", random_state=42
)
search.fit(X_train, y_train)
```

`BayesSearchCV` with `n_iter=30` typically matches `RandomizedSearchCV` with `n_iter=60–100` for the same final AUC, halving compute time by directing trials away from already-explored poor regions.

## Remember

`BayesSearchCV` matters most in quantitative finance when each cross-validation fit is expensive — fine-tuning a recurrent neural network on tick data, or running a walk-forward backtest with 10 years of rebalancing. In these cases, 30 Bayesian trials versus 100 random trials can save hours per model cycle. The practical constraint is that the GP surrogate overhead becomes significant when the hyperparameter space has more than ~10 dimensions; beyond that, `RandomizedSearchCV` or simpler heuristics may outperform. `BayesSearchCV` shares the same `best_params_`, `best_score_`, and `cv_results_` interface as `GridSearchCV` and `RandomizedSearchCV`, so it slots directly into existing scikit-learn pipelines.
