# Attention Mechanism

**Topic:** Computational Finance
**Tags:** attention, transformer, self-attention, NLP, sequence modelling, deep learning
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **attention mechanism** allows a model to dynamically weight the relevance of different positions in an input sequence when producing each output. In **self-attention**, each element queries every other element to determine how much to attend to it, capturing long-range dependencies without the sequential bottleneck of recurrent networks.

## Key Formula

**Scaled dot-product attention** for queries $\mathbf{Q}$, keys $\mathbf{K}$, values $\mathbf{V}$ (all matrices):

$$\text{Attention}(\mathbf{Q},\mathbf{K},\mathbf{V}) = \text{softmax}\!\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}\right)\mathbf{V}$$

where $d_k$ is the key dimension (scaling prevents dot products from growing large and saturating the softmax). The output is a weighted sum of value vectors, weights determined by query-key compatibility.

## Example

A transformer model reads the sentence: *"Revenue fell sharply but management maintained guidance."* The attention weight for "maintained" attending to "fell" is high — the model learns that the contrast matters for sentiment classification, producing a negative-leaning encoding despite the positive word "maintained".

## Remember

Attention is the architectural innovation behind GPT, BERT, and all modern LLMs used in financial NLP — earnings sentiment analysis, regulatory filing classification, and news-driven signal extraction. Its power for finance lies in capturing context across an entire document: a risk warning buried in paragraph 12 of an earnings call can attend to and modify the interpretation of a bullish statement in paragraph 2, which fixed-window models miss entirely.
