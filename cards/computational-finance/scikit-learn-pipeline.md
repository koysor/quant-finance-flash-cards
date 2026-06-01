# Scikit-learn Pipeline

**Topic:** Computational Finance
**Tags:** pipeline, preprocessing, scikit-learn, look-ahead bias, cross-validation, feature scaling
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

A **scikit-learn Pipeline** chains a sequence of transformers followed by a final estimator into a single object that ensures every preprocessing step is fitted only on training data — preventing look-ahead bias when used inside cross-validation.

## Key Formula

A Pipeline with $n$ preprocessing steps implements the composition:

$$\hat{y} = \text{estimator}\!\left(T_n\!\left(\cdots T_2\!\left(T_1(X)\right)\right)\right)$$

where each $T_i$ is a transformer. During `cross_val_score(pipe, X, y, cv=cv)`, for each fold $k$:

$$T_i^{(k)} = T_i.\text{fit}(X_{\text{train}}^{(k)}), \qquad \tilde{X}_{\text{test}}^{(k)} = T_i^{(k)}.\text{transform}(X_{\text{test}}^{(k)})$$

Each transformer is re-fitted from scratch on $X_{\text{train}}^{(k)}$ alone, so no test-fold statistics (mean, median, IQR) flow back into the model.

## Example

A credit model uses this pipeline:

```
Pipeline([
    ('preprocess', ColumnTransformer([
        ('scale', RobustScaler(), numeric_cols),
        ('encode', OneHotEncoder(), cat_cols)
    ])),
    ('model', GradientBoostingClassifier())
])
```

When `cross_val_score` runs 5-fold CV, the `RobustScaler` fits its median and IQR on training folds 1–4 only, then scales fold 5 using those statistics. Without a Pipeline, fitting the scaler on all 5 folds first would embed fold-5 statistics into the training transformation — a classic look-ahead bias.

## Remember

In quantitative finance, look-ahead bias is the single most damaging modelling error: a backtest contaminated by future information looks profitable but collapses on live deployment. The Pipeline is the technical mechanism that enforces the discipline of fitting transformers only on past data. It also prevents a common mistake when scaling features for a live strategy: fitting the scaler on historical data and applying it to new arrivals using `.transform()` alone (not `.fit_transform()`) ensures that live scaling uses the same distribution parameters as the backtest, avoiding a silent regime shift in the feature space on the first day of trading.
