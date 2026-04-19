# Log-Loss (Cross-Entropy Loss)

**Topic:** Computational Finance
**Tags:** log-loss, cross-entropy, cost function, logistic regression, MLE, classification
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Log-loss** (also called **binary cross-entropy**) is the cost function used to train logistic regression and other probabilistic classifiers. It measures the divergence between the model's predicted probability and the true binary label, penalising confident wrong predictions far more severely than uncertain ones.

## Key Formula

For $N$ training examples with true labels $y^{(i)} \in \{0,1\}$ and predicted probabilities $\hat{p}^{(i)}$:

$$J(\boldsymbol{\theta}) = -\frac{1}{N}\sum_{i=1}^{N}\!\left[y^{(i)}\ln\hat{p}^{(i)} + (1-y^{(i)})\ln(1-\hat{p}^{(i)})\right]$$

Unlike MSE, this cost function is **convex** when applied to logistic regression, guaranteeing that gradient descent reaches the global minimum.

## Example

A default model predicts $\hat{p} = 0.95$ for a loan that defaults ($y=1$): cost $= -\ln(0.95) \approx 0.05$. For the same loan predicted at $\hat{p} = 0.05$: cost $= -\ln(0.05) \approx 3.0$ — 60× higher. Confident wrong answers are catastrophically expensive.

## Remember

Log-loss is the negative log-likelihood of a Bernoulli model: minimising log-loss is mathematically identical to Maximum Likelihood Estimation for logistic regression. In credit risk, this property means the trained model outputs calibrated default probabilities — the predicted $\hat{p}$ is directly interpretable as the probability of default, making it suitable for pricing credit derivatives and computing expected loss.
