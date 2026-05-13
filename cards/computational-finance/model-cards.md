# Model Cards

**Topic:** Computational Finance
**Tags:** model cards, model documentation, explainability, regulatory compliance, responsible ai, bias
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **model card** is a standardised one- to two-page document that describes a machine learning model's intended use, performance characteristics, limitations, and potential biases. Introduced by Google (Mitchell et al., 2019), model cards are increasingly required by financial regulators as part of model risk management (MRM) frameworks to ensure ML models are deployed transparently and responsibly.

## Key Formula

A model card has no single mathematical formula, but its performance section typically reports disaggregated metrics across population slices:

$$\text{Report: } \left\{\text{Metric}(m) \;\middle|\; m \in \{\text{Accuracy, F1, AUC, IC}\},\; \text{slice} \in \{\text{age, geography, product}\}\right\}$$

**Standard sections:**

| Section | Content |
|---|---|
| Model details | Algorithm, version, training date |
| Intended use | Primary use cases; out-of-scope uses |
| Factors | Demographic, geographic, or behavioural variables affecting performance |
| Metrics | Performance measures and evaluation thresholds |
| Training data | Source, date range, preprocessing steps |
| Limitations | Known failure modes, edge cases |

## Example

A credit scoring model card: Intended use — personal loan decisions for UK retail customers. Metrics — AUC 0.82 on 2022–2024 test data. Disaggregated: AUC 0.84 for applicants aged 30–50, AUC 0.76 for applicants aged 18–25. Limitation — reduced performance for applicants with fewer than 12 months of credit history. Out-of-scope — corporate lending, mortgage underwriting.

## Remember

Model cards are the ML analogue of a product prospectus: they give regulators, auditors, and model risk managers a structured summary of what a model does, for whom it works, and where it fails. Under the UK FCA's Consumer Duty and the EU AI Act's requirements for high-risk AI systems, financial institutions must demonstrate that credit scoring, insurance pricing, and investment recommendation models are not producing systematically biased outcomes across protected characteristics — and model cards are the primary vehicle for this disclosure. They also serve as institutional memory when model developers leave the firm.
