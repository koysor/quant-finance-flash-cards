# Total Variance Surface

**Topic:** Volatility
**Tags:** total variance, implied volatility, volatility surface, calendar arbitrage, interpolation, log-moneyness
**Created:** 2026-07-07
**Author:** Claude Sonnet 5

---

## Definition

The **total variance surface** re-expresses the implied volatility surface as implied variance accumulated over the option's life, $w(T, y) = T\,\sigma_{\text{imp}}^2(T, y)$, as a function of expiry $T$ and log-moneyness $y$. Because variances (not volatilities) add over time, $w$ is the natural coordinate for interpolating and differentiating a volatility surface: it turns the no-calendar-arbitrage condition into a simple monotonicity requirement and is smoother than implied volatility itself at short maturities.

## Key Formula

$$w(T, y) = T\,\sigma_{\text{imp}}^2(T, y), \qquad y = \ln\!\left(\frac{K}{F_T}\right)$$

**No calendar arbitrage** requires total variance to be non-decreasing in expiry at fixed moneyness:

$$w(T_2, y) \ge w(T_1, y) \quad \text{for all } T_2 > T_1$$

Recovering implied volatility from the surface is a single division:

$$\sigma_{\text{imp}}(T, y) = \sqrt{\frac{w(T,y)}{T}}$$

Linear interpolation of $w$ in $T$ between two quoted expiries corresponds to a constant instantaneous forward variance between them — a clean, parameter-free assumption that plain interpolation of $\sigma_{\text{imp}}$ does not share.

## Example

At $y = 0$ (at-the-money), a 1-month option has $\sigma_{\text{imp}} = 20\%$ and a 3-month option has $\sigma_{\text{imp}} = 18\%$.

$$w(1M, 0) = \tfrac{1}{12}\times 0.20^2 = 0.00333, \qquad w(3M, 0) = \tfrac{1}{4}\times 0.18^2 = 0.00810$$

Since $0.00810 > 0.00333$, the calendar condition holds even though the volatility itself fell from 20% to 18% — total variance still grew because there is three times as much time for it to accumulate over. Working directly in $\sigma_{\text{imp}}$ would obscure this; working in $w$ makes the no-arbitrage check a one-line inequality.

## Remember

Total variance is the "kernel trick" of volatility surface construction: it is the coordinate system in which the maths becomes tractable. Building the surface on $w(T,y)$ rather than $\sigma_{\text{imp}}(T,K)$ pays off in three places — calendar arbitrage collapses to $\partial_T w \ge 0$, the Dupire local-variance formula has a clean closed form in $(T,y)$, and $w$ stays smooth at short maturities where $\sigma_{\text{imp}}$ can spike. This is why SVI parameterises $w$ rather than volatility directly, and why any production local-vol pipeline regularises and differentiates the total-variance grid before converting back to implied or local volatility for reporting.
