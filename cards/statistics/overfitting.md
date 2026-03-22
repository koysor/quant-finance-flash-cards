# Overfitting

**Topic:** Statistics
**Level:** A Level Mathematics
**Tags:** overfitting, model selection, in-sample, out-of-sample, bias-variance tradeoff
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Overfitting occurs when a model captures noise and idiosyncratic patterns in the training data rather than the true underlying signal, resulting in excellent in-sample performance but poor out-of-sample prediction. In quantitative finance, overfitting is the most common reason that backtested strategies fail in live trading — a model with too many parameters or too much flexibility will find spurious patterns in historical data that do not persist in the future.

## Key Formula

The **bias-variance decomposition** of prediction error:

$$E\bigl[(y - \hat{f}(x))^2\bigr] = \text{Bias}^2 + \text{Variance} + \sigma^2_{\epsilon}$$

An overfit model has low bias but high variance. The **Akaike Information Criterion** penalises model complexity:

$$\text{AIC} = 2k - 2\ln(\hat{L})$$

where $k$ is the number of parameters and $\hat{L}$ is the maximised likelihood. Lower AIC indicates a better bias-variance tradeoff.

A rule of thumb: a model needs at least $\frac{n}{k} \geq 10$ observations per parameter to avoid overfitting, where $n$ is the sample size.

## Example

A researcher fits a momentum signal to 10 years of daily data (2,520 observations). Two models:

| Model | Parameters | In-sample SR | Out-of-sample SR |
|-------|-----------|-------------|-----------------|
| Simple (3 params) | Lookback, holding period, threshold | 1.2 | 0.9 |
| Complex (25 params) | + sector weights, regime filters, interactions | 2.5 | 0.3 |

The complex model fits historical data beautifully ($\text{SR} = 2.5$) but collapses out of sample ($\text{SR} = 0.3$). With 25 parameters and 2,520 observations, the ratio is $\frac{2520}{25} = 101$ — seemingly adequate, but financial time series have low signal-to-noise ratios, so the effective degrees of freedom are much lower.

The simple model sacrifices in-sample fit but generalises far better.

## Remember

Overfitting is the cardinal sin of quantitative strategy development. The financial data environment is uniquely prone to it: signal-to-noise ratios are very low, the data is non-stationary, and researchers have strong incentives to find "working" strategies. Defence against overfitting requires strict discipline: use out-of-sample testing, limit model complexity, apply information criteria (AIC/BIC), use cross-validation adapted for time series, and adjust Sharpe ratios for the number of strategies tested (deflated Sharpe ratio). The maxim "in God we trust, all others bring data" should be amended for quant finance: "in data we trust, provided we haven't tortured it until it confessed."
