# Two-Asset Portfolio with a Risk-Free Asset

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** risk-free asset, portfolio return, portfolio risk, linear tradeoff, leverage
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

A portfolio combining one risky asset $A$ and a risk-free asset paying return $R$ has a **perfectly linear** risk-return relationship. The risk-free asset contributes zero variance, so portfolio volatility scales directly with the weight in the risky asset.

## Key Formula

Let $w_A$ be the weight in the risky asset and $w_R = 1 - w_A$ in the risk-free asset:

$$\mu_\Pi = R + w_A(\mu_A - R)$$

$$\sigma_\Pi = |w_A|\,\sigma_A$$

The opportunity set is a **straight line** from $(0, R)$ through $(\sigma_A, \mu_A)$:

$$\mu_\Pi = R + \frac{\mu_A - R}{\sigma_A} \cdot \sigma_\Pi$$

The slope is the **Sharpe ratio** of asset $A$.

## Example

A risky equity fund has $\mu_A = 10\%$, $\sigma_A = 20\%$. The risk-free rate is $R = 4\%$.

- **Conservative investor** ($w_A = 0.5$): $\mu_\Pi = 4 + 0.5(6) = 7\%$, $\sigma_\Pi = 10\%$
- **Aggressive investor** ($w_A = 1.5$, borrowing at $R$): $\mu_\Pi = 4 + 1.5(6) = 13\%$, $\sigma_\Pi = 30\%$

Sharpe ratio of A: $(10 - 4)/20 = 0.30$ — the slope of the line connecting both portfolios.

## Remember

When a risky asset is combined with the risk-free asset, the risk-return tradeoff becomes a straight line — return is linear in weight, and so is risk. This is the simplest instance of the Capital Market Line: the slope is the Sharpe ratio of the risky asset. Adding leverage simply extends the line to the right beyond $(\sigma_A, \mu_A)$, with both return and risk growing proportionally.
