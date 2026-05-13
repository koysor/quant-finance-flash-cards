# Contrastive Learning

**Topic:** Computational Finance
**Tags:** contrastive learning, self-supervised learning, representation learning, embeddings, simclr, financial time series
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Contrastive learning** is a self-supervised representation learning framework that trains an encoder by pulling together embeddings of **similar** data points (positive pairs) and pushing apart embeddings of **dissimilar** points (negative pairs) — without requiring labels. The encoder learns a latent space where semantic similarity corresponds to geometric proximity, producing rich representations suitable for downstream tasks.

## Key Formula

**NT-Xent loss** (Normalised Temperature-scaled Cross-Entropy, used in SimCLR):

$$\mathcal{L} = -\frac{1}{2N}\sum_{i=1}^{N} \left[\log \frac{\exp(\text{sim}(\mathbf{z}_i, \mathbf{z}_i^+)/\tau)}{\sum_{j \neq i} \exp(\text{sim}(\mathbf{z}_i, \mathbf{z}_j)/\tau)} + \log \frac{\exp(\text{sim}(\mathbf{z}_i^+, \mathbf{z}_i)/\tau)}{\sum_{j \neq i} \exp(\text{sim}(\mathbf{z}_i^+, \mathbf{z}_j)/\tau)}\right]$$

where $\mathbf{z}_i$ and $\mathbf{z}_i^+$ are embeddings of two augmented views of the same observation (the positive pair), $\tau$ is a temperature hyperparameter, and $\text{sim}(\cdot, \cdot)$ is cosine similarity. All other observations in the batch form the negative pairs.

**Positive pair construction** for financial time series — two windows from the same regime period are a positive pair; windows from different periods are negatives.

## Example

A contrastive encoder trained on 10 years of daily market micro-state vectors (VIX, credit spreads, yield curve slope, equity momentum — 10 features). Positive pairs: two randomly sampled windows from the same calendar quarter. After 100 training epochs, the encoder maps each day to a 16-dimensional embedding. $k$-means ($k = 5$) on the embeddings recovers historically meaningful regimes — pre-GFC expansion, GFC crisis, post-crisis QE, taper tantrum, COVID shock — with no regime labels ever provided. Regime classification accuracy on a held-out test year: 84%, versus 61% for $k$-means on the raw features.

## Remember

Contrastive learning addresses the core label scarcity problem in financial ML: labelled market regime data is expensive and subjective (when exactly did the GFC "start"?), but unlabelled historical price data is abundant. By defining positive pairs as windows from the same market period and using data augmentation (adding noise, random feature masking), a contrastive encoder learns a regime-aware representation without any human annotation. The resulting embeddings are more compact and discriminative than PCA or autoencoder representations for regime classification, because the loss function directly optimises neighbourhood structure rather than reconstruction fidelity. In practice, contrastive pre-training followed by a small fine-tuning step on a handful of labelled regime dates outperforms fully supervised classifiers trained on the limited labelled set.
