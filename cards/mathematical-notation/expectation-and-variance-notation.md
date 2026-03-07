# Expectation and Variance Notation

**Topic:** Mathematical Notation
**Tags:** notation, expectation, variance, probability, operator
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

**Expectation and variance notation** provides compact symbols for the most common probability operators. Several equivalent notations exist, and quant finance texts mix them freely.

| Symbol | Read as | Meaning |
|---|---|---|
| $E[X]$ or $\mathbb{E}[X]$ | "expectation of $X$" | Weighted average of all possible values of $X$ |
| $E^{\mathbb{Q}}[X]$ | "expectation of $X$ under $\mathbb{Q}$" | Expectation computed using the measure $\mathbb{Q}$ |
| $\mu$ or $\bar{X}$ | "mu" or "$X$-bar" | Population mean or sample mean |
| $\text{Var}(X)$ or $\sigma^2$ | "variance of $X$" | $E[(X - \mu)^2]$; spread around the mean |
| $\text{Cov}(X, Y)$ | "covariance of $X$ and $Y$" | $E[(X - \mu_X)(Y - \mu_Y)]$ |
| $\sigma$ or $\text{SD}(X)$ | "sigma" or "standard deviation" | $\sqrt{\text{Var}(X)}$ |

## Key Formula

**Linearity of expectation** (holds even for dependent variables):

$$E[aX + bY] = aE[X] + bE[Y]$$

**Variance shortcut:**

$$\text{Var}(X) = E[X^2] - (E[X])^2$$

**Variance of a scaled variable:**

$$\text{Var}(aX + b) = a^2 \text{Var}(X)$$

**Covariance and correlation:**

$$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$$

## Example

A stock's daily return has $E[R] = 0.04\%$ and $\text{Var}(R) = (1.2\%)^2 = 0.000144$.

The expected annual return and variance (assuming 252 independent days):

$$E[R_{\text{annual}}] = 252 \times 0.04\% = 10.08\%$$

$$\text{Var}(R_{\text{annual}}) = 252 \times 0.000144 = 0.03629$$

$$\sigma_{\text{annual}} = \sqrt{0.03629} = 19.05\%$$

## Remember

The superscript on the expectation operator — $E^{\mathbb{P}}$ versus $E^{\mathbb{Q}}$ — is one of the most important notational details in quantitative finance. The same random variable $X$ can have completely different expected values under different probability measures. Derivative pricing uses $E^{\mathbb{Q}}$ (risk-neutral expectation), while risk management and forecasting use $E^{\mathbb{P}}$ (real-world expectation). When no superscript is shown, the measure is implied by context — and misreading which measure is intended is a frequent source of confusion when translating between pricing and risk applications.
