# Spearman's Rank Correlation

**Topic:** Statistics
**Tags:** Spearman, rank correlation, non-parametric, monotonic, rank
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Spearman's rank correlation coefficient** $r_s$ measures the strength and direction of a **monotonic** relationship between two variables by replacing the data values with their ranks and computing Pearson's correlation on those ranks. It is a **non-parametric** measure — it makes no assumption about the underlying distribution — making it robust to outliers and applicable to ordinal data.

## Key Formula

$$r_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}$$

where $d_i = \text{rank}(x_i) - \text{rank}(y_i)$ is the difference in ranks for the $i$-th observation, and $n$ is the sample size.

$r_s \in [-1, 1]$: $+1$ = perfect positive monotonic, $-1$ = perfect negative monotonic, $0$ = no monotonic relationship.

**Tied ranks:** assign the average of the tied positions (e.g., if two values tie for ranks 3 and 4, both get rank 3.5).

## Example

Rank 5 hedge funds by Sharpe ratio and by maximum drawdown (lower drawdown ranked 1st = better):

| Fund | Sharpe rank | Drawdown rank | $d$ | $d^2$ |
|---|---|---|---|---|
| A | 1 | 2 | −1 | 1 |
| B | 2 | 1 | 1 | 1 |
| C | 3 | 3 | 0 | 0 |
| D | 4 | 5 | −1 | 1 |
| E | 5 | 4 | 1 | 1 |

$$r_s = 1 - \frac{6 \times 4}{5(25-1)} = 1 - \frac{24}{120} = 0.8$$

Strong positive rank correlation: higher-Sharpe funds tend to have lower drawdowns.

## Remember

Spearman's $r_s$ is preferred over Pearson's $r$ when return data contains **fat tails or outliers** — a single extreme return month would distort Pearson but only changes one rank. In practice, quants use Spearman to assess whether **fund performance metrics are consistently ordered**: does a fund that ranks highly on return also rank highly on risk-adjusted return? Spearman is also the workhorse of **alternative data** analysis, where variables are ordinal (e.g., analyst sentiment scores, ESG ratings) rather than continuous.
