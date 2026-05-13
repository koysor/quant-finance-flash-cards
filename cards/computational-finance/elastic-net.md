# ElasticNet

**Topic:** Computational Finance
**Tags:** elastic net, regularisation, lasso, ridge, l1, l2, sparse regression
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**ElasticNet** regularisation combines the $\ell_1$ (LASSO) and $\ell_2$ (Ridge) penalties into a single convex penalty, controlled by a mixing parameter $\alpha \in [0,1]$. It achieves both automatic feature selection (from LASSO) and grouped selection of correlated variables (from Ridge), making it the most flexible linear regulariser.

## Key Formula

$$J(\mathbf{w}) = \frac{1}{N}\sum_{i=1}^{N}(y_i - \hat{y}_i)^2 + \lambda\!\left[\alpha \sum_{j=1}^{p}|w_j| + \frac{1-\alpha}{2}\sum_{j=1}^{p}w_j^2\right]$$

| $\alpha$ | Penalty | Behaviour |
|---|---|---|
| 1 | Pure $\ell_1$ | LASSO: sparse, selects one from a correlated group |
| 0 | Pure $\ell_2$ | Ridge: shrinks all, keeps correlated group together |
| $(0,1)$ | Mixed | Selects groups of correlated features with shrinkage |

Both $\lambda$ (overall strength) and $\alpha$ (mixing ratio) are tuned by cross-validation.

## Example

A factor model uses 5 correlated momentum signals (1-month, 3-month, 6-month, 9-month, 12-month lookback). LASSO arbitrarily zeroes four of them, picking one lookback by chance. Ridge keeps all five with small weights. ElasticNet with $\alpha = 0.5$ retains the whole momentum group (like Ridge) but still zeroes genuinely uninformative features from other categories — capturing the full momentum factor without redundant signals.

## Remember

ElasticNet is the default regulariser in quantitative finance when factor signals arrive in correlated clusters, which is common with alternative data (multiple sentiment scores, several satellite-imagery metrics). Pure LASSO would discard all-but-one arbitrarily from each cluster — a coin flip masquerading as model selection. ElasticNet's $\alpha$ dial lets practitioners choose the right balance between a sparse model and one that fairly represents each feature cluster.
