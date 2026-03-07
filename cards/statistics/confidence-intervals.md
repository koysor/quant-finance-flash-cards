# Confidence Intervals

**Topic:** Statistics
**Tags:** inference, estimation, confidence level, margin of error, sampling, uncertainty
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A **confidence interval** is a range of values, computed from sample data, that is expected to contain the true population parameter with a specified probability (the **confidence level**). A 95% confidence interval means that if the sampling procedure were repeated many times, approximately 95% of the resulting intervals would contain the true value.

## Key Formula

For a population mean with known $\sigma$:

$$\bar{X} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

With unknown $\sigma$ (using the $t$-distribution):

$$\bar{X} \pm t_{\alpha/2,\, n-1} \cdot \frac{s}{\sqrt{n}}$$

The **margin of error** is $E = z_{\alpha/2} \cdot \sigma / \sqrt{n}$. To halve the margin of error, the sample size must be quadrupled.

## Example

A quant estimates annualised volatility from $n = 60$ monthly returns, obtaining $\bar{\sigma} = 18\%$ with sample standard deviation $s = 3.2\%$.

A 95% confidence interval for the true volatility estimate uses $t_{0.025,\,59} \approx 2.00$:

$$18\% \pm 2.00 \times \frac{3.2\%}{\sqrt{60}} = 18\% \pm 0.83\%$$

$$[17.17\%,\ 18.83\%]$$

We are 95% confident that the true mean volatility lies between 17.17% and 18.83%.

## Remember

Confidence intervals quantify the uncertainty around every estimated quantity in finance — expected returns, volatilities, betas, Sharpe ratios, and VaR thresholds. A point estimate alone (e.g. "the Sharpe ratio is 1.2") is incomplete without knowing its precision. The confidence interval for annualised Sharpe ratio has width proportional to $1/\sqrt{n}$, meaning short track records produce very wide intervals — a fund with 3 years of monthly data has such wide confidence bounds that a Sharpe ratio of 1.0 is often statistically indistinguishable from zero. This is why institutional investors demand long track records and why quants must report uncertainty alongside performance metrics.
