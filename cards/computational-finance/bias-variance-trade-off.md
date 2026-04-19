# Bias-Variance Trade-off

**Topic:** Computational Finance
**Tags:** bias, variance, overfitting, underfitting, model selection, regularisation
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **bias-variance trade-off** describes the tension between two sources of prediction error in a statistical model: bias (error from overly simplistic assumptions) and variance (error from excessive sensitivity to training-data noise). Minimising total error requires balancing both.

## Key Formula

$$\text{Total Error} = \text{Bias}^2 + \text{Variance} + \sigma^2_{\varepsilon}$$

where $\sigma^2_{\varepsilon}$ is irreducible noise inherent to the data-generating process.

## Example

A linear model fitted to non-linear price data has **high bias** — it systematically misses the curve. A degree-20 polynomial fitted to the same 30 data points has **high variance** — it passes through every point but fails on new data. A degree-3 polynomial typically finds the sweet spot.

## Remember

In quantitative finance, overfitting is a persistent danger: a trading strategy back-tested on 10 years of data with 50 free parameters will look impressive in-sample but degrade sharply out-of-sample. Regularisation techniques (Ridge, LASSO) and cross-validation are the standard tools for controlling variance without sacrificing too much bias.
