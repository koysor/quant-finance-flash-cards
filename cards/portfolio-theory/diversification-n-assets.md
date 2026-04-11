# Diversification with N Assets

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** diversification, N assets, idiosyncratic risk, systematic risk, equal-weight portfolio
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

As more assets are added to an equal-weight portfolio, **idiosyncratic risk vanishes** but **systematic risk remains**. The mathematical limit reveals why diversification has a floor that cannot be crossed by simply holding more assets.

## Key Formula

For an equal-weight portfolio of $N$ assets, each with variance $\sigma^2$ and pairwise correlation $\rho$:

$$\sigma_\Pi^2 = \left(\rho + \frac{1 - \rho}{N}\right)\sigma^2$$

As $N \to \infty$:

$$\sigma_\Pi^2 \;\xrightarrow{N \to \infty}\; \rho\,\sigma^2$$

**Special case** ($\rho = 0$, uncorrelated assets):

$$\sigma_\Pi^2 = \frac{\sigma^2}{N}, \qquad \sigma_\Pi = \frac{\sigma}{\sqrt{N}}$$

## Example

Individual stock volatility $\sigma = 30\%$, average pairwise correlation $\rho = 0.25$. Equal-weight portfolio:

| $N$ | $\sigma_\Pi$ |
|---|---|
| 1 | 30.0% |
| 5 | 21.2% |
| 20 | 16.7% |
| 100 | 15.4% |
| $\infty$ | $\sqrt{0.25} \times 30 = 15\%$ |

The irreducible floor is $\sqrt{\rho}\,\sigma = 15\%$ — systematic risk that no amount of diversification can eliminate.

## Remember

Idiosyncratic risk is free to eliminate — just hold more assets. Systematic risk is a floor set by the average pairwise correlation. This is why CAPM only rewards **beta** (systematic risk) with a return premium: idiosyncratic risk disappears in any sufficiently diversified portfolio, so the market will not pay for it. The formula also explains the $1/\sqrt{N}$ convergence in Monte Carlo simulation — the same mathematics governs both.
