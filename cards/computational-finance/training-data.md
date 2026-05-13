# Training Data

**Topic:** Computational Finance
**Tags:** training data, data splitting, cross-validation, data leakage, look-ahead bias, non-stationarity
**Created:** 2026-04-22
**Author:** Claude Sonnet 4.6

---

## Definition

Training data is the labelled dataset used to fit a machine learning model — the subset of observations from which the model learns the mapping between input features and target outputs. A well-designed data split holds back validation and test sets so that model performance can be assessed on genuinely unseen data.

## Key Formula

A standard temporal split for a dataset of $n$ ordered observations:

$$\text{Train}: [1,\, \lfloor 0.6n \rfloor], \quad \text{Validation}: [\lfloor 0.6n \rfloor+1,\, \lfloor 0.8n \rfloor], \quad \text{Test}: [\lfloor 0.8n \rfloor+1,\, n]$$

The generalisation error estimated on the test set is:

$$\hat{\varepsilon}_{\text{test}} = \frac{1}{|\mathcal{D}_{\text{test}}|} \sum_{i \in \mathcal{D}_{\text{test}}} \mathcal{L}(y_i,\, \hat{y}_i)$$

where $\mathcal{L}$ is the chosen loss function, $y_i$ the true label, and $\hat{y}_i$ the model prediction.

## Example

Suppose you have 10 years of daily equity returns (approximately 2,500 observations) and wish to train a return-prediction model:

- **Train** (years 1–6, ~1,500 obs.): fit model weights.
- **Validation** (years 7–8, ~500 obs.): select regularisation strength and architecture.
- **Test** (years 9–10, ~500 obs.): report final out-of-sample performance once — never touch again.

If you accidentally include year 9 closing prices in the feature set used to predict year 9 returns, you have introduced **look-ahead bias**: information that was not available at prediction time contaminates the training set, inflating apparent accuracy.

## Remember

In finance, random shuffling before splitting is almost always wrong. Returns exhibit autocorrelation and regime changes (non-stationarity), so a shuffled split leaks future information into training and produces wildly optimistic backtest results. Always split chronologically and, where possible, use walk-forward analysis to simulate live deployment. The scarcity of clean, stationary financial data — a few decades at most — means overfitting to the training set is the norm, not the exception; a healthy gap between train and test performance (the generalisation gap) is the first sign of a credible model.
