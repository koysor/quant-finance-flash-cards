# Pointwise Mutual Information

**Topic:** Computational Finance
**Tags:** nlp, information theory, co-occurrence, text mining, word similarity
**Created:** 2026-05-21
**Author:** Claude Sonnet 4.6

---

## Definition

Pointwise Mutual Information (PMI) measures how much more often two words co-occur in a corpus than would be expected if they were statistically independent. A high PMI signals a strong, meaningful association; a PMI near zero indicates the words appear together only by chance.

## Key Formula

$$\text{PMI}(x, y) = \log \frac{P(x, y)}{P(x)\, P(y)}$$

where $P(x, y)$ is the joint probability of words $x$ and $y$ appearing together in the same context window, and $P(x)$, $P(y)$ are their marginal probabilities. In practice, Positive PMI (PPMI) clamps negative values to zero:

$$\text{PPMI}(x, y) = \max\!\bigl(\text{PMI}(x, y),\ 0\bigr)$$

Negative PMI values are unreliable with finite corpora, so PPMI is the standard variant used in NLP.

## Example

In a corpus of 1,000 financial news articles (500,000 words):
- $P(\text{Federal}) = 0.01$, $P(\text{Reserve}) = 0.008$, $P(\text{Federal, Reserve}) = 0.006$

$$\text{PMI}(\text{Federal},\, \text{Reserve}) = \log\!\frac{0.006}{0.01 \times 0.008} = \log 75 \approx 4.3$$

The high PMI confirms that "Federal Reserve" is a genuine compound concept. By contrast, "Federal profit" would yield a PMI close to zero.

## Remember

In quantitative finance, PMI reveals domain-specific compound terms buried in unstructured data — "credit default", "margin call", and "quantitative easing" all score high PMI because their constituent words are strongly bound in financial corpora. The GloVe word embedding model is mathematically equivalent to factorising a shifted PMI matrix, which shows that classical co-occurrence statistics and modern neural word vectors are two views of the same underlying structure.
