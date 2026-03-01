# Fama–French Three-Factor Model

**Topic:** Financial Mathematics
**Tags:** fama-french, factor model, size effect, value effect, asset pricing
**Created:** 2026-03-01
**Author:** Claude Opus 4.6

---

## Definition

The **Fama–French Three-Factor Model** extends the CAPM by adding two empirically motivated factors to explain cross-sectional differences in stock returns. Besides the market factor, it includes **SMB** (Small Minus Big), capturing the tendency of small-capitalisation stocks to outperform large ones, and **HML** (High Minus Low), capturing the tendency of high book-to-market (value) stocks to outperform low book-to-market (growth) stocks.

## Key Formula

$$E(R_i) - R_f = \beta_i \bigl(E(R_m) - R_f\bigr) + s_i \cdot \text{SMB} + h_i \cdot \text{HML}$$

where:
- $\beta_i$ is the market factor loading (as in CAPM)
- $s_i$ is the sensitivity to the size factor (SMB)
- $h_i$ is the sensitivity to the value factor (HML)
- Factor loadings are estimated by regressing excess returns on the three factor time series

## Example

Suppose $R_f = 2\%$, $E(R_m) - R_f = 6\%$, $\text{SMB} = 3\%$, $\text{HML} = 4\%$, and a small-cap value stock has $\beta = 1.1$, $s = 0.7$, $h = 0.5$.

$$E(R_i) - R_f = 1.1 \times 6\% + 0.7 \times 3\% + 0.5 \times 4\% = 6.6\% + 2.1\% + 2.0\% = 10.7\%$$

$$E(R_i) = 2\% + 10.7\% = 12.7\%$$

CAPM alone would predict $2\% + 1.1 \times 6\% = 8.6\%$. The additional 4.1% comes from the size and value premia — returns that CAPM would incorrectly attribute to alpha.

## Remember

The Fama–French model explains much of the "alpha" that single-factor CAPM leaves unexplained. It is the foundation of **factor investing** — the idea that systematic tilts towards size, value, and other characteristics can earn persistent risk premia. In practice, performance attribution systems decompose fund returns into factor exposures to distinguish genuine skill from mechanical factor bets. Later extensions (Carhart four-factor, Fama–French five-factor) add momentum, profitability, and investment factors.
