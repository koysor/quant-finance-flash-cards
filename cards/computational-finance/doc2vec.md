# Doc2Vec

**Topic:** Computational Finance
**Tags:** word embeddings, nlp, document similarity, text mining, alternative data, paragraph vectors
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Doc2Vec** (Paragraph Vectors) is an extension of Word2Vec that learns a fixed-length dense vector representation for an entire document — paragraph, article, or annual report — by training a shallow neural network that uses both word context vectors and a unique trainable document vector to predict words.

## Key Formula

In the **PV-DM** (Distributed Memory) variant, the model predicts each word $w_t$ from the document vector $\mathbf{d}$ combined with the surrounding context words:

$$P(w_t \mid \mathbf{d}, w_{t-k}, \ldots, w_{t-1}) = \text{softmax}\!\left(\mathbf{U}\,\overline{\mathbf{h}} + \mathbf{b}\right)$$

$$\overline{\mathbf{h}} = \frac{1}{k+1}\!\left(\mathbf{d} + \sum_{j=t-k}^{t-1} \mathbf{v}_{w_j}\right)$$

where $\mathbf{d} \in \mathbb{R}^d$ is the document embedding shared across all prediction windows within that document, $\mathbf{v}_{w_j} \in \mathbb{R}^d$ are word vectors, and $\mathbf{U}$ is the output weight matrix. Unlike averaging word vectors, $\mathbf{d}$ accumulates paragraph-level meaning that individual word vectors cannot capture. For new unseen documents, word vectors are frozen and $\mathbf{d}$ is inferred by gradient descent.

## Example

Corpus: 5,000 10-K filings, $d = 100$ dimensions.

| Document pair | Cosine similarity | Interpretation |
|---|---|---|
| Boeing 10-K 2019 vs 2020 | 0.94 | Same firm, adjacent years |
| Boeing 10-K 2020 vs Airbus 2020 | 0.82 | Same industry, same pandemic shock |
| Boeing 10-K 2020 vs JPMorgan 10-K 2020 | 0.31 | Different industry, different language |

A regression shows that pairs of firms whose 10-K embedding similarity increased by more than 0.15 quarter-over-quarter experienced return correlation increases of approximately 0.08 over the following 6 months — predicting co-movement before it shows up in prices.

## Remember

Doc2Vec's key advantage over averaging Word2Vec vectors for documents is that it preserves paragraph-level context and is not diluted by document length — a 5,000-word 10-K and an 80,000-word prospectus both produce a single 100-dimensional vector of the same quality. This enables direct cosine similarity comparisons between financial documents of wildly different lengths, powering two practical applications: (1) **nearest-neighbour retrieval** — finding the 5 most historically similar 10-K filings to the current one before an earnings trade, allowing rapid scenario analysis without reading millions of words; (2) **contagion detection** — tracking when two firms' embedding trajectories start converging across quarters as an early warning signal for sector stress or M&A activity.
