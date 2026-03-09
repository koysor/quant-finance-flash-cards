# Z-Table

**Topic:** Probability
**Tags:** normal distribution, z-score, lookup table, quantile, standardisation
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

A **Z-table** (or standard normal table) is a tabulated listing of values of the standardised normal CDF $\Phi(z) = P(Z \leq z)$. The rows give the integer and first decimal place of $z$; the columns give the second decimal place. Reading the table converts any z-score into a cumulative probability without computation.

## Key Formula

The table encodes:

$$\Phi(z) = \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}}\, e^{-t^2/2}\,dt$$

**Using symmetry** to handle negative $z$:

$$\Phi(-z) = 1 - \Phi(z)$$

So only the positive half of the table is strictly needed.

**Common critical values** (memorise these):

| $z$ | $\Phi(z)$ | Tail $1 - \Phi(z)$ | Use |
|---|---|---|---|
| $1.282$ | $0.9000$ | $10\%$ | 90% confidence |
| $1.645$ | $0.9500$ | $5\%$ | 95% VaR / one-sided test |
| $1.960$ | $0.9750$ | $2.5\%$ | 95% two-sided CI |
| $2.326$ | $0.9900$ | $1\%$ | 99% VaR |
| $2.576$ | $0.9950$ | $0.5\%$ | 99% two-sided CI |

## Example

A portfolio's weekly return has $\mu = 0.2\%$ and $\sigma = 1.5\%$. What is the probability of losing more than 3%?

Standardise: $z = \frac{-0.03 - 0.002}{0.015} = \frac{-0.032}{0.015} = -2.13$

From the Z-table, read row $2.1$, column $0.03$: $\Phi(2.13) = 0.9834$.

By symmetry: $\Phi(-2.13) = 1 - 0.9834 = 0.0166$.

There is approximately a 1.7% chance of losing more than 3% in a week.

## Remember

Before computers, the Z-table was the only way to evaluate $\Phi(z)$, and every quantitative finance calculation — option pricing, VaR, hypothesis testing — required reading it fluently. Even today, the critical values $1.645$ (95%), $1.960$ (97.5%), and $2.326$ (99%) appear so frequently in risk management and regulatory capital formulae that practitioners memorise them. In exams and interviews, being able to convert between z-scores and probabilities instantly — without software — remains an expected skill. The table also builds intuition: a 3-sigma event has probability $0.13\%$, which sounds rare until you realise that daily financial markets produce roughly 252 trading days per year, making such events almost certain over a career.
