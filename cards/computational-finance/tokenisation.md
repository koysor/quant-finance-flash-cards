# Tokenisation (BPE / WordPiece)

**Topic:** Computational Finance
**Tags:** tokenisation, nlp, bert, subword, vocabulary, text preprocessing
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Tokenisation** is the process of splitting raw text into a sequence of discrete units (tokens) that a language model can process; modern NLP models use **subword** tokenisation algorithms — Byte-Pair Encoding (BPE) for GPT and WordPiece for BERT — that decompose rare words into known fragments, ensuring every string in any financial document can be represented without an unknown-word token.

## Key Formula

**BPE algorithm** (iterative merge rule): start with a character-level vocabulary, then repeatedly merge the most frequent adjacent pair $(a, b)$:

$$\text{score}(a, b) = \text{count}(ab), \qquad \text{merge: } (a, b) \to ab$$

After $V$ merges the vocabulary has size $|V_{\text{char}}| + V$. **WordPiece** uses a likelihood-based score instead:

$$\text{score}(a, b) = \frac{\text{count}(ab)}{\text{count}(a) \times \text{count}(b)}$$

This penalises merging frequent individual tokens and favours merges that most increase corpus likelihood — producing a vocabulary better suited to downstream fine-tuning tasks such as financial sentiment classification.

## Example

BERT's WordPiece vocabulary (size 30,522) tokenises financial jargon as follows:

| Input word | Tokens | Token IDs |
|---|---|---|
| *impairment* | `[impairment]` | 18458 |
| *overcollateralisation* | `[over, ##collateral, ##isation]` | 2058, 24806, 17435 |
| *EBITDA* | `[E, ##BI, ##TD, ##A]` | 142, 15682, 9998, 138 |

The `##` prefix marks continuation tokens. Even a word unseen during pre-training — e.g. a new ticker or coined acronym — is representable as a sequence of known subwords, preserving model functionality without retraining on an extended vocabulary.

## Remember

Tokenisation is the **first and irreversible step** in every financial NLP pipeline — a poor choice here degrades all downstream tasks. Domain-specific jargon poses a concrete problem: a general-purpose tokeniser trained on Wikipedia splits "EBITDA" into four meaningless characters, diluting the model's ability to learn its meaning. Two practical solutions used by quant teams: (1) **domain-adaptive pre-training** — continue pre-training BERT on SEC filings and earnings transcripts so the existing vocabulary develops better representations for financial subwords; (2) **vocabulary extension** — add high-frequency financial tokens (tickers, acronyms, regulatory abbreviations) directly to the tokeniser's vocabulary and initialise their embeddings from the average of their component subword embeddings.
