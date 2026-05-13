# Mode Collapse

**Topic:** Computational Finance
**Tags:** mode collapse, gan, generative model, synthetic data, training failure, diversity
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Mode collapse** is the primary failure mode of GAN training: the generator learns to produce only a narrow subset of the target distribution — a few high-scoring samples that reliably fool the discriminator — instead of the full diversity of realistic outputs. In financial applications, a collapsed GAN generates synthetic return paths that all look similar, failing to represent the variety of market regimes (bull, bear, crisis, low-volatility) present in the real data.

## Key Formula

The vanilla GAN objective is:

$$\min_G \max_D \; \mathbb{E}_{\mathbf{x}}[\log D(\mathbf{x})] + \mathbb{E}_{\mathbf{z}}[\log(1 - D(G(\mathbf{z})))]$$

**Why collapse occurs**: if $G$ finds a single output $\mathbf{x}^*$ that maximally fools $D$, the gradient $\nabla_G \log(1 - D(G(\mathbf{z})))$ pushes all $\mathbf{z}$ towards $\mathbf{x}^*$. $D$ then adapts to reject $\mathbf{x}^*$, and $G$ jumps to a new $\mathbf{x}^{**}$ — cycling without covering the full distribution.

**Wasserstein GAN fix** — replace discriminator loss with Wasserstein-1:

$$\min_G \max_{D \in \mathcal{F}} \; \mathbb{E}_{\mathbf{x}}[D(\mathbf{x})] - \mathbb{E}_{\mathbf{z}}[D(G(\mathbf{z}))]$$

where $\mathcal{F}$ is the set of 1-Lipschitz functions. The Wasserstein loss provides a smooth, informative gradient even when distributions are far apart, preventing the generator from cycling between modes.

**Detection metric** — measure diversity of synthetic samples by their pairwise distance standard deviation: collapse → low $\text{std}(\{d(\mathbf{x}_i, \mathbf{x}_j)\})$.

## Example

A vanilla GAN trained to generate 1-day equity return vectors (500 stocks). After 300 epochs: visual inspection of 100 synthetic returns shows 87 nearly identical samples (large-cap growth sell-off pattern), 13 samples (tech rally pattern), and zero representation of crisis, low-volatility, or value-rotation regimes. The GAN has collapsed to 2 modes from a target distribution with 5–6 distinct regimes. Switching to WGAN: after 300 epochs, synthetic samples cover all 6 regime types with proportions matching the historical 10-year frequency.

## Remember

Mode collapse is the key quality risk when using GANs for financial scenario generation and stress testing. A collapsed GAN doubles a training set only on paper — the synthetic samples add no new information because they repeat the same patterns. The practical detection test is simple: compute the pairwise cosine distance matrix of 100 synthetic samples and compare its standard deviation to the same statistic on 100 real held-out samples. A ratio below 0.5 indicates significant collapse. In production, WGAN with gradient penalty (WGAN-GP) is the standard architecture for financial data generation precisely because its Wasserstein loss explicitly prevents the mode-chasing behaviour that collapses vanilla GANs on datasets with rare but important events (market crashes, liquidity crises) that the generator learns to avoid.
