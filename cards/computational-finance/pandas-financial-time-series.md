# pandas Financial Time Series

**Topic:** Computational Finance
**Tags:** python, pandas, time series, returns, rolling window, resampling
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**pandas** is the standard Python library for manipulating financial time series. Its `DataFrame` and `Series` objects provide date-indexed storage with built-in methods for computing returns, rolling statistics, resampling across frequencies, and handling missing data — operations that underpin nearly every quant workflow from data cleaning to backtesting.

## Key Formula

**Percentage returns** from a price series:

$$r_t = \frac{S_t - S_{t-1}}{S_{t-1}}$$

**pandas implementation:**

```python
import pandas as pd

prices = pd.Series([100, 102, 99, 101, 103],
                   index=pd.date_range("2026-01-01", periods=5))
returns = prices.pct_change().dropna()
```

**Rolling 20-day volatility** (annualised):

```python
vol = returns.rolling(20).std() * np.sqrt(252)
```

## Example

Given daily FTSE 100 closing prices in a DataFrame:

```python
df = pd.read_csv("ftse100.csv", parse_dates=["date"], index_col="date")
df["returns"] = df["close"].pct_change()
df["vol_20d"] = df["returns"].rolling(20).std() * np.sqrt(252)
df["cum_return"] = (1 + df["returns"]).cumprod() - 1

# Resample to monthly returns
monthly = df["close"].resample("ME").last().pct_change()
```

Each of these operations runs as a single vectorised call over the entire time series.

## Remember

pandas is the glue between raw market data and quantitative models. In practice, a quant's day begins with loading price or trade data into a DataFrame, computing derived quantities (returns, volatilities, signals), and passing the result to NumPy or SciPy for heavier computation. The `.rolling()`, `.resample()`, and `.groupby()` methods handle the time-series-specific logic — windowed statistics, frequency conversion, and cross-sectional aggregation — that would otherwise require hundreds of lines of manual indexing code. Mastering these methods is a prerequisite for any Python-based quant role.
