# Language Modelling Loss

**Topic:** Computational Finance
**Tags:** cross-entropy, perplexity, language models, gpt, bert, nlp
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Language modelling loss** is the cross-entropy between the model's predicted token probability distribution and the true next token, summed over every position in the training corpus; its exponentiated form, **perplexity**, is the standard evaluation metric — measuring how surprised the model is by held-out text, with lower values indicating a better-calibrated model.

## Key Formula

For a sequence of $T$ tokens $w_1, w_2, \ldots, w_T$, the **cross-entropy loss** per token is:

$$\mathcal{L} = -\frac{1}{T}\sum_{t=1}^{T} \log_2 P(w_t \mid w_1, \ldots, w_{t-1};\,\theta)$$

**Perplexity** is the exponentiated cross-entropy:

$$\text{PPL} = 2^{\mathcal{L}} = \prod_{t=1}^{T} P(w_t \mid w_1,\ldots,w_{t-1})^{-1/T}$$

Intuitively, a perplexity of $k$ means the model is on average as uncertain as if it had to choose uniformly among $k$ equally likely tokens at each position. A model predicting financial text with PPL = 20 is far better than one with PPL = 500 — the former has effectively narrowed each prediction to 20 plausible continuations, the latter to 500.

## Example

A GPT model is evaluated on 1,000 tokens from held-out earnings call transcripts. The sum of log-probabilities assigned to the correct tokens is $-4{,}300$ nats ($\approx -6{,}202$ bits). Cross-entropy: $\mathcal{L} = 6{,}202 / 1{,}000 = 6.202$ bits per token. Perplexity: $\text{PPL} = 2^{6.202} \approx 73$.

After domain-adaptive pre-training on 500,000 earnings transcripts, the loss falls to $\mathcal{L} = 4.85$ bits/token, giving $\text{PPL} = 2^{4.85} \approx 29$ — a 60% reduction in perplexity, indicating the model has internalised financial vocabulary and sentence structure. Downstream sentiment F1 score improves from 0.78 to 0.86, confirming that lower perplexity on domain text correlates with better task performance.

## Remember

Language modelling loss is the **pre-training signal** that gives BERT and GPT their value for quantitative finance — but practitioners rarely report it. What matters is whether reduced perplexity on financial domain text translates to better performance on downstream tasks: sentiment classification, NER, earnings extraction. The empirical finding across many FinNLP papers is that domain-adaptive pre-training (continuing to train on SEC filings, earnings transcripts, or Bloomberg news) consistently reduces perplexity on financial text by 40–70% versus the general-domain checkpoint, and this reliably improves downstream task F1 by 3–8 percentage points — enough to matter for a cross-sectional signal with a modest Sharpe ratio.
