# Standardised Normal Variable

**Topic:** Probability
**Tags:** z-score, normal distribution, standardisation, notation, Black-Scholes
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

A **standardised normal variable** $Z$ is a random variable that follows the standard normal distribution $Z \sim N(0, 1)$ — mean zero, variance one. Any normally distributed variable $X \sim N(\mu, \sigma^2)$ can be converted into $Z$ by subtracting the mean and dividing by the standard deviation. The letter $Z$ is the universal notation for this variable in finance and statistics.

## Key Formula

**Standardisation transform:**

$$Z = \frac{X - \mu}{\sigma}$$

**Reverse transform** (generating $X$ from $Z$):

$$X = \mu + \sigma Z$$

| Symbol | Name | Meaning |
|---|---|---|
| $Z$ | Standardised normal variable | A draw from $N(0, 1)$ |
| $\phi(z)$ | Standard normal PDF | $\frac{1}{\sqrt{2\pi}} e^{-z^2/2}$ |
| $\Phi(z)$ | Standard normal CDF | $P(Z \leq z)$ |
| $\Phi^{-1}(p)$ | Probit / quantile function | The $z$ such that $\Phi(z) = p$ |
| $z_\alpha$ | Critical value | Shorthand for $\Phi^{-1}(\alpha)$ |

**Key properties of $Z$:**

$$E[Z] = 0, \quad \operatorname{Var}(Z) = 1, \quad E[Z^3] = 0, \quad E[Z^4] = 3$$

## Example

A stock's annual return is $X \sim N(8\%, 20\%^2)$. What is the probability the return falls below $-15\%$?

Standardise:

$$Z = \frac{-0.15 - 0.08}{0.20} = \frac{-0.23}{0.20} = -1.15$$

Look up: $\Phi(-1.15) = 0.1251$

There is approximately a 12.5% chance the return falls below $-15\%$. The original problem — involving bespoke $\mu$ and $\sigma$ — has been reduced to a single table look-up in the universal $Z$ distribution.

## Remember

The standardised normal variable $Z$ is the atomic building block of quantitative finance models. In Black–Scholes, the terminal stock price is written $S_T = S_0 \exp\bigl((\mu - \tfrac{1}{2}\sigma^2)T + \sigma\sqrt{T}\,Z\bigr)$ — a single draw of $Z$ generates the entire price path. Monte Carlo simulation works by sampling thousands of $Z$ values and mapping each to a scenario via $X = \mu + \sigma Z$. The $d_1$ and $d_2$ in the Black–Scholes formula are themselves standardised variables — they measure how many standard deviations the log-moneyness sits from the forward price. Whenever you see $Z$, $z$, or $N(0,1)$ in a finance paper, it refers to this variable: the universal ruler that converts every normal problem into the same standard scale.
