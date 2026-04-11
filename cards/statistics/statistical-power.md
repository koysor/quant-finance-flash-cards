# Statistical Power

**Topic:** Statistics
**Tags:** power, type II error, beta, effect size, sample size, sensitivity
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **power** of a hypothesis test is the probability of correctly rejecting $H_0$ when $H_0$ is false — the probability of detecting a true effect. Power $= 1 - \beta$, where $\beta = P(\text{Type II error})$ is the probability of failing to reject a false $H_0$. Power increases with larger sample size, larger effect size, higher significance level $\alpha$, and lower variance. A power of 80% is a common target in study design.

## Key Formula

For a one-sample $z$-test with $H_0: \mu = \mu_0$ and $H_1: \mu = \mu_1 > \mu_0$:

$$\text{Power} = P\!\left(Z > z_\alpha - \frac{\mu_1 - \mu_0}{\sigma/\sqrt{n}}\right) = \Phi\!\left(\frac{\mu_1 - \mu_0}{\sigma/\sqrt{n}} - z_\alpha\right)$$

**Required sample size for target power $1-\beta$:**

$$n = \left(\frac{(z_\alpha + z_\beta)\sigma}{\mu_1 - \mu_0}\right)^2$$

where $z_\alpha, z_\beta$ are the one-tailed critical values for significance level and Type II error rate.

**Effect size** $\delta = (\mu_1 - \mu_0)/\sigma$ — larger effect size → higher power for fixed $n$.

## Example

A quant wants 80% power to detect a daily mean return of 0.05% ($\mu_1 - \mu_0 = 0.05\%$) with $\sigma = 1\%$, one-tailed test at $\alpha = 5\%$.

$$n = \left(\frac{(1.645 + 0.842) \times 1\%}{0.05\%}\right)^2 = \left(\frac{2.487}{0.05}\right)^2 \approx 2480 \text{ trading days} \approx 10 \text{ years}$$

Detecting even a small daily edge requires a decade of data — which is why most backtests are chronically underpowered.

## Remember

Statistical power is the critical concept behind **backtest credibility**. Most published backtests are underpowered: they report statistically significant results from short samples on small effects, which are then unreliable out-of-sample. The power calculation shows why: to detect a Sharpe ratio of 0.5 with 80% power at the 5% level requires roughly **n = 500 days** (~2 years). To detect a Sharpe of 0.3 requires 1,400 days (~5.5 years). The practical implication is that a **non-significant result is not evidence of no effect** — it may simply reflect insufficient power. Reporting power alongside p-values is essential for honest research.
