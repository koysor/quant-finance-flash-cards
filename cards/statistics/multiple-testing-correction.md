# Multiple Testing Correction

**Topic:** Statistics
**Tags:** hypothesis testing, bonferroni, false discovery rate, p-value, backtesting, overfitting
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A **multiple testing correction** adjusts significance thresholds or p-values when many hypothesis tests are performed simultaneously. Without correction, the probability of at least one false positive grows rapidly with the number of tests — a phenomenon called the **multiple comparisons problem**. Common corrections include Bonferroni (controls the family-wise error rate) and Benjamini–Hochberg (controls the false discovery rate).

## Key Formula

**Bonferroni correction:** reject $H_{0,i}$ if

$$p_i < \frac{\alpha}{m}$$

where $m$ is the number of tests and $\alpha$ is the desired family-wise error rate.

**Benjamini–Hochberg (FDR) procedure:** sort p-values $p_{(1)} \leq p_{(2)} \leq \cdots \leq p_{(m)}$ and find the largest $k$ such that

$$p_{(k)} \leq \frac{k}{m} \cdot q$$

where $q$ is the target false discovery rate. Reject all hypotheses $H_{(1)}, \ldots, H_{(k)}$.

## Example

A quant screens $m = 200$ trading signals and wants $\alpha = 0.05$.

**Without correction:** expect $200 \times 0.05 = 10$ false positives among null signals.

**Bonferroni:** each signal must have $p < 0.05 / 200 = 0.00025$ to be declared significant.

**Benjamini–Hochberg at $q = 0.05$:** sorted p-values are compared against the threshold $k/200 \times 0.05$. If the 8th smallest p-value is $0.0018$ and $8/200 \times 0.05 = 0.002$, then $0.0018 < 0.002$ so the first 8 signals are declared significant, accepting that roughly 5% of them may be false discoveries.

## Remember

Multiple testing correction is arguably the most important statistical concept in quantitative strategy research. A quant who backtests hundreds of parameter combinations, factor definitions, or entry rules without adjusting for multiplicity will inevitably "discover" strategies that are pure noise — this is the primary mechanism behind backtest overfitting. Harvey, Liu, and Zhu (2016) argued that a $t$-statistic of 3.0 (not the traditional 2.0) should be required for new factor discoveries, precisely because decades of data mining have tested thousands of hypotheses on the same return data. The Benjamini–Hochberg procedure offers a practical middle ground: it is less conservative than Bonferroni, allowing more genuine signals through while still capping the proportion of false discoveries.
