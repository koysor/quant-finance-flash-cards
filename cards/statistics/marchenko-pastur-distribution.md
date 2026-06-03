# Marchenko-Pastur Distribution

**Topic:** Statistics
**Tags:** marchenko-pastur, random matrix theory, eigenvalue distribution, covariance matrix, noise threshold
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The Marchenko-Pastur distribution gives the theoretical eigenvalue density of a large random Wishart matrix, providing a benchmark for distinguishing noise eigenvalues from genuine signal eigenvalues in a sample covariance matrix.

## Key Formula

For a matrix with $N$ assets and $T$ observations, ratio $q = N/T$, and average variance $\sigma^2$, the density of eigenvalues $\lambda$ is:

$$\rho(\lambda) = \frac{\sqrt{(\lambda_+ - \lambda)(\lambda - \lambda_-)}}{2\pi \sigma^2 q\, \lambda}, \qquad \lambda \in [\lambda_-,\, \lambda_+]$$

where the noise bounds are:

$$\lambda_{\pm} = \sigma^2\!\left(1 \pm \sqrt{q}\right)^2$$

When $q > 1$ (more assets than observations), a point mass of weight $1 - 1/q$ sits at $\lambda = 0$, reflecting the rank deficiency of the matrix.

## Example

A sample covariance matrix built from $N = 200$ assets and $T = 500$ daily observations has $q = 0.4$. With $\sigma^2 = 1$, the MP bounds are $\lambda_- \approx 0.17$ and $\lambda_+ \approx 2.03$. Any of the 200 eigenvalues falling below 2.03 is statistically indistinguishable from pure noise. In practice, only 15 of the 200 eigenvalues exceed $\lambda_+$ — these 15 represent genuine risk factors; the remaining 185 are noise.

## Remember

The Marchenko-Pastur distribution is the null hypothesis for a covariance matrix: it answers "what would the eigenvalue spectrum look like if all returns were independent random noise?" Any eigenvalue above $\lambda_+$ rejects that null and represents a genuine co-movement structure. In portfolio construction, this is the theoretical foundation for denoising and eigenvalue clipping — tools that prevent Markowitz optimisation from fitting to noise.
