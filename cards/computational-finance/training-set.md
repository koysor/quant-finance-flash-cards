# Training Set

**Topic:** Computational Finance
**Tags:** training set, empirical risk minimisation, supervised learning, survivorship bias, in-sample, model fitting
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

The **training set** is the labelled subset of data on which model parameters are optimised. The learning algorithm iteratively adjusts parameters to minimise a loss function measured exclusively on training observations — the model never sees validation or test data during this phase.

## Key Formula

**Empirical Risk Minimisation (ERM):** the model parameters $\hat{\boldsymbol{\theta}}$ that minimise average loss over the $n$ training examples:

$$\hat{\boldsymbol{\theta}} = \arg\min_{\boldsymbol{\theta}} \frac{1}{n} \sum_{i=1}^{n} \mathcal{L}\!\left(f(\mathbf{x}_i;\,\boldsymbol{\theta}),\; y_i\right)$$

where $\mathbf{x}_i$ is the feature vector, $y_i$ the label, $f(\cdot;\boldsymbol{\theta})$ the model, and $\mathcal{L}$ the chosen loss (e.g. log-loss for classification, MSE for regression).

## Example

A quant analyst trains a logistic regression to predict next-week positive equity returns. Training set: daily observations from 2015–2019 (approximately 1,250 trading days). The optimiser minimises log-loss on these 1,250 examples, converging to coefficient estimates $\hat{\boldsymbol{\theta}}$. Training log-loss = 0.31. Whether this generalises is unknown until the model is evaluated on held-out data.

## Remember

In quantitative finance, training set quality is chronically damaged by **survivorship bias**: historical equity databases typically include only companies still trading today, silently excluding de-listed and bankrupt firms. A model trained on current S&P 500 constituents learns from a sample that survived — it is implicitly conditioned on success, inflating apparent predictive accuracy before a single out-of-sample day is observed. Always source point-in-time data that includes de-listed constituents when constructing a financial training set.
