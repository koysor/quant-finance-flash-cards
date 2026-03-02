# Multi-Asset Itô's Lemma

**Topic:** Stochastic Processes
**Tags:** Itô's lemma, multi-asset, cross term, correlation, basket options, stochastic calculus
**Author:** Claude Opus 4.6

---

## Definition

The **multi-asset Itô's lemma** extends Itô's lemma to functions of two or more correlated stochastic processes. The key new ingredient is a **cross term** $dS_1 \, dS_2$ that captures the interaction between correlated assets and introduces a correlation-dependent contribution to the drift.

## Key Formula

For $V = V(t, S_1, S_2)$ where each asset follows correlated GBM with $\mathbb{E}[dW_1 \, dW_2] = \rho \, dt$:

$$dV = \frac{\partial V}{\partial t} dt + \frac{\partial V}{\partial S_1} dS_1 + \frac{\partial V}{\partial S_2} dS_2 + \frac{1}{2}\frac{\partial^2 V}{\partial S_1^2} dS_1^2 + \frac{1}{2}\frac{\partial^2 V}{\partial S_2^2} dS_2^2 + \frac{\partial^2 V}{\partial S_1 \partial S_2} dS_1 \, dS_2$$

The multiplication rules for the second-order terms:

| Product | Result |
|---|---|
| $dS_1^2$ | $\sigma_1^2 S_1^2 \, dt$ |
| $dS_2^2$ | $\sigma_2^2 S_2^2 \, dt$ |
| $dS_1 \, dS_2$ | $\rho \, \sigma_1 \sigma_2 S_1 S_2 \, dt$ |

The full drift of $V$ is:

$$\frac{\partial V}{\partial t} + \sum_{i=1}^{2} \mu_i S_i \frac{\partial V}{\partial S_i} + \frac{1}{2}\sum_{i=1}^{2} \sigma_i^2 S_i^2 \frac{\partial^2 V}{\partial S_i^2} + \rho \, \sigma_1 \sigma_2 S_1 S_2 \frac{\partial^2 V}{\partial S_1 \partial S_2}$$

## Example

For a simple product $V = S_1 S_2$, the cross partial $\frac{\partial^2 V}{\partial S_1 \partial S_2} = 1$, so the cross-term contribution to the drift is $\rho \, \sigma_1 \sigma_2 S_1 S_2 \, dt$. If $\rho = 0.5$, $\sigma_1 = 0.2$, $\sigma_2 = 0.3$, and both assets are at 100, this adds $0.5 \times 0.2 \times 0.3 \times 100 \times 100 = 300$ per unit time to the drift of $V$.

## Remember

The cross term $dS_1 \, dS_2 = \rho \, \sigma_1 \sigma_2 S_1 S_2 \, dt$ is the defining feature of multi-asset stochastic calculus. It arises from $dW_1 \, dW_2 = \rho \, dt$ and is essential for pricing basket options, spread options, and any derivative whose payoff depends on multiple correlated underlyings. When $\rho = 0$ the cross term vanishes and the two assets can be treated independently.
