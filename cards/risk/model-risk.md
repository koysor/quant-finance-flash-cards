# Model Risk

**Topic:** Risk
**Tags:** model risk, model validation, mis-specification, regulatory capital, FRTB, governance
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Model risk** is the risk of financial loss or incorrect decision-making arising from errors in a quantitative model's assumptions, calibration, implementation, or inappropriate use. It is formally recognised as a sub-category of operational risk under Basel III and is subject to explicit governance requirements.

## Key Formula

Model risk is typically quantified as the spread of outputs across a set of plausible alternative models $\{M_1, \ldots, M_k\}$:

$$\text{Model Uncertainty} = \max_i V(M_i) - \min_i V(M_i)$$

where $V(M_i)$ is the fair value or risk measure produced by model $M_i$. Regulators also require a **P&L explain** test: if the model-predicted P&L diverges from actual P&L beyond a threshold, the model fails validation.

## Example

A bank prices an exotic interest rate option using a Hull–White one-factor model calibrated to the swap curve. An alternative two-factor model produces a fair value 8% higher. The 8% spread is the model uncertainty for that instrument. Under FRTB, the bank must hold additional capital if internal model outputs cannot be validated against independent benchmarks, incentivising investment in model validation infrastructure.

## Remember

Model risk is not just theoretical — it has caused catastrophic real-world losses. JPMorgan's London Whale (2012, $~6.2bn loss) resulted partly from a spreadsheet error in a VaR model that halved the measured risk. The Basel Committee's SR 11-7 guidance requires banks to maintain a model inventory, validate all models independently, and reserve against model uncertainty. In quantitative finance, model risk is the institutional acknowledgement that every price, VaR figure, and Greeks report is conditional on model assumptions that could be wrong — and that this conditionality must be managed, not ignored.
