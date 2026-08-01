# Drawdown Control

**Topic:** Risk
**Tags:** maximum acceptable drawdown, var budget, position sizing, risk limits, close-out, backtesting
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

Drawdown control is the practice of sizing risk against the distance remaining to a pre-defined maximum acceptable drawdown, rather than against a fixed limit. It converts a static risk appetite into a dynamic constraint that tightens automatically as losses accumulate.

## Key Formula

Define the maximum acceptable drawdown (MADD) in advance, then require today's value at risk to fit inside the remaining budget:

$$\text{VaR}_t \ \le\ \text{MADD} - \text{DD}_t$$

where the current drawdown is measured from the high water mark:

$$\text{DD}_t = \frac{\text{HWM}_t - \Pi_t}{\text{HWM}_t}, \qquad \text{HWM}_t = \max_{s\le t}\Pi_s$$

Because $\text{VaR}_t$ scales with position size, the constraint implies a scaling factor on exposure:

$$\text{scale}_t = \min\!\left(1,\ \frac{\text{MADD} - \text{DD}_t}{\text{VaR}_t^{\text{full}}}\right)$$

## Example

A fund sets MADD at 20%. Its full-size book carries a one-day 99% VaR of 3% of capital.

| State | $\text{DD}_t$ | Budget remaining | Constraint | Exposure |
|---|---|---|---|---|
| At the peak | 0% | 20% | $3\% \le 20\%$ | full |
| After a bad month | 12% | 8% | $3\% \le 8\%$ | full |
| Deeper loss | 18% | 2% | $3\% > 2\%$ | cut to 2/3 |
| At 19% | 19% | 1% | $3\% > 1\%$ | cut to 1/3 |

The book de-risks progressively rather than trading at full size until the limit is breached in a single move.

## Remember

The purpose is survival: a strategy with genuine positive expectancy still returns nothing if it is closed out before the edge is realised, and a prime broker or risk committee will pull the plug at a drawdown level that has nothing to do with the model's long-run merits. This matters especially for statistical arbitrage, where the spread that has moved furthest from equilibrium looks most attractive on entry criteria precisely when the position is already deepest under water — the entry rule says add, and the drawdown budget says the opposite. Note the asymmetry that makes recovery harder than the numbers suggest: a 20% drawdown requires a 25% gain to return to the high water mark, and a 50% drawdown requires 100%. That is also why the high water mark, not the current value, is the reference point — it is the level performance fees resume from, and the level investors judge you against.
