# Huber Loss

**Topic:** Computational Finance
**Tags:** huber loss, robust regression, outliers, fat tails, gradient boosting, loss function
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Huber loss** is a regression loss function that applies squared error for small residuals and linear (absolute) error for large residuals, with a threshold $\delta$ separating the two regimes. It is more robust to outliers than MSE whilst remaining differentiable everywhere — a property that absolute error (MAE) lacks.

## Key Formula

For residual $r = y - \hat{y}$:

$$L_\delta(r) = \begin{cases} \dfrac{1}{2}r^2 & \text{if } |r| \leq \delta \\[6pt] \delta\!\left(|r| - \dfrac{\delta}{2}\right) & \text{if } |r| > \delta \end{cases}$$

| Loss | Small errors | Large errors | Outlier sensitivity |
|---|---|---|---|
| MSE ($\ell_2$) | $r^2$ | $r^2$ | High — outliers dominate |
| MAE ($\ell_1$) | $\|r\|$ | $\|r\|$ | Low — but non-differentiable at 0 |
| **Huber** | $r^2$ | $\delta\|r\|$ | Low with smooth gradient |

## Example

Predicting daily equity returns. Most residuals are ±1%, but fat-tailed distributions produce ±10% residuals on crash days. With $\delta = 2\%$: a residual of 1.5% incurs MSE-style loss $(1.5)^2/2 = 1.125$; a crash-day residual of 10% incurs only $2 \times (10 - 1) = 18$ rather than the MSE penalty of $100/2 = 50$ — the outlier contributes 2.8× less, preserving fit quality for normal days.

## Remember

Financial return distributions have fat tails — a property that makes least-squares (MSE) estimators unreliable because they square large residuals, giving oversized influence to crisis observations. Huber loss is the practitioner's compromise: smooth squared-error behaviour for the bulk of the distribution (good gradient for optimisation), with linear penalties beyond $\delta$ that limit the influence of extreme market events. XGBoost and LightGBM both expose Huber loss as a built-in regression objective, making it straightforward to deploy in gradient-boosted financial forecasting models.
