# Capital Asset Pricing Model

**Topic:** Financial Mathematics
**Tags:** CAPM, expected return, beta, systematic risk, market risk, asset pricing
**Created:** 2026-03-01
**Author:** Claude Opus 4.6

---

## Definition

The **Capital Asset Pricing Model (CAPM)** describes the relationship between the expected return of an asset and its systematic risk, measured by **beta** ($\beta$). It states that an asset's expected return equals the risk-free rate plus a risk premium proportional to the asset's sensitivity to the overall market. Only systematic (non-diversifiable) risk is compensated, because idiosyncratic risk can be eliminated through diversification.

## Key Formula

$$E(R_i) = R_f + \beta_i \bigl(E(R_m) - R_f\bigr)$$

where:
- $E(R_i)$ is the expected return of asset $i$
- $R_f$ is the risk-free rate
- $E(R_m)$ is the expected return of the market portfolio
- $E(R_m) - R_f$ is the **market risk premium**
- $\beta_i = \dfrac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)}$ measures the asset's sensitivity to market movements

## Example

Suppose the risk-free rate is $R_f = 3\%$, the expected market return is $E(R_m) = 9\%$, and a stock has $\beta = 1.4$.

$$E(R_i) = 3\% + 1.4 \times (9\% - 3\%) = 3\% + 1.4 \times 6\% = 3\% + 8.4\% = 11.4\%$$

The stock's expected return is 11.4%. Because $\beta > 1$, the stock amplifies market movements — it is expected to earn more than the market but also carries greater systematic risk. A stock with $\beta = 0.6$ would earn only $3\% + 0.6 \times 6\% = 6.6\%$.

## Remember

CAPM is the foundation of modern asset pricing and cost-of-equity estimation. In practice, analysts use CAPM to set the **discount rate** in discounted cash flow (DCF) valuations — a higher beta means a higher required return and therefore a lower present value. While empirical tests reveal shortcomings (the model ignores size, value, and momentum effects captured by multi-factor models like Fama–French), CAPM remains the starting point for understanding the trade-off between risk and return in quantitative finance.
