# Momentum Regime

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** momentum, regime, trend following, momentum crash, crisis alpha, low volatility
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

The momentum regime is the prevailing market environment that determines whether momentum strategies — buying recent winners and selling recent losers — generate positive or negative returns. Momentum performs best in **trending low-volatility regimes** (persistent directional moves, low realised vol) and suffers most in **high-volatility reversal regimes** (sharp drawdowns followed by rapid recoveries), where the abrupt regime change causes winners and losers to reverse simultaneously.

## Key Formula

A simple momentum signal (12-month minus 1-month return) is regime-dependent:

$$\text{MOM}_{t} = r_{t-12, t-1}$$

The signal's expected return conditioned on volatility regime:

$$\mathbb{E}[\text{MOM return} \mid \sigma_t] \approx \alpha - \beta \cdot \sigma_t$$

where $\sigma_t$ is current realised volatility. Empirically, $\beta > 0$: higher volatility forecasts lower (often negative) momentum returns. Barroso and Santa-Clara (2015) show that **volatility-scaled momentum** largely eliminates this regime sensitivity:

$$\text{MOM}^{\text{scaled}}_t = \frac{\sigma_{\text{target}}}{\hat{\sigma}_t} \times \text{MOM}_t$$

## Example

S&P 500 momentum strategy (long top decile, short bottom decile, monthly rebalancing), average monthly returns by volatility regime:

| VIX Regime | Avg Monthly Return | Sharpe (ann.) |
|------------|-------------------|--------------|
| VIX $< 15$ (low vol) | +1.8% | +1.4 |
| VIX 15–25 (medium) | +0.7% | +0.5 |
| VIX $> 25$ (high vol) | −2.1% | −0.8 |
| VIX $> 35$ (crisis) | −5.3% | −2.1 |

The strategy's full-period Sharpe of 0.7 masks a −5.3% monthly average during crises — the momentum crash.

## Remember

Understanding the momentum regime is essential for strategy allocation in multi-factor portfolios: momentum and low-volatility factors are negatively correlated during high-vol regimes (low-vol stocks hold up better), making them natural complements. CTAs (trend-followers) who apply time-series momentum across multiple asset classes experience a different regime dependency — cross-sectional equity momentum crashes while commodity and bond trend-following continues working, because the crisis triggers bond rallies and commodity dislocations that create new cross-asset trends. This is why diversified trend-following funds show **crisis alpha** even when equity momentum crashes.

