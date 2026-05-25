# StratifiedKFold

**Topic:** Computational Finance
**Tags:** cross-validation, class imbalance, scikit-learn, stratification, classification, model evaluation
**Created:** 2026-05-24
**Author:** Claude Sonnet 4.6

---

## Definition

`StratifiedKFold` is a scikit-learn cross-validation splitter that partitions data into $k$ folds while preserving the class proportion (prevalence) of each class in both the training and test folds. It prevents pathological splits where a rare class is absent from a fold entirely, which would make PR-AUC and F1-score undefined or misleading on that fold.

## Key Formula

For a dataset with class prevalence $p$ (fraction of positive examples), `StratifiedKFold` ensures each fold $j$ satisfies:

$$\frac{|y_j = 1|}{|y_j|} \approx p \quad \text{for all } j = 1, \ldots, k$$

In an unbalanced dataset with $N$ total samples and $N_+ = p \cdot N$ positives, each test fold of size $N/k$ contains approximately $p \cdot N/k$ positives:

$$\text{Expected positives per fold} = \frac{p \cdot N}{k}$$

If $p \cdot N/k < 1$, stratification is impossible and the fold may contain zero positives — a hard lower bound on the usable number of folds.

## Example

Credit default dataset: 10,000 samples, 200 defaults (prevalence $p = 2\%$).

| CV Splitter | Positives per fold (expected) | Risk |
|---|---|---|
| `KFold(n_splits=5)` | ~40 (random, could be 0–80) | Fold may have 0 defaults |
| `StratifiedKFold(n_splits=5)` | Exactly 40 in every fold | AUC/F1 always well-defined |
| `StratifiedKFold(n_splits=200)` | Exactly 1 per fold | Borderline: LOO-CV |

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf, scoring="average_precision")
```

## Remember

In financial classification tasks — credit default, fraud detection, market crash prediction — the positive class is rare by design. Without stratification, standard `KFold` can produce a fold with zero defaults, making F1-score and PR-AUC undefined (division by zero) and making AUC unreliable due to a single-class test set. `StratifiedKFold` is the correct default for any non-temporal classification task with imbalanced classes. For financial time-series data, however, stratification must be abandoned in favour of `TimeSeriesSplit` to avoid look-ahead bias — the two concerns are in tension, and temporal ordering always takes priority when data is sequential.
