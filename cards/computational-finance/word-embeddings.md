# Word Embeddings

**Topic:** Computational Finance
**Tags:** nlp, word2vec, semantic similarity, alternative data, feature engineering, deep learning
**Created:** 2026-05-22
**Author:** Claude Sonnet 4.6

---

## Definition

**Word embeddings** are dense, low-dimensional vector representations of words learned from large text corpora such that words with similar meanings are geometrically close in the embedding space. They replace sparse one-hot or bag-of-words vectors with continuous vectors that capture semantic and syntactic relationships.

## Key Formula

Word2Vec (skip-gram) learns embeddings by maximising the probability of context words $w_c$ given a centre word $w_t$:

$$\mathcal{L} = \sum_{t} \sum_{c \in \text{context}(t)} \log P(w_c \mid w_t), \quad P(w_c \mid w_t) = \frac{\exp(\mathbf{v}_{w_c}^\top \mathbf{v}_{w_t})}{\sum_{w} \exp(\mathbf{v}_w^\top \mathbf{v}_{w_t})}$$

The learnt vectors exhibit linear arithmetic structure:

$$\vec{v}(\text{King}) - \vec{v}(\text{Man}) + \vec{v}(\text{Woman}) \approx \vec{v}(\text{Queen})$$

## Example

A 2-dimensional finance embedding might place:

| Word | $v_1$ (credit risk) | $v_2$ (equity) |
|---|---|---|
| `stock` | 0.10 | 0.92 |
| `equity` | 0.12 | 0.89 |
| `bond` | 0.88 | 0.11 |

Cosine similarity between `stock` and `equity` ≈ 0.998; between `stock` and `bond` ≈ 0.04, correctly reflecting domain proximity.

## Remember

FinBERT and domain-specific Word2Vec models trained on Reuters or SEC filings outperform general embeddings on financial NLP tasks because the semantic neighbourhood of words like "bearish", "writedown", or "covenant" differs sharply from everyday English. A sentiment classifier using general-purpose embeddings may assign near-zero weight to "impairment" — a highly negative signal in earnings calls — whereas a finance-tuned embedding places it close to "loss" and "decline".
