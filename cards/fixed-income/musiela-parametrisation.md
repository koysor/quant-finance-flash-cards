# Musiela Parametrisation

**Topic:** Fixed Income
**Tags:** musiela, hjm, forward rate, tenor, yield curve, term structure
**Created:** 2026-06-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **Musiela parametrisation** reformulates the HJM forward rate $f(t, T)$ in terms of a fixed **time-to-maturity** (tenor) $\tau = T - t$ rather than a fixed calendar maturity $T$. This change of variables keeps the tenor $\tau$ constant as calendar time $t$ advances, matching how market practitioners and data providers quote rates (e.g. "the 10-year rate").

## Key Formula

Define the tenor-indexed forward rate:

$$r(t, \tau) = f(t,\, t + \tau)$$

Differentiating using the chain rule introduces a **convection term** $\partial r / \partial \tau$, so the SDE becomes:

$$dr(t, \tau) = \left(\frac{\partial r}{\partial \tau} + m(t, \tau)\right)dt + \sigma(t, \tau)\,dW_t$$

where $m(t, \tau)$ is the HJM no-arbitrage drift and $\sigma(t, \tau)$ is the volatility function, both expressed in tenor coordinates.

## Example

In standard HJM, modelling the "10-year forward rate" requires tracking $f(t, t+10)$ whose maturity date $T = t + 10$ moves as $t$ increases. Under Musiela, $r(t, 10)$ always refers to the 10-year tenor — exactly the rate quoted on Bloomberg or in central bank data. This stationarity makes fitting PCA factors to historical time series straightforward: a 10-year eigenvector has the same meaning every day.

## Remember

Market risk systems store yield curves as vectors of tenors (3M, 6M, 1Y, 2Y, 5Y, 10Y, 30Y), not as fixed calendar dates. The Musiela parametrisation aligns HJM mathematics with this convention, making it the natural starting point for PCA-based calibration: the covariance matrix of daily $\Delta r(t, \tau)$ changes is stable in $\tau$-space, so its eigenvectors (Level, Slope, Curvature) can be used directly as the volatility functions $\sigma_i(t, \tau)$ in a multi-factor HJM model.
