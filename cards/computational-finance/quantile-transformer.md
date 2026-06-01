# QuantileTransformer

**Topic:** Computational Finance
**Tags:** preprocessing, quantiles, heavy tails, feature scaling, scikit-learn, non-parametric
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**`QuantileTransformer`** is a non-parametric scikit-learn preprocessing class that maps each feature to a uniform $[0, 1]$ or Gaussian distribution by applying the empirical cumulative distribution function (ECDF) — completely removing any distributional shape including extreme outliers, at the cost of discarding relative spacing between observations.

## Key Formula

For a feature with $n$ training observations, each value $x$ is mapped via its empirical rank:

$$x_{\text{uniform}} = \hat{F}(x) = \frac{\text{rank}(x)}{n}$$

To obtain a Gaussian output, compose with the inverse standard normal CDF $\Phi^{-1}$:

$$x_{\text{normal}} = \Phi^{-1}\!\left(\hat{F}(x)\right)$$

The transformation is entirely non-parametric — no parameter is estimated; the empirical distribution of the training set is the model. Out-of-sample values beyond the training range are clipped to the $[0, 1]$ interval before applying $\Phi^{-1}$, so extreme test-set observations are treated as the most extreme training observations.

## Example

A credit risk model uses the logarithm of a borrower's gross debt as a feature. The training set spans debt from \$10k to \$500M; a crisis-era observation has debt of \$4B — four times the training maximum. `RobustScaler` would produce a scaled value far outside the training range, potentially disrupting the model. `QuantileTransformer` clips it to rank 1.0 (mapped to the 100th percentile of the training distribution), treating it the same as the largest training observation. This is conservative but prevents a single extreme test value from dominating model inputs.

## Remember

`QuantileTransformer` is the most aggressive outlier-handling preprocessor in scikit-learn: by construction, the transformed output always lies in $[0, 1]$ (uniform) or within a bounded normal range, regardless of how extreme the input is. This makes it valuable for financial derivatives positions or structured credit exposures where mark-to-market values can take on extreme outlier magnitudes during stress events. The key trade-off versus `PowerTransformer` is that `QuantileTransformer` destroys the relative spacing between large values — a debt of \$400M and \$4B might map to ranks 0.99 and 1.00, appearing nearly identical — which removes information that may genuinely matter for the model.
