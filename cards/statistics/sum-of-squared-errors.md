# Sum of Squared Errors (SSE)

**Topic:** Statistics
**Tags:** sum of squared errors, model comparison, regression, forecast evaluation, residuals
**Created:** 2026-07-07
**Author:** Claude Sonnet 5

---

## Definition

The **sum of squared errors (SSE)**, also called the residual sum of squares, totals the squared difference between each observed value and the value a model predicted for it: $\text{SSE} = \sum_i (y_i - \hat{y}_i)^2$. It is the most basic scalar measure of how badly a model fits a sample, and it is the building block for a wide family of derived statistics — $R^2$, the F-test for regression significance, and ratio-based effectiveness scores that compare two competing models on the same data.

## Key Formula

$$\text{SSE} = \sum_{i=1}^{n} \left(y_i - \hat{y}_i\right)^2$$

where $y_i$ is the observed value and $\hat{y}_i$ is the model's prediction for observation $i$. Two common derived quantities:

$$R^2 = 1 - \frac{\text{SSE}}{\text{SST}}, \qquad \text{SST} = \sum_{i=1}^n (y_i - \bar{y})^2$$

and, for comparing a candidate model against a benchmark on identical data, a proportional-improvement ratio of the same shape as $R^2$:

$$\text{Improvement} = 1 - \frac{\text{SSE}_{\text{candidate}}}{\text{SSE}_{\text{benchmark}}}$$

which is positive when the candidate's errors are smaller than the benchmark's, and negative when the candidate is worse.

## Example

Ten daily forecasts are compared against ten realised values, giving squared errors $\{0.4, 1.2, 0.1, 2.0, 0.3, 0.8, 1.5, 0.2, 0.6, 0.9\}$, summing to $\text{SSE} = 8.0$. A second, benchmark model on the same ten days gives $\text{SSE} = 12.0$. The proportional improvement is $1 - 8.0/12.0 = 0.333$: the candidate model's forecast errors have one-third less squared magnitude than the benchmark's, over this sample.

## Remember

SSE is rarely reported on its own — it is not comparable across datasets of different sizes or scales — but the *ratio* of two SSE values computed on the same data is scale-free and directly interpretable as a percentage improvement. This is the pattern behind $R^2$ (candidate model vs a mean-only benchmark) and behind finance-specific effectiveness scores such as the Gain statistic used to compare a minimum-variance hedge against a Black-Scholes hedge: both are "1 minus a ratio of SSEs" applied to a different pair of competing predictors. Recognising this common structure means any new "does model A beat model B" question in a backtest reduces to the same one-line calculation, once both models' prediction errors have been squared and summed on the identical out-of-sample data.
