# Expectation and Variance

**Topic:** Probability
**Tags:** expectation, variance, moments, linearity, standard deviation, probability
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **expectation** $E[X]$ is the probability-weighted average outcome of a random variable — the long-run mean of repeated observations. The **variance** $\text{Var}(X)$ measures how spread out outcomes are around the expectation. Together they are the two most fundamental descriptors of any distribution.

$$E[X] = \begin{cases} \displaystyle\sum_k k\,p_X(k) & \text{discrete} \\[6pt] \displaystyle\int_{-\infty}^{\infty} x\,f_X(x)\,dx & \text{continuous} \end{cases}$$

$$\text{Var}(X) = E\!\left[(X - E[X])^2\right] = E[X^2] - (E[X])^2$$

## Key Formula

**Linearity of expectation** (holds for all random variables, even dependent):

$$E[aX + bY + c] = aE[X] + bE[Y] + c$$

**Variance rules:**

$$\text{Var}(aX + b) = a^2\,\text{Var}(X)$$

$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X, Y)$$

$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) \quad \text{if } X \perp\!\!\!\perp Y$$

**Standard deviation:** $\sigma_X = \sqrt{\text{Var}(X)}$ — same units as $X$.

**Computational shortcut:**

$$\text{Var}(X) = E[X^2] - \mu^2$$

## Example

A portfolio holds £60,000 in stock $A$ ($\mu_A = 8\%$, $\sigma_A = 15\%$) and £40,000 in stock $B$ ($\mu_B = 5\%$, $\sigma_B = 10\%$), with correlation $\rho = 0.3$.

Weights: $w_A = 0.6$, $w_B = 0.4$. Portfolio return $R_P = 0.6R_A + 0.4R_B$.

$$E[R_P] = 0.6(8\%) + 0.4(5\%) = 6.8\%$$

$$\text{Var}(R_P) = (0.6)^2(0.15)^2 + (0.4)^2(0.10)^2 + 2(0.6)(0.4)(0.3)(0.15)(0.10)$$

$$= 0.0081 + 0.0016 + 0.00216 = 0.01186, \qquad \sigma_P = \sqrt{0.01186} \approx 10.9\%$$

## Remember

Linearity of expectation is the most useful property in quantitative finance — it means $E[\text{portfolio return}]$ is always the weighted average of individual returns, regardless of how correlated the assets are. Variance, by contrast, is **not** linear: it depends on correlations through the $2\text{Cov}(X,Y)$ term, which is why diversification reduces portfolio risk without reducing expected return. This asymmetry — linearity in expectation, non-linearity in variance — is the mathematical core of the entire Markowitz framework.
