# Natural Language Processing

**Topic:** Computational Finance
**Tags:** nlp, text analysis, sentiment, tokenisation, embeddings, alternative data
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Natural Language Processing (NLP)** is the branch of machine learning concerned with enabling computers to understand, interpret, and generate human language by converting text into numerical representations that models can process.

## Key Formula

**TF-IDF** (Term Frequency–Inverse Document Frequency) scores how distinctive a word $t$ is to document $d$ in corpus $D$:

$$\text{TF-IDF}(t,d,D) = \underbrace{\frac{f_{t,d}}{\sum_{t'} f_{t',d}}}_{\text{term frequency}} \times \underbrace{\log\frac{|D|}{|\{d \in D : t \in d\}|}}_{\text{inverse document frequency}}$$

where $f_{t,d}$ is the count of term $t$ in document $d$ and $|D|$ is the total number of documents. High TF-IDF means the word is frequent in this document but rare across the corpus — a strong signal of the document's topic.

**Sentiment score** (simple lexicon approach):

$$S = \frac{N_{\text{positive}} - N_{\text{negative}}}{N_{\text{total words}}}$$

## Example

An earnings call transcript has 5,000 words. The word "headwinds" appears 8 times ($f = 8$, $\text{TF} = 0.0016$). Across 10,000 earnings transcripts in the corpus, "headwinds" appears in 200 ($\text{IDF} = \log(10000/200) = 3.91$). TF-IDF $= 0.0016 \times 3.91 = 0.006$.

Using a financial sentiment lexicon (e.g. Loughran–McDonald), the same transcript has 120 positive words, 85 negative, and 5,000 total: $S = (120 - 85)/5000 = 0.007$, a mildly positive tone. A regression shows this score predicts next-day excess returns of $+0.3\%$ on average.

## Remember

NLP is the primary tool for extracting alpha from **alternative text data** in quantitative finance: earnings call transcripts, central bank statements, analyst reports, news wires, and social media. The Loughran–McDonald sentiment dictionary is preferred over general-purpose dictionaries (e.g. Harvard GI) because financial language is domain-specific — "liability" is negative in everyday speech but neutral in a balance sheet context. Modern NLP pipelines replace TF-IDF with transformer-based embeddings (BERT, FinBERT) that capture context, but TF-IDF remains a strong baseline for document classification and is directly interpretable.
