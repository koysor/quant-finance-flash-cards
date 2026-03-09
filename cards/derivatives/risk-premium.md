# Risk Premium

**Topic:** Derivatives
**Tags:** risk premium, expected return, risk-free rate, compensation, CAPM, equilibrium
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **risk premium** of an asset is the expected return in excess of the risk-free rate — the compensation investors demand for bearing the asset's risk rather than holding a riskless investment. It is the drift that Girsanov's theorem removes when moving from the physical measure $\mathbb{P}$ to the risk-neutral measure $\mathbb{Q}$.

## Key Formula

$$\text{Risk premium} = \mu - r$$

where $\mu = E^{\mathbb{P}}[R]$ is the expected return under the physical measure and $r$ is the risk-free rate.

**CAPM decomposition:**

$$\mu_i - r = \beta_i(\mu_M - r)$$

where $\beta_i = \text{Cov}(R_i, R_M)/\text{Var}(R_M)$ and $\mu_M - r$ is the **equity risk premium**.

**Relationship to market price of risk:**

$$\mu - r = \theta \sigma \qquad \Longleftrightarrow \qquad \theta = \frac{\mu - r}{\sigma}$$

## Example

The long-run equity risk premium is approximately 5%. A stock has $\beta = 1.3$, and the risk-free rate is $r = 4\%$.

$$\mu - r = 1.3 \times 5\% = 6.5\%$$

$$\mu = 4\% + 6.5\% = 10.5\%$$

If the stock's volatility is $\sigma = 30\%$, the market price of risk is:

$$\theta = \frac{0.065}{0.30} = 0.217$$

Under $\mathbb{Q}$, this 6.5% risk premium vanishes — the stock's drift becomes the risk-free rate $r = 4\%$.

## Remember

The risk premium is what makes $\mathbb{P}$ different from $\mathbb{Q}$. Under the physical measure, risky assets earn $\mu > r$ on average to compensate investors for uncertainty; under the risk-neutral measure, this premium is stripped away so that all assets earn $r$. This is why the Black–Scholes formula does not depend on $\mu$ — the hedging argument removes the risk premium, leaving only the risk-free rate and volatility. In risk management, however, the risk premium matters enormously: VaR and expected shortfall must use $\mathbb{P}$-dynamics (with the real drift $\mu$), and estimating the equity risk premium is one of the most debated problems in empirical finance — small changes in its estimate can shift portfolio allocations and pension fund valuations by billions.
