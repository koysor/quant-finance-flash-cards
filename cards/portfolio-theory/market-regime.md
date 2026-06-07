# Market Regime

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** market regime, bull market, bear market, risk-on, risk-off, regime detection, volatility
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

A **market regime** is a period during which asset return distributions, correlations, and volatility are approximately stationary — the market is behaving according to a consistent set of underlying dynamics. Regimes shift when macroeconomic conditions, investor risk appetite, or liquidity conditions change structurally, causing the parameters of return-generating processes to move to a new, different stationary state.

## Key Formula

A simple two-regime classification uses rolling realised volatility $\hat{\sigma}_t$ against a threshold $\sigma^*$:

$$\text{Regime}_t = \begin{cases} \text{Low-vol (Risk-on)} & \hat{\sigma}_t \leq \sigma^* \\ \text{High-vol (Risk-off)} & \hat{\sigma}_t > \sigma^* \end{cases}$$

Common empirical markers for the four canonical regimes:

| Regime | Key Indicator | Typical Equity Return | Typical Equity Vol |
|--------|--------------|----------------------|-------------------|
| Bull (risk-on) | VIX $< 15$, 200-day MA uptrend | $+12\%$ to $+20\%$ p.a. | $10\%$–$15\%$ |
| Bear (risk-off) | VIX $> 25$, drawdown $> 15\%$ | $-10\%$ to $-40\%$ p.a. | $25\%$–$50\%$ |
| Recovery | Falling VIX, improving credit spreads | $+20\%$–$+40\%$ p.a. | $15\%$–$25\%$ |
| Stagnation | Flat 200-day MA, low volume | $-2\%$ to $+4\%$ p.a. | $8\%$–$12\%$ |

## Example

In 2008, the S&P 500 spent the first half of the year in a deteriorating bull regime, then transitioned to a full bear regime after Lehman collapsed in September. A momentum strategy calibrated to the 2004–2007 bull regime assumed return autocorrelation of +0.05 (trends persist). In the bear regime, autocorrelation flipped to $-0.12$ (trends reverse intraday) — the same strategy lost 40% in Q4 2008. Strategies that detected the VIX crossing 30 and reduced risk in early October avoided most of the drawdown.

## Remember

Regime misidentification is one of the most common causes of live strategy underperformance relative to backtest results. Backtests often cover a single dominant regime (e.g. the 2010–2020 low-volatility bull market) and strategies are implicitly calibrated to it. When the regime shifts — higher inflation, rising rates, correlation breakdowns — model parameters are no longer valid and positions sized for calm markets become catastrophically large. In practice, quants layer regime indicators (VIX level, yield curve slope, credit spread, 200-day moving average) before committing capital, using them as *meta-signals* that determine which sub-strategy is currently relevant rather than blindly applying a single model across all conditions.

