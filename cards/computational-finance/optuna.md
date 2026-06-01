# Optuna

**Topic:** Computational Finance
**Tags:** hyperparameter optimisation, bayesian search, tpe, pruning, mlops, model selection
**Created:** 2026-05-29
**Author:** Claude Sonnet 4.6

---

## Definition

Optuna is an open-source Python framework for automated hyperparameter optimisation that uses a **define-by-run** API — the search space is constructed dynamically inside the objective function rather than declared upfront. By default it employs a **Tree-structured Parzen Estimator (TPE)** sampler, which builds probabilistic models of good and bad regions of the search space and focuses trials where improvement is most likely; a built-in **pruner** (e.g. MedianPruner) terminates unpromising trials early based on intermediate evaluation metrics.

## Key Formula

```python
import optuna

def objective(trial):
    alpha = trial.suggest_float("alpha", 1e-3, 10.0, log=True)
    model = Lasso(alpha=alpha)
    model.fit(X_train, y_train)
    return model.score(X_val, y_val)   # maximise out-of-sample R²

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=100)

best_alpha = study.best_params["alpha"]
```

The `log=True` flag samples `alpha` on a log-uniform scale, concentrating proposals near small values where Lasso behaviour changes most rapidly.

## Example

A quant team is fitting a Lasso regression to predict next-week equity returns from a panel of 50 fundamental and technical features. The regularisation parameter `alpha` controls how aggressively the model zeroes out noisy factors. A manual grid search over `{0.001, 0.01, 0.1, 1, 10}` requires re-running five complete walk-forward cross-validations.

Using Optuna with `n_trials=50` and a log-uniform range `[1e-3, 10]`:

- The TPE sampler identifies a promising region around `alpha ≈ 0.03` after roughly 15 trials.
- The MedianPruner halts a further 20 trials early once their interim R² falls below the running median, saving approximately 40 % of compute.
- The best trial achieves out-of-sample R² = 0.12, compared to 0.09 for the best grid-search value, because Optuna explored a denser region of the continuous interval.

## Remember

In quantitative finance, hyperparameter choices — regularisation strength in factor models, lookback windows in momentum strategies, decision-tree depth in credit-scoring models — can each require a full backtest to evaluate. Grid search scales exponentially: searching three parameters over five values each demands 125 backtests. Optuna's TPE-guided search reaches near-optimal parameters in a fraction of that budget, and its pruner discards unpromising parameter combinations after only a few evaluation steps. This makes Optuna particularly valuable when a single evaluation is expensive (e.g. a multi-year vectorised backtest or a Monte Carlo pricer), turning what would be a days-long sweep into an overnight run.
