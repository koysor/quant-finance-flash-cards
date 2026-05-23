# SentencePiece

**Topic:** Computational Finance
**Tags:** tokenisation, nlp, subword, vocabulary, multilingual, text preprocessing
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**SentencePiece** is a language-agnostic subword tokenisation library developed by Google that treats text as a raw unicode character sequence — including spaces — and learns a vocabulary of subword units directly from the data using either Byte-Pair Encoding (BPE) or unigram language model training. It is the tokeniser used in T5, XLNet, and multilingual models such as mBERT and XLM-RoBERTa.

## Key Formula

The **unigram language model** variant selects a vocabulary $V$ of size $|V|$ by maximising the log-likelihood of the training corpus $\mathcal{D}$ under a unigram model:

$$\mathcal{L}(V) = \sum_{x \in \mathcal{D}} \log P(x), \quad P(x) = \max_{\mathbf{s} \in S(x)} \prod_{i=1}^{|s|} p(s_i)$$

where $S(x)$ is the set of all possible segmentations of sentence $x$ and $p(s_i)$ is the unigram probability of subword $s_i$. Subwords that contribute least to $\mathcal{L}$ when removed are pruned iteratively until $|V|$ is reached.

## Example

Tokenising the financial phrase "overcollateralisation" with a SentencePiece vocabulary trained on financial text:

| Vocabulary type | Tokens |
|---|---|
| General BPE (GPT-2) | `["over", "coll", "ateral", "is", "ation"]` |
| SentencePiece (finance) | `["▁over", "collateral", "isation"]` |

The `▁` (underscore) prefix marks word boundaries — replacing the whitespace before a token — so the model can reconstruct the original string exactly, including spacing, without any separate pre-tokenisation step.

## Remember

SentencePiece's key advantage in financial NLP is **language-agnosticism and reproducibility**: because it treats raw bytes rather than pre-split words as input, the same model can tokenise English filings, Japanese annual reports, and multilingual ESG disclosures without any language-specific preprocessing. For global quant teams parsing foreign-language regulatory documents, SentencePiece tokenisation means the model's vocabulary can be shared across languages, and a single fine-tuned multilingual model (e.g. XLM-RoBERTa) can extract sentiment and named entities from cross-border M&A filings without building a separate pipeline per jurisdiction.
