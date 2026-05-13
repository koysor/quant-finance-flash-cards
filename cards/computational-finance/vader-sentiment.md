# VADER Sentiment Analysis

**Topic:** Computational Finance
**Tags:** vader, sentiment analysis, nlp, social media, news, text mining
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**VADER (Valence Aware Dictionary and sEntiment Reasoner)** is a rule-based and lexicon-based sentiment analysis tool designed specifically for short, informal text such as social media posts, news headlines, and earnings call excerpts. It assigns a compound sentiment score to a piece of text without requiring model training.

## Key Formula

VADER scores each word in a lexicon with a valence from $-4$ (most negative) to $+4$ (most positive), applies rule-based adjustments, then computes a normalised compound score:

$$\text{compound} = \frac{\text{sum of valences}}{\sqrt{\text{sum}^2 + \alpha}}, \quad \alpha = 15$$

$$\text{compound} \in [-1, 1]$$

**Classification thresholds:**
- Positive: compound $\geq 0.05$
- Negative: compound $\leq -0.05$
- Neutral: $-0.05 <$ compound $< 0.05$

Rule-based adjustments account for: capitalisation ("GREAT" vs "great"), punctuation ("great!!!"), negation ("not great"), and degree modifiers ("very great").

## Example

Earnings call headline: *"Revenue beats expectations but margin pressure persists amid rising costs."*
VADER scores: beats (+2.0), pressure (−1.5), rising (+0.3, but context makes it negative), costs (−1.0). Compound $\approx −0.12$ → Negative. Compare to: *"Record profits! Guidance raised."* → compound $= +0.87$ → Strongly positive. In a systematic news-driven strategy, the compound score is used as a real-time signal for event-driven momentum.

## Remember

VADER requires no training data and runs in milliseconds — making it practical for real-time news and social media signal generation where labelled training sets don't exist. Its key limitation is that it is domain-agnostic: financial jargon ("short", "bearish", "spread") is not modelled with finance-specific valence. For high-stakes applications (earnings prediction, M&A sentiment), practitioners use VADER as a fast first-pass filter and supplement it with finance-specific models (FinBERT, GPT-based classifiers) that are trained on labelled financial text and understand domain-specific polarity reversals.
