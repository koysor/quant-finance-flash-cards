# Deflated Sharpe Ratio

**Topic:** Statistics
**Tags:** Sharpe ratio, multiple testing, backtesting, data snooping, factor research, statistical significance
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

The Deflated Sharpe Ratio (DSR), introduced by Bailey and López de Prado (2014), adjusts a reported Sharpe ratio downward to account for the number of strategies tried, the non-normality of returns, and the length of the track record. It answers: given that the best Sharpe was selected from $N$ trials, what is the probability that the true Sharpe exceeds a benchmark?

## Key Formula

The DSR is the probability that the observed Sharpe ratio $\widehat{SR}$ exceeds the expected maximum Sharpe ratio under the null of no skill. It uses the Sharpe ratio benchmark:

$$\widehat{SR}^* \approx \left(1 - \gamma_E + \gamma_E \cdot \ln N\right)^{1/2} \cdot \left(\frac{1}{T-1}\right)^{1/2}$$

Where $N$ is the number of trials, $T$ is the number of observations, and $\gamma_E \approx 0.5772$ is the Euler-Mascheroni constant. The DSR is then:

$$DSR(\widehat{SR}^*) = \Phi\!\left(\frac{(\widehat{SR} - \widehat{SR}^*)\sqrt{T-1}}{\sqrt{1 - \hat{\gamma}_3\,\widehat{SR} + \tfrac{\hat{\gamma}_4 - 1}{4}\,\widehat{SR}^2}}\right)$$

Where $\hat{\gamma}_3$ is the skewness and $\hat{\gamma}_4$ is the excess kurtosis of returns. A DSR $> 0.95$ (i.e. $p < 0.05$ after deflation) is required to claim statistical significance.

## Example

A researcher tests $N = 100$ strategies on 3 years of daily data ($T = 756$) and reports the best Sharpe of $\widehat{SR} = 1.5$. The expected maximum under the null is $\widehat{SR}^* \approx 0.85$. With skewness $= -0.4$ and excess kurtosis $= 2.1$, the DSR $= 0.72$ — not significant. The researcher would need a Sharpe ratio above approximately 2.0 to claim a DSR $> 0.95$ after 100 trials.

## Remember

The DSR is essential reading for any quant evaluating backtested strategies or published academic factors. Most reported factor alphas in the literature were selected from a large set of candidates; without deflation, p-values are meaningless. Harvey, Liu, and Zhu (2016) estimated that the minimum $t$-statistic required for a newly discovered factor to be considered significant should be around 3.0 rather than the conventional 2.0 — precisely because hundreds of factors have already been tried on the same historical data.
