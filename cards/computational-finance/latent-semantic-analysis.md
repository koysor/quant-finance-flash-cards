# Latent Semantic Analysis

**Topic:** Computational Finance
**Tags:** nlp, dimensionality reduction, topic modelling, text mining, svd
**Created:** 2026-05-21
**Author:** Claude Sonnet 4.6

---

## Definition

Latent Semantic Analysis (LSA) compresses a sparse document-term matrix into a dense, low-dimensional representation by applying Truncated Singular Value Decomposition (SVD). The $k$ largest singular values capture the dominant latent topics, discarding noise and synonymy and mapping synonymous terms — such as "earnings" and "profit" — to nearby vectors.

## Key Formula

Given document-term matrix $\mathbf{D} \in \mathbb{R}^{M \times N}$, LSA computes the rank-$k$ approximation:

$$\mathbf{D} \approx \mathbf{U}_k \boldsymbol{\Sigma}_k \mathbf{V}_k^\top$$

where:
- $\mathbf{U}_k \in \mathbb{R}^{M \times k}$ — document embeddings in the $k$-dimensional topic space
- $\boldsymbol{\Sigma}_k \in \mathbb{R}^{k \times k}$ — diagonal matrix of the $k$ largest singular values (topic strengths)
- $\mathbf{V}_k \in \mathbb{R}^{N \times k}$ — term embeddings in the topic space

Typical values are $k \in [50, 300]$.

## Example

A corpus of 10,000 earnings call transcripts with a 20,000-word vocabulary gives $\mathbf{D} \in \mathbb{R}^{10000 \times 20000}$. With $k = 100$, LSA compresses each document to a 100-dimensional vector. Clustering these vectors with K-Means identifies latent themes — "revenue growth", "cost-cutting", "regulatory risk" — without any labelled training data.

## Remember

LSA was one of the first techniques to convert financial documents into continuous vector representations for unsupervised analysis. Its advantage over BoW and TF-IDF is that synonyms map to nearby points because they appear in similar documents. Its limitation — now addressed by Word2Vec and transformer models — is that it builds a static, corpus-wide matrix and cannot adapt to shifting financial vocabulary or capture word-order context.
