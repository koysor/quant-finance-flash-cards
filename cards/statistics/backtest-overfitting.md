# Backtest Overfitting

**Topic:** Statistics
**Tags:** backtesting, overfitting, multiple testing, sharpe ratio, strategy selection, p-hacking
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**Backtest overfitting** is the inflation of a strategy's reported performance that arises from testing many strategy configurations on the same historical dataset and selecting the best-performing one, causing the maximum observed Sharpe ratio to exceed the true expected Sharpe ratio by a predictable amount.

## Key Formula

When $N$ independent strategies are tested on the same dataset, the **expected maximum Sharpe ratio** under the null hypothesis of zero true Sharpe is approximately:

$$E\!\left[\max_{1 \leq i \leq N} SR_i\right] \approx \frac{(1-\gamma)\,\Phi^{-1}\!\left(1 - \frac{1}{N}\right) + \gamma\,\Phi^{-1}\!\left(1 - \frac{1}{Ne}\right)}{\sqrt{T}}$$

where $\gamma \approx 0.5772$ is the Euler–Mascheroni constant, $\Phi^{-1}$ is the standard normal quantile, $T$ is the number of observations, and $e$ is Euler's number. The **Deflated Sharpe Ratio (DSR)** adjusts the reported Sharpe downward by this expected maximum:

$$DSR = \frac{SR - E[\max SR]}{\sqrt{\widehat{\sigma}^2_{SR} / T}}$$

where $\widehat{\sigma}^2_{SR}$ accounts for non-normality of returns (skewness and kurtosis).

## Example

A quant tests $N = 100$ momentum variants on 5 years of daily data ($T = 1{,}260$ observations). Even if every variant has zero true Sharpe, the expected maximum by chance alone is approximately $\Phi^{-1}(1 - 1/100)\,/\,\sqrt{1260} \approx 2.33/35.5 \approx 0.066$. The best strategy reports $SR = 1.8$; after the DSR adjustment it falls to $0.9$ — still positive, but far more modest than the headline figure suggests.

## Remember

Every time a quant modifies a strategy and re-runs the backtest, they consume one "trial" from their multiple-testing budget. A portfolio manager who reviews 200 strategy variants over a year and selects the top performer has implicitly run 200 hypothesis tests — even if no formal hypothesis testing was conducted. The expected maximum Sharpe under the null rises with $\sqrt{\ln N}$, so doubling the number of trials raises the false-discovery threshold by about 18%. The only remedies are pre-registration of strategy hypotheses before testing, out-of-sample validation on held-out data, or CPCV to compute the probability of backtest overfitting directly.
