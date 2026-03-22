# Momentum Strategy

**Topic:** Portfolio Theory & Asset Pricing
**Level:** A Level Mathematics
**Tags:** momentum, trend following, cross-sectional, winner-loser, factor strategy
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A momentum strategy systematically buys recent winners and sells (or shorts) recent losers, exploiting the empirical tendency for assets that have performed well over the past 3–12 months to continue outperforming, and vice versa. Cross-sectional momentum ranks assets within a universe and takes long-short positions based on relative performance, while time-series momentum (trend following) goes long or short each asset based on its own past return.

## Key Formula

The **cross-sectional momentum signal** for asset $i$ over a formation period of $J$ months (typically skipping the most recent month):

$$\text{MOM}_i = \frac{P_{i,t-1}}{P_{i,t-J-1}} - 1$$

The **momentum factor return** (Winners Minus Losers, WML):

$$R_{\text{WML}} = \bar{R}_{\text{top decile}} - \bar{R}_{\text{bottom decile}}$$

In the Carhart four-factor model, momentum is added to the Fama–French three factors:

$$R_i - R_f = \alpha_i + \beta_i (R_m - R_f) + s_i \cdot \text{SMB} + h_i \cdot \text{HML} + w_i \cdot \text{WML} + \epsilon_i$$

## Example

A fund ranks 500 stocks by their 12-month return (skipping the most recent month). The top 50 stocks (winners) returned an average of 28% over the formation period; the bottom 50 (losers) returned $-15\%$.

The fund goes long the winners and short the losers with equal capital of £5 million each side. Over the next month:

- Winners portfolio return: $+2.1\%$ → gain of $£5{,}000{,}000 \times 0.021 = £105{,}000$
- Losers portfolio return: $-0.8\%$ → gain on short of $£5{,}000{,}000 \times 0.008 = £40{,}000$

$$R_{\text{WML}} = 2.1\% - (-0.8\%) = 2.9\%$$

Total profit: £145,000 on a market-neutral position with zero net market exposure.

## Remember

Momentum is one of the most robust anomalies in finance — documented across equities, bonds, currencies, and commodities, and persisting for over a century of data. The Carhart four-factor model added momentum (WML) to the Fama–French framework precisely because momentum explained a large fraction of mutual fund performance that the three-factor model could not. However, momentum carries severe tail risk: it is prone to sudden, violent reversals ("momentum crashes") that typically occur during market recoveries after crises, when past losers snap back sharply. Risk management for momentum strategies must account for this crash risk, often through volatility scaling or dynamic exposure reduction when market volatility spikes.
