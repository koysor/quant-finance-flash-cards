# Regularisation

**Topic:** Statistics
**Tags:** regularisation, ridge, lasso, shrinkage, overfitting, penalty, sparse
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Regularisation** adds a penalty term to a model's loss function to prevent overfitting by discouraging large parameter values. It introduces a controlled bias that reduces variance and improves out-of-sample performance. The two standard methods are **Ridge** ($\ell_2$ penalty, shrinks all coefficients) and **LASSO** ($\ell_1$ penalty, shrinks many coefficients to exactly zero, producing a sparse model).

## Key Formula

**Ridge regression:**

$$\min_\mathbf{w} \left\{ \frac{1}{n}\sum_{i=1}^n (y_i - \mathbf{w}^\top\mathbf{x}_i)^2 + \lambda \sum_j w_j^2 \right\}$$

**LASSO regression:**

$$\min_\mathbf{w} \left\{ \frac{1}{n}\sum_{i=1}^n (y_i - \mathbf{w}^\top\mathbf{x}_i)^2 + \lambda \sum_j |w_j| \right\}$$

The **regularisation parameter** $\lambda \geq 0$ controls the bias-variance tradeoff: $\lambda = 0$ recovers OLS; $\lambda \to \infty$ shrinks all weights to zero.

**Ridge closed form:** $\hat{\mathbf{w}}_\text{Ridge} = (\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}$

## Example

A quant tests 50 candidate alpha factors. OLS selects all 50 with high in-sample $R^2 = 0.45$ but poor out-of-sample $R^2 = 0.02$ — classic overfitting.

LASSO with $\lambda = 0.05$ shrinks 43 weights to exactly zero, retaining 7 factors. Out-of-sample $R^2$ rises to 0.11. The 7 surviving factors are the genuinely predictive signals; the other 43 were noise.

## Remember

Regularisation is the statistical formalisation of **Occam's razor** in finance. The Ridge penalty $\lambda\sum w_j^2$ has a direct Bayesian interpretation: it corresponds to a Gaussian prior on each weight, which is identical to the **James-Stein shrinkage estimator** used to regularise sample covariance matrices. In portfolio construction, shrinking the sample covariance matrix towards a structured target (e.g. a single-index model) is Ridge regularisation applied to the covariance estimate — reducing estimation error and improving the stability of mean-variance optimal portfolios. LASSO's sparsity property makes it ideal for **factor model selection**: it automatically discards redundant factors, solving a problem that would otherwise require expensive combinatorial search.
