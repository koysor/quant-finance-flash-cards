# SMOTE

**Topic:** Computational Finance
**Tags:** smote, class imbalance, oversampling, synthetic data, credit scoring, fraud detection
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**SMOTE (Synthetic Minority Oversampling TEchnique)** addresses class imbalance by generating synthetic minority-class observations rather than simply duplicating existing ones. Each synthetic sample is created by interpolating between a minority-class point and one of its $k$ nearest minority-class neighbours in feature space.

## Key Formula

For minority-class sample $\mathbf{x}_i$ and a randomly chosen neighbour $\mathbf{x}_{nn}$:

$$\mathbf{x}_{\text{synthetic}} = \mathbf{x}_i + \lambda \cdot (\mathbf{x}_{nn} - \mathbf{x}_i), \quad \lambda \sim \text{Uniform}(0, 1)$$

This places the synthetic point along the line segment between $\mathbf{x}_i$ and $\mathbf{x}_{nn}$, in the minority-class region of feature space. SMOTE is applied only to the training set; the test set is never resampled.

**Variants:**
- **ADASYN** — generates more samples near the decision boundary (harder cases)
- **SMOTE-ENN** — combines SMOTE oversampling with Edited Nearest Neighbours undersampling to clean the resulting dataset

## Example

Credit default dataset: 9,500 non-default, 500 default (1:19 imbalance). SMOTE with 10× oversampling generates 4,500 synthetic defaults by interpolating between existing defaulters in (income, debt-ratio, tenure) space — now 9,500 vs 5,000 (roughly 2:1). XGBoost trained on the resampled set achieves Recall 78% vs 45% on the original imbalanced set, at the cost of slightly lower Precision (68% vs 82%). F1 improves from 58% to 73%.

## Remember

Class imbalance is structural in credit and fraud datasets — defaults are rare by design. Without resampling, most classifiers converge to the majority class (the accuracy paradox). SMOTE improves minority-class Recall by giving the model more exposure to the minority manifold during training. The critical constraint is that SMOTE must be applied inside the cross-validation loop (after the train/test split), not to the full dataset — applying it before splitting causes data leakage where synthetic test-set copies appear in training, inflating out-of-sample metrics.
