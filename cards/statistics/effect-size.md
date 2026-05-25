# Effect Size

**Topic:** Statistics
**Tags:** effect size, Cohen's d, practical significance, hypothesis testing, backtesting, Sharpe ratio
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

Effect size is a standardised measure of the **practical magnitude** of a difference or relationship, independent of sample size. While a p-value answers "is this effect real?", the effect size answers "how large is it?" — a distinction that is critical in quantitative finance where large samples can make economically trivial effects statistically significant.

## Key Formula

**Cohen's $d$** (standardised mean difference):

$$d = \frac{\bar{x} - \mu_0}{\sigma}$$

**Interpretation:**

| $\lvert d\rvert$ | Conventional label |
|---|---|
| 0.2 | Small |
| 0.5 | Medium |
| 0.8 | Large |

**For a trading strategy**, the natural effect size is the **annualised Sharpe ratio** $SR$, which is Cohen's $d$ scaled to a one-year horizon:

$$SR = \frac{\mu - r_f}{\sigma} \times \sqrt{252}$$

**Relationship between effect size, sample size $n$, and p-value:**

$$z = d \times \sqrt{n} \implies p = 2\,\Phi(-|z|)$$

A small effect $d = 0.1$ achieves $p < 0.05$ when $n > 1{,}537$ — statistically significant but economically trivial.

## Example

Two strategies are backtested over 5 years (1,260 days):

| Strategy | Mean daily return | Daily $\sigma$ | Cohen's $d$ | Annualised Sharpe | p-value |
|---|---|---|---|---|---|
| A | 0.01% | 1.0% | 0.01 | 0.16 | 0.37 |
| B | 0.06% | 1.0% | 0.06 | 0.95 | 0.003 |

Strategy A is neither statistically nor economically significant. Strategy B is both. But with 10 years of data, Strategy A would also achieve $p < 0.05$ — purely because of the larger sample — while its Sharpe ratio (the economically meaningful measure) would remain unchanged at 0.16.

## Remember

In factor research and backtesting, **always report effect size alongside the p-value**. A factor with a Sharpe ratio of 0.1 may be publishable (small p-value with years of data) but not tradeable after costs. The Sharpe ratio is the finance-native effect size: it tells you whether the strategy survives transaction costs, slippage, and the bid-ask spread — information that a p-value is structurally incapable of providing. Regulators and sophisticated allocators increasingly require both statistics when evaluating quantitative strategies.
