# Adjusted R-Squared

**Topic:** Statistics
**Tags:** regression, goodness of fit, model selection, overfitting, degrees of freedom
**Created:** 2026-05-30
**Author:** Claude Sonnet 4.6

---

## Definition

**Adjusted R-squared** ($\bar{R}^2$) modifies the ordinary coefficient of determination to penalise for the number of predictors $k$, so that adding an irrelevant variable cannot artificially inflate the measure of fit. Unlike $R^2$, which always increases when a predictor is added, $\bar{R}^2$ decreases if the new predictor explains less variance than would be expected by chance.

## Key Formula

$$\bar{R}^2 = 1 - \frac{\text{RSS}/(n - k - 1)}{\text{TSS}/(n - 1)} = 1 - (1 - R^2)\frac{n - 1}{n - k - 1}$$

where $n$ is the number of observations, $k$ is the number of predictors, RSS is the residual sum of squares, and TSS is the total sum of squares.

The relationship between $\bar{R}^2$ and $R^2$:

$$\bar{R}^2 = 1 - \frac{n - 1}{n - k - 1}(1 - R^2)$$

Adding a predictor raises $\bar{R}^2$ only if its F-statistic exceeds 1.

## Example

A factor model is fitted to $n = 60$ monthly returns with $k = 3$ predictors, giving $R^2 = 0.72$:

$$\bar{R}^2 = 1 - (1 - 0.72)\frac{59}{56} = 1 - 0.28 \times 1.054 = 1 - 0.295 = 0.705$$

A fourth predictor is added and $R^2$ rises to $0.723$; the new $\bar{R}^2$:

$$\bar{R}^2 = 1 - (1 - 0.723)\frac{59}{55} = 1 - 0.277 \times 1.073 = 1 - 0.297 = 0.703$$

$\bar{R}^2$ fell from 0.705 to 0.703, signalling the fourth factor added noise rather than genuine explanatory power.

## Remember

Adjusted $R^2$ is the standard fit measure when comparing factor models with different numbers of predictors — it answers the question "does adding this factor actually improve the model?" In quantitative factor investing, practitioners frequently discover that a model with 8 factors has a higher $R^2$ but lower $\bar{R}^2$ than one with 5 factors; the extra factors are fitting idiosyncratic noise in the estimation sample rather than capturing systematic return drivers. Adjusted $R^2$ is also a useful guard against the temptation to add macro or sentiment variables whose in-sample contribution looks impressive but whose out-of-sample performance degrades due to overfitting.
