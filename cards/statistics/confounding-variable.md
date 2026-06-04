# Confounding Variable

**Topic:** Statistics
**Tags:** confounding, causation, correlation, spurious regression, omitted variable bias
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

A **confounding variable** (or confounder) is a variable that is correlated with both the explanatory variable $X$ and the outcome variable $Y$, creating the appearance of a causal relationship between $X$ and $Y$ when the true driver is the confounder $Z$. Failing to account for confounders leads to biased coefficient estimates and false inference — a relationship that looks causal in a regression may be entirely spurious.

## Key Formula

In a simple regression $Y = \alpha + \beta X + \varepsilon$, the OLS estimate is biased if a confounder $Z$ is omitted:

$$\hat{\beta}_{\text{OLS}} = \beta + \delta \cdot \frac{\text{Cov}(X, Z)}{\text{Var}(X)}$$

where $\delta$ is the coefficient of $Z$ in the true model $Y = \alpha + \beta X + \delta Z + \varepsilon$. The bias is $\delta \cdot \text{Cov}(X, Z) / \text{Var}(X)$ — called **omitted variable bias**. It is zero only if $Z$ is uncorrelated with $X$ or has no effect on $Y$.

## Example

A quant observes that tech stock returns ($Y$) are highly correlated with coffee shop visits ($X$) during a bull market. Running the regression $Y = \alpha + \beta X + \varepsilon$ gives a statistically significant positive $\hat{\beta}$.

The confounder is **general economic sentiment** $Z$: when the economy is strong, both consumer spending (coffee) and equity returns rise together. There is no causal link from coffee to returns. Controlling for a sentiment index (e.g. consumer confidence) drives $\hat{\beta}$ close to zero — the correlation was entirely spurious.

## Remember

Confounding is the central threat to **factor model backtesting** in quantitative finance. A strategy that appears to earn alpha may actually be loading on a known risk factor (e.g. value, momentum, or low volatility) that was omitted from the regression. The Fama-French three-factor model was motivated precisely by this: the apparent "alpha" of small-cap value stocks was largely explained by the size (SMB) and value (HML) factors that earlier single-factor CAPM regressions omitted. Any time a backtest shows a compelling signal, the first question should be: what confounders could produce this correlation without genuine predictive power?
