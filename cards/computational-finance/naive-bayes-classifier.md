# Naive Bayes Classifier

**Topic:** Computational Finance
**Tags:** naive bayes, classification, bayes theorem, conditional independence, fraud detection, NLP
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **Naive Bayes Classifier** is a probabilistic supervised learning algorithm that applies Bayes' theorem with the simplifying assumption that all features are conditionally independent given the class label. Despite this strong (often unrealistic) assumption, it performs well in practice and is computationally efficient.

## Key Formula

$$P(C_k \mid \mathbf{x}) \propto P(C_k)\prod_{i=1}^{n} P(x_i \mid C_k)$$

The predicted class is:

$$\hat{y} = \arg\max_{k}\; P(C_k)\prod_{i=1}^{n} P(x_i \mid C_k)$$

## Example

Classify a transaction as fraudulent ($C_1$) or legitimate ($C_0$) using three features: transaction amount, merchant country, and time of day. For each class, estimate $P(x_i \mid C_k)$ from historical data, multiply the three likelihoods together, and pick the class with the higher posterior.

## Remember

In financial compliance and anti-money-laundering systems, Naive Bayes provides a fast, interpretable baseline for alert-scoring. The conditional-independence assumption is analogous to treating risk factors as uncorrelated — incorrect but useful: just as a diagonal covariance matrix simplifies portfolio optimisation, independence simplifies posterior computation without dramatically sacrificing accuracy.
