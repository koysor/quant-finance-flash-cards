# Historical Simulation VaR

**Topic:** Risk
**Tags:** var, historical simulation, non-parametric, fat tails, backtesting, quantile
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

**Historical simulation VaR** is a non-parametric method that estimates Value at Risk directly from observed historical returns, making no assumption about the shape of the return distribution. By using actual past returns, it implicitly captures fat tails, skewness, and non-linear payoffs without needing a parametric model.

Three steps:
1. Collect a window of at least 500 trading days of daily returns.
2. Sort returns in ascending order (worst to best).
3. Read off the return at rank $\lfloor (1 - c) \times N \rfloor$ for confidence level $c$ and sample size $N$.

## Key Formula

$$\text{VaR}_{c,\,1d} = -r_{\lfloor (1-c)\,N \rfloor}$$

where $r_1 \le r_2 \le \cdots \le r_N$ are the sorted daily returns and $\lfloor \cdot \rfloor$ denotes the floor function.

**Scaling to a $T$-day horizon** (assuming independent returns):

$$\text{VaR}_{c,\,T\text{d}} = \text{VaR}_{c,\,1d} \times \sqrt{T}$$

## Example

A risk manager uses $N = 2{,}524$ trading days of FTSE 100 returns.

At 99% confidence, the rank of the VaR observation is:

$$\lfloor (1 - 0.99) \times 2{,}524 \rfloor = \lfloor 25.24 \rfloor = 25$$

The 25th worst daily return is $-3.11\%$, so for a £100 position:

$$\text{VaR}_{99\%,\,1d} = 3.11\% \times £100 = £3.11$$

Scaling to 10 days using the square-root rule:

$$\text{VaR}_{99\%,\,10d} = £3.11 \times \sqrt{10} \approx £9.84$$

## Remember

Historical simulation is the most widely used VaR method in practice because it needs no distributional assumption and automatically reflects the fat tails and skewness present in actual returns. Its central weakness is the reliance on history being representative: it will miss crises outside the observation window entirely, and the result is highly sensitive to the chosen lookback period. A 500-day window containing the 2008 crisis produces a very different VaR from one that does not. Regulators (Basel) require at least one year of data and mandate backtesting to verify that actual losses exceed the VaR estimate no more often than the confidence level implies.
