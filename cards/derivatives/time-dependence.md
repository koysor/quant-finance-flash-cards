# Time Dependence in Options

**Topic:** Derivatives
**Tags:** time dependence, volatility term structure, black-scholes, implied volatility, calibration
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

An option has **time-dependent parameters** when the coefficients of its pricing model — typically volatility $\sigma(t)$ and interest rate $r(t)$ — are deterministic functions of time rather than constants. The Black–Scholes PDE retains its structure with time-varying coefficients, and a European call prices as a constant-volatility option using the root-mean-square effective volatility over the option's life.

## Key Formula

The time-dependent Black–Scholes PDE:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma(t)^2 S^2 \frac{\partial^2 V}{\partial S^2} + r(t) S \frac{\partial V}{\partial S} - r(t)V = 0$$

For a European call, this reduces to the standard formula with effective volatility:

$$\bar{\sigma} = \sqrt{\frac{1}{T}\int_0^T \sigma(t)^2\,dt}$$

so that only the integrated (total) variance $\int_0^T \sigma(t)^2\,dt$ determines the price, not the precise shape of $\sigma(t)$.

## Example

A 6-month call has volatility $\sigma = 20\%$ in the first quarter and $\sigma = 30\%$ in the second. Effective volatility:

$$\bar{\sigma} = \sqrt{\frac{0.20^2 \times 0.25 + 0.30^2 \times 0.25}{0.5}} = \sqrt{\frac{0.01 + 0.0225}{0.5}} = \sqrt{0.065} \approx 25.5\%$$

A standard Black–Scholes call with $\bar{\sigma} = 25.5\%$ and $T = 0.5$ gives the exact same price as solving the time-dependent PDE — even though instantaneous volatility was never 25.5%.

## Remember

The key practical insight is that European option prices depend only on total variance, not on the path of volatility over time. This is why the implied volatility surface shows different volatilities at different maturities: each implied vol is the market's estimate of the effective RMS volatility $\bar{\sigma}$ over that horizon, not the instantaneous volatility at that date. Stripping $\sigma(t)$ from a set of observed implied vols at increasing maturities — a procedure called **bootstrapping the vol term structure** — is the simplest form of model calibration performed daily on options desks.
