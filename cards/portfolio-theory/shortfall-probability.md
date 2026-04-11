# Shortfall Probability and Roy's Safety-First Criterion

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** shortfall probability, Roy's criterion, safety-first ratio, downside risk, liability
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **probability of shortfall** is the probability that a portfolio's return $R_P$ falls below a threshold $R_L$ (a liability rate or minimum acceptable return). **Roy's safety-first criterion** (1952) says to choose the portfolio that **minimises** this probability.

## Key Formula

**Objective:** $\min_{\mathbf{w}} \; P(R_P < R_L)$

When returns are **normally distributed**, minimising shortfall probability is equivalent to maximising the **safety-first ratio (SFR)**:

$$\text{SFR} = \frac{E[R_P] - R_L}{\sigma_P}$$

$$\max_{\mathbf{w}} \; \frac{E[R_P] - R_L}{\sigma_P}$$

The SFR is identical to the **Sharpe ratio** but with the threshold $R_L$ replacing the risk-free rate $R_F$.

## Example

A pension fund must earn at least 5% to cover liabilities ($R_L = 5\%$). Two candidate portfolios:

| Portfolio | $E[R]$ | $\sigma$ | SFR |
|---|---|---|---|
| A | 8% | 10% | $(8-5)/10 = 0.30$ |
| B | 11% | 18% | $(11-5)/18 = 0.33$ |

Portfolio B has the higher SFR, so it minimises the probability of falling short of the 5% liability target.

## Remember

Roy's safety-first criterion reframes portfolio selection from "maximise expected utility" to "minimise the chance of disaster." For a pension fund or insurer with explicit liability targets, the SFR is more relevant than the Sharpe ratio — the benchmark is the liability rate, not the risk-free rate. Under normality, the two objectives (minimise shortfall probability and maximise SFR) are mathematically identical, connecting goal-based investing to classical mean-variance analysis.
