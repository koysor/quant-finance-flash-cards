# Sentence Transformers (SBERT)

**Topic:** Computational Finance
**Tags:** sbert, sentence embeddings, bert, semantic search, nlp, similarity
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Sentence Transformers (SBERT)** is a modification of BERT that uses a **siamese network** architecture and contrastive training to produce fixed-size sentence embeddings — dense vectors that capture the full semantic meaning of a sentence — so that semantic similarity can be measured with a single cosine similarity computation rather than expensive pairwise BERT inference.

## Key Formula

SBERT is trained on sentence pairs $(s_a, s_b)$ with a known similarity label $y \in \{0, 1\}$ using the **cosine similarity loss**. Mean-pooling collapses BERT's token embeddings into one sentence vector:

$$\mathbf{u} = \frac{1}{T}\sum_{t=1}^{T} \mathbf{h}_t, \quad \mathbf{u} \in \mathbb{R}^{768}$$

The model is fine-tuned to minimise the distance between semantically similar pairs and maximise it for dissimilar ones. At inference, semantic similarity is:

$$\text{sim}(s_a, s_b) = \frac{\mathbf{u}_a \cdot \mathbf{u}_b}{\|\mathbf{u}_a\|\,\|\mathbf{u}_b\|}$$

This $O(1)$ lookup replaces the $O(n^2)$ all-pairs BERT comparisons that would otherwise be required to find the most similar document in a corpus.

## Example

A fund encodes 50,000 analyst report summaries into 768-dimensional SBERT vectors and stores them in a vector database. When a new earnings release arrives, it is encoded in ~5 ms and the top-10 most semantically similar historical reports are retrieved via cosine similarity lookup in ~2 ms — replacing an overnight manual process. The retrieved reports are fed to a downstream GPT model to generate a comparative analysis, producing a structured signal within seconds of the release.

## Remember

SBERT is the **scalable retrieval layer** for financial document search. Raw BERT cannot be used to rank 50,000 documents against a query in real time because it requires feeding every $(query, document)$ pair through the full 12-layer encoder — that is $50{,}000$ forward passes. SBERT solves this by pre-computing a single embedding per document; retrieval then costs one matrix multiply. In quant finance this unlocks: (1) finding precedents for novel earnings scenarios in milliseconds; (2) clustering thousands of analyst notes by theme to build a macro sentiment dashboard; (3) detecting when two differently-worded covenant clauses from different bond indentures are semantically equivalent.
