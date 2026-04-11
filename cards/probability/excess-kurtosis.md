# Excess Kurtosis

**Topic:** Probability
**Tags:** excess kurtosis, fat tails, kurtosis, non-normality, tail risk
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Excess kurtosis** is kurtosis minus 3 — the amount by which a distribution's tail weight exceeds that of the normal distribution. A positive excess kurtosis means fatter tails and a higher peak than normal; a negative excess kurtosis means thinner tails.

$$\text{Excess kurtosis} = \gamma_2 - 3 = \frac{E[(X-\mu)^4]}{\sigma^4} - 3$$

The normal distribution has $\gamma_2 = 3$, so its excess kurtosis is zero by definition.

## Key Formula

| Excess kurtosis | Name | Tails vs normal | Distribution examples |
|---|---|---|---|
| $\gamma_2 - 3 > 0$ | Leptokurtic | Fatter | Student's $t$, Laplace, equity returns |
| $\gamma_2 - 3 = 0$ | Mesokurtic | Same | Normal |
| $\gamma_2 - 3 < 0$ | Platykurtic | Thinner | Uniform, beta with low variance |

**Student's $t_\nu$ excess kurtosis:**

$$\gamma_2 - 3 = \frac{6}{\nu - 4}, \qquad \nu > 4$$

As $\nu \to \infty$, excess kurtosis $\to 0$ (converges to normal).

## Example

S&P 500 daily log-returns (1990–2020): excess kurtosis $\approx 8$ to $15$. Compare with the normal's 0. This means that on a day modelled as a "one-in-a-million" event under normality, the actual frequency is far higher — explaining why 2–3 standard deviation moves occur far more often than a normal model predicts.

A Student's $t_5$ model has excess kurtosis $= 6/(5-4) = 6$ — a much more realistic representation of daily equity return tails.

## Remember

Excess kurtosis quantifies exactly how much fatter the tails are than a normal distribution — it is the single most important statistic for tail risk. A VaR model that assumes excess kurtosis = 0 (normal) will underestimate the frequency of large losses by orders of magnitude for real financial data. Using a $t$-distribution with the empirically estimated excess kurtosis is a simple but effective improvement over the normal model for risk measurement.
