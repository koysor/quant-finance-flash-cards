# Transfer Learning

**Topic:** Computational Finance
**Tags:** transfer learning, fine-tuning, pre-trained model, NLP, deep learning, domain adaptation
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Transfer learning** reuses a model pre-trained on a large source task as the starting point for a related target task, fine-tuning only part of the network on the (typically smaller) target dataset. It transfers the general feature representations learned from abundant data to domains where labelled examples are scarce.

## Key Formula

A pre-trained model $f_{\boldsymbol{\theta}^*}$ learned on source data $\mathcal{D}_S$ is adapted to target task $\mathcal{D}_T$ by minimising:

$$\mathcal{L}_T(\boldsymbol{\theta}) = \frac{1}{|\mathcal{D}_T|}\sum_{(x,y)\in\mathcal{D}_T} \ell(f_{\boldsymbol{\theta}}(x), y)$$

starting from $\boldsymbol{\theta} = \boldsymbol{\theta}^*$ rather than random initialisation. Common strategies:
- **Feature extraction**: freeze all layers, retrain only the output head.
- **Fine-tuning**: unfreeze upper layers, train with a small learning rate.

## Example

FinBERT is a BERT language model pre-trained on financial news and SEC filings. A hedge fund fine-tunes it on 2,000 labelled earnings-call transcripts (positive/negative sentiment) — achieving 89% accuracy using a dataset too small to train BERT from scratch, which would require millions of examples.

## Remember

Transfer learning addresses one of finance's biggest data constraints: labelled financial events (defaults, earnings surprises, fraud) are rare. By borrowing representations from a model trained on terabytes of general text or market data, a firm can build a powerful classifier from hundreds of labelled examples. This is why FinBERT, BloombergGPT, and similar financial LLMs have become standard tools for extracting signals from unstructured text in quantitative research.
