# Survivorship Bias

**Topic:** Statistics
**Level:** A Level Mathematics
**Tags:** survivorship bias, selection bias, backtesting, data quality, research pitfall
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Survivorship bias is a form of selection bias that occurs when a dataset includes only entities that have "survived" a selection process and excludes those that failed, were delisted, or disappeared. In finance, this most commonly arises when historical stock databases include only companies that still exist today, omitting those that went bankrupt, were acquired, or delisted. Analyses run on survivor-only data systematically overestimate returns and underestimate risk.

## Key Formula

The **survivorship bias** in average returns:

$$\text{Bias} = \bar{R}_{\text{survivors}} - \bar{R}_{\text{all}}$$

If $n_s$ survivors have mean return $\bar{R}_s$ and $n_d$ delisted firms have mean return $\bar{R}_d$:

$$\bar{R}_{\text{all}} = \frac{n_s \cdot \bar{R}_s + n_d \cdot \bar{R}_d}{n_s + n_d}$$

$$\text{Bias} = \bar{R}_s - \bar{R}_{\text{all}} = \frac{n_d}{n_s + n_d} \times (\bar{R}_s - \bar{R}_d)$$

The bias grows with the delisting rate and the return gap between survivors and non-survivors.

## Example

A universe of 1,000 stocks existed in 2010. By 2025, 800 survive (average return +9% p.a.) and 200 were delisted (average return $-15\%$ p.a. up to delisting):

$$\bar{R}_{\text{all}} = \frac{800 \times 9\% + 200 \times (-15\%)}{1{,}000} = \frac{72\% - 30\%}{10} = 4.2\%$$

$$\text{Bias} = 9\% - 4.2\% = 4.8\% \text{ per annum}$$

A researcher using only the 800 surviving stocks would conclude the market returned 9% per year, when the true return was 4.2% — an overstatement of 4.8 percentage points annually. A backtest of a value strategy on this data would appear far more profitable than it actually was.

## Remember

Survivorship bias is one of the most insidious errors in quantitative finance because it inflates returns silently — the missing data leaves no visible gap. Academic studies estimate the bias in US equity mutual fund databases at 0.5–1.5% per year, and in hedge fund databases at 2–5% per year (due to higher attrition). Any serious backtest must use a survivorship-bias-free database that includes delisted securities with their full return history up to delisting. The bias is particularly dangerous for value and distressed-debt strategies, where the stocks most likely to be delisted (bankruptcies) are exactly the ones the strategy would have held.
