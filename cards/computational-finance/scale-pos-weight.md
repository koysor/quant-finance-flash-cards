# scale_pos_weight

**Topic:** Computational Finance
**Tags:** xgboost, class imbalance, classification, credit scoring, fraud detection, hyperparameter
**Created:** 2026-05-24
**Author:** Claude Sonnet 4.6

---

## Definition

`scale_pos_weight` is an XGBoost hyperparameter that rescales the gradient and Hessian contributions of positive-class examples during tree building. Setting it above 1 makes the model treat each positive example as though it were worth more observations, which compensates for severe class imbalance without modifying the training data itself.

## Key Formula

The recommended default value is the ratio of negative to positive observations in the training set:

$$\texttt{scale\_pos\_weight} = \frac{N_{\text{neg}}}{N_{\text{pos}}}$$

Internally, XGBoost multiplies the first- and second-order loss gradients $(g_i, h_i)$ for each positive example by this factor before computing optimal leaf weights:

$$w_j^* = -\frac{\sum_{i \in \text{leaf}_j} g_i}{\sum_{i \in \text{leaf}_j} h_i + \lambda}$$

where $\lambda$ is the $\ell_2$ leaf regularisation term. The rescaling raises the gradient magnitude of the minority class, so splits that correctly classify positive examples gain more leaf weight improvement and are therefore preferred during tree construction.

## Example

Credit default dataset: 9,800 non-defaults, 200 defaults. Ratio = 49.

```
scale_pos_weight = 9800 / 200 = 49
```

| Setting | Precision (default) | Recall (default) | F1 |
|---|---|---|---|
| `scale_pos_weight=1` (none) | 0.81 | 0.22 | 0.35 |
| `scale_pos_weight=49` | 0.61 | 0.74 | 0.67 |
| `scale_pos_weight=10` (tuned) | 0.69 | 0.61 | 0.65 |

A tuned value between 1 and the raw ratio often outperforms the exact ratio, so it is treated as a hyperparameter to optimise via cross-validation on F1 or PR-AUC.

## Remember

In financial ML, `scale_pos_weight` is the lowest-cost first response to class imbalance — it requires no data augmentation and no change to the training pipeline, only a single hyperparameter. For credit default or fraud detection where the positive class is rare by design, setting this parameter correctly can recover 30–40 percentage points of minority-class Recall that a default (`=1`) model loses by collapsing to the majority class. It trades Precision for Recall, so the target value should be calibrated to the business cost of a missed default versus a false alarm.
