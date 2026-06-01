# Missing Value Imputation

**Topic:** Computational Finance
**Tags:** imputation, missing data, preprocessing, scikit-learn, knn, look-ahead bias
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**Missing value imputation** is the process of replacing absent entries in a dataset with estimated values so that downstream models can be trained, where the choice of strategy (mean, median, forward-fill, KNN, iterative) determines both the statistical bias introduced and the risk of look-ahead bias in a time-series context.

## Key Formula

**KNN imputation** estimates a missing value $x_{ij}$ (row $i$, feature $j$) as the mean of the same feature across the $k$ nearest non-missing neighbours in feature space:

$$\hat{x}_{ij} = \frac{1}{k}\sum_{l \in \mathcal{N}_k(i)} x_{lj}$$

**MICE (Multiple Imputation by Chained Equations)** iteratively fits a regression for each feature $j$ using all other features as predictors, cycling through missing features until convergence:

$$\hat{x}_{ij}^{(t+1)} = \hat{f}_j\!\left(\mathbf{x}_{i,-j}^{(t)}\right)$$

**Forward-fill** (time series): $\hat{x}_{t} = x_{t-1}$ — propagates the last observed value forward, the correct choice when a missing price means "no trade occurred".

## Example

A daily equity dataset has 2\% of volume observations missing due to public holidays and trading halts. Three strategies compared on a gradient-boosted model's AUC:

| Strategy | AUC | Look-ahead risk |
|---|---|---|
| Mean imputation | 0.71 | Yes (uses full-sample mean) |
| Forward-fill | 0.73 | No (uses only past values) |
| KNN imputation ($k=5$) | 0.75 | Yes (uses all rows) |

The best AUC comes from KNN, but forward-fill is the only method safe to use without careful point-in-time implementation.

## Remember

In financial datasets, missing values are almost never random — they carry information. A missing bid-ask spread often means the instrument was illiquid or halted; a missing earnings figure might mean the company had not yet reported. Imputing with the training-set mean silently assumes the missing value was typical, which is almost always wrong. More critically, any imputation method that uses statistics from the full dataset (mean, KNN, MICE) introduces look-ahead bias if the train/test split is not applied *before* fitting the imputer — only forward-fill and constant imputation are inherently safe in time-series cross-validation without being wrapped in a `Pipeline`.
