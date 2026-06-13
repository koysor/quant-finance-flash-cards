# Vasicek Parameter Estimation via MLE

**Topic:** Statistics
**Tags:** maximum likelihood, ornstein-uhlenbeck, vasicek, time-series, parameter estimation, mean reversion, interest rate, AR(1)
**Created:** 2026-06-14
**Author:** Claude Sonnet 4.6

---

## Definition

Vasicek parameter estimation fits the model $dr = \kappa(\theta - r)\,dt + \sigma\,dW_t$ to historical rate data by exploiting the fact that the discretised process is an **AR(1) regression**: $r_{t+\Delta t} = \alpha + \beta r_t + \epsilon_t$, whose coefficients map exactly to the model parameters via closed-form formulas.

## Key Formula

The conditional distribution of $r_{t+\Delta t}$ given $r_t$ is Gaussian:

$$r_{t+\Delta t} \mid r_t \;\sim\; \mathcal{N}\!\bigl(\alpha + \beta r_t,\; s^2\bigr)$$

Maximising this likelihood is equivalent to OLS on the AR(1). The model parameters are recovered by:

$$\hat{\beta} = e^{-\kappa\Delta t} \implies \hat{\kappa} = -\frac{\ln\hat{\beta}}{\Delta t}$$

$$\hat{\theta} = \frac{\hat{\alpha}}{1-\hat{\beta}}$$

$$\hat{\sigma}^2 = \frac{2\hat{\kappa}\,\hat{s}^2}{1 - \hat{\beta}^2}$$

where $\hat{s}^2$ is the OLS residual variance.

## Example

Monthly US Treasury rate data ($\Delta t = 1/12$). OLS gives $\hat{\beta}=0.95$, $\hat{\alpha}=0.003$, residual std $\hat{s}=0.004$. Then:

- $\hat{\kappa} = -12\ln(0.95) \approx 0.62$ per year (half-life $\approx 13$ months)
- $\hat{\theta} = 0.003/0.05 = 0.06$ (6% long-run rate)
- $\hat{\sigma} = \sqrt{2\times0.62\times0.004^2/0.0975} \approx 4.9\%$ per year

## Remember

Vasicek MLE is the "time-series fitting" counterpart to yield-curve calibration: instead of inverting today's bond prices to get the drift, you run OLS on historical rate data. The AR(1) connection is what makes it tractable — the Ornstein-Uhlenbeck SDE has exact Gaussian transitions, so the MLE log-likelihood is a simple sum of squared residuals.
