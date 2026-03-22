# Diversification

**Topic:** Portfolio Theory & Asset Pricing
**Level:** A Level Mathematics
**Tags:** diversification, correlation, portfolio risk, unsystematic risk, risk reduction
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Diversification is the reduction of portfolio risk by combining assets whose returns are not perfectly correlated. When assets do not move in lockstep, gains on some positions offset losses on others, reducing the overall volatility of the portfolio below the weighted average volatility of its components. Diversification eliminates **unsystematic (idiosyncratic) risk** but cannot remove **systematic (market) risk**, which affects all assets.

## Key Formula

The **variance of a two-asset portfolio**:

$$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2$$

When $\rho_{12} < 1$, the portfolio variance is strictly less than the weighted average of individual variances. The **diversification benefit** is:

$$\text{Benefit} = (w_1 \sigma_1 + w_2 \sigma_2) - \sigma_p$$

For $n$ uncorrelated, equal-weight, equal-variance assets:

$$\sigma_p = \frac{\sigma}{\sqrt{n}}$$

showing that idiosyncratic risk falls as $1/\sqrt{n}$.

## Example

Two stocks each have $\sigma = 20\%$, held in equal weights ($w_1 = w_2 = 0.5$). Compare portfolio risk at different correlations:

| $\rho$ | $\sigma_p$ | Diversification benefit |
|---------|-----------|------------------------|
| 1.0 | 20.0% | 0.0% |
| 0.5 | 17.3% | 2.7% |
| 0.0 | 14.1% | 5.9% |
| $-0.5$ | 10.0% | 10.0% |
| $-1.0$ | 0.0% | 20.0% |

With $\rho = 0.5$:

$$\sigma_p = \sqrt{0.25 \times 0.04 + 0.25 \times 0.04 + 2 \times 0.25 \times 0.5 \times 0.04} = \sqrt{0.03} = 17.3\%$$

Each stock has 20% volatility, but the portfolio has only 17.3%.

## Remember

Diversification is the only "free lunch" in finance — it reduces risk without reducing expected return. It is the mathematical foundation of Modern Portfolio Theory and explains why rational investors hold portfolios rather than individual stocks. However, diversification has limits: during market crises, correlations spike towards 1.0, reducing the benefit precisely when it is needed most. This "correlation breakdown" is why tail risk measures like Expected Shortfall and copula models exist — they capture the nonlinear dependence that Pearson correlation misses. Understanding that diversification reduces idiosyncratic risk but not systematic risk is the conceptual bridge to the CAPM, which says only systematic risk is compensated.
