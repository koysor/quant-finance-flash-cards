# SASB Materiality Map

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** sasb, esg, materiality, sustainability, factor model, responsible investing
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **SASB (Sustainability Accounting Standards Board) Materiality Map** is a framework that identifies which Environmental, Social, and Governance (ESG) issues are **financially material** — likely to affect a company's cash flows, risk profile, or cost of capital — for each of 77 industry sectors. Materiality varies by industry: greenhouse gas emissions are material for oil and gas but less so for software companies.

## Key Formula

SASB organises ESG issues across five sustainability dimensions:

| Dimension | Examples |
|---|---|
| Environment | GHG emissions, water usage, waste & hazardous materials |
| Social capital | Customer privacy, data security, access & affordability |
| Human capital | Employee safety, diversity, labour practices |
| Business model | Product design, supply chain management, innovation |
| Leadership & governance | Business ethics, systemic risk, competitive behaviour |

Materiality is determined by whether an issue affects the **long-run equity value**:

$$\Delta V = \int_0^{\infty} e^{-rt}\, \Delta \text{CF}_t\, dt$$

A material ESG issue is one that significantly alters expected future cash flows $\Delta \text{CF}_t$ or the discount rate $r$ for a given industry.

## Example

For a food & beverage company, SASB identifies water management and food safety as material (a contamination event or drought directly reduces revenue and raises costs). For a commercial bank, SASB identifies data security and systemic risk management as material, but GHG emissions as less material — reflecting that the bank's business model risk is concentrated in information infrastructure and credit cycles, not physical operations.

## Remember

SASB materiality is the bridge between qualitative ESG data and quantitative factor models: it tells a quant researcher which ESG signals to use as input features for a given industry, preventing the inclusion of immaterial ESG metrics that add noise without alpha. Major asset managers (BlackRock, Vanguard) use SASB-aligned frameworks to assess ESG risk in fixed income and equity portfolios, and IFRS Sustainability Disclosure Standards (S1/S2) explicitly reference SASB industry-specific metrics for corporate sustainability reporting, making SASB fluency increasingly expected in portfolio management and credit risk roles.
