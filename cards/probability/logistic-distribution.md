# Logistic Distribution

**Topic:** Probability
**Tags:** logistic distribution, logistic function, sigmoid, logistic regression, credit scoring
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **logistic distribution** is a continuous symmetric distribution with location $\mu$ and scale $s > 0$. Its CDF is the **logistic (sigmoid) function**, which maps the real line to $(0, 1)$ with a characteristic S-shape. The logistic distribution resembles the normal but has heavier tails (excess kurtosis = 1.2). It is the foundation of **logistic regression**, where the probability of a binary outcome is modelled as a logistic CDF.

## Key Formula

**PDF and CDF:**

$$f(x) = \frac{e^{-(x-\mu)/s}}{s\left(1 + e^{-(x-\mu)/s}\right)^2}, \qquad F(x) = \frac{1}{1 + e^{-(x-\mu)/s}} = \sigma\!\left(\frac{x-\mu}{s}\right)$$

**Mean, variance, kurtosis:**

$$\mathbb{E}[X] = \mu, \qquad \text{Var}(X) = \frac{\pi^2 s^2}{3}, \qquad \text{excess kurtosis} = 1.2$$

**Log-odds (logit):** $\text{logit}(p) = \ln\!\left(\frac{p}{1-p}\right) = \frac{x-\mu}{s}$ — the inverse of the logistic CDF.

**Logistic regression model:** $P(Y=1 \mid \mathbf{x}) = \sigma(\boldsymbol{\beta}^\top \mathbf{x}) = \frac{1}{1+e^{-\boldsymbol{\beta}^\top \mathbf{x}}}$

## Example

A credit scoring model for mortgage applications predicts default probability using applicant features. The logistic regression gives:

$$\log\!\left(\frac{p}{1-p}\right) = -3 + 0.5 \times \text{LTV} + 0.8 \times \text{DTI}$$

For LTV = 0.9, DTI = 1.2: log-odds $= -3 + 0.45 + 0.96 = -1.59$, so $p = \sigma(-1.59) \approx 17\%$ default probability.

## Remember

The logistic distribution is the backbone of **credit scoring and binary classification** in finance. Every logistic regression — used for PD models under Basel IRB, application scoring, and default prediction — implicitly assumes errors follow a logistic distribution. The sigmoid function appears throughout machine learning as the activation function in neural network output layers for binary classification. The **log-odds interpretation** is directly used in credit: a one-unit increase in the DTI score increases the log-odds of default by 0.8, which underwriters translate into a multiplicative change in odds ratio $e^{0.8} \approx 2.2$ — the risk doubles with each unit increase.
