# Validation Set

**Topic:** Computational Finance
**Tags:** validation set, hyperparameter selection, model development, early stopping, cross-validation, out-of-sample
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

The **validation set** is a labelled subset held out during model development to guide hyperparameter selection, architecture choice, and early-stopping decisions. It sits between the training set (used to fit parameters) and the test set (reserved for final evaluation only): unlike the test set, the validation set may be consulted many times — but every consultation slightly contaminates it as a performance estimator.

## Key Formula

Hyperparameter selection on the validation set: given candidates $\Lambda = \{\lambda_1, \lambda_2, \ldots, \lambda_K\}$, choose:

$$\lambda^* = \arg\min_{\lambda \in \Lambda}\; \frac{1}{|\mathcal{D}_\text{val}|} \sum_{i \in \mathcal{D}_\text{val}} \mathcal{L}\!\left(y_i,\; f_\lambda(\mathbf{x}_i)\right)$$

where $f_\lambda$ is the model trained on $\mathcal{D}_\text{train}$ under regularisation $\lambda$. Performance on $\mathcal{D}_\text{val}$ is a biased estimator of true out-of-sample error: it is optimistically biased by the number of configurations $K$ evaluated.

## Example

A LASSO return-prediction model is tuned on five years of daily returns. Training set (years 1–3): fits regression coefficients for each candidate penalty $\lambda \in \{10^{-3}, 10^{-2}, 10^{-1}, 1\}$. Validation set (year 4): $\lambda^* = 10^{-2}$ chosen, achieving the lowest validation MSE. Test set (year 5): model evaluated once with $\lambda^*$. Only the test set score is published as the honest out-of-sample estimate.

## Remember

The validation set is what allows a test set to remain genuinely uncontaminated. In quantitative finance, the most common mistake is conflating the two: a practitioner who iterates signal parameters until an "out-of-sample" period looks good has converted that period into a validation set. Once any model decision is informed by a data window, that window is no longer a test set — it is a validation set. The distinction is not semantic; it determines whether reported performance is a credible estimate of live alpha or an artefact of implicit data mining.
