# Svensson Model

**Topic:** Fixed Income
**Tags:** Svensson, extended Nelson-Siegel, yield curve, calibration, curvature, central bank
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **Svensson model** (1994) extends Nelson–Siegel by adding a second curvature term with its own decay speed $\lambda_2$. The two hump terms can fit yield curves with two local extrema — a shape that Nelson–Siegel's single curvature factor cannot reproduce — while retaining the interpretability of level, slope, and curvature factors.

## Key Formula

$$y(\tau) = \beta_1 + \beta_2\frac{1-e^{-\lambda_1\tau}}{\lambda_1\tau} + \beta_3\!\left(\frac{1-e^{-\lambda_1\tau}}{\lambda_1\tau} - e^{-\lambda_1\tau}\right) + \beta_4\!\left(\frac{1-e^{-\lambda_2\tau}}{\lambda_2\tau} - e^{-\lambda_2\tau}\right)$$

| Parameter | Role |
|---|---|
| $\beta_1$ | Long-run level ($\tau \to \infty$) |
| $\beta_2$ | Slope (short-minus-long yield spread) |
| $\beta_3$ | First curvature — hump at $1/\lambda_1$ |
| $\beta_4$ | Second curvature — additional hump at $1/\lambda_2$ |
| $\lambda_1, \lambda_2$ | Decay speeds for the two hump terms |

Six parameters $(\beta_1, \beta_2, \beta_3, \beta_4, \lambda_1, \lambda_2)$ are fitted by nonlinear least squares to market yields.

## Example

ECB Svensson fit to the euro area AAA yield curve (June 2024): $\beta_1 = 3.95\%$, $\beta_2 = -2.70\%$, $\beta_3 = 4.10\%$, $\beta_4 = -2.20\%$, $\lambda_1 = 0.60$, $\lambda_2 = 2.10$. The first curvature term creates a hump at 1–3 years; the second creates a second inflection near 6 months. Root mean squared fitting error: 2 bp across 10 maturities.

## Remember

Svensson is the standard model for central bank yield curve publication because it fits the typical double-humped shapes that arise when monetary policy creates a kink at the short end while long-run inflation expectations anchor the long end. The European Central Bank, the Federal Reserve (for the off-the-run Treasury curve), and the Bank of England all publish Svensson parameters. For quant use, Svensson is a **calibration interpolation tool** — it is not a dynamic model, so it cannot price options or derivatives without extension to a stochastic framework.
