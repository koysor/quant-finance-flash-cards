# Loughran-McDonald Sentiment Word List

**Topic:** Computational Finance
**Tags:** sentiment analysis, nlp, text mining, alternative data, 10-k, financial lexicon
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **Loughran-McDonald (L&M) Sentiment Word List** is a domain-specific financial lexicon that classifies words in regulatory filings into sentiment categories — Negative, Positive, Uncertainty, Litigious, Strong Modal, and Weak Modal — accounting for the fact that common words carry different polarity in financial documents than in everyday language.

## Key Formula

**Net tone** of a document with $N_{\text{total}}$ words:

$$\text{Tone} = \frac{N_{\text{pos}} - N_{\text{neg}}}{N_{\text{pos}} + N_{\text{neg}}}$$

**Uncertainty ratio** (proportion of hedging language):

$$U = \frac{N_{\text{uncertain}}}{N_{\text{total}}}$$

where $N_{\text{pos}}$, $N_{\text{neg}}$, $N_{\text{uncertain}}$ are counts of words matching the corresponding L&M category lists. A more negative Tone or higher $U$ signals managerial pessimism or opacity about future outcomes.

## Example

A technology company's 10-K filing contains 8,000 words. Applying the L&M dictionary: $N_{\text{neg}} = 180$, $N_{\text{pos}} = 54$, $N_{\text{uncertain}} = 110$.

$$\text{Tone} = \frac{54 - 180}{54 + 180} = \frac{-126}{234} \approx -0.54$$

$$U = \frac{110}{8{,}000} = 0.0138$$

Both metrics are significantly more negative than sector peers, flagging elevated downside risk. A cross-sectional regression shows that companies in the bottom Tone quintile underperform peers by approximately 3% over the subsequent 12 months.

## Remember

The L&M list was built specifically because general-purpose dictionaries (e.g. Harvard General Inquirer) misclassify financial language: "liability", "capital", and "tax" are marked negative by Harvard GI but are neutral in a balance sheet context. Loughran and McDonald (2011) showed Harvard GI misclassified 73.8% of negative-word occurrences in 10-K filings. The L&M list is now the standard lexicon for academic and practitioner analysis of SEC filings, earnings transcripts, and central bank statements — any context where financial domain-specificity matters and general sentiment tools would produce noise.
