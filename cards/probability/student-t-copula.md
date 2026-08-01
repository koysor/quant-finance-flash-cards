# Student's t Copula

**Topic:** Probability
**Tags:** copula, tail dependence, degrees of freedom, default correlation, monte carlo, rank correlation
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

The Student's t copula is the dependence structure extracted from a multivariate Student's t distribution. It differs from the Gaussian copula in one decisive respect: it exhibits **tail dependence**, so extreme outcomes across variables occur together with non-vanishing probability however far into the tail you look.

## Key Formula

Sampling an $n$-dimensional correlated uniform vector requires one extra draw compared with the Gaussian case:

1. Decompose the correlation matrix $\hat{\Sigma} = AA'$ (Cholesky)
2. Draw independent standard normals $\mathbf{Z} = (z_1,\dots,z_n)'$
3. Draw an independent chi-squared variate $s \sim \chi^2_\nu$
4. Form $\mathbf{Y} = \mathbf{Z}\big/\sqrt{s/\nu}$
5. Impose correlation, $\mathbf{X} = A\mathbf{Y}$
6. Map to uniforms with the t CDF, $\mathbf{U} = T_\nu(\mathbf{X})$

The coefficient of lower tail dependence is strictly positive for finite $\nu$:

$$\lambda_L = 2\,T_{\nu+1}\!\left(-\sqrt{\frac{(\nu+1)(1-\rho)}{1+\rho}}\right)$$

whereas the Gaussian copula has $\lambda_L = 0$ for every $\rho < 1$. The degrees of freedom $\nu$ are fitted by maximum likelihood on pseudo-samples, maximising $\sum_t \ln c(\mathbf{u}_t;\nu,\hat\Sigma)$ over a grid of integer $\nu$.

## Example

Two names with $\rho = 0.5$ and $\nu = 7$:

$$\lambda_L = 2\,T_8\!\left(-\sqrt{\frac{8 \times 0.5}{1.5}}\right) = 2\,T_8(-1.633) \approx 2 \times 0.0705 = 0.141$$

So given one name suffering an extreme move, there is roughly a 14% chance the other does too — against 0% under a Gaussian copula with the same correlation. The single shared $\chi^2_7$ divisor is what produces this: a small draw of $s$ inflates every component of $\mathbf{Y}$ at once.

## Remember

In a basket CDS this is the difference between a plausible price and a dangerous one. The Gaussian copula, which fitted the same pairwise correlations, was the model that underpriced senior CDO tranches before 2008 precisely because it assigns vanishing probability to many names failing at once. Under a t copula with $\nu = 7$ the joint defaults that matter for the 2nd-, 3rd- and 5th-to-default legs become materially more likely, so those spreads widen while the 1st-to-default — which needs only one failure — barely moves or even tightens. Two practical consequences follow: the calibrated $\nu$ deserves as much scrutiny as the correlation matrix, since it alone controls the tail, and higher $k$ needs well beyond 10,000 Monte Carlo paths to converge, because the payout depends on rare joint events that the t copula makes less rare but still uncommon.
