# Hedging Gain Statistic

**Topic:** Computational Finance
**Tags:** hedging effectiveness, minimum variance delta, backtesting, hull-white, sum of squared errors
**Created:** 2026-07-07
**Author:** Claude Sonnet 5

---

## Definition

The **Gain statistic** (Hull and White, 2017) scores how much better a candidate delta hedges an option book than the plain Black-Scholes delta, measured as the proportional reduction in the sum of squared daily hedging errors. It is the standard backtesting metric for comparing minimum-variance-style deltas against $\delta_{BS}$ across a historical sample of daily price moves.

## Key Formula

$$\text{Gain} = 1 - \frac{\text{SSE}\left(\Delta f - \delta_{MV}\,\Delta S\right)}{\text{SSE}\left(\Delta f - \delta_{BS}\,\Delta S\right)}$$

where $\text{SSE}(\cdot)$ sums the squared daily hedging errors over the backtest sample, $\Delta f$ is the daily change in option price and $\Delta S$ is the daily change in the underlying. $\text{Gain} > 0$ means the candidate delta hedged better than Black-Scholes; $\text{Gain} < 0$ means it hedged worse.

## Example

Over a 60-day backtest of 1-month SPX puts, the Black-Scholes-delta hedging errors have $\text{SSE}(\Delta f - \delta_{BS}\Delta S) = 480$. Hedging the same book with the minimum-variance delta gives $\text{SSE}(\Delta f - \delta_{MV}\Delta S) = 360$.

$$\text{Gain} = 1 - \frac{360}{480} = 1 - 0.75 = 0.25$$

A Gain of 25% means the minimum-variance delta removed a quarter of the Black-Scholes hedging-error variance over that sample — but the same statistic computed separately on an at-the-money bucket over the same period might come out negative, since Gain is not guaranteed to be positive in every slice of the data.

## Remember

Gain must be reported by delta bucket and by maturity, not as a single blended number, because trading activity — and therefore squared-error mass — concentrates near the forward: an aggregate Gain can look flat or negative even when the minimum-variance delta clearly wins in the sparsely-traded wings, or vice versa, a headline-positive Gain can be hiding losses exactly where most of the book's risk actually sits. Hull and White's own study found this pattern for S&P options — improvements out-of-the-money, deterioration near-the-money — and a breakdown of the whole approach during the March 2023 regime shift, when index implied volatility stopped falling as spot fell (the smile went "sticky" rather than moving with spot). A negative or mixed Gain result is a legitimate, expected finding, not a failed experiment.
