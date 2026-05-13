# Beta-VAE

**Topic:** Computational Finance
**Tags:** beta-vae, disentangled representation, variational autoencoder, latent space, factor model, generative model
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Beta-VAE** is a variant of the variational autoencoder that multiplies the KL regularisation term by a scalar $\beta > 1$, encouraging the learned latent variables to be **statistically independent** (disentangled). Each latent dimension then captures a separate, interpretable factor of variation in the data rather than a mixture of correlated features.

## Key Formula

**Beta-VAE training objective** — maximise the modified ELBO:

$$\mathcal{L}_{\beta} = \mathbb{E}\!\left[\|\mathbf{x} - \hat{\mathbf{x}}\|^2\right] - \beta \, D_{\text{KL}}\!\left(\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\sigma}^2) \,\|\, \mathcal{N}(\mathbf{0}, \mathbf{I})\right), \qquad \beta > 1$$

**Disentanglement trade-off:**

| $\beta$ | Reconstruction | Disentanglement |
|---|---|---|
| $1$ | Faithful (standard VAE) | Not enforced |
| $4$–$10$ | Slightly blurred | Moderate disentanglement |
| $> 10$ | Poor reconstruction | Strong disentanglement |

Increasing $\beta$ tightens the posterior towards $\mathcal{N}(\mathbf{0}, \mathbf{I})$, forcing the model to use fewer, more independent latent dimensions to explain the data.

## Example

A Beta-VAE ($\beta = 6$) trained on 10 years of daily macro factor scores (yield curve slope, credit spreads, equity implied vol, USD index, commodity prices — 20 features). After training, 3 of the 10 latent dimensions account for $> 95\%$ of reconstructed variance, and each is interpretable: $z_1$ tracks risk sentiment (loads on VIX and credit spreads), $z_2$ tracks monetary policy stance (loads on yield curve and real rates), $z_3$ tracks commodity/EM conditions. A standard VAE ($\beta = 1$) mixes all three into every latent dimension, making interpretation impossible.

## Remember

In quantitative finance, disentanglement matters because a Beta-VAE with interpretable latent dimensions allows a portfolio manager to perform **targeted stress testing**: holding $z_2$ fixed and varying $z_1$ simulates a risk-off shock in a stable rate environment — a scenario impossible to construct by simply replaying historical dates. With a standard VAE, latent dimensions are correlated and scenario navigation is opaque. The cost of disentanglement is reconstruction fidelity: Beta-VAE scenarios look smoother and less sharp than the historical data. Choosing $\beta$ is a calibration decision between the faithfulness of the reconstructed scenarios and the clarity of the latent factor structure.
