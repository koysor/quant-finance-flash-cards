# Covariance Matrix

**Topic:** Linear Algebra
**Tags:** covariance matrix, portfolio risk, symmetric matrices, positive definite, mean-variance
**Author:** Claude Opus 4.6

---

## Definition

The **covariance matrix** (or variance-covariance matrix) $\Sigma$ is a symmetric matrix whose $(i, j)$ entry is the covariance between asset $i$ and asset $j$. The diagonal entries are the variances of the individual assets. Every valid covariance matrix is positive semi-definite, ensuring that portfolio variance $\mathbf{w}^\top \Sigma \, \mathbf{w} \geq 0$ for any weight vector $\mathbf{w}$.

## Key Formula

For $n$ assets with return vector $\mathbf{R}$:

$$\Sigma = E\!\left[(\mathbf{R} - \boldsymbol{\mu})(\mathbf{R} - \boldsymbol{\mu})^\top\right]$$

$$\Sigma = \begin{pmatrix} \sigma_1^2 & \sigma_{12} & \cdots & \sigma_{1n} \\ \sigma_{12} & \sigma_2^2 & \cdots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{1n} & \sigma_{2n} & \cdots & \sigma_n^2 \end{pmatrix}$$

**Portfolio variance:**

$$\sigma_p^2 = \mathbf{w}^\top \Sigma \, \mathbf{w} = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \sigma_{ij}$$

## Example

Three assets have volatilities $\sigma_1 = 20\%$, $\sigma_2 = 15\%$, $\sigma_3 = 25\%$ and pairwise correlations $\rho_{12} = 0.5$, $\rho_{13} = -0.2$, $\rho_{23} = 0.3$.

$$\Sigma = \begin{pmatrix} 0.0400 & 0.0150 & -0.0100 \\ 0.0150 & 0.0225 & 0.01125 \\ -0.0100 & 0.01125 & 0.0625 \end{pmatrix}$$

For an equal-weight portfolio $\mathbf{w} = (1/3, \; 1/3, \; 1/3)^\top$:

$$\sigma_p^2 = \frac{1}{9}(0.04 + 0.0225 + 0.0625) + \frac{2}{9}(0.015 - 0.01 + 0.01125) = 0.01389 + 0.00361 = 0.01750$$

$$\sigma_p = \sqrt{0.01750} \approx 13.2\%$$

This is well below the average individual volatility of 20%, demonstrating the diversification benefit from negative and moderate correlations.

## Remember

The covariance matrix is the single most important input to portfolio construction. In Markowitz optimisation, changing $\Sigma$ changes every efficient portfolio. In practice, estimating $\Sigma$ reliably from historical data is notoriously difficult — with $n$ assets there are $n(n+1)/2$ parameters to estimate, and sampling noise causes the matrix to become ill-conditioned or even lose positive definiteness when $n$ approaches the sample size. This is why practitioners use shrinkage estimators, factor models, or the Ledoit-Wolf method to regularise $\Sigma$ before optimising.
