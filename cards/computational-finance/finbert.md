# FinBERT

**Topic:** Computational Finance
**Tags:** nlp, transformers, sentiment analysis, transfer learning, alternative data, bert
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**FinBERT** is a BERT (Bidirectional Encoder Representations from Transformers) model pre-trained on general English text and then fine-tuned on financial corpora — 10-K filings, earnings call transcripts, and analyst reports — to classify the sentiment of financial sentences as positive, negative, or neutral.

## Key Formula

FinBERT appends a linear classification head to BERT's [CLS] token representation:

$$P(y \mid \mathbf{x}) = \text{softmax}\!\left(\mathbf{W}\,\mathbf{h}_{[\text{CLS}]} + \mathbf{b}\right)$$

where $\mathbf{h}_{[\text{CLS}]} \in \mathbb{R}^{768}$ is the contextualised representation produced by 12 bidirectional transformer layers, $\mathbf{W} \in \mathbb{R}^{3 \times 768}$ maps to three classes, and the output is a probability distribution over $\{$positive, negative, neutral$\}$.

Each transformer layer computes context via scaled dot-product self-attention:

$$\text{Attention}(\mathbf{Q},\mathbf{K},\mathbf{V}) = \text{softmax}\!\!\left(\frac{\mathbf{Q}\mathbf{K}^{\!\top}}{\sqrt{d_k}}\right)\mathbf{V}$$

This lets every token attend to every other token simultaneously, so "not improving" is correctly negative and "raised guidance" is correctly positive.

## Example

Input sentence: *"Revenue declined 12% year-over-year due to margin compression and restructuring charges."*

| Model | Output |
|---|---|
| L&M lexicon | Tone = −0.40 (counts "declined", "charges" as negative) |
| VADER | compound = −0.18 (weakly negative — misses financial jargon) |
| **FinBERT** | P(negative) = **0.89**, P(neutral) = 0.09, P(positive) = 0.02 |

FinBERT correctly identifies "margin compression" as a strongly negative financial phrase, whereas VADER — trained on social media — assigns it a near-neutral score because "compression" has no inherent sentiment in everyday language.

## Remember

FinBERT is the practitioner's go-to model for financial sentiment because it combines two advantages: (1) **domain vocabulary** — fine-tuned on financial text so it understands "margin compression", "going concern", and "covenant breach" as negative signals; (2) **context sensitivity** — bidirectional attention handles negation and irony that fool lexicon-based tools. A common production pattern is to score earnings call transcripts in the first five minutes using the pre-trained `ProsusAI/finbert` model from Hugging Face, then rank stocks by the shift in P(negative) from the prior quarter's call — stocks with the largest increase in negative probability have historically underperformed their sector by 2–4% in the subsequent month.
