# Volatility Arbitrage

**Topic:** Volatility
**Tags:** volatility arbitrage, implied volatility, realised volatility, delta hedging, mispricing
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

Volatility arbitrage (vol arb) is a trading strategy that seeks to profit from the difference between the implied volatility of an option and a forecast of the underlying's future realised volatility. The trader buys options when implied volatility is below their forecast (long vol) or sells options when implied is above (short vol), then delta-hedges to remove directional exposure. The residual P&L depends purely on whether the trader's volatility forecast is more accurate than the market's implied estimate.

## Key Formula

The total P&L of a delta-hedged option position over its lifetime:

$$\text{P\&L} = \frac{1}{2} \int_0^T \Gamma_t \, S_t^2 \left(\sigma_{\text{realised},t}^2 - \sigma_{\text{implied}}^2\right) dt$$

For a single discrete rehedge period:

$$\Delta\text{P\&L} \approx \frac{1}{2}\,\Gamma\,S^2 \left[\left(\frac{\Delta S}{S}\right)^2 - \sigma_{\text{implied}}^2 \, \Delta t\right]$$

The first term is the squared realised return; the second is the implied variance over the interval. Each rehedge is a small bet on whether the actual move exceeds or falls short of the implied move.

## Example

A trader believes that a stock currently at £50 will realise 30% volatility over the next month, but the ATM option implies only 22%. The trader buys the call at 22% implied vol and delta-hedges daily. The option has $\Gamma = 0.04$ and the stock moves £2 on the first day:

$$\Delta\text{P\&L} = \frac{1}{2} \times 0.04 \times 50^2 \times \left[\left(\frac{2}{50}\right)^2 - (0.22)^2 \times \frac{1}{252}\right]$$

$$= 50 \times \left[0.0016 - 0.000192\right] = 50 \times 0.001408 = £0.070$$

The large move (4% daily vs implied daily vol of 1.4%) generates a gamma profit. If this pattern continues — realised vol consistently exceeding implied — the cumulative P&L will be significantly positive by expiry.

## Remember

Volatility arbitrage is the core activity of options market-making desks and dedicated vol funds. The strategy's edge comes entirely from having a superior volatility forecast — whether from GARCH models, high-frequency realised vol estimators, or proprietary signals. For quant developers, the implementation challenge is that the continuous-time P&L formula assumes continuous rehedging, but in practice discrete rebalancing introduces path dependency and hedging error. The gamma weighting ($\Gamma_t S_t^2$) means that P&L is concentrated when the option is near the money and close to expiry — precisely when the bet is most sensitive to whether your forecast was correct.
