# Multi-Head Attention

**Topic:** Computational Finance
**Tags:** multi-head attention, transformer, self-attention, nlp, deep learning
**Created:** 2026-05-19
**Author:** Claude Sonnet 4.6

---

## Definition

**Multi-head attention** runs $H$ independent attention operations (heads) in parallel, each learning to attend to different positions or feature subspaces of the input sequence. The outputs are concatenated and linearly projected back to the model dimension. This allows the model to simultaneously capture different types of relationships — e.g. syntactic structure in one head and semantic similarity in another.

## Key Formula

Each head $h$ computes scaled dot-product attention over its own learned projections of the input $\mathbf{X}$:

$$\text{head}_h = \text{Attention}(\mathbf{X}\mathbf{W}_h^Q,\; \mathbf{X}\mathbf{W}_h^K,\; \mathbf{X}\mathbf{W}_h^V)$$

$$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

The $H$ heads are concatenated and projected:

$$\text{MultiHead}(\mathbf{X}) = \text{Concat}(\text{head}_1,\ldots,\text{head}_H)\,\mathbf{W}^O$$

where $\mathbf{W}_h^Q, \mathbf{W}_h^K, \mathbf{W}_h^V \in \mathbb{R}^{d_\text{model} \times d_k}$ with $d_k = d_\text{model}/H$, and $\mathbf{W}^O \in \mathbb{R}^{d_\text{model} \times d_\text{model}}$.

## Example

BERT-base uses $H = 12$ heads with $d_\text{model} = 768$, giving $d_k = 64$ per head. When processing an earnings call sentence "revenue grew despite headwinds", analysis of BERT's attention weights shows: heads 1–3 align similar sentiment words ("grew" ↔ "positive"); heads 4–7 track syntactic dependencies ("revenue" as subject); heads 8–12 attend to negation and contrast markers ("despite"). No single head captures all relationships — the richness arises from their combination.

## Remember

Multi-head attention is the key architectural feature that makes transformer-based models such as BERT and FinBERT so effective at financial NLP tasks. In earnings call analysis, different heads specialise in different linguistic relationships: one head may track forward-looking guidance phrases, another may capture hedging language ("may", "could", "subject to"), and another may align accounting terms with their qualifiers. By learning $H$ independent attention patterns jointly, the model builds richer document representations than single-head attention allows. For financial text, $H = 8$ to $H = 12$ heads is standard — fewer heads reduce capacity for capturing the varied rhetorical patterns in regulatory filings; more heads increase cost without proportional benefit at typical dataset sizes.
