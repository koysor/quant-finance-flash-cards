# Cumulative Frequency

**Topic:** Statistics
**Tags:** cumulative frequency, ogive, quartiles, median, percentile, grouped data
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **cumulative frequency** curve (ogive) plots the running total of frequencies against the upper class boundary of each interval. Reading off the graph at specific cumulative frequencies gives estimates of the **median** (50th percentile), **lower quartile** $Q_1$ (25th percentile), and **upper quartile** $Q_3$ (75th percentile), as well as any percentile of a grouped distribution.

## Key Formula

**Cumulative frequency up to upper boundary $x_k$:**

$$CF_k = \sum_{i=1}^{k} f_i$$

**Estimated median** from grouped data (interpolation within the median class):

$$\text{Median} \approx L + \frac{\frac{n}{2} - CF_{\text{before}}}{f_{\text{median class}}} \times h$$

where $L$ is the lower boundary, $h$ is the class width, $n$ is total frequency, and $CF_{\text{before}}$ is cumulative frequency before the median class.

## Example

Annual returns for 200 funds grouped into 5% intervals. The median class is $[5\%, 10\%)$ with $L = 5$, $h = 5$, $f = 80$, $CF_{\text{before}} = 60$.

$$\text{Median} \approx 5 + \frac{100 - 60}{80} \times 5 = 5 + 2.5 = 7.5\%$$

Reading the ogive at $CF = 50$ gives $Q_1 \approx 2\%$ and at $CF = 150$ gives $Q_3 \approx 11\%$, so IQR $\approx 9\%$.

## Remember

Cumulative frequency is the discrete analogue of the **cumulative distribution function (CDF)**. In quantitative finance, the CDF of returns is central to **Value at Risk**: VaR at 99% confidence is the 1st percentile of the return distribution, read directly from the empirical CDF (or ogive). Regulatory stress scenarios also use percentile language — a "1-in-200 year event" corresponds to the 0.5th percentile — making cumulative frequency a foundational tool for translating between frequency counts and probability statements.
