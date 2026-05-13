# Representative Vectors

**Topic:** Computational Finance
**Tags:** embeddings, latent space, vector representation, similarity, nlp, dimensionality reduction
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

A **representative vector** (or **embedding**) maps a discrete object — a word, a financial instrument, a market regime — to a dense numeric vector in a low-dimensional latent space, such that objects with similar properties or behaviour are placed geometrically close together. The vector is not a raw observation but a learned or constructed summary of the object's identity.

## Key Formula

An embedding function $\phi$ maps object $o$ from a discrete set to a continuous vector space:

$$\phi: o \mapsto \mathbf{v} \in \mathbb{R}^d$$

**Cosine similarity** measures how alike two representative vectors are:

$$\text{sim}(\mathbf{v}_i, \mathbf{v}_j) = \frac{\mathbf{v}_i \cdot \mathbf{v}_j}{\|\mathbf{v}_i\| \|\mathbf{v}_j\|}$$

Cluster centroid (the representative vector for a group $C_k$ of $n_k$ points):

$$\boldsymbol{\mu}_k = \frac{1}{n_k}\sum_{\mathbf{x} \in C_k} \mathbf{x}$$

**Vector arithmetic** can encode semantic relationships — the classic result for word embeddings:

$$\phi(\text{"king"}) - \phi(\text{"man"}) + \phi(\text{"woman"}) \approx \phi(\text{"queen"})$$

## Example

A quant team trains a Word2Vec model on 10 years of earnings call transcripts. Each word maps to a 100-dimensional vector. Words like "headwinds", "uncertainty", and "challenging" cluster together in the embedding space — high cosine similarity — whilst "record", "growth", and "expansion" form a separate cluster. A sentence's sentiment is summarised by the mean of its word vectors, giving a 100-dimensional **document embedding**.

Two documents with cosine similarity $> 0.85$ are likely to describe similar market conditions. The earnings call from Q3 2008 and Q1 2020 are closest in embedding space: both discuss liquidity stress, credit tightening, and operational disruption.

## Remember

Representative vectors are the backbone of **alternative data NLP pipelines** in quantitative finance. Rather than using raw word counts (sparse, high-dimensional), analysts embed words and sentences into a compact latent space where arithmetic is meaningful:

- **Sentiment direction**: the vector difference $\phi(\text{"beat"}) - \phi(\text{"miss"})$ points in the direction of positive earnings surprise — projecting a document vector onto this direction gives a continuous sentiment score.
- **Asset embeddings**: analogous to word embeddings, assets can be embedded using co-movement patterns; stocks that frequently move together have high cosine similarity, enabling data-driven sector classification without predefined labels.
- **Regime centroids**: k-means on return vectors produces $K$ representative vectors (centroids) — each is the "average" market state for that regime and can be used to classify new days by finding the nearest centroid.

The key insight is that by choosing a good embedding, complex discrete objects become points in a continuous space where standard ML tools (distance metrics, clustering, regression) apply directly.
