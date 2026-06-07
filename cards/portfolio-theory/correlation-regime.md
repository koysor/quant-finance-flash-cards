# Correlation Regime

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** correlation regime, crisis correlation, contagion, diversification, dcc-garch, tail dependence
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

A correlation regime is the prevailing level of pairwise asset return correlations across the portfolio. In calm markets, correlations are low and diversification is effective; during crises, correlations spike toward 1 across risky assets as forced selling and contagion overwhelm fundamentals — destroying diversification precisely when it is most needed. The shift between low- and high-correlation regimes is the central challenge of multi-asset risk management.

## Key Formula

**Dynamic Conditional Correlation (DCC-GARCH)** models time-varying correlations:

$$Q_t = (1 - a - b)\bar{Q} + a\,\varepsilon_{t-1}\varepsilon_{t-1}' + b\,Q_{t-1}$$
$$R_t = \text{diag}(Q_t)^{-1/2} Q_t\,\text{diag}(Q_t)^{-1/2}$$

where $Q_t$ is the pseudo-correlation matrix, $\bar{Q}$ is the unconditional correlation matrix, $\varepsilon_t$ are standardised residuals, and $a + b < 1$ ensures stationarity. The correlation between assets $i$ and $j$ at time $t$ is $\rho_{ij,t} = Q_{ij,t}/\sqrt{Q_{ii,t}Q_{jj,t}}$.

## Example

Historical pairwise correlations (60-day rolling) between a US equity fund (S&P 500) and a diversified credit portfolio:

| Period | $\rho_{\text{equity,credit}}$ | Portfolio vol reduction vs solo equity |
|--------|------------------------------|---------------------------------------|
| 2017 (calm) | 0.18 | 21% |
| 2008 Q4 (crisis) | 0.82 | 4% |
| 2020 Q1 COVID | 0.76 | 6% |
| 2022 inflation | 0.71 | 7% |

The correlation spike in 2008 meant that adding credit bonds to an equity portfolio barely reduced portfolio volatility — the diversification benefit collapsed from 21% to 4%.

## Remember

Correlation regimes expose the Achilles heel of static Markowitz optimisation: a portfolio with 60% equities and 40% bonds that appears well-diversified at $\rho = 0.2$ becomes effectively a 90%+ equity portfolio at $\rho = 0.8$. This is why **maximum diversification portfolios** and **risk parity** strategies recalculate allocations dynamically using DCC-GARCH rather than historical rolling correlations — stale correlations underestimate concentration risk in the exact moments when it matters most. For tail risk management, the **copula framework** is used instead of linear correlation, capturing the fact that correlations in the tails of the distribution (extreme losses) are systematically higher than unconditional correlations — a feature called upper or lower tail dependence.

