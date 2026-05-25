# mutual_info_classif

**Topic:** Computational Finance
**Tags:** feature selection, mutual information, filter methods, scikit-learn, classification, non-linear
**Created:** 2026-05-24
**Author:** Claude Sonnet 4.6

---

## Definition

`mutual_info_classif` is a scikit-learn function (`sklearn.feature_selection`) that estimates the mutual information between each continuous or categorical feature and a discrete classification target. Unlike correlation, mutual information captures non-linear dependencies, making it a model-agnostic filter that scores features without fitting any classifier.

## Key Formula

Mutual information between feature $X_j$ and target $Y$ is:

$$I(X_j;\, Y) = H(Y) - H(Y \mid X_j)$$

where $H(Y) = -\sum_k p_k \log p_k$ is the entropy of the target and $H(Y \mid X_j)$ is the remaining uncertainty after observing $X_j$. For continuous features, scikit-learn estimates $I$ using the $k$-nearest-neighbours entropy estimator (Kraskov–Stögbauer–Grassberger):

$$\hat{I}(X_j;\, Y) \approx \psi(k) - \langle \psi(n_{x,i}) \rangle + \langle \psi(n_{y,i}) \rangle + \psi(N)$$

where $\psi$ is the digamma function and $n_{x,i}$, $n_{y,i}$ count neighbours within the ball radius set by the $k$-th neighbour. A score of 0 means the feature and target are independent; higher scores indicate stronger dependence.

## Example

Credit default classification: 20 candidate features including LTV, income, debt-to-income, postcode, and months in employment.

```python
from sklearn.feature_selection import mutual_info_classif
scores = mutual_info_classif(X_train, y_train, random_state=42)
```

| Feature | MI score | Pearson |r|| Verdict |
|---|---|---|---|
| Debt-to-income | 0.31 | 0.28 | Predictive (linear) |
| LTV | 0.24 | 0.04 | Predictive (non-linear) |
| Income | 0.19 | 0.17 | Predictive |
| Postcode | 0.37 | 0.01 | High MI, low corr — non-linear |
| Gender | 0.01 | 0.01 | Non-informative |

LTV and Postcode are captured by MI but missed by Pearson — a key advantage of mutual information over linear correlation screens.

## Remember

In quantitative credit and fraud models, many predictive relationships are non-linear — for example, LTV ratio predicts default sharply above 80% but is flat below it. `mutual_info_classif` surfaces these thresholded, stepwise, or interaction-driven relationships that Pearson correlation would score near zero. It is best used as a cheap filter-stage screen to rank candidates before a wrapper method (recursive feature elimination) or embedded method (LASSO), consistent with the two-stage pipeline used in systematic factor research.
