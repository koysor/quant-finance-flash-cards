# Sentiment Analysis Pipeline

**Topic:** Computational Finance
**Tags:** nlp, sentiment analysis, alternative data, text mining, text classification
**Created:** 2026-05-21
**Author:** Claude Sonnet 4.6

---

## Definition

A sentiment analysis pipeline is an ordered sequence of NLP transformations that converts raw text into a directional score — positive, negative, or neutral. In quantitative finance it is applied to earnings call transcripts, news headlines, and regulatory filings to generate tradable signals.

## Key Formula

The three-stage pipeline maps each document $d$ to a predicted label:

$$d \xrightarrow{\text{tokenise}} \mathbf{t} \xrightarrow{\text{vectorise}} \mathbf{x} \xrightarrow{\text{classify}} \hat{y} \in \{-1,\, 0,\, +1\}$$

where $\mathbf{t}$ is the token sequence, $\mathbf{x}$ is the feature vector (BoW, TF-IDF, or an embedding), and $\hat{y}$ is the sentiment label. The classifier often outputs a continuous probability $\hat{p} \in [0, 1]$ for the positive class rather than a hard label.

## Example

**Input:** "Management expressed confidence in Q3 earnings despite margin headwinds."

| Stage | Output |
|---|---|
| Tokenise | ["management", "confidence", "Q3", "earnings", "despite", "margin", "headwinds"] |
| Vectorise (TF-IDF) | sparse vector over 50,000-word vocabulary |
| Classify (FinBERT) | positive, $\hat{p} = 0.84$ |

A long/short strategy that trades on $\hat{p} > 0.7$ must ensure the pipeline sees only text that was publicly available before the trading decision — any future-text leakage constitutes look-ahead bias.

## Remember

In quantitative finance the classifier is rarely the bottleneck: sourcing timestamped, cleaned financial text and eliminating look-ahead bias are the hard problems. FinBERT and Loughran-McDonald lexicons address the domain-vocabulary gap, but the pipeline architecture — how raw documents become return-generating signals — determines whether academic performance translates into live alpha.
