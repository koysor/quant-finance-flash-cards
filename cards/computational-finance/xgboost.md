# XGBoost

**Topic:** Computational Finance
**Tags:** xgboost, gradient boosting, decision tree, regularisation, feature importance, financial forecasting
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**XGBoost** (eXtreme Gradient Boosting) is a regularised gradient-boosted tree library that builds an ensemble of decision trees sequentially, each correcting the residuals of its predecessors. It extends vanilla gradient boosting with $\ell_1$/$\ell_2$ regularisation on leaf weights, column (feature) subsampling, and second-order Taylor approximation of the loss — making it faster and more resistant to overfitting on tabular financial data.

## Key Formula

At step $m$, a new tree $f_m$ is fitted to the negative gradient (pseudo-residuals). The objective also penalises tree complexity:

$$\mathcal{L}^{(m)} = \sum_{i=1}^{n} \ell\!\left(y_i,\, \hat{y}_i^{(m-1)} + f_m(\mathbf{x}_i)\right) + \Omega(f_m)$$

$$\Omega(f) = \gamma T + \frac{\lambda}{2}\sum_{j=1}^{T} w_j^2 + \alpha \sum_{j=1}^{T} |w_j|$$

where $T$ is the number of leaves, $w_j$ are leaf weights, $\gamma$ is the minimum gain to split, $\lambda$ is $\ell_2$ regularisation, and $\alpha$ is $\ell_1$ regularisation.

## Example

Predicting next-month cross-sectional equity returns using 40 alpha signals. XGBoost with `colsample_bytree=0.7` (each tree uses a random 70% of features), `max_depth=4`, `reg_lambda=1.0`. Trained with Huber loss (`objective="reg:pseudohubererror"`) to limit influence of return outliers. Feature importance ranks momentum and value signals highest; 200-tree ensemble achieves out-of-sample information coefficient 0.06 versus 0.04 for a Ridge regression baseline.

## Remember

XGBoost is the de facto standard for tabular financial forecasting because it handles the three pathologies endemic to financial data: low signal-to-noise (column subsampling decorrelates trees), fat-tailed return distributions (native Huber/quantile loss support), and correlated features (regularisation limits coefficient instability that would affect linear models). Its built-in feature importance (gain, cover, or SHAP-based) also provides a natural signal-ranking mechanism for factor research — making it both the forecasting model and the signal selection tool in a single step.
