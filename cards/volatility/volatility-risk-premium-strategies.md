# Volatility Risk Premium Strategies

**Topic:** Volatility
**Tags:** volatility risk premium, short volatility, options selling, straddle, iron condor, premium harvesting
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

Volatility risk premium (VRP) strategies are systematic trading approaches that harvest the persistent gap between implied and realised volatility. Because implied volatility exceeds realised volatility on average, these strategies sell options or variance to collect the premium, profiting in calm markets and losing during volatility spikes. Common implementations include selling straddles, strangles, iron condors, and variance swaps, each offering a different trade-off between premium collected and tail risk exposure.

## Key Formula

The expected return from selling a delta-hedged ATM straddle over period $T$:

$$\mathbb{E}[\text{P\&L}] \approx \text{Vega} \times (\sigma_{\text{implied}} - \sigma_{\text{realised}})$$

For a short iron condor (sell OTM call and put spreads at strikes $K_1 < K_2 < K_3 < K_4$), the maximum profit equals the net premium received $P$:

$$\text{Max profit} = P, \qquad \text{Max loss} = (K_2 - K_1) - P$$

The Sharpe ratio of a VRP strategy is approximately:

$$\text{SR} \approx \frac{\overline{\sigma_{\text{impl}} - \sigma_{\text{real}}}}{\text{std}(\sigma_{\text{impl}} - \sigma_{\text{real}})}$$

## Example

A trader sells a monthly ATM straddle on the FTSE 100 when implied volatility is 18%. The straddle premium collected is £4.20 per unit. Over the month, realised volatility turns out to be 14%. The approximate vega-based profit:

$$\text{P\&L} \approx \text{Vega} \times (18\% - 14\%) = £0.80 \times 4 = £3.20$$

The strategy keeps most of the £4.20 premium. However, if a shock pushes realised volatility to 35%, the straddle loss could be:

$$\text{P\&L} \approx £0.80 \times (18\% - 35\%) = -£13.60$$

One bad month erases several months of premium — the classic short volatility return profile.

## Remember

VRP strategies are among the most popular systematic strategies at quantitative hedge funds and structured product desks. The key insight is that the premium exists because investors are willing to overpay for downside protection — put options embed a fear premium that exceeds the actuarial cost of the protection. For quant developers, implementing these strategies requires careful attention to sizing (keeping losses survivable), tail risk management (using spreads rather than naked options), and regime detection (reducing exposure when the VRP compresses or inverts during crises). The strategy's Sharpe ratio of roughly 0.5–0.8 is attractive but masks extreme negative skewness — a feature that standard risk metrics like VaR systematically understate.
