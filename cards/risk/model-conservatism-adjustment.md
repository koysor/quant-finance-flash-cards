# Model Conservatism Adjustment

**Topic:** Risk
**Tags:** model conservatism, capital add-on, model validation, FRTB, regulatory capital, model uncertainty
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

A **model conservatism adjustment** (also called a **model add-on** or **prudential valuation adjustment**) is an additional capital reserve applied when independent model validation reveals that a model systematically underestimates risk or fair-value uncertainty. It is the quantitative regulatory response to model risk.

## Key Formula

Under FRTB and EBA prudent valuation rules, the Additional Valuation Adjustment (AVA) for model uncertainty is:

$$\text{AVA}_{\text{model}} = \max\!\left(0,\; V_{\text{exit}} - V_{\text{model}}\right) \times (1 - \text{confidence level})$$

where $V_{\text{exit}}$ is the prudent exit price (estimated at 90% confidence from an alternative model range) and $V_{\text{model}}$ is the mark-to-model value. Banks must hold capital covering the difference at a 90% confidence level across all positions.

## Example

A bank prices a long-dated correlation swap using a Gaussian copula model at fair value $\$10\text{m}$. An independent validation team uses two alternative models and finds plausible values ranging from $\$8.5\text{m}$ to $\$11.5\text{m}$. The 90th percentile of the exit price distribution is $\$9.2\text{m}$, implying an AVA of $\$10\text{m} - \$9.2\text{m} = \$0.8\text{m}$. This $\$0.8\text{m}$ must be deducted from CET1 capital, directly reducing the bank's regulatory capital ratio.

## Remember

Model conservatism adjustments are the financial penalty for model risk — they translate the abstract concern that a model might be wrong into a concrete capital charge that affects return on equity. In practice, they create a strong incentive for banks to invest in better models and more rigorous validation: a 1% AVA on a $\$1\text{bn}$ book costs $\$10\text{m}$ in regulatory capital, generating an ROE drag of roughly 15bp at a 15% capital cost. The prudent valuation framework under FRTB (Article 105 of CRR) requires AVAs for ten risk categories, with model uncertainty being the most significant for exotic derivatives desks.
