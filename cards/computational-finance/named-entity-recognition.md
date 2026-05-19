# Named Entity Recognition

**Topic:** Computational Finance
**Tags:** nlp, sequence labelling, bert, information extraction, alternative data, text mining
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Named Entity Recognition (NER)** is an NLP task that identifies and classifies named entities — organisations, monetary values, dates, people, and locations — in raw text by assigning a structured label to each token, converting unstructured financial documents into queryable, structured data.

## Key Formula

NER is framed as **token-level sequence labelling** using the BIO scheme (Beginning, Inside, Outside). A BERT encoder produces a contextual embedding $\mathbf{h}_t \in \mathbb{R}^{768}$ for each token $t$; a linear head converts it to label probabilities:

$$P(y_t \mid \mathbf{h}_t) = \text{softmax}\!\left(\mathbf{W}\,\mathbf{h}_t + \mathbf{b}\right), \quad \mathbf{W} \in \mathbb{R}^{L \times 768}$$

where $L$ is the number of label types (e.g. B-ORG, I-ORG, B-MONEY, I-MONEY, O). The model is fine-tuned by minimising cross-entropy summed over all token positions:

$$\mathcal{L} = -\sum_{t=1}^{T} \log P\!\left(y_t^*\;\middle|\;\mathbf{h}_t\right)$$

where $y_t^*$ is the gold-standard label at position $t$.

## Example

Input: *"Apple Inc. reported \$2.4 billion in net income, beating JPMorgan's estimate of \$2.1 billion."*

| Token | Predicted label | Entity |
|---|---|---|
| Apple | B-ORG | ↗ Apple Inc. |
| Inc. | I-ORG | ↗ |
| \$2.4 | B-MONEY | ↗ \$2.4 billion |
| billion | I-MONEY | ↗ |
| JPMorgan's | B-ORG | ↗ JPMorgan |
| \$2.1 | B-MONEY | ↗ \$2.1 billion |
| billion | I-MONEY | ↗ |
| All others | O | — |

Extracted automatically: firms = {Apple Inc., JPMorgan}, amounts = {\$2.4B, \$2.1B}. Combined across 10,000 press releases, this builds a structured earnings database without human data entry.

## Remember

NER is the **structuring layer** of financial NLP pipelines: raw text from earnings releases, analyst reports, and regulatory filings is transformed into a queryable knowledge graph of company names, monetary figures, and dates. This enables downstream quantitative strategies that were previously impossible — for example, systematically extracting every analyst price target revision from sell-side PDFs and constructing a daily cross-sectional signal from consensus drift, or mapping undisclosed supply-chain relationships by tracking entity co-mentions across 10-K filings. Modern financial NER models are fine-tuned BERT variants (SpaCy's en_core_web_trf, or custom models trained on annotated SEC data) that achieve F1 > 0.90 on financial entity types.
