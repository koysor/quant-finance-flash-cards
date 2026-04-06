# Laplace Distribution

**Topic:** Probability
**Tags:** Laplace, double exponential, jump diffusion, Kou model, fat tails, symmetric
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Laplace distribution** (double exponential) is a symmetric continuous distribution centred at location $\mu$, with scale $b > 0$. It has heavier tails than the normal but lighter than the Cauchy — tails decay exponentially rather than as a power law. Its PDF has a sharp peak at the mode and the characteristic "tent" shape. It arises naturally as the **difference of two independent exponentials**.

## Key Formula

**PDF:**

$$f(x; \mu, b) = \frac{1}{2b} \exp\!\left(-\frac{|x - \mu|}{b}\right)$$

**Mean, variance, and kurtosis:**

$$\mathbb{E}[X] = \mu, \qquad \text{Var}(X) = 2b^2, \qquad \text{excess kurtosis} = 3$$

**MGF:** $M(t) = \frac{e^{\mu t}}{1 - b^2 t^2}$ for $|t| < 1/b$.

**Asymmetric Laplace:** jump sizes in the Kou model follow an asymmetric Laplace — upward jumps $\sim \text{Exp}(\eta_1)$ with probability $p$, downward jumps $\sim \text{Exp}(\eta_2)$ with probability $1-p$.

## Example

The **Kou double-exponential jump diffusion model** for stock prices adds a compound Poisson jump term to GBM:

$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t + S_{t-} d\!\left(\sum_{i=1}^{N_t} (e^{J_i} - 1)\right)$$

where $N_t \sim \text{Poisson}(\lambda)$ and $J_i$ follows an asymmetric double-exponential. Calibrated to implied vol smiles, the Kou model gives closed-form option prices while capturing observed positive kurtosis in log-returns.

## Remember

The Laplace distribution has excess kurtosis of 3 (versus 0 for normal), making it a simple heavy-tailed alternative for modelling **daily P&L**. In machine learning applied to finance, **LASSO regularisation** (L1 penalty) corresponds to placing a Laplace prior on regression coefficients — the sharp peak at zero encourages sparsity by making exactly-zero coefficients highly probable a priori. This connection between the Laplace prior and LASSO is why L1 regularisation promotes **sparse factor models**, discarding irrelevant predictors, a desirable property when building alpha signals from large feature sets.
