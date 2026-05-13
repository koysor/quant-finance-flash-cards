# Look-Ahead Bias

**Topic:** Computational Finance
**Tags:** look-ahead bias, backtesting, point-in-time data, survivorship bias, data leakage, overfitting
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Look-ahead bias** occurs when a backtest or model training uses information that would not have been available at the point of the simulated decision. It causes artificially inflated in-sample performance that collapses in live trading, because the model is effectively "cheating" by using future data.

## Key Formula

A decision at time $t$ is valid only if all inputs satisfy:

$$\text{info}(t) \subseteq \mathcal{F}_t \quad \text{(information available at or before } t\text{)}$$

Common violations:
| Source | Mechanism |
|---|---|
| Accounting data | Full-year earnings used before annual filing date |
| Index membership | S&P 500 composition at backtest end applied to past |
| Restatements | Revised revenue figures used instead of originally reported |
| Feature scaling | `StandardScaler` fit on the full dataset, then applied to "past" |
| CV shuffling | Standard $k$-fold leaks future into training folds |

## Example

A backtest uses P/E ratios from a Bloomberg data pull. The database stores the *current* price and *restated* trailing earnings. A firm that reported £2 EPS in 2018 but later restated to £1.50 appears with £1.50 in 2018 — artificially improving the model's apparent ability to identify overvalued stocks. A point-in-time database stores only what was reported at each date, eliminating the restatement leak.

## Remember

Look-ahead bias is the most common cause of live strategy underperformance versus backtest Sharpe ratios. The three main channels in quantitative finance are: (1) **non-point-in-time data** — accounting or index data that reflects later revisions; (2) **survivorship bias** — backtesting only on companies that survived to the present, implicitly avoiding the losers; (3) **training leakage** — fitting a scaler, PCA, or model on the entire dataset before splitting into train/test. Point-in-time vendor databases (e.g. Compustat PIT, FactSet Revere), explicit calendar alignment, and time-series cross-validation are the standard defences.
