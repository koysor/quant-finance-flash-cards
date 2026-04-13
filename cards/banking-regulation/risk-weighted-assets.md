# Risk-Weighted Assets

**Topic:** Banking Regulation
**Tags:** risk-weighted assets, rwa, capital ratio, standardised approach, credit risk
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Risk-Weighted Assets (RWA) are a bank's total assets and off-balance-sheet exposures, each scaled by a regulatory risk weight that reflects the riskiness of the counterparty or asset class. RWA is the denominator of all Basel capital ratios; by assigning lower weights to safer assets, the framework allows banks to hold proportionally less capital against low-risk portfolios.

## Key Formula

$$\text{RWA} = \sum_{i} \text{Exposure}_i \times w_i$$

Under the Standardised Approach, risk weights are set by the regulator based on credit rating or asset class:

| Asset | Risk weight $w$ |
|---|---|
| Cash and central bank reserves | 0% |
| Sovereign debt (AAA–AA rated) | 0% |
| Residential mortgages | 35% |
| Unrated corporate loans | 100% |
| Subordinated debt | 150% |

Under the Internal Ratings-Based (IRB) approach, banks use their own PD and LGD estimates to calculate risk weights, typically producing lower RWA than Standardised for high-quality portfolios.

## Example

A bank has three assets: £200 m government bonds ($w = 0\%$), £500 m residential mortgages ($w = 35\%$), and £300 m corporate loans ($w = 100\%$).

$$\text{RWA} = 0 + 0.35 \times £500\text{m} + 1.00 \times £300\text{m} = £475\text{m}$$

With a CET1 ratio requirement of 7%, the bank must hold £33.25 m of CET1 — far less than the 7% of total assets (£70 m) that a leverage-based rule would require.

## Remember

The choice of RWA methodology directly affects a bank's competitive position: two banks with identical balance sheets but different model approvals (Standardised vs. Advanced IRB) may face capital requirements differing by 30–40%. This creates powerful incentives for banks to invest in IRB models — but also creates the "RWA variability" problem that Basel IV's output floor (75% of Standardised RWA) was designed to address, preventing banks from using internal models to produce unrealistically low capital requirements.
