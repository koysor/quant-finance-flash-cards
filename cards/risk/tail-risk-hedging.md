# Tail Risk Hedging

**Topic:** Risk
**Tags:** tail risk, hedging, put options, convexity, portfolio protection, black swan
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

Tail risk hedging is the practice of protecting a portfolio against extreme adverse market moves — the rare but severe events in the far left tail of the return distribution. Rather than hedging small day-to-day fluctuations, tail risk hedges are designed to pay off only during crises (typically drawdowns exceeding 15–20%), providing convex payoffs that offset catastrophic losses. The cost of the hedge is the premium paid during normal markets, which acts as a form of portfolio insurance.

## Key Formula

The payoff of a protective put with strike $K$ on a portfolio worth $S$:

$$\text{Payoff} = \max(K - S_T, \, 0)$$

The annualised cost of continuous tail protection as a percentage of portfolio value:

$$\text{Cost}_{\text{annual}} = \frac{P_{\text{put}}}{S} \times \frac{12}{T_{\text{months}}}$$

The **hedge ratio** — the notional amount of protection relative to portfolio value — is sized using the target maximum drawdown $D_{\text{max}}$:

$$\text{Hedge ratio} = \frac{D_{\text{max}} - D_{\text{unhedged}}}{\text{Put payoff at } D_{\text{unhedged}}}$$

## Example

A £10 million equity portfolio buys 3-month 10% OTM put options on the FTSE 100 (strike at 90% of current level). Each put costs 1.2% of notional, so the quarterly cost is:

$$\text{Cost} = 0.012 \times £10{,}000{,}000 = £120{,}000$$

Annualised: £480,000, or 4.8% of portfolio value. If the FTSE 100 falls 30%:

$$\text{Put payoff} = (0.90 - 0.70) \times £10{,}000{,}000 = £2{,}000{,}000$$

The portfolio loses £3,000,000 on equities but recovers £2,000,000 from the puts, reducing the net loss from 30% to 10%. In the 75% of quarters where the market does not crash, the puts expire worthless and the £120,000 premium is the cost of sleeping well at night.

## Remember

Tail risk hedging is the mirror image of short volatility strategies — it pays the variance risk premium instead of collecting it. The mathematical challenge is that naive tail hedging (continuously holding deep OTM puts) is expensive, bleeding 3–5% per year. Sophisticated approaches use roll timing (buying protection when implied volatility is low), strike selection (balancing cost against protection level), and instrument choice (VIX calls, variance swaps, or swaptions for rates). For quant risk managers, the key insight is that tail hedges should be evaluated not on standalone P&L but on their portfolio-level impact: a hedge that costs 2% per year but prevents a 40% drawdown dramatically improves compound returns over a full market cycle.
