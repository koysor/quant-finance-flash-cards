# Correlation Breakdown

**Topic:** Probability
**Tags:** correlation, tail dependence, crisis, diversification, contagion
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Correlation breakdown** is the empirical phenomenon whereby pairwise correlations between risky assets, which appear low or moderate in normal markets, spike sharply towards $+1$ during financial crises. This destroys the diversification benefits that investors relied upon during calm periods.

## Key Formula

In normal conditions, a two-asset portfolio variance benefits from low correlation:

$$\text{Var}(R_P) = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1 w_2\,\rho\,\sigma_1\sigma_2$$

As $\rho \to 1$ during a crisis (while individual volatilities $\sigma_i$ also spike), portfolio variance approaches:

$$\text{Var}(R_P) \to (w_1\sigma_1 + w_2\sigma_2)^2$$

— the worst case where volatilities add rather than partially cancel. The diversification benefit, measured as the reduction in $\sigma_P$ versus the weighted average of individual volatilities, collapses to zero.

**Diversification benefit:**

$$\text{Benefit} = \overline{\sigma} - \sigma_P = (w_1\sigma_1 + w_2\sigma_2) - \sigma_P \ge 0$$

This is maximised when $\rho = -1$ and equals zero when $\rho = +1$.

## Example

Pre-crisis: equity fund $A$ ($\sigma_A = 15\%$) and credit fund $B$ ($\sigma_B = 10\%$), $\rho = 0.2$, equal weights.

$$\sigma_P = \sqrt{0.25(0.0225) + 0.25(0.01) + 2(0.25)(0.2)(0.15)(0.10)} \approx 9.0\%$$

During crisis: same weights, but $\rho$ rises to $0.9$, $\sigma_A = 30\%$, $\sigma_B = 20\%$.

$$\sigma_P = \sqrt{0.25(0.09) + 0.25(0.04) + 2(0.25)(0.9)(0.30)(0.20)} \approx 24.2\%$$

The portfolio volatility has nearly tripled despite "diversification" — and the correlation spike is the primary driver beyond the individual volatility increases.

## Remember

Correlation breakdown is the central failure mode of mean-variance portfolio construction. Markowitz optimisation treats correlations as constant parameters, but empirically they are strongly time-varying and tend to rise dramatically during the very tail events that matter most. The 2008 GFC saw cross-asset correlations jump from typical values of 0.1–0.4 to above 0.8. This is why practitioners supplement mean-variance optimisation with stress tests, tail-dependence measures (copulas), and maximum drawdown constraints — tools that explicitly account for the behaviour of correlations when markets dislocate.
