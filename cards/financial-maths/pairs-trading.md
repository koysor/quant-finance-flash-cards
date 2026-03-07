# Pairs Trading

**Topic:** Financial Mathematics
**Tags:** pairs trading, mean reversion, market neutral, cointegration, spread
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Pairs trading is a market-neutral strategy that identifies two historically correlated securities, goes long the relatively undervalued one and short the relatively overvalued one, and profits when the price spread between them reverts to its historical mean.

## Key Formula

The **spread** between two co-moving stocks $A$ and $B$ is:

$$S_t = P_t^A - \beta \, P_t^B$$

where $\beta$ is the hedge ratio estimated from regression: $P^A = \alpha + \beta P^B + \varepsilon$.

A trade is opened when the **z-score** of the spread exceeds a threshold:

$$z_t = \frac{S_t - \bar{S}}{\sigma_S}$$

- Enter long $A$ / short $B$ when $z_t < -k$ (spread unusually narrow)
- Enter short $A$ / long $B$ when $z_t > +k$ (spread unusually wide)
- Exit when $z_t$ returns to zero

## Example

Two oil companies have a historical spread with mean $\bar{S} = £2.00$ and standard deviation $\sigma_S = £0.50$. The entry threshold is $k = 2$.

Today, stock $A$ trades at £48 and stock $B$ at £50, with $\beta = 1$:

$$S_t = £48 - 1 \times £50 = -£2.00$$

$$z_t = \frac{-2.00 - 2.00}{0.50} = -8.0$$

The spread is 8 standard deviations below the mean — a strong signal to go long $A$ and short $B$. If the spread reverts to £2.00, the profit is £4.00 per share pair, regardless of whether the overall market rises or falls.

## Remember

Pairs trading is one of the oldest quantitative strategies, pioneered by Nunzio Tartaglia's group at Morgan Stanley in the 1980s. Its appeal is **market neutrality** — because the long and short legs roughly cancel out market exposure, the strategy's return depends on the spread reverting, not on market direction. The mathematical foundation is **cointegration**: the two prices may individually be non-stationary, but their linear combination is stationary. The main risk is that the spread diverges permanently (a "broken pair"), which can happen when one company faces an idiosyncratic shock like a takeover bid or earnings collapse. Robust pairs trading therefore requires continuous monitoring of the cointegration relationship.
