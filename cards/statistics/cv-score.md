# CV Score

**Topic:** Statistics
**Tags:** cross-validation, model selection, nested cv, bias, hyperparameter tuning, out-of-sample
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **CV score** is the mean performance metric computed across the held-out folds of a cross-validation procedure, used as an estimator of a model's true out-of-sample performance. When hyperparameters are selected by maximising the CV score on the same folds used to report it, the score is **optimistically biased** — it understates the true out-of-sample error because the model configuration was chosen to fit that particular sample of folds. **Nested cross-validation** corrects this by separating the tuning loop (inner CV) from the evaluation loop (outer CV).

## Key Formula

**Standard CV score** (potentially biased when used for both tuning and reporting):

$$\bar{s}_{\text{CV}} = \frac{1}{K}\sum_{k=1}^{K} s_k, \qquad s_k = \mathcal{L}\!\left(\hat{f}_{\boldsymbol{\theta}^*}^{(-k)},\, \mathcal{D}_k\right)$$

where $\boldsymbol{\theta}^*$ was chosen by maximising $\bar{s}_{\text{CV}}$ itself — the same folds both tune and evaluate.

**Nested CV score** (unbiased):

$$\bar{s}_{\text{nested}} = \frac{1}{K_{\text{out}}}\sum_{k=1}^{K_{\text{out}}} \mathcal{L}\!\left(\hat{f}_{\boldsymbol{\theta}^*(k)}^{(-k)},\, \mathcal{D}_k\right)$$

where $\boldsymbol{\theta}^*(k)$ is chosen by an **inner** CV on the training folds of fold $k$ only — the outer fold never touches the tuning process.

## Example

A quant analyst tunes an XGBoost model's regularisation and depth using 5-fold CV on equity signal data, achieving a CV AUC of 0.84. She then reports 0.84 as the model's expected live AUC. A colleague reruns the evaluation using 5-fold outer / 3-fold inner nested CV: the nested CV score is 0.79 — the standard CV score was optimistically biased by 0.05 AUC due to hyperparameter selection overfitting.

In scikit-learn, nested CV is:
```python
from sklearn.model_selection import cross_val_score, GridSearchCV, KFold

inner_cv = KFold(n_splits=3, shuffle=True)
outer_cv = KFold(n_splits=5, shuffle=True)

clf = GridSearchCV(estimator=xgb_pipe, param_grid=param_grid, cv=inner_cv)
nested_scores = cross_val_score(clf, X, y, cv=outer_cv, scoring="roc_auc")
# nested_scores.mean() is the honest out-of-sample estimate
```

## Remember

In quantitative finance, reporting the tuned model's CV score as if it were an unbiased performance estimate is equivalent to backtest overfitting — the strategy looks better in sample than it will perform live. Nested CV is the correct protocol whenever hyperparameter selection and model evaluation share the same data: the inner loop tunes, the outer loop evaluates on data the tuning process never saw. The gap between the standard CV score and the nested CV score directly measures how much the analyst's model selection process overfitted the validation data — a large gap is a red flag that the parameter search space is too wide or the dataset too small.
