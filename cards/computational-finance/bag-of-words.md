# Bag-of-Words

**Topic:** Computational Finance
**Tags:** nlp, text mining, feature engineering, alternative data, sparse vectors
**Created:** 2026-05-21
**Author:** Claude Sonnet 4.6

---

## Definition

The Bag-of-Words (BoW) model represents a text document as a vector of word counts, discarding grammar and word order entirely. Each dimension of the vector corresponds to a word in a fixed vocabulary, and the value is how many times that word appears in the document.

## Key Formula

For a vocabulary $V = \{w_1, w_2, \dots, w_N\}$, document $d$ is represented as:

$$\mathbf{v}_d = \bigl[f(w_1, d),\ f(w_2, d),\ \dots,\ f(w_N, d)\bigr]$$

where $f(w_i, d)$ is the count of word $w_i$ in $d$. Because $N$ can be tens of thousands but each document uses only a small fraction of the vocabulary, $\mathbf{v}_d$ is extremely sparse (mostly zeros).

## Example

**Vocabulary:** {buy, hold, profit, risk, sell}

**Headline:** "Strong profit growth signals a hold, not a sell"

$$\mathbf{v}_d = [0,\ 1,\ 1,\ 0,\ 1]$$

A second, longer headline — "Rising profit signals a hold rather than a sell position" — that contains the same key words yields a vector pointing in the same direction. Cosine similarity between the two equals 1.0, correctly identifying them as semantically equivalent in terms of topic, despite the differing lengths.

## Remember

In quantitative finance, BoW converts earnings call transcripts, news articles, and regulatory filings into numerical feature vectors for sentiment classifiers and topic models. Its critical weakness is that word order is lost: "not profit" and "profit not" produce identical vectors, so negation is invisible. TF-IDF and word embeddings address this, but BoW remains a useful, fast baseline when labelled data is scarce.
