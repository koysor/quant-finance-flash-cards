# p-value

**Topic:** Statistics
**Tags:** p-value, significance, hypothesis testing, probability, type I error, misinterpretation
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **p-value** is the probability of obtaining a test statistic at least as extreme as the one observed, **assuming the null hypothesis $H_0$ is true**. It measures how compatible the data are with $H_0$: a small p-value indicates the observed result would be rare under $H_0$. The p-value is **not** the probability that $H_0$ is true — a common misinterpretation.

## Key Formula

For a two-tailed $z$-test:

$$p = P(|Z| \geq |z_{\text{obs}}| \mid H_0) = 2\,\Phi(-|z_{\text{obs}}|)$$

**Decision rule:** reject $H_0$ at significance level $\alpha$ if $p < \alpha$.

**What the p-value is NOT:**
- $P(H_0 \text{ is true})$ — that requires Bayesian reasoning
- The probability of a Type I error — $\alpha$ (fixed) is the long-run Type I error rate
- A measure of effect size — a tiny effect can give $p < 0.05$ with a large sample

**Effect size** (Cohen's $d$ for a mean test): $d = (\bar{x} - \mu_0)/\sigma$ — independent of sample size.

## Example

A backtest of 500 trading days gives a Sharpe ratio of 0.6 with $\sigma = 1$. Testing $H_0: \mu = 0$:

$$z = \frac{0.6 \times 1}{\sqrt{1}/\sqrt{500}} \approx 0.6 \times 22.4 = 13.4, \quad p \approx 0$$

The p-value is essentially zero — not because the strategy is spectacular, but because $n = 500$ gives high power to detect even tiny effects. The **annualised Sharpe of 0.6** is the economically meaningful number; the p-value only confirms the return is not exactly zero.

## Remember

p-value misinterpretation is endemic in quantitative finance research. The key correction: a p-value below 0.05 means the result is **statistically significant**, not that it is practically significant. A factor with Sharpe ratio 0.05 can achieve $p = 0.001$ with enough data — it is real but not useful. In backtesting, the appropriate framework is to report **both** the p-value (statistical significance) and the effect size (economic significance). The **p-value also depends on the test chosen** — the same data can give different p-values under a $t$-test vs a permutation test vs a bootstrap — so the testing procedure must be pre-specified to keep the p-value interpretable.
