# Cross-Entropy

**Topic:** Computational Finance
**Tags:** cross-entropy, information theory, kl divergence, loss function, classification, probability
**Created:** 2026-05-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Cross-entropy** $H(p, q)$ measures the average number of bits needed to encode outcomes drawn from the true distribution $p$ using a code optimised for the predicted distribution $q$. It is always at least as large as the true entropy $H(p)$; the excess is the KL divergence $D_{\text{KL}}(p \| q)$.

## Key Formula

$$H(p, q) = -\sum_{k=1}^{K} p_k \log q_k$$

**Decomposition** into irreducible and reducible parts:

$$H(p, q) = H(p) + D_{\text{KL}}(p \| q)$$

where $H(p) = -\sum_k p_k \log p_k$ is the Shannon entropy of the true distribution and $D_{\text{KL}}(p \| q) \geq 0$ is the KL divergence. Minimising cross-entropy over model parameters is therefore equivalent to minimising KL divergence, since $H(p)$ is fixed.

For binary classification ($K = 2$, with $p_1 = y$, $q_1 = \hat{p}$):

$$H(p, q) = -y \log \hat{p} - (1 - y)\log(1 - \hat{p})$$

which is the familiar log-loss.

## Example

A three-state market regime model (bull, bear, sideways) predicts $q = (0.7, 0.2, 0.1)$ for a day where the true outcome is bull ($p = (1, 0, 0)$).

$$H(p, q) = -1 \cdot \log(0.7) - 0 - 0 = -\log(0.7) \approx 0.515 \text{ nats}$$

If the model had predicted $q = (0.9, 0.05, 0.05)$, the cross-entropy falls to $-\log(0.9) \approx 0.105$ nats — rewarding greater confidence in the correct regime. A perfectly confident correct prediction gives $H = 0$.

## Remember

Cross-entropy is the standard training loss for any model that outputs a probability distribution — logistic regression, softmax neural networks, gradient boosted classifiers. In quantitative finance this covers credit default models, market regime classifiers, and earnings-surprise predictors. The decomposition $H(p, q) = H(p) + D_{\text{KL}}(p \| q)$ is practically important: it shows that the irreducible floor $H(p)$ is set by the noise in the data, and the only part the model can improve is $D_{\text{KL}}$. A cross-entropy loss that plateaus during training may indicate the model has already minimised $D_{\text{KL}}$ and is simply sitting on the irreducible $H(p)$ floor.
