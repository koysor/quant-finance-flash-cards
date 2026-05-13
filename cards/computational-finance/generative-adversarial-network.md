# Generative Adversarial Network

**Topic:** Computational Finance
**Tags:** gan, generative model, discriminator, generator, synthetic data, minimax game
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **generative adversarial network (GAN)** is an architecture in which two neural networks — a **generator** $G$ and a **discriminator** $D$ — are trained simultaneously in an adversarial game. $G$ learns to produce synthetic samples indistinguishable from real data; $D$ learns to distinguish real from synthetic. Equilibrium is reached when $G$ produces samples so realistic that $D$ can do no better than random guessing.

## Key Formula

**Minimax objective** — $G$ minimises, $D$ maximises:

$$\min_G \max_D \; \mathbb{E}_{\mathbf{x} \sim p_{\text{data}}}[\log D(\mathbf{x})] + \mathbb{E}_{\mathbf{z} \sim p_{\mathbf{z}}}[\log(1 - D(G(\mathbf{z})))]$$

where $\mathbf{z}$ is random noise sampled from a prior (typically $\mathcal{N}(\mathbf{0}, \mathbf{I})$) and $G(\mathbf{z})$ is a synthetic sample.

**Training loop:**
1. Update $D$: maximise $\log D(\mathbf{x}) + \log(1 - D(G(\mathbf{z})))$
2. Update $G$: minimise $\log(1 - D(G(\mathbf{z})))$, equivalently maximise $\log D(G(\mathbf{z}))$

**Theoretical equilibrium**: $p_G = p_{\text{data}}$ and $D(\mathbf{x}) = \tfrac{1}{2}$ everywhere.

## Example

A GAN trained on 10 years of daily equity return vectors (500 stocks). The generator maps 50-dimensional noise vectors to 500-dimensional synthetic return days. After 200 epochs: (1) the synthetic return distribution matches the real distribution's fat tails and sector correlations; (2) the discriminator accuracy falls from 98% at epoch 1 to 53% at epoch 200 — near-random, confirming that synthetic days are statistically indistinguishable from real ones. The synthetic dataset doubles the training set for a regime classification model, improving out-of-sample F1 from 0.71 to 0.79.

## Remember

The primary use of GANs in quantitative finance is **scenario augmentation for rare events**: historical market crashes are scarce (GFC, COVID crash, Black Monday — perhaps 20–50 days each), but a GAN trained on those episodes can generate thousands of synthetic crisis-period return vectors with realistic cross-asset correlation structure. This directly addresses the class imbalance problem in credit default and fraud detection models. The key risk is **mode collapse**: the generator learns to produce only a few realistic samples rather than the full diversity of the real distribution. In practice, Wasserstein GANs (WGAN) are preferred over vanilla GANs because the Wasserstein-1 loss provides a stable, informative gradient even when the generator and real distributions have little overlap early in training.
