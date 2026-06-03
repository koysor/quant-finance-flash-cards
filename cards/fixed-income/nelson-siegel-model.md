# Nelson-Siegel Model

**Topic:** Fixed Income
**Tags:** nelson-siegel, yield curve, level, slope, curvature, term structure
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The Nelson-Siegel model is a parsimonious parametric yield curve model that represents the term structure as a linear combination of three factors — level, slope, and curvature — with analytically specified loadings that decay exponentially with maturity.

## Key Formula

The zero-coupon yield at maturity $\tau$ is:

$$y(\tau) = \beta_1 + \beta_2\,\frac{1 - e^{-\lambda\tau}}{\lambda\tau} + \beta_3\!\left(\frac{1 - e^{-\lambda\tau}}{\lambda\tau} - e^{-\lambda\tau}\right)$$

- $\beta_1$: long-run level (the yield as $\tau \to \infty$)
- $\beta_2$: slope (short-minus-long yield; negative → upward-sloping curve)
- $\beta_3$: curvature (hump magnitude; the loading peaks near $\tau = 1/\lambda$)
- $\lambda > 0$: decay speed (controls where the hump occurs; typically calibrated once to the most liquid maturity bucket)

The model fits four parameters $(\beta_1, \beta_2, \beta_3, \lambda)$ via OLS (when $\lambda$ is fixed) or nonlinear least squares (when $\lambda$ is free).

## Example

UK gilt curve parameters: $\beta_1 = 4.20\%$, $\beta_2 = -1.80\%$, $\beta_3 = 2.10\%$, $\lambda = 0.70$. Fitted yields: 3-month $\approx 2.42\%$, 2-year $\approx 3.20\%$, 5-year $\approx 3.71\%$ (the hump peak), 10-year $\approx 3.45\%$, 30-year $\approx 4.05\%$. The model captures the hump-shaped UK curve using only four numbers, compared to 15+ nodes in a bootstrapped zero curve.

## Remember

Nelson-Siegel is the official yield curve model of the Bank for International Settlements and most central banks because its three factors map directly to monetary policy intuition: $\beta_1$ represents long-run rate expectations, $\beta_2$ represents the slope driven by the term premium, and $\beta_3$ captures mid-curve supply/demand imbalances. Fixed income risk managers decompose portfolio P&L into level, slope, and curvature sensitivities ($\partial V/\partial\beta_i$) that correspond exactly to the three Nelson-Siegel factors — a far more interpretable risk framework than per-bucket DV01 at 15 maturities.
