# Entropy Minimisation

**Topic:** Computational Finance
**Tags:** entropy, optimisation, cross-entropy, decision tree, portfolio concentration, information gain
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Entropy minimisation** is the principle of choosing model parameters or portfolio weights such that the resulting probability distribution is as concentrated (low-uncertainty) as possible, subject to observed constraints. It appears as the learning objective in decision trees, classification model training, and minimum-entropy portfolio construction.

## Key Formula

**Conditional entropy** minimised at each decision tree split on feature $A$:

$$H(Y \mid A) = \sum_v \frac{|S_v|}{|S|} H(S_v) \quad \Rightarrow \quad \text{choose } A^* = \arg\min_A H(Y \mid A)$$

**Cross-entropy loss** (entropy minimisation as ML training):

$$\mathcal{L}(\boldsymbol{\theta}) = -\frac{1}{N}\sum_{i=1}^{N} y_i \log \hat{p}_i(\boldsymbol{\theta})$$

Minimising cross-entropy is equivalent to minimising the KL divergence between the predicted distribution $\hat{P}$ and the true distribution $P$:

$$D_{\text{KL}}(P \| \hat{P}) = H(P, \hat{P}) - H(P)$$

Since $H(P)$ is constant w.r.t. $\boldsymbol{\theta}$, minimising $\mathcal{L}$ minimises the KL divergence.

**Minimum-entropy portfolio**: given return forecasts, the weights $\mathbf{w}^*$ that minimise $H(\mathbf{w}) = -\sum_i w_i \log w_i$ (discrete entropy of weights) subject to $\sum_i w_i = 1$, $w_i \ge 0$ produce a maximally concentrated portfolio.

## Example

A credit classification model trained with cross-entropy loss on 10,000 loan outcomes. At epoch 0, predictions are uniform: $\hat{p}_i \approx 0.5$ for all loans — high entropy, low confidence. After 50 epochs of gradient descent on $\mathcal{L}$, the model assigns $\hat{p}_i > 0.9$ to clear defaults and $\hat{p}_i < 0.1$ to clear non-defaults: entropy of predictions is low.

Training loss falls from $\mathcal{L} = 0.693$ (log 2, the entropy of a fair coin) to $\mathcal{L} = 0.18$ — the model has extracted signal that concentrates its probability mass.

## Remember

Entropy minimisation has a dual role in quantitative finance:

1. **Training classifiers**: cross-entropy loss is the standard objective for all probabilistic models (logistic regression, neural networks, gradient-boosted trees) used in credit scoring, default prediction, and fraud detection. Minimising cross-entropy forces the model to be confidently right, not just occasionally right — a lower training loss directly corresponds to better-calibrated probability of default (PD) estimates.

2. **Portfolio concentration vs. diversification**: minimum-entropy weights are the *opposite* of the maximum-entropy (most diversified) portfolio. Entropy of weights $H(\mathbf{w}) = -\sum_i w_i \ln w_i$ is minimised at a single-asset portfolio ($H = 0$) and maximised at equal weights ($H = \ln N$). Portfolio managers use entropy as a diversification measure: **maximising** $H(\mathbf{w})$ subject to return and risk constraints constructs a "risk-budget" portfolio, whilst **minimising** it concentrates in high-conviction positions. Entropy of weights thus provides a convex concentration measure that generalises the Herfindahl index.
