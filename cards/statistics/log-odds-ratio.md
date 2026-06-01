# Log-Odds Ratio

**Topic:** Statistics
**Tags:** log-odds ratio, logit, logistic regression, credit scoring, odds ratio, weight of evidence
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

The **log-odds ratio** is the natural logarithm of the ratio of two odds. It measures how much the log-odds of an event in group A exceed those in group B, and equals the difference of the two logit values. It is the fundamental unit of effect size in logistic regression and credit scorecard models.

$$\text{Log-Odds Ratio} = \text{logit}(p_A) - \text{logit}(p_B) = \ln\!\left(\frac{p_A/(1-p_A)}{p_B/(1-p_B)}\right)$$

Exponentiating recovers the **odds ratio** (OR):

$$\text{OR} = \frac{p_A/(1-p_A)}{p_B/(1-p_B)} = e^{\,\text{log-odds ratio}}$$

If $\text{OR} = 2$, group A has **double the odds** of the event compared with group B.

## Key Formula

Let $p_A$ and $p_B$ be probabilities in two groups:

$$\text{Log-Odds Ratio} = \ln\!\left(\frac{p_A}{1-p_A}\right) - \ln\!\left(\frac{p_B}{1-p_B}\right)$$

**Sign and direction:**

| Value | Interpretation |
|---|---|
| $> 0$ | Group A has higher odds than group B |
| $= 0$ | Both groups have equal odds |
| $< 0$ | Group A has lower odds than group B |

**Weight of Evidence (WoE)** — used in credit scorecards — is a log-odds ratio relative to the population baseline:

$$\text{WoE}_i = \ln\!\left(\frac{\text{Events}_i / \text{Total Events}}{\text{Non-events}_i / \text{Total Non-events}}\right)$$

Each WoE value is the log-odds ratio comparing bin $i$ to the overall population distribution of events and non-events.

## Example

A bank models probability of default (PD) for two borrower segments:

- High-LTV borrowers: $p_A = 0.12$ (odds $= 0.12/0.88 \approx 0.136$)
- Low-LTV borrowers: $p_B = 0.03$ (odds $= 0.03/0.97 \approx 0.031$)

$$\text{Log-Odds Ratio} = \ln(0.136) - \ln(0.031) \approx -1.995 - (-3.474) = 1.479$$

$$\text{OR} = e^{1.479} \approx 4.39$$

High-LTV borrowers have roughly 4.4 times the default odds of low-LTV borrowers.

In a fitted logistic regression, the coefficient on LTV is the log-odds ratio per unit change in LTV. If $\hat{\beta}_{\text{LTV}} = 0.04$ per percentage point, a 10-percentage-point increase in LTV multiplies default odds by $e^{0.04 \times 10} = e^{0.4} \approx 1.49$ — a 49% increase in odds.

## Remember

In logistic regression for credit scoring, every fitted coefficient **is** a log-odds ratio: it measures how the log-odds of default shift per unit increase in the feature. Exponentiating converts it to the more intuitive odds ratio language used in regulatory reporting. Weight of Evidence — the workhorse transformation in Basel IRB scorecards — is simply a log-odds ratio comparing each risk band to the portfolio baseline, making the log-odds ratio the unifying concept behind both scorecard calibration and model interpretation.
