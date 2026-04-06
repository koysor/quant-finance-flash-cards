# Box Plots

**Topic:** Statistics
**Tags:** box plot, quartiles, IQR, median, five-number summary, whiskers
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **box plot** (box-and-whisker diagram) displays the **five-number summary** of a dataset: minimum, lower quartile $Q_1$, median $Q_2$, upper quartile $Q_3$, and maximum. The box spans from $Q_1$ to $Q_3$ (the interquartile range, IQR), with a line at the median. Whiskers extend to the smallest and largest non-outlier values. Outliers — values beyond $Q_1 - 1.5 \times \text{IQR}$ or $Q_3 + 1.5 \times \text{IQR}$ — are plotted as individual points.

## Key Formula

**Interquartile range:**

$$\text{IQR} = Q_3 - Q_1$$

**Outlier fences:**

$$\text{Lower fence} = Q_1 - 1.5 \times \text{IQR}, \qquad \text{Upper fence} = Q_3 + 1.5 \times \text{IQR}$$

**Skewness from box plot:** if median is closer to $Q_1$ than $Q_3$, the distribution is positively skewed (right-skewed).

## Example

Daily P&L (£k) for a trading desk over a quarter: $Q_1 = -5$, $Q_2 = 3$, $Q_3 = 12$.

$$\text{IQR} = 17, \quad \text{Lower fence} = -5 - 25.5 = -30.5, \quad \text{Upper fence} = 12 + 25.5 = 37.5$$

A day with P&L of $-£45k$ lies below the lower fence — flagged as an outlier. The median being closer to $Q_1$ than $Q_3$ reveals positive skew (more upside days than downside extreme days).

## Remember

Box plots are the standard tool for **comparing return distributions** across multiple assets or strategies side by side. In risk management, the whisker length and outlier count give an immediate visual assessment of **tail risk**: a long lower whisker relative to the upper whisker indicates asymmetric downside exposure. The IQR is also a **robust measure of dispersion** — unlike variance, it is not distorted by extreme outliers — making it useful for describing return distributions that are fat-tailed.
