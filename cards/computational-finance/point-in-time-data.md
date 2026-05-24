# Point-in-Time Data

**Topic:** Computational Finance
**Tags:** point-in-time data, PIT, restatements, look-ahead bias, fundamental data, backtesting
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**Point-in-time (PIT) data** is a database format that records every observation with the timestamp at which it became known, preserving historical revisions and restatements. A query for a variable at date $t$ returns the value that was publicly available on $t$ — not any later-revised figure — enabling backtests to use only information that would have been observable at the simulated decision date.

## Key Formula

Let $v(t, \tau)$ denote the value of a variable at reference period $t$, as known at publication time $\tau \geq t$. A point-in-time query at date $d$ returns:

$$v_\text{PIT}(t, d) = v\!\left(t,\; \tau^*\right) \quad \text{where } \tau^* = \min\{\tau \geq t : \tau \leq d\}$$

that is, the first published version of the figure that was available by date $d$. A non-PIT database returns the most recent revision $v(t, \infty)$, introducing look-ahead bias of magnitude $v(t, \infty) - v(t, \tau^*)$.

## Example

A UK company reports Q2 2019 EPS of 42p on 12 August 2019. A restatement on 5 March 2020 revises this to 31p due to an accounting error.

| Query date | PIT result | Non-PIT result | Bias |
|---|---|---|---|
| 1 September 2019 | 42p | 31p | −11p (look-ahead) |
| 1 June 2020 | 31p | 31p | none |

A backtest run on 1 September 2019 that uses a non-PIT database would "know" the restated 31p figure three months before it was announced.

## Remember

Point-in-time data is the most important infrastructure requirement for fundamental quantitative strategies. Academic studies have shown that up to 50% of apparent alpha from accounting-based signals (earnings yield, book-to-market) disappears when non-PIT databases are replaced with PIT equivalents — the "alpha" was information arbitrage against data that was not actually available to any investor at the time. Commercial PIT databases include Compustat PIT, FactSet Revere, and Bloomberg's "as-reported" fields; they are expensive because storing every vintage of every filing requires substantially more storage and operational overhead than simply keeping the latest revision.
