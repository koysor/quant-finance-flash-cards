# Permutation Feature Importance

**Topic:** Computational Finance
**Tags:** permutation feature importance, feature selection, model-agnostic, explainability, factor model, overfitting
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Permutation feature importance** measures how much a model's performance degrades when the values of a single feature are randomly shuffled, breaking its relationship with the target whilst leaving everything else unchanged. A large drop in performance indicates a genuinely important feature; no drop indicates the feature is redundant or uninformative.

## Key Formula

For a fitted model with baseline score $S_0 = \mathcal{L}(f, \mathbf{X}, \mathbf{y})$:

$$\text{Importance}_j = S_0 - \frac{1}{K}\sum_{k=1}^{K} \mathcal{L}\!\left(f,\, \mathbf{X}^{(\pi_k, j)},\, \mathbf{y}\right)$$

where $\mathbf{X}^{(\pi_k, j)}$ is the data matrix with column $j$ randomly permuted on the $k$-th repetition. Averaging over $K$ shuffles reduces variance from a single random permutation. A positive importance means the feature contributes; zero or negative means the model performs equally well without it.

## Example

An XGBoost model trained on 30 alpha signals predicts next-month equity returns. Permutation importance on the held-out test set: shuffling the 12-month momentum signal drops Sharpe ratio from 0.65 to 0.41 (importance 0.24); shuffling short interest drops it to 0.62 (importance 0.03); shuffling analyst revision drops it to 0.64 (importance 0.01). Conclusion: momentum is the dominant signal; analyst revision adds negligible independent information and can be dropped.

## Remember

Permutation feature importance is the practitioner's first choice for post-hoc signal ranking in quantitative finance because it is model-agnostic (works identically for XGBoost, Ridge regression, or neural networks), measures importance on held-out data (avoiding in-sample inflation), and is conceptually transparent enough to explain to a risk committee. Crucially, it captures a feature's contribution *after* accounting for all other features — so correlated alpha signals that duplicate existing factors score near zero, directly guiding portfolio-level signal consolidation. Scikit-learn provides `permutation_importance()` as a one-call utility.
