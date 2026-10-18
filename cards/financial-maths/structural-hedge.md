# Structural Hedge

**Topic:** Financial Mathematics
**Tags:** structural hedge, replicating portfolio, non-maturity deposits, net interest income, swaps, equity
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

A **structural hedge** is a rolling portfolio of fixed-rate assets or receive-fixed swaps that a bank holds against funding that does not reprice with market rates, mainly shareholders' equity and the stable core of non-maturity deposits. It converts that funding's short, floating behaviour into a stable, longer-dated income stream, smoothing net interest income through the rate cycle.

## Key Formula

A **ladder** of $N$ equal tranches, one maturing and rolling each year, produces an income rate that adjusts gradually:

$$y_k = \frac{(N-k)\,y_0 + \sum_{j=1}^{k} r_j}{N}$$

where $y_0$ is the initial yield, $r_j$ the rate at which tranche $j$ was reinvested, and $k$ the number of years since rates moved.

## Example

A bank hedges £20bn in a five-year ladder of £4bn tranches, all yielding 4%. Rates fall to 1% and stay there. Each year one tranche rolls at 1%:

| Year | Hedge yield | Income vs unhedged at 1% |
|---|---|---|
| 1 | $(16 \times 4\% + 4 \times 1\%)/20 = 3.4\%$ | $20\text{bn} \times 2.4\% = £480\text{m}$ |
| 2 | 2.8% | £360m |
| 3 | 2.2% | £240m |
| 5 | 1.0% | £0 |

An unhedged bank would have seen its yield drop to 1% immediately; the hedge delays the fall by years.

## Remember

The hedge cuts both ways: when rates rise, it earns less than the market until it rolls up. Its value is stability, not extra profit. It depends critically on the behavioural assumption about how much of the deposit base is genuinely sticky, which is why a structural hedge is sized from the same core and non-core deposit modelling that drives the IRRBB measure. Mis-estimating the sticky share means hedging funding that is not there.
