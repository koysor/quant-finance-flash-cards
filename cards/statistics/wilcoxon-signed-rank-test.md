# Wilcoxon Signed-Rank Test

**Topic:** Statistics
**Tags:** Wilcoxon, non-parametric, signed-rank, median, paired, robust
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Wilcoxon signed-rank test** is the non-parametric alternative to the one-sample or paired t-test. It tests whether the **median** of a distribution (or the median difference of paired observations) equals a specified value, without requiring normality. It uses the **ranks** of the absolute differences rather than the raw values, making it robust to outliers and heavy-tailed distributions.

## Key Formula

**Procedure:**
1. Compute differences $d_i = X_i - \mu_0$ (or $d_i = X_{i1} - X_{i2}$ for paired data); discard zeros.
2. Rank the absolute values $|d_i|$ from smallest (rank 1) to largest.
3. Compute $W^+ = \sum_{\{i: d_i > 0\}} R_i$ and $W^- = \sum_{\{i: d_i < 0\}} R_i$. Test statistic: $W = \min(W^+, W^-)$.
4. Compare $W$ to critical values (or use normal approximation for large $n$).

**Large-$n$ approximation** ($n \geq 25$):

$$z = \frac{W^+ - n(n+1)/4}{\sqrt{n(n+1)(2n+1)/24}} \sim N(0,1) \text{ under } H_0$$

## Example

A portfolio manager tests whether the median daily excess return differs from zero, using 30 days of data with heavy-tailed returns (a t-test would be unreliable). After ranking absolute returns and summing positive-sign ranks:

$W^+ = 310$, $n = 30$. Under $H_0$: expected $W^+ = 30 \times 31/4 = 232.5$.

$$z = \frac{310 - 232.5}{\sqrt{30 \times 31 \times 61/24}} = \frac{77.5}{48.6} = 1.59, \quad p \approx 0.11$$

Fail to reject $H_0$ — no significant evidence of non-zero median return.

## Remember

The Wilcoxon signed-rank test is the standard **non-parametric one-sample test for financial return data** where the normality assumption is violated. It is more powerful than the sign test (which ignores magnitude) and more robust than the t-test when outliers are present. In **performance evaluation**, using a parametric t-test on hedge fund returns with occasional large gains or losses gives misleading p-values — the Wilcoxon test provides a valid alternative. The test is also used in **pairs trading research** to check whether the spread between two cointegrated assets has a significant non-zero median, which would indicate mispricing rather than a pure mean-reversion signal.
