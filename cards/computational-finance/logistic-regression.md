# Logistic Regression

**Topic:** Computational Finance
**Tags:** logistic regression, classification, sigmoid, maximum likelihood, credit scoring, probability of default
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Logistic regression** is a supervised learning model for binary classification. It estimates the probability that an observation belongs to class 1 by applying the **sigmoid function** to a linear combination of input features, mapping any real-valued score to the interval $(0, 1)$.

## Key Formula

**Sigmoid function:**

$$\sigma(z) = \frac{1}{1 + e^{-z}}, \qquad z = \mathbf{w}^\top \mathbf{x} + b$$

**Predicted probability:**

$$\hat{p} = P(Y = 1 \mid \mathbf{x}) = \sigma(\mathbf{w}^\top \mathbf{x} + b)$$

**Log-odds (logit):**

$$\ln\frac{\hat{p}}{1 - \hat{p}} = \mathbf{w}^\top \mathbf{x} + b$$

**Log-loss** (negative log-likelihood, the training objective):

$$\mathcal{L} = -\frac{1}{n}\sum_{i=1}^n \left[y_i \ln\hat{p}_i + (1-y_i)\ln(1-\hat{p}_i)\right]$$

## Example

A bank trains a logistic regression with two features: credit score $x_1$ (standardised) and debt-to-income ratio $x_2$.

With fitted weights $w_1 = -1.2$, $w_2 = 0.8$, $b = -0.5$, for an applicant with $x_1 = 0.5$, $x_2 = 1.0$:

$$z = -1.2(0.5) + 0.8(1.0) - 0.5 = -0.6 - 0.5 + 0.8 = -0.3$$

$$\hat{p} = \sigma(-0.3) = \frac{1}{1 + e^{0.3}} \approx 0.426$$

The model assigns a 42.6% probability of default. Above a threshold (e.g. 50%), the loan is declined.

## Remember

Logistic regression is the **standard model for probability of default (PD)** in credit risk under IFRS 9 and Basel IRB. The output $\hat{p}$ is used directly as the PD in Expected Credit Loss = PD × LGD × EAD. The log-odds interpretation is also important: a one-unit increase in a standardised feature multiplies the default odds by $e^{w_j}$ — a format regulators and credit officers can interpret without statistical training. Unlike neural networks, logistic regression produces interpretable coefficients and satisfies the explainability requirements of SR 11-7 model risk guidance.
