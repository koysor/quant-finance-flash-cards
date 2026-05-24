# Data Leakage

**Topic:** Computational Finance
**Tags:** data leakage, target leakage, train-test contamination, feature leakage, preprocessing, backtesting
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**Data leakage** occurs when information from outside the training boundary flows into model inputs or outputs, causing inflated apparent performance that does not persist out-of-sample. It is a superset of look-ahead bias, covering not just temporal leakage but also target leakage (a feature is derived from the label) and preprocessing contamination (scalers or encoders fitted on the full dataset before the train/test split).

## Key Formula

A feature $x_j^{(i)}$ is leaky if it was constructed using information from the future or from the label:

$$\text{Leaky if: } x_j^{(i)} = g\!\left(\ldots,\; y^{(i)},\; \ldots\right) \quad \text{(target leakage)}$$
$$\text{Leaky if: } x_j^{(i)} = g\!\left(\ldots,\; z_t \text{ for some } t > t_i,\; \ldots\right) \quad \text{(temporal leakage)}$$

Preprocessing contamination: fitting a `StandardScaler` on $\mathcal{D}_\text{train} \cup \mathcal{D}_\text{test}$ leaks the test-set mean and variance into normalised training features.

## Example

Predicting next-quarter loan default:

| Feature | Leaky? | Why |
|---|---|---|
| `credit_score_at_origination` | No | Known before lending decision |
| `num_missed_payments_in_default_quarter` | Yes (target leakage) | Determined simultaneously with the default event |
| `scaler_fit_on_full_dataset` | Yes (contamination) | Test mean/variance embedded in training inputs |
| `return_next_week` | Yes (temporal leakage) | Unavailable at prediction time |

## Remember

In quantitative finance, target leakage is the most insidious form because it is rarely deliberate: including a variable that reflects the same event as the label (e.g. credit rating downgrades in the default quarter) can make a useless model appear highly predictive. The correct defence is a strict feature construction timeline — every input must be fixed before the prediction date. The practical test: could a trader have observed this feature value at the point of the decision? If not, the feature is leaky.
