# Likelihood Ratio Test

**Topic:** Statistics
**Tags:** likelihood ratio, nested models, chi-squared, maximum likelihood, model comparison, LRT
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **likelihood ratio test (LRT)** compares two **nested** models: a restricted model ($H_0$, fewer parameters) and an unrestricted model ($H_1$, more parameters). The test statistic is twice the log ratio of their maximised likelihoods. By Wilks' theorem, this statistic converges to a chi-squared distribution under $H_0$, with degrees of freedom equal to the number of additional parameters in $H_1$.

## Key Formula

Let $\hat{L}_0$ and $\hat{L}_1$ be the maximised likelihoods under $H_0$ and $H_1$:

$$\Lambda = -2\ln\!\left(\frac{\hat{L}_0}{\hat{L}_1}\right) = 2(\ell_1 - \ell_0) \xrightarrow{d} \chi^2_q \text{ under } H_0$$

where $\ell = \ln \hat{L}$ is the maximised log-likelihood and $q$ is the number of additional parameters.

**Decision:** reject $H_0$ if $\Lambda > \chi^2_{q,\,\alpha}$.

**AIC and BIC** penalise the log-likelihood for complexity: $\text{AIC} = -2\ell + 2k$, $\text{BIC} = -2\ell + k\ln n$ — used for non-nested model comparison.

## Example

Testing whether GARCH(1,1) (3 parameters: $\omega, \alpha, \beta$) significantly improves on ARCH(1) (2 parameters: $\omega, \alpha$). With $n = 500$ daily returns:

$$\ell_{\text{GARCH}} = -710.3, \quad \ell_{\text{ARCH}} = -718.6$$

$$\Lambda = 2(-710.3 - (-718.6)) = 16.6 > \chi^2_{1,\,0.001} = 10.8$$

Strongly reject $H_0$ — GARCH(1,1) fits significantly better than ARCH(1): the $\beta$ parameter (persistence) is significant.

## Remember

The likelihood ratio test is the **universal model selection tool in quantitative finance** wherever maximum likelihood estimation is used — which covers virtually all parametric models. GARCH vs ARCH, normal vs t-distributed errors, one-factor vs multi-factor yield curve models: all can be compared via LRT when one model is nested in the other. For non-nested models (e.g. GARCH vs EGARCH), AIC or BIC replace the LRT. In credit modelling, LRT is used to test whether adding a macroeconomic variable significantly improves a logistic PD model — the test determines whether the additional complexity of the macro-conditional model is statistically justified.
