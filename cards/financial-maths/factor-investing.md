# Factor Investing

**Topic:** Financial Mathematics
**Tags:** factor investing, value, momentum, quality, size, systematic strategy
**Author:** Claude Opus 4.6

---

## Definition

Factor investing is a systematic investment approach that targets specific, persistent drivers of return — known as factors — rather than selecting individual securities. Common equity factors include value (cheap stocks outperform expensive ones), momentum (recent winners continue to outperform), size (small-cap stocks earn a premium), and quality (profitable, low-leverage firms outperform). Factor strategies are typically implemented as long-short portfolios that isolate the factor premium from broad market exposure.

## Key Formula

A multi-factor model expresses expected return as exposure to $k$ factors:

$$R_i - R_f = \alpha_i + \sum_{j=1}^{k} \beta_{ij} \cdot F_j + \epsilon_i$$

where $F_j$ is the return of factor $j$ and $\beta_{ij}$ is asset $i$'s loading on that factor.

A factor portfolio is constructed by going long the top quantile and short the bottom quantile of stocks ranked by the factor characteristic:

$$R_{\text{factor}} = \bar{R}_{\text{top quantile}} - \bar{R}_{\text{bottom quantile}}$$

## Example

Using the Fama–French three-factor model, a stock has $\beta_{\text{mkt}} = 1.1$, $\beta_{\text{SMB}} = 0.4$ (small-cap tilt), and $\beta_{\text{HML}} = 0.6$ (value tilt). If the factor premia are:

| Factor | Premium |
|--------|---------|
| Market | 6%      |
| SMB    | 3%      |
| HML    | 4%      |

$$E[R_i - R_f] = 1.1 \times 6\% + 0.4 \times 3\% + 0.6 \times 4\% = 6.6\% + 1.2\% + 2.4\% = 10.2\%$$

The expected excess return is 10.2%, of which 3.6% comes from size and value factor exposures beyond simple market beta.

## Remember

Factor investing represents the industrialisation of alpha — what was once the domain of skilled stock pickers is now captured systematically and cheaply through smart-beta ETFs and quantitative strategies. The key insight is that much of what appears to be alpha in traditional active management is actually compensated factor exposure that can be replicated without paying "2 and 20" fees. Understanding factors is essential in modern quantitative finance because every portfolio's returns can be decomposed into factor exposures, and any alpha claim must first survive factor adjustment.
