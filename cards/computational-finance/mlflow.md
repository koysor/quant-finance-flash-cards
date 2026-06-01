# MLflow

**Topic:** Computational Finance
**Tags:** experiment tracking, model registry, mlops, reproducibility, model versioning, quantitative research
**Created:** 2026-05-29
**Author:** Claude Sonnet 4.6

---

## Definition

**MLflow** is an open-source MLOps platform that provides four integrated components — **Tracking** (logging parameters, metrics, and artefacts), **Projects** (packaging code for reproducible runs), **Models** (a standard model format), and the **Model Registry** (versioned model lifecycle management) — giving teams a single, self-hosted audit trail from research to deployment. In quantitative finance, MLflow is used to track every factor-model experiment, version trained signal models, and enforce a controlled promotion process from research environment to live trading infrastructure.

## Key Formula

Core MLflow logging pattern for a supervised finance model:

```python
import mlflow
import mlflow.sklearn

with mlflow.start_run(run_name="ridge-equity-signals"):
    mlflow.log_param("alpha", 0.1)
    mlflow.log_param("features", ["momentum_20d", "vol_ratio", "pb_ratio"])
    mlflow.log_param("train_end", "2022-12-31")

    model = train_ridge(X_train, y_train, alpha=0.1)
    train_r2, test_rmse = evaluate(model, X_train, X_test, y_train, y_test)

    mlflow.log_metric("train_r2", train_r2)
    mlflow.log_metric("test_rmse", test_rmse)
    mlflow.sklearn.log_model(model, artifact_path="ridge_model")
```

`mlflow.start_run()` opens a new experiment run; `log_param()` records immutable inputs; `log_metric()` records scalar outputs; `log_model()` serialises and stores the fitted model artefact.

## Example

A quant builds a Ridge regression to forecast daily FTSE 100 constituent returns. She logs five runs to an MLflow tracking server, varying regularisation strength $\alpha \in \{0.001, 0.01, 0.1, 1.0, 10.0\}$. The MLflow UI shows that $\alpha = 0.001$ achieves train $R^2 = 0.74$ but test RMSE of \$0.0041 — a clear overfitting signal. At $\alpha = 1.0$, train $R^2 = 0.38$ and test RMSE drops to \$0.0027, confirming the better-generalising model. She registers the winning model under the name `ftse-ridge-signal`, applies the `Staging` tag, and after live-trading paper tests, promotes it to `Production` via the MLflow Model Registry — giving the trading desk a fully versioned, rollback-capable artefact.

## Remember

In quantitative finance, reproducibility is not optional: regulators, risk committees, and future quants all need to reconstruct exactly how a signal model was built. MLflow addresses three specific failure modes. First, it guards against **look-ahead bias** by logging the exact train/test date window as a parameter at run time, making it auditable. Second, it prevents **data leakage** by recording the full feature list and preprocessing config, so a reviewer can verify that no future information entered the training set. Third, the **Model Registry** enforces a governance gate — a model must be explicitly promoted from `None` → `Staging` → `Production`, preventing an analyst from accidentally deploying an experimental artefact to live execution. Unlike proprietary SaaS tools, MLflow can be self-hosted, which matters for firms with strict data-residency requirements.
