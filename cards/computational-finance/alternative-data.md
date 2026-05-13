# Alternative Data

**Topic:** Computational Finance
**Tags:** alternative data, satellite imagery, sentiment, nlp, alpha generation, esg
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Alternative data** refers to non-traditional information sources used by quantitative investors to generate alpha signals beyond what is available in standard market data (price, volume) and financial statements (earnings, dividends). It typically requires specialist data acquisition and NLP or computer vision processing pipelines before it can be fed into a model.

## Key Formula

A generic alpha signal construction pipeline from raw alternative data:

$$\alpha_t = f_{\boldsymbol{\theta}}\!\left(\text{AltData}_t\right), \quad \text{IC} = \text{corr}\!\left(\alpha_t,\, r_{t+h}\right)$$

| Category | Examples | Signal type |
|---|---|---|
| Satellite | Parking lot occupancy, oil tank levels | Retail sales, supply proxy |
| Social / NLP | Twitter sentiment, Reddit discussions | Momentum, event-driven |
| Credit-card transactions | Spend by merchant category | Revenue nowcast |
| Job postings | Hiring by department | Business cycle, R&D proxy |
| Web traffic | App downloads, search trends | Product demand |

## Example

A quant fund acquires satellite imagery of supermarket car parks across 500 US locations. Using computer vision to count vehicles per day, they construct a same-store sales proxy one month before the official earnings report. Cross-sectionally, retailers with unusually high car park occupancy in the 30 days before earnings outperform by 2.3% on announcement — a signal invisible to earnings-watching discretionary funds.

## Remember

Alternative data is the primary source of new alpha in modern quantitative equity investing precisely because standard data (price, earnings) is immediately arbitraged away. The edge is not the data itself but the ability to process it — NLP pipelines for earnings call transcripts, computer vision for satellite imagery, and graph analysis for supply chain networks. Regulatory constraints matter: alternative data must not constitute material non-public information (MNPI) or breach data privacy regulations (GDPR, CCPA), making legal review part of the data acquisition process in any institutional setting.
