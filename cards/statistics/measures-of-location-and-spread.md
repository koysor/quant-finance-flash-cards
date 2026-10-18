# Measures of Location and Spread

**Topic:** Statistics
**Tags:** mean, median, variance, interquartile range, outliers, Bessel correction, robust statistics
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

Summarising a dataset means saying where it sits (**location**: mean, median) and how far it is spread out (**spread**: variance, standard deviation, interquartile range). The right pair depends on whether the data is symmetric and free of outliers.

## Key Formula

$$\bar{x} = \frac{\sum x}{n}, \qquad s^2 = \frac{S_{xx}}{n - 1}, \qquad S_{xx} = \sum x^2 - \frac{\bigl(\sum x\bigr)^2}{n}$$

| Measure | Property |
|---|---|
| Mean | Uses every value; sensitive to outliers |
| Median | Middle value; robust to outliers |
| IQR | $Q_3 - Q_1$, the spread of the middle half |
| $n - 1$ | Bessel's correction: makes $s^2$ unbiased for $\sigma^2$ |

An outlier lies beyond $Q_1 - 1.5\,\mathrm{IQR}$ or $Q_3 + 1.5\,\mathrm{IQR}$.

## Example

Data: $4, 6, 7, 9, 14$. Then $\sum x = 40$, so $\bar{x} = 8$; $\sum x^2 = 378$, so $S_{xx} = 378 - \tfrac{1600}{5} = 58$ and $s^2 = \tfrac{58}{4} = 14.5$. The median is $7$.

Replace $14$ by $140$: the mean jumps to $33.2$ but the median stays at $7$.

## Remember

Financial returns have fat tails, so a single crisis day can drag the mean and standard deviation while the median and IQR barely move. Use the mean and standard deviation for roughly symmetric data, and median and IQR (or median absolute deviation) when outliers are present. The $S_{xx}$ and $S_{xy}$ shorthand recurs throughout regression.
