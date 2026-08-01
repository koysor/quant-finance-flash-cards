# Kendall's Tau

**Topic:** Statistics
**Tags:** rank correlation, concordance, copula calibration, non-parametric, spearmans rho, robust statistics
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

Kendall's tau is a rank correlation coefficient measuring the difference between the probability that two paired observations are **concordant** (both variables move the same way) and the probability that they are **discordant**. It depends only on ordering, so it is invariant to any strictly increasing transformation of either variable.

## Key Formula

For $n$ paired observations there are $\binom{n}{2}$ distinct pairs:

$$\tau = \frac{C - D}{\binom{n}{2}} = \frac{2(C-D)}{n(n-1)}$$

where $C$ counts concordant pairs, for which $(x_i - x_j)(y_i - y_j) > 0$, and $D$ counts discordant pairs.

For any elliptical copula — Gaussian or Student's t — the rank measures map to the linear correlation parameter analytically:

$$\rho = \sin\!\left(\frac{\pi}{2}\tau\right), \qquad \rho = 2\sin\!\left(\frac{\pi}{6}\rho_S\right)$$

the second being the corresponding relation for Spearman's rho.

## Example

Five days of paired credit-spread changes for two reference names, ranked:

| Day | Name A rank | Name B rank |
|---|---|---|
| 1 | 1 | 2 |
| 2 | 2 | 1 |
| 3 | 3 | 3 |
| 4 | 4 | 5 |
| 5 | 5 | 4 |

Of the $\binom{5}{2} = 10$ pairs, 8 are concordant and 2 are discordant (days 1–2 and days 4–5):

$$\tau = \frac{8 - 2}{10} = 0.6 \quad\Longrightarrow\quad \rho = \sin\!\left(\frac{\pi}{2}\times 0.6\right) = \sin(0.942) = 0.809$$

The linear correlation implied by the ranks is 0.81 — noticeably higher than $\tau$ itself, so the two must never be used interchangeably.

## Remember

Rank correlation is the right input when calibrating a copula to credit data, because Pearson correlation on raw CDS levels is close to meaningless: the series are non-stationary, strongly trending, and heavily influenced by a handful of crisis observations, which is how naive estimates end up implausibly high in the 0.9 range even for unrelated sovereigns. Tau sidesteps this by discarding magnitudes entirely, and its invariance to monotone transformation means it gives the same answer whether computed on spreads, on survival probabilities, or on the uniform pseudo-samples fed to the copula — a property Pearson lacks. The $\sin$ conversions matter in implementation: a t copula is parameterised by a linear correlation matrix, so the fitted $\tau$ must be transformed before use, and the resulting matrix is not guaranteed positive definite and may need repairing first.
