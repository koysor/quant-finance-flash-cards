# Non-Modellable Risk Factor (NMRF)

**Topic:** Risk
**Tags:** NMRF, FRTB, expected shortfall, capital, regulation, market risk
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

A **Non-Modellable Risk Factor (NMRF)** is a risk factor in a trading book that fails the FRTB **Risk Factor Eligibility Test (RFET)** — a regulatory criterion requiring that the factor has at least 24 real price observations in the preceding 12 months, with no gap exceeding 90 days. Risk factors that fail this test cannot be included in the firm's internal model and must instead be capitalised separately using a **stress scenario** approach.

## Key Formula

The NMRF capital charge uses a **stressed expected shortfall** calculated from a single worst-case stress scenario rather than from a historical simulation. For each NMRF $i$, the stress scenario loss $SES_i$ is determined and the aggregate NMRF charge is:

$$K_{\text{NMRF}} = \sqrt{\sum_{i \in \text{uncorrelated}} SES_i^2 \;+\; \left(\sum_{j \in \text{correlated}} SES_j\right)^2}$$

where "correlated" NMRFs share a common underlying bucket and "uncorrelated" NMRFs are bucketed separately. The formula applies a square-root aggregation (assuming zero correlation) across buckets, but a simple sum (assuming perfect correlation) within each bucket.

## Example

A bank trades an illiquid emerging-market interest rate swap. The underlying curve point (say, the 7-year NGN swap rate) has only 10 real price observations over the past year — well below the RFET threshold of 24. It is therefore classified as an NMRF.

The risk team determines the worst-case stress scenario for this curve point: a 300 basis point move. If the bank's position has a DV01 (dollar value of a basis point) of $50,000, the scenario loss is:

$$SES = 300 \times \$50{,}000 = \$15{,}000{,}000$$

This $15 million charge is included in the NMRF aggregation, in addition to the firm's standard IMA capital charge. In practice, NMRF charges are significantly larger per unit of risk than modellable-factor charges because no diversification credit is assumed.

## Remember

NMRFs are a key feature of the **FRTB** (Fundamental Review of the Trading Book, finalised under Basel III/IV). Before FRTB, banks could include virtually any risk factor in their internal model regardless of how illiquid or sparsely quoted it was. NMRFs force banks to confront the true cost of holding illiquid positions: the stressed ES charge is typically far higher than the equivalent IMA charge, creating a direct regulatory incentive to concentrate activity in liquid, well-observed markets and to exit positions in hard-to-observe curve points.
