# Variational Autoencoder

**Topic:** Computational Finance
**Tags:** variational autoencoder, vae, generative model, latent space, kl divergence, synthetic data
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **variational autoencoder (VAE)** is a generative extension of the standard autoencoder that constrains the latent space to follow a probability distribution — typically $\mathcal{N}(\mathbf{0}, \mathbf{I})$. Instead of encoding $\mathbf{x}$ to a fixed point $\mathbf{z}$, the encoder outputs a mean $\boldsymbol{\mu}$ and variance $\boldsymbol{\sigma}^2$, and $\mathbf{z}$ is sampled from $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\sigma}^2)$. This structured latent space supports interpolation between points and generation of novel, plausible samples.

## Key Formula

**Reparameterisation trick** (enables gradient flow through sampling):

$$\mathbf{z} = \boldsymbol{\mu} + \boldsymbol{\sigma} \odot \boldsymbol{\varepsilon}, \qquad \boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$$

**Evidence lower bound (ELBO)** — the training objective to maximise:

$$\mathcal{L}_{\text{VAE}} = \underbrace{\mathbb{E}[\|\mathbf{x} - \hat{\mathbf{x}}\|^2]}_{\text{reconstruction loss}} - \underbrace{\beta \, D_{\text{KL}}\!\left(\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\sigma}^2) \,\|\, \mathcal{N}(\mathbf{0}, \mathbf{I})\right)}_{\text{regularisation}}$$

The KL term in closed form:

$$D_{\text{KL}} = -\tfrac{1}{2}\sum_{j}\!\left(1 + \log\sigma_j^2 - \mu_j^2 - \sigma_j^2\right)$$

The $\beta$ weight controls the trade-off between reconstruction fidelity and latent space regularity.

## Example

A VAE trained on 10 years of daily macro factor scores (yield curve, credit spreads, equity volatility, commodity indices — 20 features, 2,520 observations) with a 3-dimensional latent space. After training, the latent space organises itself: crisis regimes cluster near $(z_1 \approx 2, z_2 \approx 1)$, QE expansion near the origin. Sampling $\mathbf{z}^* \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ and decoding produces novel synthetic macro scenarios with realistic cross-feature correlations, without repeating any historical date — useful for stress testing when genuine historical crisis episodes are scarce.

## Remember

The VAE's critical advantage over the standard autoencoder for financial applications is the **smooth, continuous latent space**: interpolating between two historical latent codes produces economically coherent intermediate scenarios, not nonsensical outputs. This makes VAEs the preferred tool for **synthetic stress test scenario generation** — regulators require institutions to test portfolios under scenarios beyond the historical record, and a VAE trained on macro factor data can generate plausible but never-observed crisis paths. The $\beta$ parameter must be tuned carefully: too high collapses all market regimes towards the same latent code (over-regularised), too low recovers a standard autoencoder with a discontinuous latent space that cannot generate novel scenarios.
