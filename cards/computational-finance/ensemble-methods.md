# Ensemble Methods

**Topic:** Computational Finance
**Tags:** ensemble, bagging, boosting, random forest, variance reduction, model averaging
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Ensemble methods** combine the predictions of multiple individual models to produce a single, more accurate and robust prediction. The two principal strategies are **bagging** (parallel independent learners to reduce variance) and **boosting** (sequential learners that correct each other's errors to reduce bias).

## Key Formula

**Bagging** — average $M$ models trained on bootstrap samples:

$$\hat{y} = \frac{1}{M}\sum_{m=1}^{M} h_m(\mathbf{x})$$

For classification, use majority vote. Variance of the average:

$$\text{Var}\!\left(\bar{h}\right) = \frac{\rho \sigma^2 + (1-\rho)\sigma^2/M}{1} \approx \rho\sigma^2 \quad (\text{for large } M)$$

where $\rho$ is the pairwise correlation between learners — decorrelating the trees reduces variance further.

## Example

Random Forest (bagging): 500 decision trees each trained on a bootstrap sample with random feature subsets. Predictions are averaged. Gradient Boosting (boosting): 300 shallow trees fitted sequentially to residuals, summed with a learning rate of 0.05.

## Remember

In quantitative finance, ensemble methods are favoured over single models for credit scoring, default prediction, and factor signal combination because they are robust to overfitting on any single data pattern. The key insight is that diverse, weakly correlated models combine to a lower-error ensemble — the same principle that motivates portfolio diversification: uncorrelated assets reduce portfolio variance beyond any single asset's contribution.
