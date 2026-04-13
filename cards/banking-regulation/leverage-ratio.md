# Leverage Ratio

**Topic:** Banking Regulation
**Tags:** leverage ratio, tier 1 capital, total exposure, backstop, basel iii
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The leverage ratio is a non-risk-based capital backstop that expresses Tier 1 capital as a fraction of total exposure — the sum of all on- and off-balance-sheet items measured without risk-weighting. Unlike RWA-based ratios, it treats a £1 government bond and a £1 sub-prime loan identically, preventing banks from artificially inflating their risk-adjusted capital ratios by concentrating in assets with low regulatory risk weights.

## Key Formula

$$\text{Leverage Ratio} = \frac{\text{Tier 1 Capital}}{\text{Total Exposure Measure}} \geq 3\%$$

The **Total Exposure Measure** includes:
- On-balance-sheet assets (at accounting values, not risk-weighted)
- Off-balance-sheet exposures: derivatives (converted using the SA-CCR method), securities financing transactions (repo/reverse repo), and undrawn credit facilities

Basel III minimum: **3%** for all banks; higher buffers apply to Global Systemically Important Banks (G-SIBs).

## Example

A bank has Tier 1 capital of £10 bn, loans of £200 bn, government bonds of £100 bn, and off-balance-sheet derivative exposures of £50 bn (SA-CCR equivalent). Total exposure = £350 bn.

$$\text{Leverage Ratio} = \frac{£10\text{bn}}{£350\text{bn}} = 2.86\%$$

This breaches the 3% minimum despite the bank potentially having a healthy CET1 ratio, because the large government bond portfolio — zero risk-weighted — still contributes to the leverage exposure base.

## Remember

The leverage ratio gained prominence after 2008 when banks like Deutsche Bank had risk-based capital ratios above the minimum while carrying leverage of 40:1 or more on their balance sheets — a level that made them acutely vulnerable to small declines in asset values. For quants designing trading strategies, the leverage ratio creates a binding constraint separate from risk-weighted capital: a strategy that is capital-efficient on a risk-weighted basis (e.g., long government bonds) may still consume precious leverage capacity and trigger balance-sheet constraints at quarter-end.
