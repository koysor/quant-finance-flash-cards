# Measurement Error

**Topic:** Statistics
**Tags:** measurement error, regression, residuals, homoscedasticity, model assumptions
**Created:** 2026-04-22
**Author:** Claude Sonnet 4.6

---

## Definition

**Measurement error** (also called the **irreducible error**) is the component of a response variable that cannot be explained by any predictor, represented by the error term $\varepsilon$ in the regression model $y = f(x) + \varepsilon$. It arises from inherent randomness, omitted variables, and imprecision in observation — it is irreducible because it persists even if the true functional form $f(x)$ is known exactly.

## Key Formula

The standard linear regression model:

$$y = \beta_0 + \beta_1 x + \varepsilon$$

The three classical assumptions on $\varepsilon$:

$$\text{(i)}\;\mathbb{E}[\varepsilon] = 0 \qquad \text{(ii)}\;\operatorname{Var}(\varepsilon) = \sigma^2 \quad \text{(constant)} \qquad \text{(iii)}\;\operatorname{Cov}(\varepsilon_i, \varepsilon_j) = 0 \; (i \neq j)$$

These three conditions — **zero mean**, **homoscedasticity** (constant variance), and **independence** — are collectively the Gauss–Markov assumptions. The irreducible error variance $\sigma^2_\varepsilon$ sets a floor on mean squared prediction error:

$$E\!\left[(y - \hat{f}(x))^2\right] = \underbrace{\operatorname{Bias}^2[\hat{f}(x)]}_{\text{reducible}} + \underbrace{\operatorname{Var}[\hat{f}(x)]}_{\text{reducible}} + \underbrace{\sigma^2_\varepsilon}_{\text{irreducible}}$$

## Example

Suppose a quant regresses daily stock excess returns $y$ on the market excess return $x$:

$$y = 0.02 + 1.3\,x + \varepsilon, \qquad \hat{\sigma}_\varepsilon = 0.8\%$$

Even with the true $\beta_0$ and $\beta_1$ known exactly, the model cannot predict tomorrow's return more accurately than $\pm 0.8\%$ (one standard deviation). If the analyst doubles the estimation sample to reduce estimation uncertainty, $\hat{\sigma}_\varepsilon$ remains at $0.8\%$ — it is a property of the asset, not the model.

## Remember

In quantitative finance, the irreducible error is the **idiosyncratic risk** of an asset: the return component unexplained by any systematic factor. For a fully diversified portfolio this noise averages away, which is why CAPM asserts that only systematic risk (beta) commands a risk premium — idiosyncratic risk is free to eliminate. When comparing models, a drop in $R^2$ from adding a new factor does not always indicate a worse model; if the new factor merely reallocates noise, $\hat{\sigma}_\varepsilon$ remains unchanged. Always inspect the residual variance alongside $R^2$ when evaluating factor model improvements.
