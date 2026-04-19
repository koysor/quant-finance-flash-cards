# Feature Engineering

**Topic:** Computational Finance
**Tags:** feature engineering, feature selection, signal construction, factor, data preprocessing, ML pipeline
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Feature engineering** is the process of transforming raw data into informative input variables (features) that improve machine learning model performance. It encompasses creating new variables, selecting relevant ones, and transforming existing ones to expose underlying patterns more clearly.

## Key Formula

Common transformations applied to a raw price series $S_t$:

**Momentum signal:**
$$\text{Mom}_{t} = \frac{S_t - S_{t-n}}{S_{t-n}}$$

**z-score normalisation:**
$$\tilde{x}_t = \frac{x_t - \mu_{[t-w,t]}}{\sigma_{[t-w,t]}}$$

**Correlation-based feature selection** (remove redundant features where $|\rho_{ij}| > 0.95$).

## Example

Raw data: daily OHLCV for 500 stocks. Engineered features: 1-month return, 3-month volatility, volume z-score, RSI(14), 50/200-day moving average ratio, and sector dummy. These 6 features per stock replace 250+ raw price observations and are far more predictive for a monthly-return model.

## Remember

In quantitative finance, feature engineering is equivalent to signal research: constructing momentum, value, carry, and quality factors from raw market data. The quality of features dominates model architecture — a well-engineered set of 5 features beats 500 raw features fed into a deep neural network, because machine learning models cannot manufacture economic intuition that is absent from the input data.
