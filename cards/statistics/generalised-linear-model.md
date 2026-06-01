# Generalised Linear Model

**Topic:** Statistics
**Tags:** glm, link function, logistic regression, maximum likelihood, credit risk, exponential family
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

A **generalised linear model (GLM)** extends ordinary linear regression by allowing the response variable $y$ to follow any distribution in the **exponential family** (Normal, Binomial, Poisson, Gamma, Inverse Gaussian, …) and by connecting the linear predictor $\eta = \mathbf{x}^\top \boldsymbol{\beta}$ to the conditional mean $\mu = \mathbb{E}[y \mid \mathbf{x}]$ through a **link function** $g$:

$$g(\mu) = \eta = \mathbf{x}^\top \boldsymbol{\beta}$$

The three components of a GLM are:

1. **Random component** — the distribution of $y$ (member of the exponential family).
2. **Systematic component** — the linear predictor $\eta = \mathbf{x}^\top \boldsymbol{\beta}$.
3. **Link function** $g$ — a monotone differentiable function mapping $\mu$ to $\eta$.

Canonical link functions by distribution:

| Distribution | Canonical link | Finance use |
|---|---|---|
| Normal | Identity: $g(\mu) = \mu$ | OLS regression |
| Binomial | Logit: $g(\mu) = \ln\!\left(\frac{\mu}{1-\mu}\right)$ | PD modelling |
| Poisson | Log: $g(\mu) = \ln(\mu)$ | Default counts |
| Gamma | Inverse: $g(\mu) = 1/\mu$ | LGD modelling |

Parameters are estimated by **maximum likelihood** via iteratively reweighted least squares (IRLS), a unified algorithm that reduces to standard OLS for the Normal/identity case.

## Key Formula

The log-likelihood for an exponential-family GLM:

$$\ell(\boldsymbol{\beta}) = \sum_{i=1}^{n} \frac{y_i \theta_i - b(\theta_i)}{a(\phi)} + c(y_i, \phi)$$

where $\theta_i$ is the natural parameter (a function of $\mu_i = g^{-1}(\mathbf{x}_i^\top \boldsymbol{\beta})$), $b(\cdot)$ is the cumulant function, $a(\phi)$ is a scale function in the dispersion parameter $\phi$, and $c(\cdot)$ is a normalising term independent of $\boldsymbol{\beta}$.

The **score equations** (set gradient to zero):

$$\sum_{i=1}^{n} \frac{(y_i - \mu_i)}{\text{Var}(\mu_i)} \cdot \frac{\partial \mu_i}{\partial \eta_i} \, \mathbf{x}_i = \mathbf{0}$$

For the Binomial GLM with logit link ($\mu_i = \sigma(\mathbf{x}_i^\top \boldsymbol{\beta})$, where $\sigma$ is the sigmoid function):

$$\ell(\boldsymbol{\beta}) = \sum_{i=1}^{n} \bigl[ y_i \ln \mu_i + (1 - y_i) \ln(1 - \mu_i) \bigr]$$

## Example

A credit risk team models the 12-month probability of default (PD) for 500 retail borrowers using a Binomial GLM with logit link. The predictors are loan-to-income ratio ($x_1$) and credit score ($x_2$):

$$\ln\!\left(\frac{\hat{\mu}}{1 - \hat{\mu}}\right) = -3.2 + 0.8\,x_1 - 0.004\,x_2$$

For a borrower with $x_1 = 2.5$ and $x_2 = 650$:

$$\hat{\eta} = -3.2 + 0.8 \times 2.5 - 0.004 \times 650 = -3.2 + 2.0 - 2.6 = -3.8$$

$$\hat{\mu} = \frac{1}{1 + e^{3.8}} \approx 0.022 \quad (2.2\%\ \text{PD})$$

A coefficient of $0.8$ on the loan-to-income ratio means a one-unit increase multiplies the default odds by $e^{0.8} \approx 2.23$, holding credit score fixed.

## Remember

GLMs are the statistical backbone of **IFRS 9 credit risk models**. Banks use:

- **Binomial GLM (logistic regression)** to estimate the probability of default (PD) — the key input to expected credit loss (ECL) calculations.
- **Gamma GLM** to model loss given default (LGD), whose distribution is strictly positive and right-skewed, making the Normal assumption inappropriate.
- **Poisson GLM** to model default counts in retail portfolios or operational risk event frequencies.

The unified MLE framework means all three models share the same estimation software (e.g. `statsmodels.formula.api.glm` in Python) and the same model-validation toolkit — a significant advantage for regulatory implementation under Basel IV, where consistent model governance across the credit risk suite is mandatory.
