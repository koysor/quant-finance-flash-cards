# Option Greeks

**Topic:** Derivatives
**Tags:** options, Greeks, delta, gamma, theta, vega, rho
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

The **Greeks** measure the sensitivity of an option's price to changes in the underlying parameters. They are partial derivatives of the option pricing function.

## Key Greeks

| Greek | Symbol | Measures sensitivity to... | Typical sign (call) |
|---|---|---|---|
| Delta | Δ | Change in underlying price S | 0 to +1 |
| Gamma | Γ | Change in Delta (curvature) | Positive |
| Theta | Θ | Passage of time | Negative |
| Vega | ν | Change in volatility σ | Positive |
| Rho | ρ | Change in risk-free rate r | Positive |

## Key Formulae (Black-Scholes, European call)

$$\Delta = N(d_1)$$

$$\Gamma = \frac{N'(d_1)}{S \, \sigma \sqrt{T}}$$

$$\Theta = -\frac{S \, N'(d_1) \, \sigma}{2\sqrt{T}} - r K e^{-rT} N(d_2)$$

Where N(·) is the cumulative standard normal CDF and N'(·) is the standard normal PDF.

## Example

If a call option has Δ = 0.60 and the underlying rises by £1:

ΔV ≈ Δ × ΔS = 0.60 × £1 = **+£0.60**

If Γ = 0.05, the new Delta after the move is approximately:

Δ_new ≈ 0.60 + 0.05 × £1 = 0.65

## Remember

- **Delta hedging**: buying or selling Δ units of the underlying to make a portfolio Delta-neutral (insensitive to small moves in S).
- **Gamma** is the reason Delta hedging requires constant rebalancing — it measures how quickly Delta changes.
- **Theta** is almost always negative (options lose value as time passes) — this is known as **time decay**.
- **Vega** is not a Greek letter — it is a convention used in finance. All options (calls and puts) gain value when volatility rises.
