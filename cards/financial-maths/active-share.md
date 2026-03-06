# Active Share

**Topic:** Financial Mathematics
**Tags:** active share, benchmark, active management, closet indexing, portfolio construction
**Author:** Claude Opus 4.6

---

## Definition

Active share is the percentage of a portfolio's holdings that differ from its benchmark index, measured as half the sum of the absolute differences between portfolio and benchmark weights. It ranges from 0% (identical to the benchmark) to 100% (no overlap). Active share distinguishes genuine stock-pickers from "closet indexers" who charge active fees while closely mimicking the index.

## Key Formula

$$\text{Active Share} = \frac{1}{2} \sum_{i=1}^{N} |w_{p,i} - w_{b,i}|$$

where $w_{p,i}$ is the portfolio weight of stock $i$ and $w_{b,i}$ is the benchmark weight. The factor of $\frac{1}{2}$ avoids double-counting, since overweights and underweights must sum to the same magnitude.

## Example

A simplified portfolio and its benchmark:

| Stock | Portfolio Weight | Benchmark Weight | Difference |
|-------|-----------------|-----------------|-----------|
| A     | 30%             | 20%             | 10%       |
| B     | 25%             | 25%             | 0%        |
| C     | 10%             | 30%             | 20%       |
| D     | 35%             | 25%             | 10%       |

$$\text{Active Share} = \frac{1}{2}(10 + 0 + 20 + 10) = 20\%$$

An active share of 20% is low — the portfolio is mostly tracking the benchmark. Research suggests that funds with active share below 60% are essentially closet indexers, while truly active managers typically have active share above 80%.

## Remember

Active share became a widely discussed metric after Cremers and Petajisto (2009) showed that funds with high active share tend to outperform their benchmarks after fees, while closet indexers consistently underperform. For investors, active share answers a crucial question: am I paying active management fees for a portfolio that is genuinely different from the index I could buy cheaply? Combined with tracking error, active share provides a two-dimensional view of active management — high active share with low tracking error implies concentrated stock bets, while high tracking error with low active share implies sector or factor tilts.
