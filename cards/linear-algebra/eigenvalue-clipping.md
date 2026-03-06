# Eigenvalue Clipping

**Topic:** Linear Algebra
**Tags:** eigenvalue clipping, random matrix theory, Marchenko-Pastur, covariance matrix, noise reduction
**Author:** Claude Opus 4.6

---

## Definition

**Eigenvalue clipping** is a technique for denoising a sample covariance matrix by replacing eigenvalues that are consistent with pure noise with a constant value. The **Marchenko-Pastur law** from random matrix theory predicts the distribution of eigenvalues for a purely random matrix — any sample eigenvalue falling within this bulk distribution is indistinguishable from noise and is clipped (replaced), while eigenvalues above the upper bound carry genuine signal.

## Key Formula

**Marchenko-Pastur upper bound** for a random matrix with ratio $q = n/T$ (assets/observations):

$$\lambda_+ = \sigma^2 (1 + \sqrt{q})^2$$

where $\sigma^2$ is the average eigenvalue (total variance divided by $n$).

Eigenvalues $\lambda_i \leq \lambda_+$ are clipped to a constant $\lambda_c$ chosen to preserve the total trace:

$$\lambda_c = \frac{\text{tr}(\Sigma) - \sum_{\lambda_i > \lambda_+} \lambda_i}{|\{i : \lambda_i \leq \lambda_+\}|}$$

The cleaned covariance matrix is then reconstructed: $\hat{\Sigma} = V \hat{\Lambda} V^\top$.

## Example

A portfolio of $n = 100$ stocks with $T = 250$ daily observations gives $q = 100/250 = 0.4$.

Average eigenvalue: $\sigma^2 = 0.0004$ (typical daily variance).

$$\lambda_+ = 0.0004 \times (1 + \sqrt{0.4})^2 = 0.0004 \times (1.632)^2 = 0.0004 \times 2.664 = 0.001066$$

Any eigenvalue below $0.001066$ is noise. If 85 of the 100 eigenvalues fall below this threshold, only 15 carry genuine information about asset co-movement — the remaining 85 are replaced by a constant, dramatically reducing the condition number.

## Remember

The sample covariance matrix of a large portfolio is dominated by noise. With 500 stocks and 2 years of daily data ($T = 504$), $q \approx 1$ and the Marchenko-Pastur bound nearly doubles the average eigenvalue — meaning almost all eigenvalues are noise. Eigenvalue clipping exploits random matrix theory to separate signal from noise without requiring any economic assumptions. Combined with shrinkage or factor models, it is one of the most effective tools for producing stable covariance estimates that lead to sensible portfolio weights. The technique was popularised in finance by Laloux, Cizeau, Bouchaud, and Potters (1999).
