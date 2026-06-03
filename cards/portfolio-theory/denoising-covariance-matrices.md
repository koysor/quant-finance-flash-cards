# Denoising Covariance Matrices

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** covariance matrix, random matrix theory, marchenko-pastur, eigenvalues, portfolio optimisation, noise
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Denoising a covariance matrix is the process of filtering out eigenvalues that arise from statistical noise rather than genuine asset correlations, using the Marchenko-Pastur distribution as a theoretically grounded boundary between signal and noise.

## Key Formula

For $N$ assets and $T$ observations with ratio $q = N/T$, the Marchenko-Pastur distribution gives the noise eigenvalue bounds:

$$\lambda_{\pm} = \sigma^2\!\left(1 \pm \sqrt{q}\right)^2$$

Eigenvalues below $\lambda_+$ are classified as noise and replaced by their average $\bar{\lambda}$ to preserve the matrix trace:

$$\tilde{\Lambda}_{ii} = \begin{cases} \lambda_i & \text{if } \lambda_i > \lambda_+ \\ \bar{\lambda} & \text{if } \lambda_i \leq \lambda_+ \end{cases}$$

The denoised covariance matrix is then reconstructed as $\tilde{\Sigma} = W\tilde{\Lambda}W^\top$.

## Example

A portfolio of $N = 50$ assets with $T = 100$ daily observations gives $q = 0.5$. With $\sigma^2 = 1$, the upper noise bound is $\lambda_+ = (1 + \sqrt{0.5})^2 \approx 2.91$. All 45 eigenvalues below 2.91 are replaced by their mean; the 5 eigenvalues above 2.91 are kept unchanged. The reconstructed matrix has the same five informative principal components but a flat, stable noise floor.

## Remember

Markowitz optimisation amplifies estimation error: a noisy covariance matrix generates extreme, opposing weights that perform poorly out-of-sample. Denoising stabilises the matrix by replacing the many small spurious eigenvalues with a flat floor, making portfolio weights far more robust. This is a core pre-processing step in the Lopez de Prado framework for machine-learning-driven portfolio construction.
