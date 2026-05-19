# Cosine Similarity

**Topic:** Computational Finance
**Tags:** word embeddings, nlp, similarity, distance metrics, text mining, linear algebra
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Cosine similarity** measures the cosine of the angle between two vectors, quantifying how similar they are in direction regardless of their magnitude — two vectors pointing the same way score 1, orthogonal vectors score 0, and opposite vectors score −1.

## Key Formula

For vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^d$:

$$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|} = \frac{\displaystyle\sum_{i=1}^d u_i v_i}{\sqrt{\displaystyle\sum_{i=1}^d u_i^2}\;\sqrt{\displaystyle\sum_{i=1}^d v_i^2}}$$

The corresponding **cosine distance** is $d_{\cos} = 1 - \cos\theta \in [0, 2]$, which converts the similarity into a non-negative dissimilarity measure suitable for clustering.

## Example

Two 3-dimensional word vectors from a GloVe model:

$$\mathbf{u} = \underbrace{[0.8,\; 0.3,\; -0.1]}_{\text{"impairment"}}, \qquad \mathbf{v} = \underbrace{[0.7,\; 0.4,\; -0.2]}_{\text{"writedown"}}$$

$$\mathbf{u} \cdot \mathbf{v} = 0.56 + 0.12 + 0.02 = 0.70$$

$$\|\mathbf{u}\| = \sqrt{0.64 + 0.09 + 0.01} = 0.860, \qquad \|\mathbf{v}\| = \sqrt{0.49 + 0.16 + 0.04} = 0.831$$

$$\cos\theta = \frac{0.70}{0.860 \times 0.831} = \frac{0.70}{0.715} \approx 0.979$$

"Impairment" and "writedown" are nearly synonymous in financial filings — cosine similarity 0.979 confirms this. By contrast, computing with $\mathbf{w} = [-0.6, 0.1, 0.8]$ ("growth") gives $\cos\theta \approx -0.61$: semantically opposite.

## Remember

Cosine similarity is the standard metric for comparing word and document embeddings (Word2Vec, GloVe, FinBERT) precisely because it is **magnitude-invariant**: a short 10-K filing and a long one discussing identical risks produce vectors pointing in the same direction, so cosine similarity correctly marks them as similar even though their Euclidean distance is large. This property is exploited in two key quant finance workflows: (1) **nearest-neighbour retrieval** — finding the 10 most similar historical earnings transcripts to a current one before an event-driven trade; (2) **sentiment axis projection** — computing $\cos(\mathbf{d}, \hat{\mathbf{s}})$ where $\hat{\mathbf{s}} = \mathbf{v}(\text{beat}) - \mathbf{v}(\text{miss})$ gives a continuous earnings-surprise score for any document $\mathbf{d}$.
