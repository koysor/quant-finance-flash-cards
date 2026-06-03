# Feature Importance: Gain

**Topic:** Computational Finance
**Tags:** feature importance, gain, xgboost, gradient boosting, tree models, explainability
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Gain** is XGBoost's native feature importance metric: for each feature, it accumulates the total reduction in the training objective achieved by all splits that used that feature, averaged over the number of trees. A split with high Gain means the feature sharply reduced the loss at that node — high-Gain features are the ones the model leans on most to fit the data.

## Key Formula

When XGBoost evaluates a candidate split of node $t$ on feature $j$ into left child $L$ and right child $R$, the split Gain is:

$$\text{Gain}(j, t) = \frac{1}{2}\!\left[\frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda}\right] - \gamma$$

where $G_L = \sum_{i \in L} g_i$ and $H_L = \sum_{i \in L} h_i$ are the sums of first- and second-order loss gradients over the left-child samples (analogously for $R$), $\lambda$ is the $\ell_2$ leaf-weight regularisation, and $\gamma$ is the minimum-gain threshold that prunes trivial splits.

Feature importance by Gain is then:

$$\text{Importance}_j^{\text{Gain}} = \frac{1}{M}\sum_{m=1}^{M}\sum_{\substack{s \,:\, \text{feature}(s)=j \\ s \in \text{tree } m}} \text{Gain}(j, s)$$

the mean per-tree total Gain attributable to feature $j$ across all $M$ trees.

## Example

An XGBoost credit-default model trained on 20 features across 300 trees. Calling `model.get_score(importance_type='gain')` returns (partial):

| Feature | Gain |
|---|---|
| debt\_to\_income | 1 842 |
| utilisation\_rate | 1 104 |
| months\_since\_delinquency | 673 |
| num\_open\_accounts | 89 |

Debt-to-income achieves 20× the Gain of the account-count feature, indicating it drives the largest objective improvements when chosen for a split. Removing num\_open\_accounts and re-training causes no material change in AUC, confirming it as a low-signal feature.

## Remember

In quantitative finance, Gain-based importance is the fastest signal-ranking tool available: it is computed from the tree structure itself — no retraining, no held-out data — making it ideal for exploratory factor research. However, Gain can be misleading when features have different cardinalities: continuous numerical features (e.g., price-to-book ratio) tend to accumulate more splits — and therefore more total Gain — than binary flags (e.g., index membership), even if their true predictive contribution is similar. For final signal selection before portfolio construction, combine Gain rankings with permutation importance on held-out data to control for this bias.
