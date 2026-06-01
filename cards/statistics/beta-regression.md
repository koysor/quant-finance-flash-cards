# Beta Regression

**Topic:** Statistics
**Tags:** beta regression, loss given default, bounded response, generalised linear model, credit risk, logit
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

Beta regression models a continuous response variable $Y \in (0, 1)$ — strictly between zero and one — using a **Beta distribution** for the response. The conditional mean $\mu = \mathbb{E}[Y \mid X]$ is linked to a linear predictor via the **logit link**:

$$\operatorname{logit}(\mu) = \ln\!\left(\frac{\mu}{1-\mu}\right) = \mathbf{x}^\top\boldsymbol{\beta}$$

The Beta distribution is re-parameterised in terms of mean $\mu \in (0,1)$ and **precision** $\phi > 0$:

$$Y \sim \operatorname{Beta}(\mu\phi,\ (1-\mu)\phi)$$

This is a **generalised linear model (GLM)** with a Beta response family. It is entirely distinct from the market-sensitivity "beta" ($\beta$) used in CAPM.

## Key Formula

| Quantity | Expression |
|---|---|
| Mean | $\mu = \operatorname{logit}^{-1}(\mathbf{x}^\top\boldsymbol{\beta}) = \dfrac{e^{\mathbf{x}^\top\boldsymbol{\beta}}}{1 + e^{\mathbf{x}^\top\boldsymbol{\beta}}}$ |
| Variance | $\operatorname{Var}(Y) = \dfrac{\mu(1-\mu)}{1+\phi}$ |
| Precision effect | Higher $\phi$ $\Rightarrow$ tighter distribution around $\mu$ |
| Log-likelihood | $\ell(\mu,\phi) = \ln\Gamma(\phi) - \ln\Gamma(\mu\phi) - \ln\Gamma((1-\mu)\phi) + (\mu\phi - 1)\ln y + ((1-\mu)\phi - 1)\ln(1-y)$ |

Parameters are estimated by **maximum likelihood**; the precision $\phi$ may itself be modelled as a function of covariates if heteroscedasticity is present.

## Example

A bank models **Loss Given Default (LGD)** — the fraction of an exposure lost when a borrower defaults — for a portfolio of corporate loans. OLS regression is inappropriate because:

1. It can predict values outside $[0, 1]$.
2. It assumes constant variance, but low-LGD exposures (highly secured loans) have less variation than mid-range ones.

Using beta regression with covariates $\{$loan-to-value ratio, seniority, collateral type$\}$:

- The fitted mean satisfies $0 < \hat{\mu} < 1$ by construction.
- Variance $\operatorname{Var}(Y) = \hat{\mu}(1-\hat{\mu})/(1+\hat{\phi})$ is automatically largest near $\hat{\mu} = 0.5$, matching the empirical pattern.
- Under IFRS 9, the model's LGD estimates feed directly into the **Expected Credit Loss (ECL)** calculation: $\text{ECL} = \text{PD} \times \text{LGD} \times \text{EAD}$.

## Remember

Beta regression is the **natural GLM for rates and proportions**. Whenever a finance quantity is a rate bounded strictly between 0 and 1 — LGD, recovery rates, prepayment speeds, or fund expense ratios — beta regression respects the bounds and allows heteroscedasticity that OLS cannot capture. Under Basel III / IFRS 9, institutions must report LGD as a fraction; beta regression satisfies the regulatory constraint while providing well-calibrated uncertainty estimates.
