# Supervised Learning

**Topic:** Computational Finance
**Tags:** supervised learning, classification, regression, labelled data, credit scoring, prediction
**Created:** 2026-04-22
**Author:** Claude Sonnet 4.6

---

## Definition

**Supervised learning** is a machine learning paradigm in which an algorithm learns a mapping $f: \mathbf{x} \mapsto y$ from input features $\mathbf{x}$ to a known output $y$ using a labelled training dataset $\{(\mathbf{x}^{(i)}, y^{(i)})\}_{i=1}^{N}$. When $y$ is continuous the task is **regression**; when $y$ is a discrete class label the task is **classification**.

## Key Formula

The general supervised learning objective is to find parameters $\boldsymbol{\theta}$ that minimise the empirical loss over $N$ training examples:

$$\hat{\boldsymbol{\theta}} = \arg\min_{\boldsymbol{\theta}} \frac{1}{N}\sum_{i=1}^{N} \mathcal{L}\!\left(y^{(i)},\, f_{\boldsymbol{\theta}}(\mathbf{x}^{(i)})\right) + \lambda\,\Omega(\boldsymbol{\theta})$$

where $\mathcal{L}$ is the task-specific loss (mean squared error for regression, log-loss for classification) and $\lambda\,\Omega(\boldsymbol{\theta})$ is a regularisation penalty that controls model complexity.

## Example

A bank builds a credit-scoring model with $N = 50{,}000$ labelled loan applications. Each application $\mathbf{x}^{(i)}$ contains five features: credit score, debt-to-income ratio, loan amount, employment length, and number of missed payments. The label $y^{(i)} \in \{0, 1\}$ indicates whether the borrower defaulted within 12 months. A logistic regression is fitted by minimising log-loss; the trained model achieves an AUC of 0.82 on a held-out test set, meaning it correctly ranks 82% of default/non-default pairs.

## Remember

Supervised learning underpins two of the highest-value applications of ML in finance. For **credit scoring**, classification models (logistic regression, gradient-boosted trees) predict probability of default using applicant features — the output feeds directly into Expected Credit Loss = PD × LGD × EAD under IFRS 9. For **price prediction**, regression models forecast asset returns or option prices from market features; a firm's alpha signal is effectively $\hat{y} = f_{\boldsymbol{\theta}}(\mathbf{x})$ where $\mathbf{x}$ encodes momentum, value, and alternative data. The critical distinction from unsupervised or reinforcement learning is the requirement for labelled historical outcomes, making data quality and label construction (e.g. defining "default") as important as model choice.
