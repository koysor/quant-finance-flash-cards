# Transformer

**Topic:** Computational Finance
**Tags:** transformers, self-attention, nlp, deep learning, pre-training, language models
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **Transformer** is a deep learning architecture (Vaswani et al., 2017) that processes sequences entirely through stacked self-attention layers rather than recurrence, enabling full parallelisation during training and long-range dependency modelling — it is the foundation of all modern large language models (BERT, GPT, FinBERT).

## Key Formula

Each transformer layer applies **multi-head attention** — $h$ independent attention heads whose outputs are concatenated and projected:

$$\text{MultiHead}(\mathbf{Q},\mathbf{K},\mathbf{V}) = \text{Concat}(\text{head}_1,\ldots,\text{head}_h)\,\mathbf{W}^O$$
$$\text{head}_i = \text{Attention}\!\left(\mathbf{Q}\mathbf{W}_i^Q,\,\mathbf{K}\mathbf{W}_i^K,\,\mathbf{V}\mathbf{W}_i^V\right)$$

Since attention is position-invariant, word order is injected via **sinusoidal positional encoding** added to the input embeddings:

$$\text{PE}(\text{pos},\,2i) = \sin\!\left(\frac{\text{pos}}{10000^{2i/d}}\right), \qquad \text{PE}(\text{pos},\,2i{+}1) = \cos\!\left(\frac{\text{pos}}{10000^{2i/d}}\right)$$

Each sublayer (attention, feed-forward) is wrapped with a residual connection and layer normalisation: $\text{LayerNorm}(\mathbf{x} + \text{Sublayer}(\mathbf{x}))$.

## Example

An encoder-only transformer (12 layers, $h = 12$ heads, $d = 768$) reads a 512-token 10-K extract. In layer 6, head 3 attends strongly from the token "impairment" to "goodwill" (attention weight 0.43) and "writedown" (0.31), while other heads capture syntactic relations. The resulting [CLS] token embedding is passed to a linear classifier: P(negative sentiment) = 0.87.

Without positional encoding, "revenue declined" and "declined revenue" would produce identical representations — the sinusoidal terms resolve this ambiguity.

## Remember

The Transformer's parallelism means it can be pre-trained on vast corpora (billions of words) on GPU clusters in days — something impossible with sequential RNNs. This pre-training investment is then amortised across many downstream financial tasks through **transfer learning**: FinBERT fine-tunes a pre-trained transformer on labelled earnings data for less than £200 of compute, achieving accuracy that would cost millions of labelled examples to match with a model trained from scratch. Every production financial NLP pipeline — earnings sentiment scoring, regulatory filing risk classification, central bank statement analysis — relies on a transformer backbone.
