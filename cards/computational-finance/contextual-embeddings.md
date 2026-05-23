# Contextual Embeddings

**Topic:** Computational Finance
**Tags:** bert, nlp, word embeddings, transformers, semantic similarity, language models
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**Contextual embeddings** are word representations where the vector assigned to a word changes depending on its surrounding context, produced by running text through a deep language model such as BERT or GPT. Unlike static embeddings (Word2Vec, GloVe), which assign a single fixed vector to each word regardless of usage, contextual embeddings capture polysemy — the same word having different meanings in different sentences.

## Key Formula

In BERT, each token $w_i$ in a sequence $[w_1, \dots, w_n]$ produces a contextual representation $\mathbf{h}_i^{(L)}$ after $L$ transformer layers of bidirectional self-attention:

$$\mathbf{h}_i^{(\ell)} = \text{TransformerLayer}^{(\ell)}\!\left(\mathbf{h}_1^{(\ell-1)}, \dots, \mathbf{h}_n^{(\ell-1)}\right)$$

$$\text{Attention}(\mathbf{Q},\mathbf{K},\mathbf{V}) = \text{softmax}\!\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}\right)\mathbf{V}$$

The output $\mathbf{h}_i^{(L)} \in \mathbb{R}^{768}$ depends on every other token in the sequence, so the same word token produces a different vector in every new sentence.

## Example

The word "short" in two financial sentences:

| Sentence | Contextual embedding meaning |
|---|---|
| *"The fund took a **short** position in TSLA."* | Captures: selling borrowed shares, bearish bet |
| *"The bond has a **short** maturity of 3 months."* | Captures: duration, tenor, liquidity |

A static Word2Vec embedding gives "short" the same vector in both cases — the average across all its usages. BERT's contextual embedding places the two usages in distinct regions of the 768-dimensional space, enabling a downstream model to classify the sentence correctly.

## Remember

Contextual embeddings are what make transformer-based models materially better than Word2Vec for financial sentence classification tasks. In earnings call analysis, "guidance was revised" is positive if preceded by "upward" and negative if preceded by "downward" — a distinction that requires the full sentence context to resolve. Static embeddings cannot handle this; contextual embeddings handle it natively because the attention mechanism reads every surrounding token before producing the representation. This is the primary reason FinBERT outperforms lexicon-based sentiment tools on financial text.
