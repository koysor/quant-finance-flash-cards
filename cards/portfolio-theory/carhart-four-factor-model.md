# Carhart Four-Factor Model

**Topic:** Portfolio Theory & Asset Pricing
**Level:** A Level Mathematics
**Tags:** carhart, four-factor model, momentum, performance attribution, factor model
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The Carhart four-factor model extends the Fama–French three-factor model by adding a momentum factor (WML — Winners Minus Losers). Proposed by Mark Carhart in 1997, it was motivated by the finding that mutual fund performance persistence was largely explained by momentum exposure rather than genuine manager skill. The model is the standard benchmark for performance attribution in academic finance.

## Key Formula

$$R_i - R_f = \alpha_i + \beta_i (R_m - R_f) + s_i \cdot \text{SMB} + h_i \cdot \text{HML} + w_i \cdot \text{WML} + \epsilon_i$$

where:
- $R_m - R_f$ is the market excess return
- $\text{SMB}$ is the size factor (Small Minus Big)
- $\text{HML}$ is the value factor (High Minus Low book-to-market)
- $\text{WML}$ is the momentum factor (Winners Minus Losers, 12-month return skipping the most recent month)
- $\alpha_i$ is the unexplained return — genuine skill if statistically significant

## Example

A fund returned 15% over the year. The risk-free rate was 3%. Factor returns and the fund's estimated loadings:

| Factor | Return | Loading |
|--------|--------|---------|
| Market ($R_m - R_f$) | 8% | 1.10 |
| SMB | 2% | 0.30 |
| HML | 3% | $-0.10$ |
| WML | 6% | 0.40 |

$$\text{Explained} = 1.10 \times 8\% + 0.30 \times 2\% + (-0.10) \times 3\% + 0.40 \times 6\%$$
$$= 8.80\% + 0.60\% - 0.30\% + 2.40\% = 11.50\%$$

$$\alpha = (15\% - 3\%) - 11.50\% = 0.50\%$$

The fund's 12% excess return is almost entirely explained by factor exposures. The alpha of 0.50% is modest and likely not statistically significant — the manager's apparent skill was mostly compensated momentum and market beta.

## Remember

The Carhart model is the gatekeeper of alpha claims in quantitative finance. Before crediting a fund manager with skill, their returns must survive four-factor adjustment — if the "alpha" disappears after accounting for market, size, value, and momentum exposures, the manager is simply harvesting known risk premia. Carhart's original study showed that after four-factor adjustment, the vast majority of mutual funds had zero or negative alpha, and that performance persistence was driven by momentum loading, not stock-picking ability. This finding was instrumental in the growth of passive and factor-based investing.
