# Momentum Crash

**Topic:** Portfolio Theory & Asset Pricing
**Level:** A Level Mathematics
**Tags:** momentum crash, tail risk, factor risk, drawdown, market recovery
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A momentum crash is a sudden, severe loss suffered by momentum strategies when past losers sharply outperform past winners. These crashes typically occur during market recoveries following bear markets: the stocks that fell most during the downturn (now in the short leg of the momentum portfolio) snap back violently, while the defensive stocks that held up (now in the long leg) lag behind. The result is a dramatic reversal that can erase years of accumulated momentum profits in weeks.

## Key Formula

The **momentum portfolio return** during a crash:

$$R_{\text{WML}} = \bar{R}_{\text{winners}} - \bar{R}_{\text{losers}}$$

During a crash, $\bar{R}_{\text{losers}} \gg \bar{R}_{\text{winners}}$, so $R_{\text{WML}} \ll 0$.

The **conditional beta** of the momentum portfolio flips sign in high-volatility regimes:

$$\beta_{\text{WML} | \text{high vol}} < 0 \quad \text{vs.} \quad \beta_{\text{WML} | \text{low vol}} \approx 0$$

This means momentum acts as a short put on the market — it offers steady gains in calm markets but suffers catastrophic losses during sharp reversals.

## Example

In March 2009, as markets recovered from the financial crisis, the US momentum factor (WML) lost approximately 40% in two months. The short leg (beaten-down financial stocks) surged as investors anticipated a recovery:

| Leg | Monthly return |
|-----|---------------|
| Winners (long) | +5% |
| Losers (short) | +45% |

$$R_{\text{WML}} = 5\% - 45\% = -40\%$$

A fund with £10 million in a momentum strategy would have lost £4 million in two months, despite having near-zero market beta in normal conditions.

## Remember

Momentum crashes are the primary reason that momentum's high average return does not represent a "free lunch" — the strategy carries embedded crash risk that standard risk measures like volatility and Sharpe ratio fail to capture. Daniel and Moskowitz (2016) showed that momentum's returns resemble a short option position: frequent small gains punctuated by rare but devastating losses. In practice, quantitative funds manage this risk through volatility scaling (reducing exposure when market volatility rises), dynamic hedging, or blending momentum with value and mean reversion strategies that tend to perform well during exactly the conditions that trigger momentum crashes.
