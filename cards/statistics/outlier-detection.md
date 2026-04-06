# Outlier Detection

**Topic:** Statistics
**Tags:** outlier, IQR fence, anomaly, robust statistics, data cleaning
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

An **outlier** is an observation that lies far from the bulk of the data. The two standard detection rules are: (1) the **IQR fence rule** — a value is an outlier if it falls more than $1.5 \times \text{IQR}$ beyond the quartiles; and (2) the **mean ± 2 (or 3) standard deviations rule** — a value is an outlier if $|x - \bar{x}| > k\sigma$ for $k = 2$ or $k = 3$. The IQR rule is more robust for skewed or fat-tailed data.

## Key Formula

**IQR fence rule:**

$$\text{Lower fence} = Q_1 - 1.5 \times \text{IQR}, \qquad \text{Upper fence} = Q_3 + 1.5 \times \text{IQR}$$

**Standard deviation rule:**

$$\text{Outlier if } |x - \bar{x}| > k\sigma, \quad k = 2 \text{ or } 3$$

**For normal data:** $P(|X - \mu| > 2\sigma) \approx 4.6\%$, $\quad P(|X - \mu| > 3\sigma) \approx 0.3\%$.

## Example

Weekly P&L observations (£m): most values between −2 and +3. $Q_1 = -0.8$, $Q_3 = 1.5$, IQR = 2.3.

$$\text{Lower fence} = -0.8 - 3.45 = -4.25, \qquad \text{Upper fence} = 1.5 + 3.45 = 4.95$$

A week with P&L = −£6m lies below the lower fence and is flagged as an outlier. Using the standard deviation rule ($\sigma = 1.4$), $\bar{x} + 3\sigma = 3 + 4.2 = 7.2$: the −£6m observation would not be flagged, illustrating that the two rules can disagree when data is skewed.

## Remember

In quantitative finance, outliers are never simply deleted — they are the tail events that **matter most**. A risk model that removes outliers will systematically **underestimate VaR** and CVaR. The correct response is to investigate: is the outlier a data error (wrong trade booking, system glitch), or a genuine extreme event? If genuine, **robust statistics** (median instead of mean, IQR instead of standard deviation) or **heavy-tailed distributions** (Student-$t$, EVT) should be used instead. Many of the largest trading losses in history (Barings, Long-Term Capital Management) were observations that standard models classified as "impossible" outliers.
