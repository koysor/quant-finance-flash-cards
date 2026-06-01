# Odds Ratio

**Topic:** Statistics
**Tags:** odds ratio, logistic regression, credit scoring, probability of default, risk factor, binary outcome
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

The **odds ratio** (OR) measures the ratio of the odds of an event occurring in one group relative to another. It is the standard effect-size measure for binary outcomes and is directly interpretable as a multiplicative change in default odds when used in credit risk modelling.

## Key Formula

**Odds of an event** with probability $p$:

$$\text{Odds} = \frac{p}{1 - p}$$

**Odds ratio** comparing group A (probability $p_A$) against group B (probability $p_B$):

$$\text{OR} = \frac{p_A / (1 - p_A)}{p_B / (1 - p_B)} = \frac{\text{Odds}_A}{\text{Odds}_B} = e^{\,\text{logit}(p_A) - \text{logit}(p_B)}$$

**Interpretation:**

| OR | Meaning |
|---|---|
| $> 1$ | Event more likely in group A |
| $= 1$ | Equal likelihood in both groups |
| $< 1$ | Event less likely in group A |

**Logistic regression link:** each fitted coefficient $\hat{\beta}_j$ satisfies $e^{\hat{\beta}_j} = \text{OR}$ for a one-unit increase in feature $j$.

## Example

A mortgage lender compares default rates by loan-to-value (LTV) band:

- High LTV ($> 90\%$): default rate $p_A = 0.15$, odds $= 0.15 / 0.85 \approx 0.176$
- Low LTV ($< 60\%$): default rate $p_B = 0.03$, odds $= 0.03 / 0.97 \approx 0.031$

$$\text{OR} = \frac{0.176}{0.031} \approx 5.7$$

High-LTV borrowers have **5.7 times the default odds** of low-LTV borrowers. A logistic regression on LTV would yield $\hat{\beta}_{\text{LTV}} = \ln(5.7) \approx 1.74$ for this split.

## Remember

The odds ratio is the **natural output unit of logistic regression**: exponentiating each coefficient gives the factor by which default odds are multiplied per unit increase in that feature. In credit risk under Basel IRB and IFRS 9, reporting model coefficients as odds ratios allows credit officers to communicate results without statistical jargon — "a 10-point drop in credit score multiplies default odds by 1.8" is directly actionable, whereas the raw logit coefficient $0.588$ is not.
