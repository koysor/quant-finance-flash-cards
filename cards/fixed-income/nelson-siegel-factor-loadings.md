# Nelson-Siegel Factor Loadings

**Topic:** Fixed Income
**Tags:** nelson-siegel, factor loadings, level, slope, curvature, term structure
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

The Nelson-Siegel model expresses a yield curve as a linear combination of three loading functions — level, slope, and curvature — each with a distinct maturity profile, whose coefficients $(\beta_0, \beta_1, \beta_2)$ are estimated by least squares given an observed set of yields.

## Key Formula

$$y(\tau) = \beta_0 \cdot \underbrace{1}_{\text{level}} + \beta_1 \cdot \underbrace{\frac{1 - e^{-\tau/\lambda}}{\tau/\lambda}}_{\text{slope}} + \beta_2 \cdot \underbrace{\left(\frac{1 - e^{-\tau/\lambda}}{\tau/\lambda} - e^{-\tau/\lambda}\right)}_{\text{curvature}}$$

The three loading functions have contrasting maturity profiles:

| Loading | $\tau \to 0$ | $\tau \to \infty$ | Shape |
|---------|:---:|:---:|-------|
| Level: $1$ | 1 | 1 | Flat |
| Slope: $\frac{1 - e^{-\tau/\lambda}}{\tau/\lambda}$ | 1 | 0 | Monotone decay |
| Curvature: $\frac{1 - e^{-\tau/\lambda}}{\tau/\lambda} - e^{-\tau/\lambda}$ | 0 | 0 | Hump, peak $\approx \lambda$ |

## Example

With $\lambda = 2$ (years), the loadings at three benchmark tenors are:

| Tenor $\tau$ | Level | Slope | Curvature |
|:---:|:---:|:---:|:---:|
| 1Y | 1.000 | 0.787 | 0.181 |
| 5Y | 1.000 | 0.367 | 0.285 |
| 10Y | 1.000 | 0.199 | 0.192 |

The slope loading decays steadily while the curvature loading peaks around $\tau \approx 3.6$ years and then falls — demonstrating that $\beta_2$ controls the intermediate part of the curve independently of the long end.

## Remember

Empirical PCA of daily yield curve changes consistently identifies three factors — parallel shift, twist, and butterfly — that explain over 99% of yield variance. The Nelson-Siegel loadings are an analytical approximation to these PCA factors: level ↔ shift, slope ↔ twist, curvature ↔ butterfly. This is why central banks favour Nelson-Siegel: the three $\beta$ parameters have direct economic interpretations (long-run rate, spread, hump), making monetary policy communication precise.
