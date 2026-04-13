# Basel IV Output Floor

**Topic:** Banking Regulation
**Tags:** output floor, irb, standardised approach, rwa, basel iv
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Basel IV output floor is a regulatory constraint that prevents a bank's internally-modelled Risk-Weighted Assets from falling below 72.5% of what the Standardised Approach would produce for the same portfolio. It was finalised in 2017 as part of the "Basel IV" package (officially the finalisation of Basel III) to address the observation that IRB banks had produced wildly varying — and often implausibly low — capital requirements for identical exposures.

## Key Formula

For each capital category (credit, market, operational risk):

$$RWA_{\text{floored}} = \max\!\left(RWA_{\text{model}},\; 72.5\% \times RWA_{\text{SA}}\right)$$

The floor applies at the consolidated group level, meaning portfolios where internal models produce low RWA are cross-subsidised by portfolios where they exceed the floor.

The implied capital requirement including the floor:

$$\text{Capital} = \max\!\left(RWA_{\text{IRB}},\; 0.725 \times RWA_{\text{SA}}\right) \times k$$

where $k$ is the applicable capital ratio (e.g., 8% Total Capital, 7% CET1).

## Example

A bank with a £500 bn mortgage book estimates IRB RWA of £50 bn (10% density). The Standardised Approach produces £175 bn (35% density). The floor requires: $\max(50, 0.725 \times 175) = \max(50, 126.9) = £126.9\text{bn}$. The bank must hold capital against £126.9 bn rather than £50 bn — a 154% increase in capital requirement for the mortgage book, potentially requiring billions in additional CET1.

## Remember

The output floor fundamentally changes the economics of IRB approval: for banks with large mortgage books or SME portfolios where IRB risk weights are far below Standardised, the floor reduces the capital benefit to at most 27.5% of the Standardised requirement. Banks that invested heavily in IRB models for capital savings will need to reassess whether the regulatory overhead (model maintenance, validation, supervisory review) remains worthwhile when the floor limits the achievable saving. Implementation is phased in from 2025 to 2030 to allow banks to raise capital incrementally.
