# GridSearchCV

**Topic:** Computational Finance
**Tags:** hyperparameter tuning, grid search, cross-validation, scikit-learn, model selection, exhaustive search
**Created:** 2026-05-24
**Author:** Claude Sonnet 4.6

---

## Definition

`GridSearchCV` is a scikit-learn class that exhaustively evaluates every combination of hyperparameter values on a predefined discrete grid, scoring each via cross-validation. It guarantees finding the optimum within the grid at the cost of training time that grows multiplicatively with the number of values per hyperparameter.

## Key Formula

For $d$ hyperparameters each with $n$ candidate values, the number of configurations evaluated is:

$$N_{\text{grid}} = n^d$$

Each configuration requires $k$ cross-validation fits, so the total training runs are $k \cdot n^d$. With $d = 5$ hyperparameters and $n = 5$ values each, $N_{\text{grid}} = 3{,}125$ — equivalent to over 15,000 model fits at $k = 5$ folds.

The selected configuration is:

$$\hat{\boldsymbol{\lambda}} = \underset{\boldsymbol{\lambda} \in \Lambda}{\arg\max} \; \text{CV}(\boldsymbol{\lambda}) = \underset{\boldsymbol{\lambda} \in \Lambda}{\arg\max} \; \frac{1}{k}\sum_{j=1}^{k} \mathcal{L}\!\left(f_{\boldsymbol{\lambda}}^{(-j)},\, \mathcal{D}_j\right)$$

where $\Lambda$ is the full Cartesian product of the grid values.

## Example

Tuning a logistic regression credit model over 2 hyperparameters:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit

param_grid = {
    "C":       [0.001, 0.01, 0.1, 1, 10],   # 5 values
    "penalty": ["l1", "l2"],                  # 2 values
}
# 5 × 2 = 10 configurations × 5 folds = 50 total fits

search = GridSearchCV(
    LogisticRegression(solver="saga"),
    param_grid,
    cv=TimeSeriesSplit(n_splits=5),
    scoring="roc_auc", n_jobs=-1
)
search.fit(X_train, y_train)
print(search.best_params_)   # e.g. {'C': 0.1, 'penalty': 'l2'}
print(search.best_score_)    # e.g. 0.814
```

## Remember

`GridSearchCV` is preferable to `RandomizedSearchCV` when the hyperparameter space is small and discrete — for instance, comparing penalty type (L1 vs L2) and a handful of regularisation strengths in a logistic regression credit scorecard. Its exhaustiveness provides a complete map via `cv_results_`, showing how AUC degrades as regularisation is tightened or loosened, which can inform model governance documentation submitted to risk committees. For larger spaces (gradient-boosted trees with 5+ continuous hyperparameters), `RandomizedSearchCV` or `BayesSearchCV` is preferred because the exponential scaling of grid search becomes prohibitive.
