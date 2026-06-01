# Weights & Biases

**Topic:** Computational Finance
**Tags:** experiment tracking, hyperparameter logging, model reproducibility, overfitting, backtesting, mlops
**Created:** 2026-05-29
**Author:** Claude Sonnet 4.6

---

## Definition

**Weights & Biases (W&B)** is an experiment tracking platform that automatically logs every ML run's hyperparameters, metrics, model weights, and artefacts to a centralised dashboard, making it possible to compare hundreds of experiments at a glance. In quantitative finance, W&B is used to maintain a reproducible audit trail of alpha signal models, ensuring that every backtest result is tied to an exact set of features, date ranges, and hyperparameter choices.

## Key Formula

Core W&B logging pattern for a supervised finance model:

```python
import wandb

wandb.init(
    project="equity-return-prediction",
    config={"alpha": 0.01, "features": ["momentum", "vol_ratio", "pb"], "train_end": "2022-12-31"},
)

for epoch in range(n_epochs):
    train_r2, test_r2, rmse = train_and_eval(model, X_train, X_test, y_train, y_test)
    wandb.log({"train_r2": train_r2, "test_r2": test_r2, "rmse": rmse, "epoch": epoch})

wandb.finish()
```

`wandb.init()` starts a run and records the config; `wandb.log()` streams metrics per epoch; `wandb.finish()` marks the run complete and persists all artefacts.

## Example

A quant is tuning a Ridge regression to forecast daily NIFTY 50 returns using three factors. She runs five experiments varying the regularisation strength $\alpha \in \{0.001, 0.01, 0.1, 1.0, 10.0\}$. Each run calls:

```python
wandb.init(project="nifty-ridge", config={"alpha": alpha, "train_window": "2018-2023", "features": ["momentum_20d", "vol_ratio", "pb_ratio"]})
wandb.log({"train_r2": 0.41, "test_r2": 0.18, "rmse": 0.0032})
```

The W&B dashboard immediately flags that $\alpha = 0.001$ achieves train $R^2 = 0.73$ but test $R^2 = 0.11$, a classic overfitting signature. The run with $\alpha = 1.0$ yields train $R^2 = 0.39$ and test $R^2 = 0.22$ with RMSE of \$0.0028, confirming that heavier regularisation generalises better.

## Remember

In quantitative finance, experiment tracking is not merely a convenience — it is a defence against invisible bias. Without a tool like W&B, it is easy to inadvertently introduce **look-ahead bias** (e.g. using data beyond `train_end` in a feature calculation) or **data leakage** (e.g. normalising features on the full dataset before splitting). Because W&B records the exact `config` — including date windows, feature lists, and preprocessing choices — at the moment of the run, any such mistake becomes auditable and reproducible. The ability to compare run configs side-by-side also prevents **p-hacking on backtests**: if fifty model variants were tried, the live deployment decision should account for the full search, not just report the single best in-sample result.
