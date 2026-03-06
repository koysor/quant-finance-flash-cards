# Multivariate Normal Distribution

**Topic:** Probability
**Tags:** multivariate normal, covariance matrix, joint distribution, Gaussian, portfolio theory
**Author:** Claude Opus 4.6

---

## Definition

The **multivariate normal distribution** generalises the normal distribution to a vector of random variables. It is fully specified by a mean vector $\boldsymbol{\mu}$ and a covariance matrix $\Sigma$. Any linear combination of jointly normal variables is itself normal, and the marginal and conditional distributions are also normal — properties that make the multivariate normal the default model for joint asset returns.

## Key Formula

**Probability density function** for $\mathbf{x} \in \mathbb{R}^n$:

$$f(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^n \det(\Sigma)}} \exp\!\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^\top \Sigma^{-1} (\mathbf{x} - \boldsymbol{\mu})\right)$$

**Key properties:**

- If $\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$ and $\mathbf{Y} = A\mathbf{X} + \mathbf{b}$, then $\mathbf{Y} \sim \mathcal{N}(A\boldsymbol{\mu} + \mathbf{b}, \; A\Sigma A^\top)$
- Marginals: $X_i \sim \mathcal{N}(\mu_i, \sigma_i^2)$
- Zero covariance $\Leftrightarrow$ independence (only for the multivariate normal)

## Example

Two assets with $\boldsymbol{\mu} = \begin{pmatrix} 0.08 \\ 0.05 \end{pmatrix}$ and $\Sigma = \begin{pmatrix} 0.04 & 0.006 \\ 0.006 & 0.01 \end{pmatrix}$.

A portfolio with $\mathbf{w} = (0.6, \; 0.4)^\top$:

$$\mu_p = 0.6 \times 0.08 + 0.4 \times 0.05 = 0.068 = 6.8\%$$

$$\sigma_p^2 = \mathbf{w}^\top \Sigma \, \mathbf{w} = 0.36 \times 0.04 + 2 \times 0.24 \times 0.006 + 0.16 \times 0.01 = 0.01888$$

$$\sigma_p \approx 13.7\%$$

Under the multivariate normal assumption, $R_p \sim \mathcal{N}(6.8\%, \; 13.7\%^2)$, so the 5th percentile loss (parametric VaR) is:

$$\text{VaR}_{0.05} = 6.8\% - 1.645 \times 13.7\% \approx -15.7\%$$

## Remember

The multivariate normal is the probabilistic backbone of mean-variance portfolio theory — the assumption that returns are jointly normal means the entire distribution is captured by just $\boldsymbol{\mu}$ and $\Sigma$, which is precisely why Markowitz optimisation only needs these two inputs. It also justifies parametric VaR and the Black-Scholes assumption of log-normal prices. The critical limitation is that real asset returns exhibit fat tails, skewness, and tail dependence that the multivariate normal cannot capture — correlations tend to spike during crises, precisely when the Gaussian model is most dangerous.
