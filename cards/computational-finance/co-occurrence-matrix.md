# Co-occurrence Matrix

**Topic:** Computational Finance
**Tags:** nlp, word embeddings, text mining, matrix factorisation, corpus analysis, glove
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

A **co-occurrence matrix** $X$ is a $V \times V$ matrix (where $V$ is the vocabulary size) in which entry $X_{ij}$ counts how many times word $j$ appears within a context window of size $k$ around word $i$ across the entire corpus — encoding the statistical association between every pair of words globally.

## Key Formula

For a corpus $\mathcal{D}$ of documents, with context window half-size $k$:

$$X_{ij} = \sum_{d \in \mathcal{D}}\; \sum_{t=1}^{|d|} \mathbf{1}[w_t^{(d)} = i] \sum_{\substack{s=t-k \\ s \neq t}}^{t+k} \mathbf{1}[w_s^{(d)} = j]$$

The matrix is symmetric ($X_{ij} = X_{ji}$). Raw counts are often converted to **Pointwise Mutual Information (PMI)** to control for the fact that frequent words co-occur with everything:

$$\text{PMI}(i, j) = \log \frac{X_{ij} \cdot N}{\left(\displaystyle\sum_{k} X_{ik}\right)\!\left(\displaystyle\sum_{k} X_{kj}\right)}$$

where $N = \sum_{i,j} X_{ij}$ is the total co-occurrence count. Only positive PMI is retained: $\text{PPMI}(i,j) = \max(0,\,\text{PMI}(i,j))$.

## Example

Corpus: 1,000 earnings call transcripts. Vocabulary: 5 selected terms. Window size $k = 2$.

|  | impairment | goodwill | writedown | revenue | growth |
|---|---|---|---|---|---|
| **impairment** | 0 | 420 | 310 | 80 | 25 |
| **goodwill** | 420 | 0 | 280 | 110 | 18 |
| **writedown** | 310 | 280 | 0 | 60 | 12 |
| **revenue** | 80 | 110 | 60 | 0 | 670 |
| **growth** | 25 | 18 | 12 | 670 | 0 |

The impairment/goodwill/writedown cluster and the revenue/growth cluster emerge purely from co-occurrence counts — no human labelling required.

$\text{PMI}(\text{impairment},\,\text{goodwill}) = \log\frac{420 \times N}{835 \times 828} \gg 0$ — strong positive association.

## Remember

The co-occurrence matrix is the raw data structure that GloVe factorises into dense word embeddings. Its key strength for quantitative finance is that it captures **global** corpus statistics: terms that never share a sentence but frequently appear in the same section of 10-K filings (e.g. "covenant" and "default") will still have a high $X_{ij}$ count. In practice, a full matrix over a 30,000-word financial vocabulary has $9 \times 10^8$ entries — almost all zero — so it is stored as a sparse matrix. Applications include: automatically discovering financial risk theme clusters from SEC filings without labels, and building frequency priors that augment smaller supervised datasets for credit-risk classification.
