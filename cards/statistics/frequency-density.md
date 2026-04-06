# Frequency Density

**Topic:** Statistics
**Tags:** frequency density, histogram, grouped data, class width, continuous data
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Frequency density** is the quantity plotted on the $y$-axis of a histogram for grouped continuous data. It equals frequency divided by class width, ensuring that the **area** of each bar — not its height — represents the frequency. This allows histograms to display classes of unequal width without visual distortion.

## Key Formula

$$\text{Frequency density} = \frac{\text{Frequency}}{\text{Class width}}$$

$$\text{Frequency} = \text{Frequency density} \times \text{Class width}$$

For a class $[a, b)$: class width $= b - a$.

**Total area of all bars** $=$ total frequency (or 1 if using relative frequency density).

## Example

Daily trading volume (millions of shares) for a stock over 50 days:

| Volume $v$ | Frequency | Class width | Freq. density |
|---|---|---|---|
| $0 \leq v < 2$ | 10 | 2 | 5.0 |
| $2 \leq v < 3$ | 20 | 1 | 20.0 |
| $3 \leq v < 5$ | 15 | 2 | 7.5 |
| $5 \leq v < 10$ | 5 | 5 | 1.0 |

The bar for $[2, 3)$ is tallest but covers only 1 unit; the bar for $[5, 10)$ is short but wide. Area correctly shows 40% of days had volume $2$–$5$M.

## Remember

Frequency density underpins **probability density functions (PDFs)**: the PDF is the continuous limit of a relative frequency density histogram as class width shrinks to zero. In quantitative finance, histograms of log-returns are constructed with equal class widths (so frequency density is proportional to frequency), but the concept matters when working with **option expiry bucketing** — grouping trades by unequal maturity buckets requires frequency density thinking to avoid misleading visual analysis of expiry concentration.
