# Correlated Brownian Motions

**Topic:** Stochastic Processes
**Tags:** correlation, Brownian motion, multi-asset, Cholesky, simulation, portfolio
**Author:** Claude Opus 4.6

---

## Definition

**Correlated Brownian motions** are two or more Wiener processes whose increments are statistically linked. In multi-asset models, the correlation between the driving Brownian motions captures how assets tend to move together. Two Brownian motions $W_1$ and $W_2$ are correlated with parameter $\rho$ when their increments satisfy $\mathbb{E}[dW_1 \, dW_2] = \rho \, dt$.

## Key Formula

Two assets following correlated GBMs:

$$dS_1 = \mu_1 S_1 \, dt + \sigma_1 S_1 \, dW_1$$

$$dS_2 = \mu_2 S_2 \, dt + \sigma_2 S_2 \, dW_2$$

with the correlation condition:

$$\mathbb{E}[dW_1 \, dW_2] = \rho \, dt$$

| $\rho$ value | Interpretation |
|---|---|
| $\rho = 1$ | Perfectly correlated — always move together |
| $\rho = 0$ | Independent — no systematic relationship |
| $\rho = -1$ | Perfectly anti-correlated — always move opposite |

To simulate, generate correlated normals $\phi_1, \phi_2$ using Cholesky decomposition:

$$\phi_1 = \varepsilon_1, \qquad \phi_2 = \rho \, \varepsilon_1 + \sqrt{1 - \rho^2} \, \varepsilon_2$$

where $\varepsilon_1, \varepsilon_2 \sim \mathcal{N}(0, 1)$ are independent.

## Example

Two stocks have $\rho = 0.6$. Drawing independent normals $\varepsilon_1 = 1.2$ and $\varepsilon_2 = -0.5$:

$$\phi_1 = 1.2, \qquad \phi_2 = 0.6 \times 1.2 + \sqrt{1 - 0.36} \times (-0.5) = 0.72 - 0.40 = 0.32$$

Both draws are positive, reflecting the positive correlation — when $S_1$ gets a large upward shock, $S_2$ tends to move up as well.

## Remember

Correlated Brownian motions are essential for pricing multi-asset derivatives such as basket options, spread options, and quanto products. The correlation parameter $\rho$ directly affects portfolio diversification benefits: when $\rho$ is high, diversification is limited. In simulation, the Cholesky decomposition transforms independent random numbers into correlated ones with exactly the right structure, and this generalises to $n$ assets via the matrix factorisation $C = LL^T$.
