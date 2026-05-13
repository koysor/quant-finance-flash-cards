# Autoencoders

**Topic:** Computational Finance
**Tags:** autoencoder, unsupervised learning, dimensionality reduction, latent space, anomaly detection, neural network
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

An **autoencoder** is an unsupervised neural network that learns a compressed representation of its input by training to reconstruct the input from a low-dimensional **latent code**. The network has an encoder that maps input $\mathbf{x}$ to a bottleneck latent vector $\mathbf{z}$, and a decoder that reconstructs $\hat{\mathbf{x}}$ from $\mathbf{z}$. Reconstruction error is the only training signal — no labels are required.

## Key Formula

**Encoder:** $\mathbf{z} = f_{\boldsymbol{\phi}}(\mathbf{x})$, where $\dim(\mathbf{z}) \ll \dim(\mathbf{x})$

**Decoder:** $\hat{\mathbf{x}} = g_{\boldsymbol{\theta}}(\mathbf{z})$

**Training objective** — minimise mean squared reconstruction error:

$$\mathcal{L} = \frac{1}{N}\sum_{i=1}^{N} \|\mathbf{x}_i - g_{\boldsymbol{\theta}}(f_{\boldsymbol{\phi}}(\mathbf{x}_i))\|^2$$

The bottleneck forces $\mathbf{z}$ to encode only the most essential structure. **Anomaly detection**: a normal observation reconstructs with low error; an anomalous one (the model has never seen its structure) produces high error — providing an unsupervised outlier score.

## Example

An autoencoder trained on 5 years of daily equity return vectors (500 stocks). Encoder compresses 500 → 10 latent dimensions; decoder reconstructs 10 → 500. On normal trading days, reconstruction MSE $\approx 0.0003$. On 15 March 2020 (COVID crash), reconstruction MSE spikes to $0.0041$ — 14× above baseline — because the cross-sectional return pattern (everything falling simultaneously at unusual magnitude) is outside the distribution the autoencoder modelled. This spike flags the day as anomalous with no labelled crash examples required.

## Remember

Autoencoders are the neural network analogue of PCA — PCA finds a linear low-dimensional representation minimising reconstruction error, whilst autoencoders find a non-linear one using deep encoder/decoder networks. In quantitative finance, their primary applications are: (1) **anomaly detection** in market microstructure data (unusual order flow, fat-finger trades, circuit breaker events), (2) **feature learning** for alternative data (learning compact embeddings of satellite images or earnings call audio), and (3) **regime detection** by clustering the latent space $\mathbf{z}$ of market states. The reconstruction error threshold for anomaly flagging must be calibrated to the false-positive cost tolerance of the specific application.
