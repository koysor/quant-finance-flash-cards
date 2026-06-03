# Cross-Sectional Score

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** cross-sectional, scoring, z-score, factor investing, signal normalisation, alpha
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

A **cross-sectional score** ranks each asset relative to all other assets in the investment universe at a single point in time by standardising a raw signal — such as momentum or value — into a z-score using the cross-sectional mean and standard deviation. This removes the overall market level of the signal and retains only information about *relative* strength.

## Key Formula

For a raw signal $x_{i,t}$ (e.g., 12-month return) computed for each asset $i = 1, \ldots, N$ at time $t$:

$$z_{i,t} = \frac{x_{i,t} - \mu_t}{\sigma_t}$$

where the cross-sectional mean and standard deviation are:

$$\mu_t = \frac{1}{N} \sum_{i=1}^{N} x_{i,t}, \qquad \sigma_t = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N} (x_{i,t} - \mu_t)^2}$$

A positive $z_{i,t}$ indicates the asset is above average on the signal; a negative score indicates below average.

## Example

At month-end, the 12-month returns of five FTSE stocks are: $+18\%$, $+12\%$, $+8\%$, $-2\%$, $-6\%$. The cross-sectional mean is $\mu = 6\%$ and standard deviation is $\sigma \approx 10\%$. The z-scores are approximately $+1.2$, $+0.6$, $+0.2$, $-0.8$, $-1.2$. A long–short strategy goes long the top-scored stock and short the bottom-scored, regardless of whether the market overall was up or down.

## Remember

Cross-sectional scoring is the step that converts raw factor signals into investable positions in equity factor strategies. Without z-scoring, a value strategy might appear to hold nothing in a year when all stocks are expensive (the raw value signal is low for everyone). After cross-sectional normalisation, the strategy always holds the *relatively* cheapest stocks — which is the actual investment thesis. This is why quant equity funds standardise signals cross-sectionally before combining them into a composite score.
