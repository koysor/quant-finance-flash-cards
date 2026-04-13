# Backtesting VaR

**Topic:** Banking Regulation
**Tags:** backtesting, var, traffic light zones, hpl, model validation
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

VaR backtesting is the mandatory regulatory process of comparing a bank's daily VaR forecast against realised profit or loss to assess whether the model is calibrated correctly. Regulators require banks to use two P&L measures: Hypothetical P&L (HPL — what the unchanged portfolio would have earned, eliminating the noise of intraday trading) and Risk-Theoretical P&L (RTPL — the P&L the risk model itself produces). An **exception** occurs when the actual loss exceeds the VaR forecast.

## Key Formula

The number of exceptions $E$ in the last 250 trading days determines the regulatory capital multiplier $k$:

| Zone | Exceptions $E$ | Capital multiplier $k$ |
|---|---|---|
| Green | 0–4 | 1.5 (base) |
| Yellow | 5–9 | 1.5 + graduated addition |
| Red | 10+ | 2.0 (model must be fixed) |

For a well-calibrated 99% VaR model the expected number of exceptions in 250 days is:

$$E[\text{exceptions}] = 250 \times (1 - 0.99) = 2.5$$

## Example

A bank runs a 1-day 99% VaR model and records 7 exceptions over 250 days. Under the traffic light system this falls in the **Yellow zone**. The capital multiplier rises above 1.5, increasing the market risk capital charge even if individual exceptions were small. The model must be reviewed and parameters recalibrated before the count falls back to Green.

## Remember

The traffic light system creates a direct link between model quality and capital cost: a VaR model that produces too many exceptions becomes progressively more expensive to run, incentivising banks to maintain well-calibrated models. The distinction between HPL and RTPL also matters — under FRTB, a large gap between the two (the P&L attribution test) signals that the risk model does not explain what it claims to, triggering a shift from Internal Model Approach to the more conservative Standardised Approach.
