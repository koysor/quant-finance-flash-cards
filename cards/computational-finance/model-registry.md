# Model Registry

**Topic:** Computational Finance
**Tags:** model versioning, mlops, model governance, model deployment, reproducibility, quantitative research
**Created:** 2026-05-29
**Author:** Claude Sonnet 4.6

---

## Definition

A **model registry** is an MLOps component that stores versioned ML model artefacts — serialised weights, hyperparameters, training data windows, and feature schemas — and controls their progression through a defined lifecycle from development to live deployment. It acts as the single source of truth for which model version is currently in production, providing an auditable, rollback-capable governance layer between research and execution environments.

## Key Formula

Model lifecycle stages with semantic versioning:

```
Research environment
  │
  │  mlflow.register_model("runs:/abc123/ridge_signal", "equity-alpha-ridge")
  ▼
┌─────────────────────────────────────────────────┐
│  Registry: equity-alpha-ridge                   │
│                                                 │
│  Version 1  │  Stage: Archived  │ alpha=0.01    │
│  Version 2  │  Stage: Staging   │ alpha=0.1     │  ← out-of-sample testing
│  Version 3  │  Stage: Production│ alpha=1.0     │  ← live execution
└─────────────────────────────────────────────────┘
  │
  │  client.transition_model_version_stage(
  │      name="equity-alpha-ridge", version=2,
  │      stage="Production"
  │  )
  ▼
Live execution engine
```

Each version is immutable once registered; promotion is an explicit, logged action with a timestamp and the approving user's identity.

## Example

A quant team builds a Ridge regression to forecast daily returns for FTSE 100 constituents using three factors: 20-day momentum, volatility ratio, and price-to-book. After internal backtesting on 2018–2023 data, they register the model:

```python
with mlflow.start_run() as run:
    mlflow.log_params({"alpha": 1.0, "train_end": "2023-12-31",
                       "features": ["momentum_20d", "vol_ratio", "pb"]})
    mlflow.sklearn.log_model(ridge_model, "ridge_signal")

mlflow.register_model(f"runs:/{run.info.run_id}/ridge_signal",
                      "equity-alpha-ridge")
# Registers as Version 3, Stage: None
```

The model is promoted to `Staging` and run in shadow mode alongside the live model for six months of out-of-sample testing on 2024 equity data. After the risk committee reviews the out-of-sample information coefficient (IC = 0.041 vs 0.029 for the incumbent), it is promoted to `Production`. Version 2 moves to `Archived`. The registry records every stage transition with a timestamp and reviewer identity, satisfying the firm's SR 11-7 model governance obligations.

## Remember

In quantitative finance, the gap between backtesting and live deployment is where most model risk originates. A model registry closes that gap by guaranteeing that the exact artefact — including the regularisation strength, the training data cut-off, and the feature normalisation parameters — that passed out-of-sample validation is the same binary deployed to the execution engine. Without a registry, a subtle change (retraining on a longer window, adjusting a preprocessing step) can silently alter live behaviour without any audit trail, a form of **silent model drift** that is invisible until a drawdown or a regulatory review. The staged promotion workflow (Staging → Production) also enforces a human governance gate, ensuring no experimental model reaches live capital allocation without documented approval.
