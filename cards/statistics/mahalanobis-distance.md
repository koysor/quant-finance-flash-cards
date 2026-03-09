# Mahalanobis Distance

**Topic:** Statistics
**Tags:** multivariate, covariance, outlier detection, z-score, portfolio risk
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

The **Mahalanobis distance** is the multivariate generalisation of the z-score. It measures how many standard deviations a point $\mathbf{x}$ lies from the mean $\boldsymbol{\mu}$ of a distribution, accounting for correlations between variables via the covariance matrix $\boldsymbol{\Sigma}$. Unlike the Euclidean distance, it stretches and rotates space so that the contours of equal distance match the elliptical shape of the data.

## Key Formula

$$D_M = \sqrt{(\mathbf{x} - \boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})}$$

**Univariate case** (reduces to the absolute z-score):

$$D_M = \left|\frac{x - \mu}{\sigma}\right|$$

**For a multivariate normal** with $p$ dimensions, $D_M^2$ follows a chi-squared distribution:

$$D_M^2 \sim \chi^2_p$$

| Dimensions $p$ | $D_M^2$ threshold (95%) | $D_M^2$ threshold (99%) |
|---|---|---|
| $2$ | $5.99$ | $9.21$ |
| $5$ | $11.07$ | $15.09$ |
| $10$ | $18.31$ | $23.21$ |

## Example

A two-asset portfolio tracks daily returns $\mathbf{x} = (r_1, r_2)$ with mean $\boldsymbol{\mu} = (0.05\%, 0.03\%)$ and covariance matrix:

$$\boldsymbol{\Sigma} = \begin{pmatrix} 0.0004 & 0.0002 \\ 0.0002 & 0.0009 \end{pmatrix}, \quad \boldsymbol{\Sigma}^{-1} = \begin{pmatrix} 3214 & -714 \\ -714 & 1429 \end{pmatrix}$$

Today's returns are $\mathbf{x} = (-2.5\%, -3.0\%)$. The deviation is $\mathbf{d} = (-0.025 - 0.0005,\; -0.030 - 0.0003) = (-0.0255,\; -0.0303)$.

$$D_M^2 = (-0.0255,\; -0.0303) \begin{pmatrix} 3214 & -714 \\ -714 & 1429 \end{pmatrix} \begin{pmatrix} -0.0255 \\ -0.0303 \end{pmatrix} \approx 2.53$$

$$D_M \approx 1.59$$

Since $D_M^2 = 2.53$ is below the 95% chi-squared threshold of $5.99$ for $p = 2$, today's joint move is within normal range — despite both returns being individually negative.

## Remember

The Mahalanobis distance is essential for multivariate risk monitoring. A single asset dropping 2% might look alarming in isolation, but if it is highly correlated with other assets that also dropped, the joint move may be perfectly ordinary. Mahalanobis distance captures this by weighting deviations through the inverse covariance matrix — correlated moves are penalised less than independent ones. It is used in outlier detection for cleaning financial return data, in the Markowitz framework where portfolio risk is $\sigma_p = \sqrt{\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}}$ (a Mahalanobis-like form), and in stress testing where regulators ask "how extreme is this scenario relative to the historical distribution of joint returns?"
