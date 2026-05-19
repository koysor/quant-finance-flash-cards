# TF-IDF

**Topic:** Computational Finance
**Tags:** nlp, text mining, information retrieval, feature engineering, alternative data, document scoring
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**TF-IDF (Term Frequency–Inverse Document Frequency)** is a numerical statistic that measures how distinctive a word is to a particular document within a larger corpus: it rewards words that appear frequently in one document while penalising words that appear in nearly every document.

## Key Formula

Let $f_{t,d}$ be the count of term $t$ in document $d$, and $|D|$ be the total number of documents in corpus $D$.

$$\text{TF}(t, d) = \frac{f_{t,d}}{\displaystyle\sum_{t'} f_{t',d}}$$

$$\text{IDF}(t, D) = \log\frac{|D|}{|\{d \in D : t \in d\}|}$$

$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

A word that appears in every document gets $\text{IDF} = 0$ and is therefore completely suppressed; a word unique to one document gets the maximum IDF, amplifying its TF contribution.

## Example

A corpus of 10,000 earnings transcripts. For one filing:

| Word | $f_{t,d}$ | TF | Docs containing it | IDF | TF-IDF |
|---|---|---|---|---|---|
| "impairment" | 20 | 0.004 | 500 | $\log(10{,}000/500) = 3.00$ | 0.012 |
| "the" | 300 | 0.060 | 10,000 | $\log(1) = 0$ | 0.000 |
| "restructuring" | 8 | 0.0016 | 200 | $\log(50) = 3.91$ | 0.006 |

Total words in this filing: 5,000. "Impairment" has a high TF-IDF because it is frequent in this specific filing but uncommon across the corpus — a strong signal of write-down risk.

## Remember

In quantitative finance, TF-IDF converts raw text — earnings transcripts, 10-K filings, central bank statements — into numerical feature vectors that a machine learning model can process. It automatically down-weights boilerplate language common to all filings ("the", "pursuant to", "fiscal year") and amplifies filing-specific language that carries information ("goodwill impairment", "liquidity covenant breach", "going concern"). This makes TF-IDF the standard baseline for document classification and event-driven signal generation before more complex transformer models are applied.
