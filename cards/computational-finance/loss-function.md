# Loss Function

**Topic:** Computational Finance
**Tags:** loss function, surrogate loss, 0-1 loss, convexity, regression loss, classification loss
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

A **loss function** $\mathcal{L}(y, \hat{y})$ quantifies the penalty for predicting $\hat{y}$ when the true value is $y$. It translates the abstract goal of "predict well" into a concrete scalar that optimisation algorithms can minimise. The choice of loss function encodes assumptions about error severity, the output distribution, and what constitutes a costly mistake.

## Key Formula

**0-1 loss** (ideal for classification but non-differentiable):

$$\mathcal{L}_{0\text{-}1}(y, \hat{y}) = \mathbf{1}[\hat{y} \neq y]$$

**Surrogate losses** that upper-bound the 0-1 loss and are convex and differentiable — enabling gradient descent:

| Loss | Formula | Used for |
|---|---|---|
| Log-loss (cross-entropy) | $-y\ln\hat{p} - (1-y)\ln(1-\hat{p})$ | Probability calibration |
| Hinge loss | $\max(0,\; 1 - y\hat{f})$ | SVM classification |
| Squared error | $(\hat{y} - y)^2$ | Regression, Gaussian errors |
| Huber loss | $\begin{cases}\frac{1}{2}(y-\hat{y})^2 & \lvert y-\hat{y}\rvert\leq\delta \\ \delta\lvert y-\hat{y}\rvert-\frac{\delta^2}{2} & \text{otherwise}\end{cases}$ | Regression, fat-tailed errors |

## Example

Predicting whether a stock return will exceed its median next week. The 0-1 loss is the right measure (we care about classification accuracy) but its zero gradient everywhere makes it unoptimisable. Log-loss is used instead: a model predicting $\hat{p} = 0.95$ when $y = 0$ incurs log-loss $-\ln(0.05) \approx 3.0$, far larger than the $-\ln(0.6) \approx 0.5$ penalty for a more cautious $\hat{p} = 0.6$, encouraging calibrated probabilities.

## Remember

In quantitative finance, squared-error loss is often the wrong choice for return prediction because financial returns have fat tails — a single extreme observation dominates the MSE, causing models to over-optimise for rare events at the expense of typical market behaviour. Huber loss reduces this sensitivity by switching to linear penalisation beyond a threshold $\delta$. More fundamentally, prediction loss and trading loss are not the same: a model with low MSE may still lose money if it systematically mispredicts the largest moves, which is why Sharpe-ratio or information-coefficient objectives are used in some systematic strategies — at the cost of non-convexity.
