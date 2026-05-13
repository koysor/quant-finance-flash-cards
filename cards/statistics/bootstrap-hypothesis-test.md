# Bootstrap Hypothesis Test

**Topic:** Statistics
**Tags:** bootstrap, resampling, hypothesis testing, backtesting, non-parametric, permutation
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

A bootstrap hypothesis test uses resampling — repeatedly drawing samples with replacement from the observed data — to construct the null distribution of a test statistic empirically, without assuming any parametric form for the underlying distribution. The p-value is the fraction of bootstrap samples that produce a statistic as extreme as the one observed.

## Key Formula

**Permutation test for strategy alpha** ($H_0$: mean return $= 0$):

$$p = \frac{1}{B} \sum_{b=1}^{B} \mathbf{1}\!\left[T^{*(b)} \geq T_{\text{obs}}\right]$$

Where $T_{\text{obs}}$ is the observed statistic (e.g. Sharpe ratio), $T^{*(b)}$ is the statistic computed on the $b$-th bootstrap or permuted sample, and $B$ is the number of resamples (typically 1,000–10,000).

**Python implementation:**

```python
import numpy as np

returns = np.array([...])           # observed daily returns
obs_sharpe = returns.mean() / returns.std() * np.sqrt(252)

B = 10_000
boot_sharpes = np.array([
    np.random.choice(returns, size=len(returns), replace=True).mean()
    / np.random.choice(returns, size=len(returns), replace=True).std()
    * np.sqrt(252)
    for _ in range(B)
])

p_value = np.mean(boot_sharpes >= obs_sharpe)
```

## Example

A momentum strategy returns a Sharpe ratio of 0.85 over 3 years (756 trading days). A parametric $t$-test assumes normally distributed returns and gives $p = 0.003$. A bootstrap test (10,000 resamples of the 756 daily returns) finds that only 1.2% of resampled Sharpe ratios exceed 0.85 — giving $p = 0.012$. The bootstrap p-value is more conservative and more reliable: it captures the negative skewness and fat tails in the actual return distribution that the $t$-test ignores.

## Remember

Bootstrap tests are the natural choice for backtesting in quantitative finance because financial returns are not normally distributed. The **permutation test** variant (shuffling return signs or dates rather than resampling with replacement) is particularly useful for testing whether a strategy's alpha is genuine or merely an artefact of the specific ordering of returns. Both the bootstrap and permutation tests are honest about the actual distribution of the data — a quality that parametric tests sacrifice for the convenience of a closed-form p-value.
