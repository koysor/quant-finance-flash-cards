# Non-Parametric Model

**Topic:** Statistics
**Tags:** non-parametric, empirical distribution, historical simulation, distribution-free, kernel density
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

A **non-parametric model** makes no assumption about the functional form of the underlying probability distribution. Rather than estimating a fixed set of parameters (e.g. mean and variance of a normal), the model lets the data determine its own structure. Non-parametric methods are more flexible than parametric ones but typically require more data to achieve the same precision.

## Key Formula

The foundation of most non-parametric methods is the **empirical cumulative distribution function (ECDF)**:

$$\hat{F}_n(x) = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}(X_i \leq x)$$

This places probability mass $1/n$ on each observed data point $X_i$. Quantiles are read directly from $\hat{F}_n$ — the $p$-th quantile is the $\lceil np \rceil$-th order statistic $X_{(\lceil np \rceil)}$.

## Example

A risk manager has 500 daily P&L observations for a trading book. To compute the 99% one-day VaR non-parametrically, she sorts the losses from largest to smallest and takes the 5th-largest loss (the $\lfloor 0.01 \times 500 \rfloor = 5$th order statistic):

| Order statistic | Loss |
|----------------|------|
| $X_{(495)}$ (5th largest loss) | \$2.34 m |
| $X_{(496)}$ | \$2.19 m |

The non-parametric 99% VaR is **\$2.34 m** — no distributional assumption required.

## Remember

Historical simulation VaR is the most widely used non-parametric risk measure in banking. Its key advantage over parametric VaR is that it automatically captures fat tails, skewness, and non-linear exposures present in the actual return history — without assuming normality. Its key weakness is that it is entirely backward-looking: tail estimates depend on whether extreme events happened to occur in the observation window. The 2008 crisis showed that a 250-day window could miss severe stress episodes entirely. This motivated regulators under **FRTB** to require **stressed VaR** calibrated to a period of significant financial stress, blending the non-parametric approach with an explicit stress scenario requirement.
