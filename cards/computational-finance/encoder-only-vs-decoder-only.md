# Encoder-Only vs Decoder-Only Transformer

**Topic:** Computational Finance
**Tags:** transformers, bert, gpt, nlp, deep learning, language models
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

A **decoder-only transformer** (e.g. GPT) applies a causal mask so each token attends only to previous tokens, making it autoregressive and suited for text generation; an **encoder-only transformer** (e.g. BERT) applies full bidirectional attention so every token attends to all others, making it suited for understanding and classification tasks.

## Key Formula

Both architectures use scaled dot-product attention, but differ in the attention mask $\mathbf{M}$:

$$\text{Attention}(\mathbf{Q},\mathbf{K},\mathbf{V}) = \text{softmax}\!\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} + \mathbf{M}\right)\mathbf{V}$$

For a sequence of $n$ tokens:

- **Encoder-only (BERT):** $M_{ij} = 0$ for all $i, j$ — every token attends to every other token.
- **Decoder-only (GPT):** $M_{ij} = -\infty$ when $j > i$, otherwise $0$ — token $i$ cannot attend to future token $j$.

This single masking difference determines whether the model sees full context (classification) or only past context (generation).

## Example

Task: classify whether an earnings call extract is positive or negative.

- **BERT (encoder-only):** reads the full 256-token transcript at once; the [CLS] token aggregates bidirectional context from every word. Fine-tuned FinBERT achieves 87% accuracy on FinancialPhraseBank.
- **GPT (decoder-only):** prompted with the transcript and asked to complete "Sentiment: ___"; autoregressively generates "positive" or "negative". GPT-4 achieves similar accuracy zero-shot but uses 50× more parameters.

For high-volume classification (thousands of filings per day) BERT-style fine-tuning is preferred; GPT-style prompting is preferred when labelled data is scarce.

## Remember

The masking choice has a direct operational consequence in finance: encoder-only models require fine-tuning on labelled examples but run cheaply at inference time (one forward pass per document), whereas decoder-only models can be prompted without labelled data but generate output token-by-token, which is slow and expensive at scale. Most production financial NLP pipelines — earnings sentiment, covenant breach detection, ESG scoring — use encoder-only architectures fine-tuned on a few thousand labelled examples, reserving GPT-style models for open-ended tasks such as drafting analyst commentary or answering ad-hoc questions about a filing.
