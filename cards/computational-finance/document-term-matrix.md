# Document-Term Matrix

**Topic:** Computational Finance
**Tags:** nlp, text mining, matrix, feature engineering, alternative data
**Created:** 2026-05-21
**Author:** Claude Sonnet 4.6

---

## Definition

A document-term matrix (DTM) is a rectangular array where each row represents a document and each column represents a vocabulary term; the entry at row $i$, column $j$ records how often term $j$ appears in document $i$ (as a raw count or TF-IDF weight). It is the standard matrix representation of a text corpus.

## Key Formula

For a corpus of $M$ documents and a vocabulary of $N$ terms:

$$\mathbf{D} \in \mathbb{R}^{M \times N}, \quad D_{ij} = f(w_j,\, d_i)$$

where $f(w_j, d_i)$ is the count or TF-IDF weight of term $w_j$ in document $d_i$. Because each document uses only a small fraction of the vocabulary, $\mathbf{D}$ is extremely sparse — often more than 99 % zeros.

## Example

**Corpus:** 3 financial headlines, vocabulary $\{$buy, hold, profit, risk, sell$\}$.

| | buy | hold | profit | risk | sell |
|---|---|---|---|---|---|
| "Buy: strong profit forecast" | 1 | 0 | 1 | 0 | 0 |
| "Hold: risk to profit outlook" | 0 | 1 | 1 | 1 | 0 |
| "Sell: rising risk, falling profit" | 0 | 0 | 1 | 1 | 1 |

This $3 \times 5$ DTM encodes each headline as a row vector. Applying Truncated SVD to this matrix extracts latent themes such as "bullish", "cautious", and "bearish".

## Remember

The DTM is the gateway from unstructured financial text to matrix mathematics: once earnings reports, news articles, or analyst notes are in DTM form, standard linear-algebra methods — cosine similarity, SVD, PCA — apply directly. Its extreme sparsity means sparse matrix storage is essential in practice; a corpus of 100,000 filings with a 50,000-word vocabulary would require 40 GB as a dense float array but only megabytes as a sparse structure.
