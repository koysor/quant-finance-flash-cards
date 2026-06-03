# Large Language Model

**Topic:** Computational Finance
**Tags:** llm, transformers, nlp, scaling laws, pre-training, alternative data
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

A **Large Language Model (LLM)** is a transformer-based neural network with billions of parameters, pre-trained on massive text corpora to model the probability distribution over sequences of tokens. LLMs emerge from scaling the transformer architecture along three axes — parameters $N$, training tokens $D$, and compute budget $C$ — until the model exhibits capabilities that smaller networks cannot achieve.

## Key Formula

The **Chinchilla scaling law** (Hoffmann et al., 2022) states that for a fixed compute budget $C \approx 6ND$, the compute-optimal number of training tokens $D^*$ is proportional to model size $N$:

$$D^* = 20N$$

This means a model with $N$ parameters should be trained on approximately 20 times as many tokens to make optimal use of available compute.

## Example

A 7 billion parameter LLM ($N = 7 \times 10^9$) is compute-optimal when trained on:

$$D^* = 20 \times 7 \times 10^9 = 1.4 \times 10^{11} \text{ tokens} \approx 140 \text{ billion tokens}$$

At an average of roughly 4 characters per token, this corresponds to approximately 560 billion characters of text — comparable to hundreds of thousands of books. Models trained on substantially fewer tokens are said to be *under-trained* for their size.

## Remember

In quantitative finance, LLMs extract alpha signals from unstructured text that rule-based systems cannot parse: FOMC meeting minutes, earnings call transcripts, and regulatory filings. A fine-tuned LLM processing the Fed's statement can produce a directional view on rate expectations within seconds of publication — giving systematic traders a measurable edge over sentiment indices built on slower keyword-matching approaches.
