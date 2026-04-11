# Leptokurtic Distribution

**Topic:** Probability
**Tags:** leptokurtic, fat tails, excess kurtosis, kurtosis, heavy tails
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

A **leptokurtic** distribution has **excess kurtosis greater than zero** ($\gamma_2 - 3 > 0$). Compared to the normal distribution, it has a sharper central peak and **fatter tails** — extreme outcomes are more likely than a normal model would predict.

$$\gamma_2 - 3 > 0 \iff \text{leptokurtic}$$

## Key Formula

**Excess kurtosis** (the defining measure):

$$\gamma_2 - 3 = \frac{\mu_4}{\sigma^4} - 3 = \frac{E[(X-\mu)^4]}{\sigma^4} - 3 > 0$$

**Common leptokurtic distributions in finance:**

| Distribution | Excess kurtosis |
|---|---|
| Student's $t_\nu$ | $6/(\nu-4)$ for $\nu > 4$ |
| Laplace | 3 |
| Logistic | 1.2 |
| Normal | 0 (reference) |

The fatter the tails, the larger the excess kurtosis.

## Example

Daily equity log-returns typically have excess kurtosis of 5–15. Under a normal model, a 5-standard-deviation loss (a "five-sigma event") has probability $\approx 3 \times 10^{-7}$ (once in 10 million trading days — about 40,000 years). Under a Student's $t_5$ model with excess kurtosis 6, the same event is roughly 100× more likely — occurring perhaps once in a few hundred years instead.

## Remember

Leptokurtic means "narrow hump, fat tails." The word comes from Greek *lepto* (slender) — the peak is thin and sharp, but the tails extend further than normal. In practice, virtually every financial return series is leptokurtic. This is why the Black-Scholes model underprices deep out-of-the-money options (which pay off in the tails) and why normal-distribution VaR underestimates true tail risk. Leptokurtosis is the mathematical signature of fat tails.
