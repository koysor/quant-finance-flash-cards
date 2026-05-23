# Technical Indicators

**Topic:** Computational Finance
**Tags:** technical analysis, feature engineering, momentum, volatility, trading signals
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**Technical indicators** are mathematical functions computed from OHLCV price and volume data that summarise historical market behaviour into a scalar signal used for trading decisions or as features in machine learning models. They are broadly classified as momentum indicators (RSI, MACD), volatility indicators (Bollinger Bands, ATR), volume indicators (OBV, VWAP), and trend indicators (moving averages).

## Key Formula

The four main families and their representative formulas:

**Momentum:** $\text{RSI} = 100 - 100/(1 + \bar{G}/\bar{L})$

**Trend:** $\text{EMA}_n(P_t) = \tfrac{2}{n+1} P_t + \tfrac{n-1}{n+1}\,\text{EMA}_n(P_{t-1})$

**Volatility:** $\text{ATR}_t = \tfrac{(n-1)\,\text{ATR}_{t-1} + \text{TR}_t}{n}$, where $\text{TR}_t = \max(H_t - L_t,\, |H_t - C_{t-1}|,\, |L_t - C_{t-1}|)$

**Volume:** $\text{OBV}_t = \text{OBV}_{t-1} + \text{sign}(C_t - C_{t-1})\cdot V_t$

## Example

Features derived from NVDA daily OHLCV data for use in an XGBoost direction classifier:

| Category | Feature | Typical lookback |
|---|---|---|
| Momentum | `rsi_14` | 14 days |
| Trend | `macd_hist` | 12/26/9 days |
| Volatility | `bb_pct_b`, `atr_14` | 20, 14 days |
| Volume | `obv_diff` | 1-day difference |
| Return | `log_return_5d` | 5 days |

## Remember

Technical indicators exist because raw OHLCV values are non-stationary and difficult for a model to learn from directly — today's close of \$880 carries no information unless compared to something. Indicators perform this comparison implicitly: RSI compares up-moves to down-moves, MACD compares short-term trend to long-term trend, ATR compares today's range to recent ranges. For a financial ML pipeline, the key practical consideration is **look-ahead bias**: every indicator must be computed using only data available at the prediction point $t$, meaning the indicator value for day $t$ can use prices up to and including day $t$'s close but not beyond. Indicators computed in a vectorised pandas operation on the full dataset will silently introduce look-ahead bias unless the index is carefully managed.
