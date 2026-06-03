# Wishart Distribution

**Topic:** Statistics
**Tags:** wishart distribution, random matrix theory, covariance matrix, multivariate, chi-squared, noise
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The Wishart distribution is the multivariate generalisation of the chi-squared distribution, describing the probability distribution of sample covariance matrices constructed from normally distributed observations.

## Key Formula

If $X$ is an $n \times p$ matrix whose rows are i.i.d. draws from $\mathcal{N}(0, \Sigma)$, then the sample scatter matrix $W = X^\top X$ follows a Wishart distribution:

$$W \sim \mathcal{W}_p(\Sigma,\, n)$$

with mean $\mathbb{E}[W] = n\Sigma$ and density:

$$f(W) \propto |W|^{(n-p-1)/2} \exp\!\left(-\tfrac{1}{2}\operatorname{tr}(\Sigma^{-1}W)\right)$$

The sample covariance matrix is $S = W/n$, so $\mathbb{E}[S] = \Sigma$. When $\Sigma = I$ (independent assets with unit variance), the eigenvalue distribution of $W/n$ converges to the Marchenko-Pastur distribution as $n, p \to \infty$ with $p/n \to q$.

## Example

A portfolio of $p = 200$ assets observed over $n = 500$ days gives $q = 200/500 = 0.4$. If returns are independent ($\Sigma = I$), the sample covariance matrix $S = X^\top X / 500$ is a Wishart draw with mean $I$. Despite $\mathbb{E}[S] = I$ being exact, the actual draw has eigenvalues spread from $\lambda_- \approx 0.17$ to $\lambda_+ \approx 2.03$ — a factor-of-12 range purely from statistical noise with no genuine signal.

## Remember

Every sample covariance matrix built from financial returns is a Wishart random matrix. This single fact explains why Markowitz optimisation fails in practice: the extreme eigenvalues you feed into the optimiser are not properties of the true return-generating process — they are statistical artefacts of estimating a $200 \times 200$ matrix from only 500 observations. The Wishart distribution is the theoretical foundation that makes denoising and eigenvalue clipping necessary rather than optional.
