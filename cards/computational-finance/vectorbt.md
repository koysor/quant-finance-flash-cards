# vectorbt

**Topic:** Computational Finance
**Tags:** backtesting, vectorised, parameter sweep, numba, numpy, algorithmic trading
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**vectorbt** is a high-performance Python backtesting library that uses NumPy broadcasting and Numba JIT compilation to simulate thousands of parameter combinations simultaneously in a single pass — running in seconds what event-driven frameworks like Zipline would take hours to evaluate one combination at a time.

## Key Formula

A vectorised signal backtest operates on 2-D arrays where each column is a parameter combination. For $P$ parameter sets and $T$ time steps, the portfolio value matrix $\mathbf{V} \in \mathbb{R}^{T \times P}$ is updated at each bar:

$$V_{t,p} = V_{t-1,p} \cdot \left(1 + r_t \cdot w_{t-1,p}\right) - c \cdot \lvert\Delta w_{t,p}\rvert \cdot V_{t-1,p}$$

where $w_{t,p}$ is the position for parameter set $p$ at time $t$ and $c$ is the per-trade cost. All $P$ columns update in parallel via NumPy broadcasting, with the inner loop JIT-compiled by Numba.

## Example

```python
import vectorbt as vbt

# Test 2,500 SMA crossover combinations (50 fast × 50 slow periods)
fast = vbt.IndicatorFactory.from_pandas_ta('SMA').run(
    price, timeperiod=vbt.Param(range(5, 55)))
slow = vbt.IndicatorFactory.from_pandas_ta('SMA').run(
    price, timeperiod=vbt.Param(range(10, 105, 2)))

entries = fast.real_crossed_above(slow.real)
exits   = fast.real_crossed_below(slow.real)

pf = vbt.Portfolio.from_signals(price, entries, exits, freq='1D')
pf.sharpe_ratio().idxmax()   # find the best-performing parameter set
```

On a single laptop, this runs 2,500 backtests in under 5 seconds.

## Remember

The critical risk of vectorbt's parameter sweep capability is that it makes backtest overfitting trivially easy: testing 2,500 SMA combinations on the same dataset and selecting the best Sharpe is a textbook multiple-testing problem. The expected maximum Sharpe under the null (no skill) rises with $\sqrt{\ln 2500} \approx 2.8$ times the single-test threshold. vectorbt is correctly used as a fast **screening** tool — to eliminate obviously unprofitable signal families before committing to a full out-of-sample validation via Zipline or a CPCV test. Using it to select a final strategy parameter without a held-out period is precisely the overfitting trap that the Deflated Sharpe Ratio and PBO are designed to diagnose.
