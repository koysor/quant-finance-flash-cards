# Scikit-Learn API: Key Classes and Modules

**Topic:** Computational Finance
**Tags:** scikit-learn, python, api, pipeline, model selection, time series split
**Created:** 2026-04-24
**Author:** Claude Sonnet 4.6

---

## Definition

Scikit-Learn organises its API into modules by function: `sklearn.preprocessing` (feature scaling), `sklearn.model_selection` (splitting and cross-validation), `sklearn.pipeline` (chaining steps), `sklearn.linear_model` / `sklearn.ensemble` / `sklearn.svm` (algorithms), and `sklearn.metrics` (evaluation). Every estimator implements the same `fit(X, y)` / `predict(X)` interface, so any algorithm can be swapped into a `Pipeline` without changing surrounding code.

## Key Formula

A **Pipeline** composes transformers $\phi_1, \ldots, \phi_{k-1}$ and a final estimator $f$:

$$\hat{y} = f\!\left(\phi_{k-1}\!\left(\cdots\phi_1(X)\cdots\right)\right)$$

The two most important regularised estimators in `sklearn.linear_model`:

$$\text{Ridge:}\quad \hat{\beta} = \arg\min_{\beta} \left\|y - X\beta\right\|_2^2 + \alpha\|\beta\|_2^2$$

$$\text{Lasso:}\quad \hat{\beta} = \arg\min_{\beta} \left\|y - X\beta\right\|_2^2 + \alpha\|\beta\|_1$$

where $\alpha > 0$ controls regularisation strength and is tuned via `GridSearchCV`.

## Example

**Most-used classes by module:**

| Module | Key Classes | Finance use case |
|--------|------------|-----------------|
| `preprocessing` | `StandardScaler`, `MinMaxScaler` | Normalise factor returns |
| `model_selection` | `TimeSeriesSplit`, `cross_val_score`, `GridSearchCV` | Backtest-aware CV |
| `pipeline` | `Pipeline`, `FeatureUnion` | Prevent data leakage |
| `linear_model` | `Ridge`, `Lasso`, `LogisticRegression` | Factor models, credit scoring |
| `ensemble` | `RandomForestClassifier`, `GradientBoostingRegressor` | Alpha signal generation |
| `metrics` | `roc_auc_score`, `mean_squared_error`, `r2_score` | Model evaluation |
| `decomposition` | `PCA` | Factor extraction |

Full pipeline for classifying next-month return direction:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score, TimeSeriesSplit

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf",    GradientBoostingClassifier(n_estimators=100, max_depth=3)),
])

tscv   = TimeSeriesSplit(n_splits=5)          # respects chronological order
scores = cross_val_score(pipe, X, y, cv=tscv, scoring="roc_auc")
print(f"CV AUC: {scores.mean():.3f}")
```

## Remember

The two most important design choices in this API for quantitative finance are **`TimeSeriesSplit`** and **`Pipeline`**. Standard `KFold` randomly shuffles rows before splitting, allowing future data to enter the training set — an exact analogue of look-ahead bias in backtesting. Replacing `cv=5` with `cv=TimeSeriesSplit(n_splits=5)` ensures each validation fold lies strictly in the future of its training fold, giving a realistic out-of-sample estimate. `Pipeline` prevents preprocessing leakage: a `StandardScaler` fitted outside the pipeline uses the entire dataset's mean and variance, inflating CV scores; inside the pipeline it is refitted on each training fold only. Both mistakes are among the most common causes of overstated backtest performance in published ML-in-finance research.
