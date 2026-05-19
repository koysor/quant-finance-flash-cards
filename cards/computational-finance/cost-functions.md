# Cost Functions

**Topic:** Computational Finance
**Tags:** cost function, loss function, mse, cross-entropy, mle, model calibration
**Created:** 2026-04-22
**Author:** Claude Sonnet 4.6

---

## Definition

A **cost function** (also called a **loss function**) measures how poorly a model's predictions match the training targets. Training a model means choosing the parameters $\boldsymbol{\theta}$ that minimise the cost; the choice of cost function encodes the type of task (regression vs classification) and the assumed probability distribution over errors.

## Key Formula

**Mean Squared Error** — regression, assumes Gaussian residuals:

$$J_{\text{MSE}}(\boldsymbol{\theta}) = \frac{1}{N}\sum_{i=1}^{N}\!\left(\hat{y}^{(i)} - y^{(i)}\right)^2$$

**Cross-entropy (log-loss)** — binary classification, assumes Bernoulli outputs:

$$J_{\text{CE}}(\boldsymbol{\theta}) = -\frac{1}{N}\sum_{i=1}^{N}\!\left[y^{(i)}\ln\hat{p}^{(i)} + (1-y^{(i)})\ln(1-\hat{p}^{(i)})\right]$$

Both are **negative log-likelihoods**: minimising MSE is equivalent to MLE under a Gaussian model; minimising cross-entropy is MLE under a Bernoulli model.

## Example

A quant calibrates a Heston model to 20 market option prices. The cost function is:

$$J(\kappa, \theta, \xi, \rho, v_0) = \sum_{i=1}^{20}\!\left(C_{\text{model}}^{(i)} - C_{\text{mkt}}^{(i)}\right)^2$$

This is MSE on pricing errors — each $(C_{\text{model}}^{(i)} - C_{\text{mkt}}^{(i)})^2$ penalises large mispricings disproportionately. Gradient descent iteratively adjusts all five parameters to minimise $J$. A separate credit team uses cross-entropy to calibrate a default probability model on 5,000 loan outcomes.

## Remember

The cost function is the bridge between statistical theory and numerical optimisation in model calibration. In quantitative finance, MSE is used to calibrate derivative pricing models (Heston, SABR) to market prices, whilst cross-entropy calibrates credit and classification models (default probability, counterparty risk). The MLE connection is practically important: it justifies why the calibrated parameters are statistically consistent and enables confidence-interval construction via the Fisher information matrix.
