# Probabilistic Sharpe Ratio

**Topic:** Statistics
**Tags:** probabilistic sharpe ratio, sharpe ratio, hypothesis testing, non-normality, multiple testing, Bailey Lopez de Prado
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

The **Probabilistic Sharpe Ratio (PSR)** is the probability that a strategy's true Sharpe ratio exceeds a benchmark Sharpe ratio $\text{SR}^*$, given a finite sample of returns. It was introduced by Bailey and López de Prado (2012) to correct the naïve Sharpe ratio for small sample size, non-normality (skewness and excess kurtosis), and the multiple testing problem that inflates observed Sharpes in backtests.

## Key Formula

$$\text{PSR}(\text{SR}^*) = \Phi\!\left[\frac{(\widehat{\text{SR}} - \text{SR}^*)\sqrt{T-1}}{\sqrt{1 - \hat{\gamma}_3\,\widehat{\text{SR}} + \tfrac{\hat{\gamma}_4 - 1}{4}\,\widehat{\text{SR}}^2}}\right]$$

where $\Phi$ is the standard normal CDF, $\widehat{\text{SR}}$ is the sample Sharpe ratio (annualised), $T$ is the number of return observations, $\hat{\gamma}_3$ is the sample skewness, and $\hat{\gamma}_4$ is the sample excess kurtosis. For normally distributed returns ($\hat{\gamma}_3 = 0$, $\hat{\gamma}_4 = 0$), the denominator simplifies to $\sqrt{1 + \tfrac{1}{2}\widehat{\text{SR}}^2}$ (the standard error of the Sharpe ratio).

## Example

A strategy is backtested with $T = 60$ monthly observations and produces $\widehat{\text{SR}} = 1.2$ (annualised), with skewness $\hat{\gamma}_3 = -0.5$ (left-skewed) and excess kurtosis $\hat{\gamma}_4 = 1.0$ (fat tails). Setting benchmark $\text{SR}^* = 1.0$:

The adjusted standard error of the Sharpe: $\sqrt{1 - (-0.5)(1.2) + \tfrac{1.0}{4}(1.2)^2} / \sqrt{59} \approx 0.155$

$$\text{PSR}(1.0) = \Phi\!\left[\frac{(1.2 - 1.0)}{0.155}\right] = \Phi(1.29) \approx 90.2\%$$

With Gaussian returns the PSR would be 92.1% — the fat tails and negative skew reduce confidence by about 2 percentage points. With only $T = 12$ observations the PSR drops to 67%, making the strategy statistically weak.

## Remember

The PSR operationalises the question every quant should ask before deploying a strategy: "how likely is it that this backtest Sharpe is genuine?" A PSR above 95% (with a reasonable benchmark SR* such as 0 or the risk-free-rate equivalent) is the quantitative analogue of a p-value below 5%. The formula's most important practical use is determining the **minimum track record length**: given a target PSR of 95% and an observed SR, one can solve for the minimum $T$ needed — strategies with high vol, negative skew, and fat tails require much longer track records to reach the same confidence level as clean, normally distributed return streams.

