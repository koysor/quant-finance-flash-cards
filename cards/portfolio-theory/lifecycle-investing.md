# Lifecycle Investing and Glide Paths

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** lifecycle investing, glide path, target-date fund, human capital, retirement, equity allocation
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

Lifecycle investing holds that optimal equity allocation should **decline as an investor ages**: a young investor's total wealth is mostly future labour income (human capital), which is bond-like, so financial wealth should tilt heavily to equities. As human capital is depleted and financial wealth accumulates, the financial portfolio must become more conservative. A **glide path** is the pre-specified schedule of this declining equity weight.

## Key Formula

The "100 minus age" rule of thumb sets the equity weight in financial wealth as:

$$w_{\text{equity}}(a) = \max\!\left(w_{\min},\; 1 - \frac{a}{100}\right)$$

The economic motivation is that total wealth $W_{\text{total}}$ should hold roughly constant equity exposure:

$$w_{\text{equity}} \cdot W_F + HC(a) \approx \text{target equity value}$$

where $W_F$ is financial wealth and $HC(a) = \int_a^{65} \text{salary}(s)\, e^{-r(s-a)}\,ds$ is the present value of remaining labour income, which declines towards zero at retirement. As $HC$ falls, $w_{\text{equity}}$ must rise to maintain total equity exposure — but in practice most glide paths reduce both $HC$ and $w_{\text{equity}} \cdot W_F$, reflecting growing risk aversion near retirement.

## Example

Age 30: savings £50,000; human capital (PV of future earnings) ≈ £500,000.  
At $w_{\text{equity}} = 70\%$: financial equities = £35,000. Total "bond" exposure = £15,000 + £500,000 = £515,000.  
Total equity/total wealth = £35,000 / £550,000 ≈ 6% — appropriate for a young investor with job security.

Age 60: savings £500,000; human capital ≈ £100,000.  
At $w_{\text{equity}} = 40\%$: financial equities = £200,000. Total equity/total wealth = £200,000 / £600,000 ≈ 33%.

The equity share of total wealth rises from 6% to 33% even though the financial equity weight fell, because human capital fell much faster.

## Remember

Target-date funds (TDFs) — marketed as "fund 2050" or "fund 2060" — implement glide paths automatically, reducing equity exposure as the named retirement date approaches. They are the default investment in UK auto-enrolment pension schemes and US 401(k) plans, managing over \$3 trillion in assets globally. The key practical criticism is that the "100 minus age" rule ignores the **riskiness of human capital**: a miner's earnings correlate strongly with commodity equities (reducing diversification), while a government employee's are nearly riskless. Optimal glide paths should be calibrated to profession, salary volatility, and wealth level, not age alone.
