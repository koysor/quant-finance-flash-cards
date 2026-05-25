# RandomizedSearchCV

**Topic:** Computational Finance
**Tags:** hyperparameter tuning, random search, cross-validation, scikit-learn, model selection, grid search
**Created:** 2026-05-24
**Author:** Claude Sonnet 4.6

---

## Definition

`RandomizedSearchCV` is a scikit-learn class that searches for the best hyperparameter configuration by sampling a fixed number of candidates from user-specified probability distributions, evaluating each via cross-validation. Unlike exhaustive `GridSearchCV`, it does not evaluate every combination — it trades completeness for efficiency, making it the standard choice when the hyperparameter space is large or continuous.

## Key Formula

For a budget of $n$ trials drawn from a joint distribution $\mathcal{H}$ over the hyperparameter space, the probability that at least one trial lands in the top-$\alpha$ fraction of configurations is:

$$P(\text{at least one in top-}\alpha) = 1 - (1-\alpha)^n$$

For $\alpha = 0.05$ (top 5%) and $n = 60$: $1 - 0.95^{60} \approx 0.953$. So 60 random trials find a near-optimal configuration with 95% probability, regardless of the number of hyperparameters — an improvement not achievable with grid search, which must scale exponentially with the number of dimensions.

The cross-validated score for each sampled configuration $\boldsymbol{\lambda}_i$ is:

$$\text{CV}(\boldsymbol{\lambda}_i) = \frac{1}{k}\sum_{j=1}^{k} \mathcal{L}\!\left(f_{\boldsymbol{\lambda}_i}^{(-j)},\, \mathcal{D}_j\right)$$

The configuration with the best $\text{CV}(\boldsymbol{\lambda}_i)$ is selected and the final model is refit on the full training set.

## Example

Tuning an XGBoost credit default model with 5 hyperparameters:

```python
from scipy.stats import loguniform, randint
from sklearn.model_selection import RandomizedSearchCV, TimeSeriesSplit

param_dist = {
    "learning_rate":    loguniform(0.01, 0.3),
    "max_depth":        randint(3, 10),
    "subsample":        loguniform(0.5, 0.5),
    "reg_lambda":       loguniform(0.1, 10),
    "n_estimators":     randint(100, 500),
}

search = RandomizedSearchCV(
    xgb_model, param_dist,
    n_iter=60, cv=TimeSeriesSplit(n_splits=5),
    scoring="roc_auc", n_jobs=-1, random_state=42
)
search.fit(X_train, y_train)
```

Grid search over a $5^5 = 3{,}125$-point grid would require 3,125 fits; `RandomizedSearchCV` with `n_iter=60` finds a configuration within ~2% of the grid optimum using 60 fits — a 98% reduction in compute.

## Remember

In quantitative credit and fraud models, hyperparameter tuning must use `TimeSeriesSplit` (not standard $k$-fold) as the `cv` argument — standard folds shuffle chronological data, allowing future default outcomes to contaminate the training fold and producing overly optimistic CV AUC estimates. `RandomizedSearchCV` integrates directly with `TimeSeriesSplit`, making it straightforward to combine random search efficiency with temporally sound validation. For even tighter compute budgets (e.g. tuning neural networks on alternative data), `RandomizedSearchCV` can be replaced with `BayesSearchCV` from the `scikit-optimize` library, which uses the same API but directs trials toward promising regions.
