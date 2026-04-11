# Mann-Whitney U Test

**Topic:** Statistics
**Tags:** Mann-Whitney, Wilcoxon rank-sum, non-parametric, two-sample, ranks, stochastic dominance
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Mann-Whitney U test** (also called the Wilcoxon rank-sum test) is the non-parametric alternative to the independent two-sample t-test. It tests whether the distributions of two independent groups are identical — equivalently, whether the probability that a randomly selected observation from group 1 exceeds one from group 2 equals 0.5. It requires no normality assumption, making it appropriate for comparing financial metrics with heavy tails or outliers.

## Key Formula

**U statistic** for groups of size $n_1$ and $n_2$:

$$U_1 = n_1 n_2 + \frac{n_1(n_1+1)}{2} - R_1$$

where $R_1$ is the sum of ranks of group 1 when all $n_1 + n_2$ observations are jointly ranked. $U = \min(U_1, U_2)$.

**Large-sample approximation:**

$$z = \frac{U - n_1 n_2/2}{\sqrt{n_1 n_2 (n_1+n_2+1)/12}} \sim N(0,1) \text{ under } H_0$$

**Common language effect size:** $\hat{P}(X_1 > X_2) = U_1/(n_1 n_2)$ — interpretable as a probability.

## Example

Comparing daily Sharpe ratios of two funds over different periods: Fund A ($n_1 = 50$ months), Fund B ($n_2 = 40$ months). Joint ranking gives $R_1 = 2800$.

$$U_1 = 50 \times 40 + \frac{50 \times 51}{2} - 2800 = 2000 + 1275 - 2800 = 475$$

$$z = \frac{475 - 1000}{\sqrt{50 \times 40 \times 91/12}} = \frac{-525}{388} = -1.35, \quad p \approx 0.18$$

Fail to reject equal distributions — no significant evidence that Fund A outperforms Fund B in distribution.

## Remember

The Mann-Whitney test is the correct tool for **comparing two hedge fund return distributions** when sample sizes differ and normality is not justified. A standard two-sample t-test on monthly returns would be unreliable due to fat tails; Mann-Whitney uses ranks and remains valid. The **effect size** $\hat{P}(X_1 > X_2)$ is directly interpretable as "in what fraction of randomly chosen month-pairs does Fund A beat Fund B?" — more intuitive than a difference in means. In **factor investing research**, Mann-Whitney tests compare the return distributions of top-quintile vs bottom-quintile stocks ranked by a factor, without assuming symmetric return distributions.
