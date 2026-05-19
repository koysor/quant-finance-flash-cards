# GPT (Generative Pre-trained Transformer)

**Topic:** Computational Finance
**Tags:** gpt, transformers, language models, nlp, text generation, alternative data
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**GPT (Generative Pre-trained Transformer)** is a decoder-only transformer pre-trained via **causal language modelling** — learning to predict the next token from all preceding tokens — which gives it generative capability: it can produce coherent, contextually appropriate text continuation given a prompt.

## Key Formula

**Causal language modelling (CLM) objective** — maximise the log-likelihood of each token given all preceding tokens:

$$\mathcal{L}_{\text{CLM}} = -\sum_{t=1}^{T} \log P(w_t \mid w_1, w_2, \ldots, w_{t-1};\,\theta)$$

This is equivalent to maximising the joint probability via the chain rule:

$$P(w_1, \ldots, w_T) = \prod_{t=1}^{T} P(w_t \mid w_1, \ldots, w_{t-1})$$

GPT enforces causality in self-attention via an upper-triangular **causal mask** $\mathbf{M}$ added to attention logits: $M_{ij} = -\infty$ for $j > i$, preventing position $i$ from attending to future positions. This contrasts with BERT, which uses no mask and attends bidirectionally.

## Example

**Prompt:** *"Revenue for Q3 was \$2.1 billion, missing consensus by 4%. Management cited…"*

GPT completion: *"…supply chain disruptions and elevated input costs as the primary drivers of the shortfall. The company lowered full-year guidance from \$8.6 billion to \$8.0 billion."*

A quant fund uses this to generate 10,000 synthetic earnings call variations from 200 real transcripts, tripling the size of its sentiment classifier training set. The classifier's F1 score on a held-out test set improves from 0.74 to 0.81 — the data augmentation closes most of the gap with a model trained on 50× more labelled data.

## Remember

GPT's defining advantage over BERT in finance is **generation**: it can write text, not just classify it. This enables two workflows unavailable to encoder-only models: (1) **data augmentation** — generating realistic but novel earnings scenarios to boost training set diversity for sentiment classifiers trained on scarce labelled data; (2) **structured extraction via prompting** — providing GPT with a press release and asking it to output a JSON object of {revenue, EPS, guidance} is often faster and more flexible than training a dedicated extraction model. Larger GPT variants (GPT-4) can perform these tasks with only 3-5 in-context examples, making them effective for rare financial event types (M&A announcements, regulatory actions) where labelled training data does not exist.
