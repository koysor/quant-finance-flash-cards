# Permutation Test

**Topic:** Statistics
**Tags:** permutation test, hypothesis testing, resampling, non-parametric, backtesting, factor research
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

A permutation test constructs the null distribution of a test statistic by randomly reshuffling the labels or time-ordering of the observed data, computing the statistic on each permutation, and comparing the observed statistic to this empirical distribution. It requires no distributional assumptions and is exact in finite samples.

## Key Formula

For $B$ random permutations, the two-sided p-value is:

$$p = \frac{1}{B} \sum_{b=1}^{B} \mathbf{1}\!\left[|T^{*(b)}| \geq |T_{\text{obs}}|\right]$$

Where $T_{\text{obs}}$ is the test statistic on the original data and $T^{*(b)}$ is the statistic on the $b$-th permuted dataset.

**Python — testing whether a strategy's mean return differs from zero:**

```python
import numpy as np

returns = np.array([...])          # daily strategy returns
obs_stat = returns.mean()          # observed mean

B = 10_000
perm_stats = np.array([
    np.random.choice([-1, 1], size=len(returns)) @ returns / len(returns)
    for _ in range(B)
])                                 # sign-flip permutation under H₀: μ = 0

p_value = np.mean(np.abs(perm_stats) >= np.abs(obs_stat))
```

## Example

A long-short equity strategy returns a mean daily P&L of £1,250 over 500 trading days. The standard $t$-test gives $p = 0.031$ but assumes normal daily P&L. A sign-flip permutation test (10,000 permutations) finds 2.7% of permuted means exceed £1,250 in absolute value — giving $p = 0.027$. The close agreement validates the $t$-test here; when the two p-values diverge substantially, it signals that the parametric assumption is distorting the result.

## Remember

In quantitative finance, the permutation test's most important application is guarding against **look-ahead bias and data snooping**. When a researcher tests many candidate signals and selects the best, the multiple-testing problem inflates the apparent significance. The **max-statistic permutation test** — permuting the data, applying the full selection procedure to each permutation, and recording the maximum statistic — correctly accounts for the search over all candidates. This is the basis of the Harvey-Liu-Zhu framework for evaluating the statistical significance of reported factor alphas across the academic literature.
