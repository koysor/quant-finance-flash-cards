# Masked Language Modelling

**Topic:** Computational Finance
**Tags:** pre-training, bert, nlp, deep learning, transformers, language models
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

**Masked Language Modelling (MLM)** is a self-supervised pre-training objective where a random 15% of input tokens are replaced with a special `[MASK]` token and the model is trained to predict the original tokens from the surrounding context — enabling bidirectional representations without requiring labelled data.

## Key Formula

The training loss is the negative log-likelihood over only the masked positions:

$$\mathcal{L}_{\text{MLM}} = -\sum_{i \in \mathcal{M}} \log P\!\left(x_i \mid \mathbf{x}_{\backslash \mathcal{M}}\right)$$

where $\mathcal{M}$ is the set of masked token indices and $\mathbf{x}_{\backslash \mathcal{M}}$ denotes the full sequence with those positions hidden. Of the 15% selected tokens: 80% become `[MASK]`, 10% are replaced with a random token, and 10% are left unchanged — preventing the model from only learning to handle `[MASK]`.

## Example

Input sentence: *"The company reported a quarterly [MASK] of \$2.3 billion."*

The model receives all tokens except the masked one and must predict that the hidden token is "profit" (or "loss", "revenue", etc.) from the surrounding context. After pre-training on 3.3 billion words, FinBERT learns that financial terms cluster together: "earnings", "EBITDA", "writedown" all occupy nearby regions of the 768-dimensional embedding space.

## Remember

MLM is why BERT-style models read in both directions simultaneously — unlike GPT which predicts left-to-right. This bidirectionality is critical for financial text: assessing whether "exposure" is a risk term requires reading both what precedes it ("credit exposure", "net exposure") and what follows ("to sovereign debt", "to interest rate moves"). FinBERT uses MLM pre-training on financial corpora so that its contextual embeddings capture domain-specific meaning before any labelled sentiment data is seen.
