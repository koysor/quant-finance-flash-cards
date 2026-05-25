# cross_val_score

**Topic:** Computational Finance
**Tags:** cross-validation, model evaluation, scikit-learn, roc-auc, out-of-sample, model selection
**Created:** 2026-05-24
**Author:** Claude Sonnet 4.6

---

## Definition

`cross_val_score` is a scikit-learn function that evaluates a fixed model on a dataset using cross-validation, returning an array of per-fold scores rather than a single number. It is used when the hyperparameters are already chosen and you need an unbiased estimate of out-of-sample performance — without searching for the best configuration.

## Key Formula

`cross_val_score` computes:

$$s_j = \mathcal{L}\!\left(\hat{f}^{(-j)},\, \mathcal{D}_j\right) \quad \text{for } j = 1, \ldots, k$$

returning the array $[s_1, \ldots, s_k]$. The mean and standard deviation summarise performance and uncertainty:

$$\bar{s} = \frac{1}{k}\sum_{j=1}^{k} s_j \qquad \sigma_s = \sqrt{\frac{1}{k-1}\sum_{j=1}^{k}(s_j - \bar{s})^2}$$

A high $\sigma_s$ relative to $\bar{s}$ indicates the model is sensitive to which period is held out — a warning sign of regime dependence in financial data.

## Example

Evaluating a calibrated logistic regression on a loan default dataset:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, TimeSeriesSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf",    LogisticRegression(C=0.1, penalty="l2")),
])

scores = cross_val_score(
    pipe, X_train, y_train,
    cv=TimeSeriesSplit(n_splits=5),
    scoring="roc_auc"
)
# scores = [0.81, 0.85, 0.79, 0.83, 0.82]
print(f"CV AUC: {scores.mean():.3f} ± {scores.std():.3f}")
# CV AUC: 0.820 ± 0.020
```

The ± 0.020 is small relative to 0.820 — reasonable stability across time periods.

## Remember

The key advantage of `cross_val_score` over a single train/test split is that the per-fold score array reveals **temporal stability** in financial models. If fold scores are 0.85, 0.84, 0.83, 0.48, 0.82, the drop in one fold flags a specific market regime (perhaps the 2020 COVID shock period) where the model broke down — information a single aggregate number would hide. In credit risk modelling, regulators expect a model to be stable across economic cycles; reporting fold-level AUC across a through-the-cycle period (expansion + recession + recovery) is stronger evidence of robustness than a single out-of-sample AUC.
