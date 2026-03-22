# Data Snooping Bias

**Topic:** Statistics
**Level:** A Level Mathematics
**Tags:** data snooping, multiple testing, p-hacking, false discovery, research bias
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Data snooping bias arises when the same dataset is used repeatedly to test multiple hypotheses or strategy variations, inflating the probability of finding a statistically significant result by chance. If a researcher tests $N$ strategies on the same historical data, the probability of at least one appearing significant at the 5% level — even if none has genuine predictive power — grows rapidly. Data snooping is distinct from overfitting (which concerns model complexity) but related: both exploit noise in finite samples.

## Key Formula

The probability of finding **at least one** false positive when testing $N$ independent hypotheses at significance level $\alpha$:

$$P(\text{at least one false positive}) = 1 - (1 - \alpha)^N$$

The **Bonferroni correction** adjusts the significance threshold:

$$\alpha_{\text{adjusted}} = \frac{\alpha}{N}$$

The **expected maximum $t$-statistic** from $N$ independent random strategies:

$$E[\max(t)] \approx \sqrt{2 \ln N}$$

## Example

A quant researcher tests 100 trading strategies at the 5% significance level:

$$P(\text{at least one false positive}) = 1 - (1 - 0.05)^{100} = 1 - 0.95^{100} = 1 - 0.0059 = 99.4\%$$

It is virtually certain that at least one strategy will appear significant, even if all 100 are random noise. The expected maximum $t$-statistic:

$$E[\max(t)] \approx \sqrt{2 \ln 100} = \sqrt{9.21} = 3.03$$

So the "best" strategy will likely have a $t$-statistic around 3.0, which would look highly significant in isolation. Using the Bonferroni correction:

$$\alpha_{\text{adjusted}} = \frac{0.05}{100} = 0.05\%$$

The critical $t$-statistic rises from 1.96 to approximately 3.89, correctly filtering out most false discoveries.

## Remember

Data snooping is arguably the single biggest threat to the credibility of quantitative finance research. Harvey, Liu, and Zhu (2016) argued that the conventional $t$-statistic threshold of 2.0 for a new factor should be raised to 3.0 to account for the hundreds of factors already tested on the same datasets. The academic "factor zoo" — over 400 published factors claiming to predict returns — is likely heavily contaminated by data snooping. For practitioners, the implication is clear: never trust a strategy's in-sample statistics without adjusting for the number of alternatives considered. The deflated Sharpe ratio, Bonferroni correction, and false discovery rate control are essential tools for distinguishing genuine signals from statistical mirages.
