# Return on Equity

**Topic:** Financial Mathematics
**Tags:** return on equity, roe, dupont, leverage, profitability
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Return on equity (ROE) measures the profit a company generates per unit of shareholders' equity. It captures how effectively management uses owners' capital to produce earnings and is one of the most widely tracked profitability metrics in fundamental analysis.

## Key Formula

$$\text{ROE} = \frac{\text{Net Income}}{\text{Shareholders' Equity}}$$

The **DuPont decomposition** breaks ROE into three drivers:

$$\text{ROE} = \underbrace{\frac{\text{Net Income}}{\text{Revenue}}}_{\text{Profit Margin}} \times \underbrace{\frac{\text{Revenue}}{\text{Total Assets}}}_{\text{Asset Turnover}} \times \underbrace{\frac{\text{Total Assets}}{\text{Equity}}}_{\text{Equity Multiplier}}$$

The equity multiplier is simply $1 + \text{D/E}$, making it the leverage component of ROE.

## Example

A company reports net income of £12 million, revenue of £200 million, total assets of £150 million, and equity of £50 million.

- Profit margin: $12 / 200 = 6\%$
- Asset turnover: $200 / 150 = 1.33$
- Equity multiplier: $150 / 50 = 3.0$ (i.e. D/E = 2.0)

$$\text{ROE} = 6\% \times 1.33 \times 3.0 = 24\%$$

Without leverage (equity multiplier = 1), ROE would be only 8%. The 3x leverage triples it to 24% — but would equally triple losses if the business turned unprofitable.

## Remember

ROE is a key metric in quantitative equity screening and factor models. The DuPont decomposition reveals that a high ROE can come from genuine operational efficiency (high margin or turnover) **or** from financial leverage (high equity multiplier). Quantitative analysts must distinguish between the two because leverage-driven ROE is fragile — it collapses in downturns when earnings fall but debt obligations remain fixed. Screening for high ROE combined with low D/E identifies companies with sustainable profitability, which is a well-documented quality factor in models like Fama–French five-factor.
