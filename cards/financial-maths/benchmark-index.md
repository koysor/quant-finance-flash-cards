# Benchmark Index

**Topic:** Financial Mathematics
**Tags:** benchmark, index, passive investing, market capitalisation, performance measurement
**Author:** Claude Opus 4.6

---

## Definition

A benchmark index is a standardised portfolio of securities used as a reference point against which investment performance is measured. Most equity indices are weighted by market capitalisation, meaning larger companies have a greater influence on the index return. The choice of benchmark fundamentally shapes how a fund manager's performance is judged.

## Key Formula

For a **market-capitalisation-weighted** index with $n$ constituents:

$$R_{\text{index}} = \sum_{i=1}^{n} w_i \cdot R_i \quad \text{where} \quad w_i = \frac{M_i}{\sum_{j=1}^{n} M_j}$$

where $M_i$ is the market capitalisation of stock $i$ and $R_i$ is its return.

For an **equal-weighted** index:

$$R_{\text{index}} = \frac{1}{n} \sum_{i=1}^{n} R_i$$

## Example

A simple index has three stocks:

| Stock | Market Cap (£m) | Return |
|-------|-----------------|--------|
| A     | 500             | 12%    |
| B     | 300             | 6%     |
| C     | 200             | $-3\%$ |

The cap-weighted return is:

$$R = \frac{500}{1000} \times 0.12 + \frac{300}{1000} \times 0.06 + \frac{200}{1000} \times (-0.03) = 0.06 + 0.018 - 0.006 = 0.072$$

The index returned 7.2%. The equal-weighted return would be $\frac{0.12 + 0.06 + (-0.03)}{3} = 5.0\%$, illustrating how weighting methodology affects the result.

## Remember

Benchmark selection is one of the most consequential decisions in fund management — a UK equity fund measured against the FTSE 100 faces a very different performance bar than one measured against the FTSE All-Share. In quantitative finance, benchmarks also serve as the market portfolio in the Capital Asset Pricing Model, and the difference between cap-weighted and equal-weighted indices has real implications for factor exposure, particularly to the size factor in the Fama–French model.
