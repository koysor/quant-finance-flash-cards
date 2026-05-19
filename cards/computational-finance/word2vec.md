# Word2Vec

**Topic:** Computational Finance
**Tags:** word embeddings, nlp, neural networks, text mining, alternative data, semantic similarity
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Word2Vec** is a neural network algorithm that learns dense vector representations (embeddings) of words from a large text corpus by training a shallow network to predict either a target word from its surrounding context words (CBOW) or surrounding context words from a single target word (skip-gram).

## Key Formula

**Skip-gram objective** — maximise the average log-probability of context words given a target word $w_t$ over a window of size $m$:

$$\mathcal{L} = \frac{1}{T} \sum_{t=1}^{T} \sum_{\substack{j=-m \\ j \ne 0}}^{m} \log P(w_{t+j} \mid w_t)$$

The conditional probability is a softmax over a vocabulary of $V$ words:

$$P(w_O \mid w_I) = \frac{\exp\!\left(\mathbf{v}_{w_O}^{\prime\top} \mathbf{v}_{w_I}\right)}{\displaystyle\sum_{w=1}^{V} \exp\!\left(\mathbf{v}_w^{\prime\top} \mathbf{v}_{w_I}\right)}$$

where $\mathbf{v}_w \in \mathbb{R}^d$ is the input embedding and $\mathbf{v}_w' \in \mathbb{R}^d$ the output embedding for word $w$. After training, $\mathbf{v}_w$ encodes the word's meaning such that semantically related words have high cosine similarity — and vector arithmetic is meaningful:

$$\mathbf{v}(\text{king}) - \mathbf{v}(\text{man}) + \mathbf{v}(\text{woman}) \approx \mathbf{v}(\text{queen})$$

## Example

Word2Vec trained on five years of earnings call transcripts (10,000 calls, $d = 100$ dimensions). Selected cosine similarities:

| Word pair | Cosine similarity | Interpretation |
|---|---|---|
| "headwinds" / "challenging" | 0.87 | Semantically near |
| "record" / "growth" | 0.83 | Positive sentiment cluster |
| "headwinds" / "record" | −0.21 | Opposing sentiment poles |

The sentiment axis $\mathbf{s} = \mathbf{v}(\text{beat}) - \mathbf{v}(\text{miss})$ has unit length after normalisation. Projecting a document's mean embedding onto $\mathbf{s}$ gives a continuous earnings-surprise sentiment score — positive projection indicates language similar to earnings beats.

## Remember

Word2Vec replaces TF-IDF sparse vectors with dense semantic embeddings where arithmetic is meaningful. Its key advantage in quantitative finance is that words never seen together still receive sensible embeddings if they share similar neighbours — "liquidity crunch" in a 2008 filing and "funding stress" in a 2020 filing map to nearby vectors, allowing a model trained on one crisis to generalise to another. Practitioners use Word2Vec embeddings as fast, interpretable baselines before scaling to heavier transformer models (FinBERT, GPT); the vector arithmetic property also enables building explicit "earnings sentiment axes" and "risk factor directions" without labelled training data.
