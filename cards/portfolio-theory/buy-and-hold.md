# Buy-and-Hold Strategy

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** passive investing, benchmark, strategy evaluation, performance measurement, equity
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

A **buy-and-hold strategy** is a passive investment approach in which an investor purchases an asset (or a diversified portfolio) and retains it over a long horizon without adjusting the position in response to market fluctuations. It is the standard benchmark against which active trading strategies and machine learning–based predictive models are evaluated, because it captures the full equity risk premium at minimal transaction cost.

## Key Formula

Total return over a holding period $[0, T]$:

$$R_{\text{BH}} = \frac{P_T + \sum_{t=1}^{T} D_t}{P_0} - 1$$

where $P_0$ and $P_T$ are the entry and exit prices and $D_t$ are dividends received. The annualised Sharpe ratio of the benchmark:

$$S_{\text{BH}} = \frac{\bar{R}_{\text{BH}} - r_f}{\sigma_{\text{BH}}}$$

An active strategy is only worth deploying if its risk-adjusted return $S_{\text{active}} > S_{\text{BH}}$ net of transaction costs and taxes.

## Example

An investor buys NVDA at \$400 on 1 January 2023 and holds to 31 December 2023 when NVDA closes at \$495. Assuming no dividends:

$$R_{\text{BH}} = \frac{495}{400} - 1 = +23.75\%$$

An XGBoost direction-prediction model trading NVDA daily must generate cumulative returns above 23.75% after execution costs to justify the complexity over simply holding. In backtests, the model's Sharpe ratio and maximum drawdown are compared directly to the buy-and-hold equivalents as a sanity check.

## Remember

The buy-and-hold benchmark is harder to beat than it looks, for two reasons. First, the equity risk premium for large-cap growth stocks like NVDA is itself a significant risk-adjusted return that an active model must overcome. Second, each prediction-driven trade incurs a bid-ask spread and potential market impact — for daily rebalancing on a liquid equity, these can erode 0.1–0.5% per round trip, compounding to a material drag over hundreds of trades. A machine learning classifier that achieves 55% directional accuracy on NVDA but trades every day will often underperform buy-and-hold net of costs, demonstrating that statistical edge and economic edge are not the same thing.
