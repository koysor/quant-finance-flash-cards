# Backtesting

**Topic:** Risk
**Level:** A Level Mathematics
**Tags:** backtesting, strategy validation, historical simulation, out-of-sample, overfitting
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Backtesting is the process of evaluating a trading strategy or risk model by applying it to historical data and measuring how it would have performed. A backtest simulates trades using past prices, applying the strategy's rules as if in real time, and records the resulting returns, drawdowns, and risk metrics. Backtesting is the primary tool for strategy validation in quantitative finance, but its results are only meaningful if conducted rigorously — without lookahead bias, survivorship bias, or overfitting to the in-sample period.

## Key Formula

The **Sharpe ratio** of a backtested strategy:

$$\text{SR} = \frac{\bar{r} - r_f}{\sigma_r} \times \sqrt{252}$$

where $\bar{r}$ is the mean daily excess return and $\sigma_r$ is the standard deviation of daily returns, annualised by $\sqrt{252}$.

The **deflated Sharpe ratio** adjusts for multiple testing:

$$\text{DSR} = \Phi\!\left(\frac{(\text{SR} - \text{SR}_0)\sqrt{T-1}}{\sqrt{1 - \hat{\gamma}_3 \cdot \text{SR} + \frac{\hat{\gamma}_4 - 1}{4} \cdot \text{SR}^2}}\right)$$

where $\text{SR}_0$ accounts for the number of strategies tested, $\hat{\gamma}_3$ is skewness, and $\hat{\gamma}_4$ is kurtosis.

## Example

A momentum strategy is backtested over 10 years (2,520 trading days). It produces a mean daily return of 0.04% with standard deviation 0.80%:

$$\text{SR} = \frac{0.0004}{0.008} \times \sqrt{252} = 0.05 \times 15.87 = 0.79$$

This looks promising. However, the researcher tested 50 variations before selecting this one. The expected maximum Sharpe ratio from 50 random strategies is approximately:

$$E[\max(\text{SR})] \approx \sqrt{2 \ln(50)} \times \frac{1}{\sqrt{252}} \times \sqrt{252} \approx \sqrt{2 \times 3.91} = 2.80 \times \frac{1}{\sqrt{T/252}}$$

After deflation, the adjusted p-value may no longer be significant — the 0.79 SR could be a statistical artefact of testing many strategies on the same data.

## Remember

The gap between backtest performance and live performance is the central challenge of quantitative finance. Backtests are biased upward by overfitting, survivorship bias, and the inability to model realistic transaction costs and market impact. A robust backtesting framework uses out-of-sample validation (train on one period, test on another), walk-forward analysis, and the deflated Sharpe ratio to account for multiple testing. The rule of thumb is that live performance is typically 50% or less of backtested performance. Any strategy that looks "too good to be true" in a backtest almost certainly is.
