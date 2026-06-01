# Logit Function

**Topic:** Statistics
**Tags:** logit, log-odds, link function, logistic regression, odds ratio, probability of default
**Created:** 2026-05-30
**Author:** Claude Sonnet 4.6

---

## Definition

The **logit function** maps a probability $p \in (0, 1)$ to a log-odds value on the entire real line. It is the inverse of the logistic (sigmoid) function, and serves as the **link function** in logistic regression, connecting the linear predictor to the modelled probability.

## Key Formula

$$\text{logit}(p) = \ln\!\left(\frac{p}{1-p}\right) = \ln(p) - \ln(1-p)$$

**Key values:**

| $p$ | $\text{logit}(p)$ | Interpretation |
|---|---|---|
| $0.25$ | $-1.099$ | Odds 1:3 against |
| $0.50$ | $0$ | Even odds |
| $0.75$ | $1.099$ | Odds 3:1 for |
| $0.90$ | $2.197$ | Odds 9:1 for |

**Antisymmetry:** $\text{logit}(1-p) = -\text{logit}(p)$

**Inverse (logistic function):** $p = \sigma(x) = \dfrac{1}{1+e^{-x}}$

## Example

A credit model estimates the probability of default for two obligors:

- Obligor A: $p_A = 0.05$ (low risk) $\Rightarrow \text{logit}(0.05) = \ln(0.05/0.95) \approx -2.944$
- Obligor B: $p_B = 0.40$ (elevated risk) $\Rightarrow \text{logit}(0.40) = \ln(0.40/0.60) \approx -0.405$

A fitted logistic regression coefficient of $w = 0.8$ on a standardised income feature means that a one-standard-deviation increase in income shifts the logit by $0.8$, multiplying the default odds by $e^{0.8} \approx 2.23$.

## Remember

The logit is the **natural scale for logistic regression coefficients**: each coefficient measures the change in log-odds per unit change in a feature, and exponentiating gives the **odds ratio** — the standard language of credit risk models. In a bank's Internal Ratings Based (IRB) model, reporting PD estimates in logit units allows risk managers to compare obligors linearly: a borrower with $\text{logit}(\hat{p}) = 0$ has a 50% PD, and each unit increase roughly doubles the default odds.
