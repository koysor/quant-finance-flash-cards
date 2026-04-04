# Relative Value Strategy

**Topic:** Financial Mathematics
**Tags:** relative value, pairs trading, spread, convergence, market neutral, mispricing
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

A relative value strategy seeks to profit from the mispricing between two or more related instruments, going long the cheap one and short the expensive one, then waiting for the spread to converge. Unlike directional strategies that bet on market direction, relative value strategies are typically market-neutral — the long and short legs offset broad market moves, isolating the spread as the source of return. Examples include pairs trading in equities, yield curve trades in fixed income, and dispersion trading in volatility.

## Key Formula

The **spread** between two related instruments $A$ and $B$ with hedge ratio $\beta$:

$$\text{Spread}_t = P_{A,t} - \beta \cdot P_{B,t}$$

The **z-score** of the spread, used to generate trade signals:

$$z_t = \frac{\text{Spread}_t - \bar{\mu}}{\bar{\sigma}}$$

where $\bar{\mu}$ and $\bar{\sigma}$ are the rolling mean and standard deviation of the spread. The strategy enters when $|z_t| > z^*$ (typically 1.5–2.0) and exits when $z_t$ returns near zero.

The **expected P&L** per round trip:

$$E[\text{P\&L}] = 2 \times z^* \times \bar{\sigma} - C_{\text{transaction}}$$

## Example

Two FTSE 100 bank stocks, X and Y, historically trade with a price ratio near 1.5. Stock X is at £15.00 and Stock Y at £9.20, giving a spread of $15.00 - 1.5 \times 9.20 = £1.20$. The rolling mean spread is £0.50 with standard deviation £0.30:

$$z = \frac{1.20 - 0.50}{0.30} = 2.33$$

The spread is 2.33 standard deviations above the mean — Stock X is expensive relative to Y. The trader shorts £100,000 of X and goes long £150,000 of Y (hedge-ratio-adjusted). Over the next 3 weeks, the spread mean-reverts to £0.60:

$$\text{P\&L} = (1.20 - 0.60) \times \text{notional per spread unit} = £0.60 \times 6{,}667 = £4{,}000$$

The profit came from the convergence of the spread, not from the direction of the bank sector.

## Remember

Relative value is one of the broadest hedge fund strategy categories and the philosophical foundation of quantitative trading — the idea that mispricings between related instruments are more predictable than the direction of any single asset. In fixed income, the classic relative value trade is the on-the-run/off-the-run Treasury spread; in equities, it is statistical arbitrage and pairs trading; in volatility, it is dispersion and calendar spread trading. The key risk is that spreads can widen before they converge — a phenomenon that destroyed Long-Term Capital Management in 1998. For quant developers, implementing relative value strategies requires cointegration testing to verify the spread is mean-reverting, robust hedge ratio estimation, and careful monitoring of the holding period, because a spread that appears mispriced may reflect a genuine structural change rather than a temporary dislocation.
