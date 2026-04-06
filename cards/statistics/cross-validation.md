# Cross-Validation

**Topic:** Statistics
**Tags:** cross-validation, k-fold, overfitting, model selection, out-of-sample, generalisation
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Cross-validation** is a statistical technique for estimating out-of-sample model performance by repeatedly splitting the data into training and test subsets, fitting the model on the training portion, and evaluating it on the held-out test portion. The most common variant is **$k$-fold cross-validation**, which partitions the data into $k$ equal folds and rotates the test fold across all $k$ positions.

## Key Formula

**$k$-fold CV error:**

$$\text{CV}_k = \frac{1}{k}\sum_{i=1}^{k} \mathcal{L}\!\left(\hat{f}^{(-i)}, \mathcal{D}_i\right)$$

where $\hat{f}^{(-i)}$ is the model fitted on all folds except fold $i$, and $\mathcal{D}_i$ is the held-out test fold.

**Train/test split** (special case $k = n$: leave-one-out CV):

$$\text{LOO-CV} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_{-i})^2$$

The **generalisation gap** = training error $-$ CV error measures overfitting.

## Example

A credit analyst trains a logistic regression on 1,000 loan records using 5-fold CV ($k = 5$).

Each fold uses 800 records for training and 200 for testing, cycling through all 5 partitions. The 5 test AUC scores are: 0.82, 0.85, 0.81, 0.84, 0.83.

$$\text{CV}_5\text{ AUC} = \frac{0.82 + 0.85 + 0.81 + 0.84 + 0.83}{5} = 0.830$$

This is the unbiased estimate of how well the model predicts defaults on unseen applications.

## Remember

In quantitative finance, cross-validation is used to **select hyperparameters** (e.g. the regularisation strength $\lambda$ in Ridge/LASSO) and to **compare models** without look-ahead bias. A critical issue in financial data is **time-series structure**: standard $k$-fold shuffles past and future data, introducing future information into the training set. **Walk-forward validation** (training only on past data, testing on the next window) is the correct financial analogue — the CV error from a walk-forward test is the only reliable estimate of live trading performance for a predictive alpha model.
