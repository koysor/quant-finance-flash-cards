# BloombergGPT

**Topic:** Machine Learning
**Tags:** bloomberggpt, llm, financial nlp, domain adaptation, bloomberg
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

**BloombergGPT** (Wu et al., 2023) is a 50 billion parameter decoder-only language model trained from scratch on a mixture of Bloomberg's proprietary financial text (363 billion tokens) and general internet text (345 billion tokens), totalling 569 billion tokens. It demonstrates that domain-adaptive pre-training on proprietary financial corpora produces NLP models that outperform comparably-sized general models on financial tasks.

## Key Formula

The training corpus is a 50/50 financial–general mix by token count. Applying the Chinchilla scaling law to the compute budget $C$:

$$C \approx 6 \times 50 \times 10^9 \times 569 \times 10^9 \approx 1.7 \times 10^{23} \text{ FLOPs}$$

The ratio $D / N = 569 \times 10^9 / 50 \times 10^9 \approx 11.4$ is below the Chinchilla-optimal 20, meaning the model is slightly under-trained relative to its parameter count but constrained by available financial text.

## Example

On the Bloomberg financial phrase bank sentiment task (FPB), BloombergGPT achieves an F1 score of 0.511 (zero-shot) versus GPT-NeoX-20B at 0.454 — a meaningful improvement on a task directly relevant to earnings sentiment analysis. On general NLP benchmarks (BIG-bench), performance is comparable to general models of similar size, confirming that domain adaptation did not degrade general capability.

## Remember

BloombergGPT establishes that proprietary text is a competitive moat in financial AI: the 363 billion tokens of Bloomberg financial data are not publicly available, so no general model can replicate its domain knowledge through fine-tuning alone. Firms with large proprietary corpora — trade data, internal research, client communications — can build similarly differentiated LLMs, making data curation and retention as strategically important as model architecture choices.
