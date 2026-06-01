# Triple-Barrier Method

**Topic:** Computational Finance
**Tags:** label construction, financial machine learning, stop-loss, profit-taking, backtesting, supervised learning
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

The **triple-barrier method** is a path-dependent label construction technique that assigns a training label based on which of three barriers is reached first from entry time $t$: an upper profit-taking barrier, a lower stop-loss barrier, or a horizontal time barrier, mimicking how a real trade with explicit risk limits would be managed.

## Key Formula

Set barriers at $t$ using a multiple $k$ of the estimated daily volatility $\hat{\sigma}_t$:

$$\text{Upper barrier}: \quad p_t(1 + k\hat{\sigma}_t)$$
$$\text{Lower barrier}: \quad p_t(1 - k\hat{\sigma}_t)$$
$$\text{Time barrier}: \quad t + h \text{ (maximum holding period)}$$

The label is then:

$$y_t = \begin{cases} +1 & \text{upper barrier hit first (profit)} \\ -1 & \text{lower barrier hit first (stop-out)} \\ \pm 1 \text{ or } 0 & \text{time barrier expires first (sign of return or neutral)} \end{cases}$$

The label formation horizon $\Delta_t \leq h$ is stochastic — the trade closes early whenever a vertical barrier is hit — which reduces the purge window compared with fixed-horizon labelling.

## Example

A stock enters at $p_t = 100$ with estimated daily volatility $\hat{\sigma}_t = 1\%$ and multiplier $k = 2$. The upper barrier is at 102, the lower at 98, and the time barrier at $t + 5$ days. On day 3 the price reaches 102 — the upper barrier is hit first, so $y_t = +1$ and $\Delta_t = 3$. Had volatility been 0.3\%, the barriers would be at 100.6 and 99.4, making the time barrier far more likely to trigger, increasing the frequency of the neutral or directional-at-expiry label.

## Remember

Fixed-horizon labels assign $y_t = +1$ whenever the 5-day return is positive, regardless of whether the position dipped 10\% intraday before recovering. This mislabels many losing trades as winners. The triple-barrier method labels trades as they would actually close in practice: a position that hits its stop-loss is labelled $-1$ even if the price eventually recovers. The adaptive volatility-scaled barriers also make the labels comparable across different market regimes — a 2\% move in a calm market is treated differently from a 2\% move during a crisis. This realism makes the labels better targets for training financial ML models, at the cost of a more complex cross-validation setup due to the stochastic horizon.
