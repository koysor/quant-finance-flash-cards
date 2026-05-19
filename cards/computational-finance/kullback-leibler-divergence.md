# Kullback-Leibler Divergence

**Topic:** Computational Finance
**Tags:** kl divergence, information theory, relative entropy, model risk, cross-entropy, probability
**Created:** 2026-04-26
**Author:** Claude Sonnet 4.6

---

## Definition

The **Kullback-Leibler (KL) divergence** $D_{\text{KL}}(P \| Q)$ measures how much a probability distribution $Q$ diverges from a reference distribution $P$. It quantifies the extra information needed to encode samples from $P$ using a code optimised for $Q$ instead of $P$. It is always non-negative and equals zero if and only if $P = Q$ almost everywhere.

## Key Formula

For discrete distributions:

$$D_{\text{KL}}(P \| Q) = \sum_x p(x) \log \frac{p(x)}{q(x)}$$

For continuous distributions:

$$D_{\text{KL}}(P \| Q) = \int p(x) \log \frac{p(x)}{q(x)} \, dx$$

**Key properties:**

$$D_{\text{KL}}(P \| Q) \geq 0 \quad \text{(Gibbs' inequality)}$$

$$D_{\text{KL}}(P \| Q) \neq D_{\text{KL}}(Q \| P) \quad \text{(not symmetric)}$$

**Relationship to cross-entropy** (the ML training objective):

$$H(P, Q) = H(P) + D_{\text{KL}}(P \| Q)$$

Since $H(P)$ is constant w.r.t. model parameters $\boldsymbol{\theta}$, minimising cross-entropy $H(P, Q_{\boldsymbol{\theta}})$ is equivalent to minimising $D_{\text{KL}}(P \| Q_{\boldsymbol{\theta}})$.

## Example

A risk model calibrated to 2015–2019 data assumes equity returns follow $P = \mathcal{N}(0.08, 0.15^2)$. Post-COVID data suggests the true distribution is $Q = \mathcal{N}(0.04, 0.25^2)$.

$$D_{\text{KL}}(Q \| P) = \frac{1}{2}\left[\frac{\sigma_Q^2}{\sigma_P^2} - 1 - \ln\frac{\sigma_Q^2}{\sigma_P^2} + \frac{(\mu_Q - \mu_P)^2}{\sigma_P^2}\right]$$

$$= \frac{1}{2}\left[\frac{0.0625}{0.0225} - 1 - \ln\frac{0.0625}{0.0225} + \frac{(0.04 - 0.08)^2}{0.0225}\right] \approx 0.49 \text{ nats}$$

A KL divergence of $0.49$ nats signals material model risk: the pre-COVID model is substantially misspecified relative to post-COVID reality, and VaR estimates based on it will be understated.

## Remember

KL divergence has three distinct roles in quantitative finance:

1. **Model risk quantification** — the KL divergence between the physical measure $P$ and a risk-neutral pricing measure $Q$ quantifies the information gap between the real-world and the model's hedging assumptions. Large $D_{\text{KL}}(P \| Q)$ flags model risk: the model is encoding data under the wrong distribution, which manifests as hedging errors and mispriced tail risks.

2. **Measure change (Girsanov's theorem)** — the Radon-Nikodym derivative governing the $P$-to-$Q$ change is directly linked to $D_{\text{KL}}$. Minimum-entropy methods choose the pricing measure closest to $P$ whilst fitting observed prices.

3. **Regularisation in portfolio optimisation** — KL divergence from a reference portfolio (e.g. the market-cap index) is used as a penalty term to prevent overfit concentrated positions, analogously to how L2 regularisation penalises coefficient size in regression.
