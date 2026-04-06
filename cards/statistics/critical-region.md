# Critical Region

**Topic:** Statistics
**Tags:** critical region, hypothesis testing, significance level, rejection region, one-tailed, two-tailed
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **critical region** (rejection region) is the set of values of the test statistic for which the null hypothesis $H_0$ is rejected. It is determined by the **significance level** $\alpha$ — the maximum acceptable probability of a Type I error. For a one-tailed test, the entire critical region is in one tail; for a two-tailed test, it is split equally between both tails. The boundary of the critical region is the **critical value**.

## Key Formula

**One-tailed test** at significance level $\alpha$:

$$\text{Critical region: } T > z_\alpha \quad \text{(upper-tailed)} \quad \text{or} \quad T < -z_\alpha \quad \text{(lower-tailed)}$$

**Two-tailed test** at significance level $\alpha$:

$$\text{Critical region: } |T| > z_{\alpha/2}$$

**Exact critical region for binomial** $H_0: p = p_0$, upper-tailed at $\alpha = 5\%$: find the smallest integer $c$ such that $P(X \geq c \mid p_0) \leq 0.05$.

**Actual significance level:** $P(\text{test statistic in critical region} \mid H_0)$ — for discrete distributions this may be less than $\alpha$.

## Example

Testing $H_0: p = 0.4$ (win rate) against $H_1: p > 0.4$ at the 5% level, with $n = 20$ trades.

Using the binomial: $P(X \geq 13 \mid p = 0.4) = 0.0210 \leq 0.05$ and $P(X \geq 12 \mid p = 0.4) = 0.0565 > 0.05$.

Critical region: $X \geq 13$. Actual significance level: 2.1% (not 5%, because the binomial is discrete).

Observing 14 wins falls in the critical region → reject $H_0$.

## Remember

The critical region framework is how **backtesting** works in regulatory capital. Basel FRTB requires banks to backtest VaR models by counting the number of exceedances (days when actual loss exceeds the VaR estimate) over 250 trading days. The green zone is 0–4 exceedances, the red zone is 10+: these are the critical region boundaries of a one-tailed binomial test with $H_0: p = 0.01$. A model landing in the red zone has its risk estimates multiplied by a penalty factor — the regulatory consequence of rejecting $H_0$.
