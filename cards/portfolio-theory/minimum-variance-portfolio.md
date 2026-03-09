# Minimum Variance Portfolio

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** minimum variance, efficient frontier, portfolio optimisation, estimation error, diversification
**Author:** Claude Opus 4.6

---

## Definition

The **minimum variance portfolio (MVP)** is the portfolio on the efficient frontier with the lowest possible volatility. It is the leftmost point of the mean-variance parabola. Crucially, it depends only on the covariance matrix $\Sigma$ and requires no estimate of expected returns — making it the most robust optimal portfolio against estimation error.

## Key Formula

**Weights of the global minimum variance portfolio:**

$$\mathbf{w}_{\text{MVP}} = \frac{\Sigma^{-1} \mathbf{1}}{\mathbf{1}^\top \Sigma^{-1} \mathbf{1}}$$

where $\mathbf{1}$ is the vector of ones (enforcing full investment).

**Minimum portfolio variance:**

$$\sigma_{\text{MVP}}^2 = \frac{1}{\mathbf{1}^\top \Sigma^{-1} \mathbf{1}}$$

## Example

Two assets with $\sigma_1 = 20\%$, $\sigma_2 = 15\%$, $\rho = 0.3$.

$$\Sigma = \begin{pmatrix} 0.04 & 0.009 \\ 0.009 & 0.0225 \end{pmatrix}, \qquad \Sigma^{-1} = \begin{pmatrix} 30.77 & -12.31 \\ -12.31 & 54.70 \end{pmatrix}$$

Row sums of $\Sigma^{-1}$: $s_1 = 18.46$, $s_2 = 42.39$. Total: $60.85$.

$$w_1 = \frac{18.46}{60.85} = 30.3\%, \qquad w_2 = \frac{42.39}{60.85} = 69.7\%$$

$$\sigma_{\text{MVP}} = \sqrt{1 / 60.85} \approx 12.8\%$$

The MVP tilts heavily towards the lower-volatility asset and is below either individual volatility.

## Remember

The minimum variance portfolio is a paradox of modern finance: despite ignoring expected returns entirely, it has historically outperformed many optimised portfolios that use return forecasts. This happens because return estimates are so noisy that optimising over them introduces more error than it removes — the MVP avoids this pitfall by depending only on $\Sigma$, which can be estimated far more accurately. Many institutional "low-volatility" strategies are variants of the MVP. Its main limitation is that it concentrates in low-volatility, highly correlated stocks (utilities, consumer staples), creating sector concentration risk that must be managed through constraints.
