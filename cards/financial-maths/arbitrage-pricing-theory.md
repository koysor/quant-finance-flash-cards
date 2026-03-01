# Arbitrage Pricing Theory

**Topic:** Financial Mathematics
**Tags:** arbitrage pricing theory, factor model, systematic risk, no-arbitrage, asset pricing
**Created:** 2026-03-01
**Author:** Claude Opus 4.6

---

## Definition

**Arbitrage Pricing Theory (APT)**, developed by Stephen Ross in 1976, is a multi-factor asset pricing model derived from no-arbitrage arguments rather than the equilibrium assumptions used in CAPM. APT states that an asset's expected return is a linear function of its exposures (betas) to multiple systematic risk factors, each carrying its own risk premium. Unlike CAPM, APT does not require specifying the market portfolio and allows any number of priced factors, making it a more general framework for explaining cross-sectional differences in expected returns.

## Key Formula

$$E(R_i) = R_f + \beta_{i1}\lambda_1 + \beta_{i2}\lambda_2 + \cdots + \beta_{ik}\lambda_k$$

where:
- $E(R_i)$ is the expected return of asset $i$
- $R_f$ is the risk-free rate
- $\beta_{ij}$ is the sensitivity of asset $i$ to factor $j$
- $\lambda_j$ is the risk premium for factor $j$ (the extra return per unit of exposure)
- $k$ is the number of systematic risk factors

The underlying factor model for the realised return is:

$$R_i = E(R_i) + \beta_{i1}F_1 + \beta_{i2}F_2 + \cdots + \beta_{ik}F_k + \varepsilon_i$$

where $F_j$ are the zero-mean factor surprises and $\varepsilon_i$ is idiosyncratic noise with $E(\varepsilon_i) = 0$.

## Example

Suppose there are two factors: an interest-rate factor and an industrial-production factor. The risk-free rate is $R_f = 3\%$, and the factor risk premia are $\lambda_1 = 2\%$ (interest rate) and $\lambda_2 = 4\%$ (industrial production).

A stock has $\beta_1 = 0.8$ and $\beta_2 = 1.2$:

$$E(R) = 3\% + 0.8 \times 2\% + 1.2 \times 4\% = 3\% + 1.6\% + 4.8\% = 9.4\%$$

A bond fund has $\beta_1 = 1.5$ and $\beta_2 = 0.3$:

$$E(R) = 3\% + 1.5 \times 2\% + 0.3 \times 4\% = 3\% + 3.0\% + 1.2\% = 7.2\%$$

The bond fund loads more heavily on the interest-rate factor while the stock loads more on the production factor, producing different expected returns that reflect their distinct risk exposures.

## Remember

APT is the theoretical backbone of the statistical factor models used throughout quantitative finance. While CAPM compresses all systematic risk into a single market beta, APT allows practitioners to decompose risk into multiple sources — such as interest rates, inflation, credit spreads, or momentum — each priced separately. This generality underpins the Fama-French three-factor and five-factor models, Barra risk models, and the factor-based approaches used in alpha research and portfolio construction. The main practical challenge is that APT does not specify which factors matter or how many there are; the analyst must identify them empirically. Despite this ambiguity, the no-arbitrage foundation makes APT more robust than equilibrium models: it requires only that a sufficiently large number of assets exist to diversify away idiosyncratic risk, rather than assuming all investors hold mean-variance optimal portfolios.
