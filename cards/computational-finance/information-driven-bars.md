# Information-Driven Bars

**Topic:** Computational Finance
**Tags:** tick bars, volume bars, dollar bars, sampling, market microstructure, backtesting
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

Information-driven bars sample a price series when a fixed amount of market activity has accumulated — a set number of trades, a set volume, or a set traded notional — rather than when a fixed amount of clock time has passed. The aim is to produce observations that carry roughly equal information content.

## Key Formula

Each bar closes when its running total crosses a threshold:

| Bar type | Closes when | Accumulator |
|---|---|---|
| Time bars | $\Delta t \ge T$ | clock |
| Tick bars | $n \ge N$ | trade count |
| Volume bars | $\sum v_i \ge V$ | shares traded |
| Dollar bars | $\sum p_i v_i \ge D$ | notional traded |

For dollar bars the closing index $k$ is the smallest satisfying:

$$\sum_{i=1}^{k} p_i\,v_i \ \ge\ D$$

Statistically the payoff is that returns sampled this way are far closer to independent and identically distributed: time bars oversample quiet periods and undersample active ones, producing serial correlation, heteroskedasticity and fat tails that are artefacts of the clock rather than of the market.

## Example

A stock trades £50m of notional on a normal day but £200m on an earnings day. With a threshold of $D = £5\text{m}$:

| Day | Notional | Dollar bars | Time bars (hourly) |
|---|---|---|---|
| Normal | £50m | 10 | 8 |
| Earnings | £200m | 40 | 8 |

Hourly sampling produces eight observations on both days, so the earnings day — where nearly all the information arrives — is represented no better than a quiet one. Dollar bars automatically allocate four times the observations to it.

Dollar bars also self-correct for price drift: a stock doubling in price halves the shares needed to reach £5m, so bar counts stay stable where volume bars would drift.

## Remember

The choice of bar is a modelling decision made before any strategy exists, and it silently shapes everything downstream. Every statistical test applied to returns — the ADF test on a spread, a variance ratio, a Sharpe ratio — assumes observations are comparable draws, and time bars violate that assumption in a way that inflates apparent significance. It also has a mundane but decisive practical dimension: many retail feeds do not deliver true tick data at all, IBKR for instance aggregating to five-second bars, so the finest bar you can construct is set by your data source rather than your preference. Dollar bars are usually the default choice for backtesting because they are robust both to intraday volume patterns and to corporate actions that change share counts.
