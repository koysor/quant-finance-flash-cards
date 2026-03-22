# SABR Model

**Topic:** Derivatives
**Level:** A Level Mathematics
**Tags:** SABR, stochastic volatility, smile, rates, swaption, FX options
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The SABR (Stochastic Alpha Beta Rho) model is a stochastic volatility model introduced by Hagan, Kumar, Lesniewski, and Woodward (2002) that is the industry standard for interpolating and extrapolating the volatility smile for interest rate options and FX options. It models the forward rate and its volatility as correlated stochastic processes, with four parameters: $\alpha$ (initial volatility level), $\beta$ (CEV exponent controlling backbone shape), $\rho$ (correlation between forward and volatility), and $\nu$ (vol-of-vol controlling smile curvature).

## Key Formula

The **SABR dynamics** under the forward measure:

$$dF = \alpha F^{\beta} \, dW_1$$
$$d\alpha = \nu \alpha \, dW_2$$
$$dW_1 \, dW_2 = \rho \, dt$$

The **Hagan approximation** for implied volatility at strike $K$ with forward $F$:

$$\sigma_{\text{impl}}(K) \approx \frac{\alpha}{(FK)^{(1-\beta)/2}} \cdot \frac{z}{x(z)} \cdot \left[1 + \left(\frac{(1-\beta)^2}{24} \frac{\alpha^2}{(FK)^{1-\beta}} + \frac{\rho \beta \nu \alpha}{4(FK)^{(1-\beta)/2}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]$$

where $z = \frac{\nu}{\alpha}(FK)^{(1-\beta)/2}\ln\frac{F}{K}$ and $x(z) = \ln\frac{\sqrt{1-2\rho z + z^2} + z - \rho}{1-\rho}$.

## Example

A 5-year swaption with forward swap rate $F = 4.0\%$, calibrated SABR parameters: $\alpha = 0.035$, $\beta = 0.5$, $\rho = -0.25$, $\nu = 0.40$. Implied volatility at different strikes:

| Strike | $\sigma_{\text{impl}}$ | Moneyness |
|--------|----------------------|-----------|
| 3.0% | 28.5% | ITM payer |
| 4.0% | 25.1% | ATM |
| 5.0% | 23.8% | OTM payer |
| 6.0% | 24.2% | Deep OTM |

The negative $\rho$ produces a left-skewed smile (higher vol for low strikes), consistent with the empirical observation that rates volatility increases when rates fall. The minimum of the smile is slightly above ATM, and the uptick at high strikes is driven by $\nu$ (vol-of-vol).

## Remember

SABR is the lingua franca of rates and FX volatility desks. Every swaption, cap, floor, and exotic interest rate derivative is priced using a SABR-calibrated smile. For quant developers, implementing SABR means: (1) calibrating $\alpha$, $\rho$, $\nu$ to market quotes (typically fixing $\beta$); (2) using the Hagan approximation for fast smile interpolation; and (3) understanding its limitations — the approximation breaks down for very low rates (negative rates require shifted SABR), long expiries, and extreme strikes. The model's key advantage over local volatility is that it produces intuitive, stable smile dynamics: as the forward moves, the smile shifts in a way that closely matches empirical behaviour, making hedging with SABR-derived Greeks more reliable than with Dupire Greeks.
