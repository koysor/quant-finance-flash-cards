# Index Volatility Asymmetry vs Firm Asymmetry

**Topic:** Statistics
**Tags:** gjr-garch, asymmetric volatility, correlation, portfolio variance, leverage effect, index, stylised facts
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

**Index volatility asymmetry** refers to the empirical finding that GJR-GARCH models fitted to equity index returns exhibit far larger asymmetry parameters than the same models fitted to individual firm returns. The asymmetry parameter $\gamma$ for a major index (e.g. the DJIA or S&P 500) is typically several times larger than the weighted average of the $\gamma$ parameters from its constituent firms.

The classical **leverage explanation** (Black, 1976) — that a falling stock price raises the debt-to-equity ratio, increasing firm risk — cannot account for the gap. For most large-cap firms the individual leverage effect is modest; yet at the index level the asymmetry is dramatic.

The primary mechanism is **correlation amplification**: in a market downturn, cross-firm return correlations rise sharply. Because index variance contains pairwise covariance terms that scale with correlation, a simultaneous increase in individual volatilities and correlations amplifies index variance far beyond what firm-level effects alone would predict.

## Key Formula

For a portfolio of $n$ stocks with weights $w_i$, individual volatilities $\sigma_i$, and pairwise correlations $\rho_{ij}$:

$$\text{Var}(R_P) = \sum_{i=1}^{n} w_i^2 \sigma_i^2 + 2\sum_{i < j} w_i w_j \sigma_i \sigma_j \rho_{ij}$$

The second term — the **correlation amplification channel** — grows as $\rho_{ij}$ rises. If all pairwise correlations jump from $\rho_{\text{calm}} = 0.3$ to $\rho_{\text{stress}} = 0.7$ during a market sell-off, the covariance contribution more than doubles, even with no change in individual $\sigma_i$. For a large index the cross terms dominate (there are $\tfrac{n(n-1)}{2}$ of them versus only $n$ variance terms), so rising correlation is the dominant driver of the index volatility spike.

## Example

Two equal-weight stocks ($w_1 = w_2 = 0.5$), each with daily volatility $\sigma_1 = \sigma_2 = 2\%$:

$$\sigma_p^2 = 0.5^2 \times 0.02^2 + 0.5^2 \times 0.02^2 + 2 \times 0.5 \times 0.5 \times 0.02 \times 0.02 \times \rho$$

**Calm market** ($\rho = 0.3$):

$$\sigma_p^2 = 0.0001 + 0.0001 + 2 \times 0.25 \times 0.0004 \times 0.3 = 0.0002 + 0.000060 = 0.000260$$
$$\sigma_p \approx 1.61\%$$

**Stressed market** ($\rho = 0.7$):

$$\sigma_p^2 = 0.0001 + 0.0001 + 2 \times 0.25 \times 0.0004 \times 0.7 = 0.0002 + 0.000140 = 0.000340$$
$$\sigma_p \approx 1.84\%$$

The index volatility rises from 1.61% to 1.84% — a 14% increase — driven entirely by rising correlation, with no change in the individual firm volatilities. Scaled to a real index with hundreds of constituent stocks, this effect is far larger.

## Remember

During equity market stress, diversification benefits collapse: cross-stock correlations spike towards 1, turning the portfolio variance formula into an almost-additive sum of all variances. This is precisely why **portfolio VaR and Expected Shortfall computed bottom-up from desk-level risk estimates will systematically understate aggregate risk in a crisis**: individual desk models use calm-period correlations, whilst the index-level GJR-GARCH tells a far more alarming story. Risk managers must stress-test the correlation matrix — shifting $\rho$ from normal to crisis levels — to obtain realistic aggregate tail-risk figures, rather than simply summing desk VaRs.
