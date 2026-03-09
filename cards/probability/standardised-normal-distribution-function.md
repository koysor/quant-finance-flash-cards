# Standardised Normal Distribution Function

**Topic:** Probability
**Tags:** normal distribution, phi, CDF, Black-Scholes, quantile, z-score
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

The **standardised normal distribution function** $\Phi(z)$ is the cumulative distribution function (CDF) of the standard normal variable $Z \sim N(0, 1)$. It gives the probability that $Z$ takes a value less than or equal to $z$. Because the standard normal PDF has no closed-form antiderivative, $\Phi$ is defined by an integral and evaluated using tables or numerical methods.

## Key Formula

$$\Phi(z) = \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}}\, e^{-t^2/2}\,dt$$

**Symmetry property** (since the standard normal is symmetric about zero):

$$\Phi(-z) = 1 - \Phi(z)$$

**Standardisation** — for any $X \sim N(\mu, \sigma^2)$:

$$P(X \leq x) = \Phi\!\left(\frac{x - \mu}{\sigma}\right)$$

| $z$ | $\Phi(z)$ |
|---|---|
| $-2.326$ | $0.0100$ |
| $-1.645$ | $0.0500$ |
| $0$ | $0.5000$ |
| $1.645$ | $0.9500$ |
| $2.326$ | $0.9900$ |

## Example

The Black–Scholes call price uses $\Phi$ directly. Given $S_0 = 100$, $K = 105$, $r = 0.05$, $\sigma = 0.20$, $T = 0.5$:

$$d_1 = \frac{\ln(100/105) + (0.05 + 0.02)\times 0.5}{0.20\sqrt{0.5}} = \frac{-0.04879 + 0.035}{0.14142} \approx -0.0974$$

$$d_2 = d_1 - 0.20\sqrt{0.5} \approx -0.0974 - 0.1414 = -0.2388$$

$$C = 100\,\Phi(-0.0974) - 105\,e^{-0.025}\,\Phi(-0.2388)$$
$$C \approx 100(0.4612) - 102.41(0.4056) \approx 46.12 - 41.54 = 4.58$$

The call is worth approximately $4.58, computed entirely through evaluations of $\Phi$.

## Remember

$\Phi$ is the single most frequently called function in quantitative finance. The Black–Scholes formula is built from two evaluations of $\Phi$ — one for the delta-weighted stock component ($\Phi(d_1)$) and one for the discounted strike component ($\Phi(d_2)$). Value at Risk at the $\alpha$ confidence level for a normal portfolio is $\mu + \sigma\,\Phi^{-1}(\alpha)$, so the VaR quantile is just the inverse of $\Phi$. The symmetry identity $\Phi(-z) = 1 - \Phi(z)$ halves the size of look-up tables and simplifies put–call parity arguments. Whenever you see $N(d)$ in a finance textbook, it means $\Phi(d)$.
