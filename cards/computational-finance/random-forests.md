# Random Forests

**Topic:** Computational Finance
**Tags:** random forest, ensemble, bagging, decision trees, feature importance, alpha signals
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **random forest** is an ensemble model that combines many independently trained decision trees by averaging their predictions (regression) or taking a majority vote (classification). Two sources of randomness reduce variance: **bagging** (each tree is trained on a bootstrap sample of the data) and **feature subsampling** (each split considers only a random subset of $\sqrt{p}$ features from the full $p$ features).

## Key Formula

**Ensemble prediction** (regression):

$$\hat{y} = \frac{1}{B}\sum_{b=1}^{B} T_b(\mathbf{x})$$

where $T_b(\mathbf{x})$ is the prediction of the $b$th tree and $B$ is the number of trees.

**Feature importance** of feature $j$:

$$\text{FI}_j = \frac{1}{B}\sum_{b=1}^{B}\sum_{\text{splits on } j} \Delta G_{b,j}$$

(average reduction in Gini impurity across all splits on feature $j$, across all trees).

**Out-of-bag (OOB) error:** each tree is tested on the ~37% of data not in its bootstrap sample — a free cross-validation estimate.

## Example

A quant trains a random forest ($B = 500$ trees) to predict next-month stock returns using 40 features (momentum, value, quality, size signals). Feature importance reveals the top 5 signals contribute 62% of total information gain; the remaining 35 features are near-zero and can be safely dropped, reducing data costs and look-ahead risk.

OOB $R^2 = 0.04$ — modest but statistically significant, consistent with published academic factor premia.

## Remember

Random forests are the **workhorse ensemble model** in systematic equity research because they handle the "many weak signals, fat-tailed returns" environment better than OLS regression. Their feature importance scores provide a principled way to rank and select alpha factors from a large candidate set — solving the factor zoo problem that plagues empirical asset pricing. Unlike LASSO, which assumes linear factor effects, random forests capture non-linear and interaction effects (e.g. momentum is stronger in low-volatility regimes). The OOB error estimate also sidesteps the look-ahead bias risk that afflicts standard $k$-fold CV on financial time series.
