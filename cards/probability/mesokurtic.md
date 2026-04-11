# Mesokurtic Distribution

**Topic:** Probability
**Tags:** mesokurtic, normal distribution, kurtosis, excess kurtosis, benchmark
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

A **mesokurtic** distribution has **excess kurtosis equal to zero** ($\gamma_2 - 3 = 0$, i.e. $\gamma_2 = 3$). Its tail weight and peak shape match the normal distribution exactly. The normal distribution is the canonical mesokurtic distribution and serves as the reference point for all kurtosis comparisons.

$$\gamma_2 - 3 = 0 \iff \text{mesokurtic}$$

## Key Formula

$$\gamma_2 = \frac{E[(X-\mu)^4]}{\sigma^4} = 3 \quad \text{(mesokurtic)}$$

**The three kurtosis categories:**

| Category | Excess kurtosis | Tails | Example |
|---|---|---|---|
| Platykurtic | $< 0$ | Thinner than normal | Uniform |
| **Mesokurtic** | $= 0$ | Same as normal | **Normal** |
| Leptokurtic | $> 0$ | Fatter than normal | Student's $t$ |

**Fourth central moment of a mesokurtic distribution:**

$$\mu_4 = 3\sigma^4$$

This is the "expected" fourth moment — the baseline from which excess kurtosis measures deviation.

## Example

A portfolio of hundreds of small, genuinely independent positions — if such a thing existed — would by the CLT have approximately normally distributed returns: mesokurtic with excess kurtosis $\approx 0$. The more common finding in practice is that real portfolios have leptokurtic returns (excess kurtosis $> 0$) because positions share common factor exposures, making the portfolio far from truly diversified.

## Remember

Mesokurtic is primarily a benchmark, not an empirical finding. Stating that a distribution is mesokurtic is equivalent to saying it has the same tail behaviour as a normal distribution. In finance, the mesokurtic assumption is a shorthand for "we are assuming normality of tails." Virtually all empirical return distributions are leptokurtic; mesokurtosis is the theoretical benchmark that models deviate from, and measuring that deviation (excess kurtosis) is a standard diagnostic step in model validation.
