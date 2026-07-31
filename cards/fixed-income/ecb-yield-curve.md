# ECB AAA Yield Curve

**Topic:** Fixed Income
**Tags:** ecb, yield curve, svensson, euro area, benchmark, term structure
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

The ECB AAA yield curve is the European Central Bank's official daily estimate of the euro area risk-free term structure, derived by fitting the Svensson six-parameter model to market prices of AAA-rated euro area central government bonds spanning maturities from 3 months to 30 years.

## Key Formula

The Svensson model extends Nelson-Siegel with a second curvature term:

$$y(\tau) = \beta_0 + \beta_1\frac{1-e^{-\tau/\lambda_1}}{\tau/\lambda_1} + \beta_2\!\left[\frac{1-e^{-\tau/\lambda_1}}{\tau/\lambda_1} - e^{-\tau/\lambda_1}\right] + \beta_3\!\left[\frac{1-e^{-\tau/\lambda_2}}{\tau/\lambda_2} - e^{-\tau/\lambda_2}\right]$$

Parameters $(\beta_0, \beta_1, \beta_2, \beta_3, \lambda_1, \lambda_2)$ are estimated daily by minimising a price-weighted sum of squared residuals across eligible bonds. $\beta_0$ is the long-run level; $\beta_1$ governs slope; $\beta_2$ and $\beta_3$ capture short- and long-end curvature respectively.

## Example

Suppose fitted parameters on a given day are $\beta_0 = 3.5\%$, $\beta_1 = -1.2\%$, $\beta_2 = 0.8\%$, $\beta_3 = -0.3\%$, $\lambda_1 = 1.5$, $\lambda_2 = 5$.

At $\tau = 10$: $y(10) \approx 3.5\% - 0.18\% + 0.12\% - 0.09\% = 3.35\%$

At $\tau = 30$: without $\beta_3$, the plain Nelson-Siegel prediction is $3.48\%$; the $\beta_3$ term subtracts a further $0.05\%$, giving $y(30) = 3.43\%$ — the extra parameter captures a secondary hump or trough not reachable by the four-parameter model.

## Remember

The ECB publishes its six fitted parameters daily at 12:00 CET; these numbers are the euro area risk-free reference used for bond valuation, option-adjusted spread calculations, and FRTB risk-factor mapping. Any German Bund trading 10–15 bp above the fitted ECB curve is flagged as cheap — that gap is the first screen run by EU government bond relative value desks before initiating a convergence trade.
