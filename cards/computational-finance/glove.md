# GloVe

**Topic:** Computational Finance
**Tags:** word embeddings, nlp, co-occurrence matrix, text mining, alternative data, semantic similarity
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**GloVe (Global Vectors for Word Representation)** is a word embedding algorithm that learns dense vector representations by factorising the global word–word co-occurrence matrix of a corpus, capturing relationships between terms that appear near each other across all documents simultaneously rather than from individual local context windows.

## Key Formula

Let $X_{ij}$ be the number of times word $j$ appears within a context window of word $i$ across the entire corpus. GloVe trains embedding vectors $\mathbf{w}_i$ and context vectors $\tilde{\mathbf{w}}_j$ to minimise a weighted least-squares objective:

$$J = \sum_{i,\,j=1}^{V} f(X_{ij})\!\left(\mathbf{w}_i^{\top} \tilde{\mathbf{w}}_j + b_i + \tilde{b}_j - \log X_{ij}\right)^{2}$$

where $b_i$, $\tilde{b}_j$ are scalar biases and $f$ is a capping weighting function that prevents very frequent co-occurrences from dominating:

$$f(x) = \begin{cases} \!\left(\dfrac{x}{x_{\max}}\right)^{\!\alpha} & x < x_{\max} \\ 1 & x \ge x_{\max} \end{cases} \qquad \alpha = 0.75,\; x_{\max} = 100$$

The final embedding for word $i$ is taken as $\mathbf{w}_i + \tilde{\mathbf{w}}_i$.

## Example

Corpus: 50,000 SEC 10-K filings. Selected global co-occurrence counts (window size 5):

| Word pair | $X_{ij}$ | $\log X_{ij}$ | $f(X_{ij})$ |
|---|---|---|---|
| "impairment" / "goodwill" | 9,200 | 9.13 | 1.00 |
| "covenant" / "breach" | 740 | 6.61 | 0.86 |
| "impairment" / "the" | 920,000 | 13.73 | 1.00 (capped) |

GloVe learns that "covenant" and "breach" share a meaningful relationship despite lower raw frequency, whereas the ubiquitous "the" is suppressed relative to its raw count. After training ($d = 100$), cosine similarity: sim("covenant", "breach") = 0.79; sim("impairment", "writedown") = 0.82.

## Remember

GloVe's advantage over Word2Vec in financial text is its use of **global** co-occurrence statistics: a rare but important term pair (e.g. "liquidity" and "covenant") may never appear in the same sentence, yet co-occurs meaningfully across thousands of separate filings — a signal Word2Vec's local context window misses entirely. This makes GloVe particularly suited to formal regulatory language (10-Ks, prospectuses, ISDA confirmations) where specialist terms are spread across long documents. Practitioners often initialise financial NLP models with Stanford's pre-trained GloVe vectors and fine-tune on domain-specific corpora, using the embeddings to build credit-risk lexicons, classify litigation language in filings, or cluster analyst reports by thematic content.
