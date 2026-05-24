# Empirical Risk Minimisation

**Topic:** Computational Finance
**Tags:** empirical risk minimisation, ERM, statistical learning, expected risk, generalisation, PAC learning
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**Empirical Risk Minimisation (ERM)** is the principle of selecting model parameters by minimising the average loss over the training set as a proxy for the true expected risk over the data-generating distribution. Because the true distribution is unknown, ERM replaces the population expectation with a sample average.

## Key Formula

**True (expected) risk** — unknown, requires knowledge of the joint distribution $P(X,Y)$:

$$R(f) = \mathbb{E}_{(X,Y)\sim P}\!\left[\mathcal{L}\!\left(f(X), Y\right)\right]$$

**Empirical risk** — computable from $n$ training examples:

$$\hat{R}(f) = \frac{1}{n}\sum_{i=1}^{n}\mathcal{L}\!\left(f(\mathbf{x}_i),\; y_i\right)$$

**ERM solution:** $\hat{f} = \arg\min_{f \in \mathcal{F}} \hat{R}(f)$

By the law of large numbers, $\hat{R}(f) \xrightarrow{n\to\infty} R(f)$, so ERM is asymptotically consistent — but with finite training data the gap $R(\hat{f}) - \hat{R}(\hat{f})$ is the generalisation gap.

## Example

A linear return predictor $f(\mathbf{x}) = \boldsymbol{\theta}^\top \mathbf{x}$ is fitted on $n = 1{,}000$ daily observations using MSE loss. Gradient descent minimises $\hat{R}(\boldsymbol{\theta}) = \frac{1}{1000}\sum_{i=1}^{1000}(\boldsymbol{\theta}^\top \mathbf{x}_i - y_i)^2$. The solution $\hat{\boldsymbol{\theta}}$ is the empirical risk minimiser. On a fresh 200-day test set, $\hat{R}_\text{test} = 0.0042$ vs $\hat{R}_\text{train} = 0.0031$: the generalisation gap of 0.0011 reflects finite-sample estimation error.

## Remember

ERM is the theoretical skeleton of all supervised learning, and its failure modes map precisely onto quantitative finance's backtest pathologies. Minimising empirical risk on historical returns does not guarantee low expected risk on future returns, because financial data violates the i.i.d. assumption: returns are autocorrelated, non-stationary, and subject to regime shifts. Regularisation adds a penalty $\Omega(f)$ to the empirical risk to constrain model complexity, shrinking the generalisation gap — this is why L1/L2 regularisation, dropout, and early stopping are not optional in financial ML.
