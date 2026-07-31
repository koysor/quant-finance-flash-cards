# Option Quote Filtering

**Topic:** Computational Finance
**Tags:** data cleaning, liquidity filter, bid-ask spread, open interest, volatility surface, calibration
**Created:** 2026-07-31
**Author:** Claude Opus 5

---

## Definition

Option quote filtering is the pre-calibration step that removes illiquid or economically meaningless option quotes from a raw end-of-day chain, so that a volatility surface is fitted only to prices a trader could actually transact at. It is a screening rule applied before any interpolation, not a smoothing applied afterwards.

## Key Formula

A standard liquidity screen keeps a quote $(T_i, K_j)$ only if all of the following hold:

$$\text{DTE} \ge 14, \qquad 0.05 \le \lvert \delta_{BS}\rvert \le 0.90, \qquad \text{bid} > 0, \qquad \text{OI} > 0$$

Relative spread is the usual quality weight for a weighted least-squares fit:

$$s_{ij} = \frac{\text{ask}_{ij} - \text{bid}_{ij}}{\text{mid}_{ij}}, \qquad \omega_{ij} = \frac{1}{s_{ij}^2}$$

Vega weighting is the alternative when fitting in volatility rather than price space, since a fixed price error maps to a larger implied-volatility error where vega is small:

$$\omega_{ij} = \mathcal{V}_{ij}^2$$

## Example

An SPX chain has 6,200 raw rows on one date. Applying the screen in sequence:

| Filter | Rows removed | Remaining |
|---|---|---|
| Raw chain | — | 6,200 |
| DTE $< 14$ | 1,340 | 4,860 |
| $\lvert\delta_{BS}\rvert$ outside $[0.05, 0.90]$ | 2,180 | 2,680 |
| Zero bid | 410 | 2,270 |
| Zero open interest | 355 | 1,915 |

Under a third of the chain survives. A deep out-of-the-money put quoted 0.05 bid / 0.45 ask has a relative spread of 160% — its implied volatility is essentially unconstrained by the market, and including it would drag the fitted wing by several volatility points.

## Remember

Surface quality is set by the input filter far more than by the choice of interpolator. Two failures dominate: stale quotes with zero open interest carry an implied volatility from whenever they last traded, and near-expiry options have vega so small that a single tick of price noise moves implied volatility by whole percentage points — the $1/\Delta T$ factor in Dupire's formula then magnifies that noise into a wild short-end local volatility. Filtering by Black-Scholes delta rather than by strike is deliberate: a fixed strike band is far too wide for a one-week option and far too narrow for a one-year option, whereas a delta band automatically scales with $\sigma\sqrt{T}$ and keeps a consistent liquidity standard across the whole term structure.
