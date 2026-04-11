# Inverse Cumulative Distribution Function

**Topic:** Probability
**Tags:** inverse CDF, quantile function, percentile, VaR, simulation
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **inverse CDF** (also called the **quantile function**) $F_X^{-1}(p)$ returns the value $x$ such that $P(X \leq x) = p$. It reverses the CDF: given a probability level, it returns the corresponding threshold.

$$F_X^{-1}(p) = \inf\{x \in \mathbb{R} : F_X(x) \geq p\}, \qquad p \in (0, 1)$$

## Key Formula

**For the normal distribution** (using the standard normal $\Phi$):

$$F_X^{-1}(p) = \mu + \sigma\,\Phi^{-1}(p)$$

Common quantiles of $\mathcal{N}(0,1)$:

| $p$ | $\Phi^{-1}(p)$ | Use |
|---|---|---|
| 0.95 | 1.645 | 95% VaR (one-tailed) |
| 0.975 | 1.960 | 97.5% quantile |
| 0.99 | 2.326 | 99% VaR |
| 0.001 | −3.090 | Extreme loss threshold |

**Inverse transform sampling:** to simulate $X \sim F_X$, draw $U \sim \text{Uniform}(0,1)$ and set $X = F_X^{-1}(U)$.

## Example

A portfolio loss $L \sim \mathcal{N}(£0, £500{,}000^2)$. The 99% VaR is:

$$\text{VaR}_{99\%} = F_L^{-1}(0.99) = 0 + 500{,}000 \times \Phi^{-1}(0.99) = 500{,}000 \times 2.326 = £1{,}163{,}000$$

There is a 1% chance of losing more than £1.163 million in a day.

## Remember

The inverse CDF connects three core areas of quantitative finance. In **risk**, VaR is $F_{\text{Loss}}^{-1}(\alpha)$ — the $\alpha$-quantile of the loss distribution. In **simulation**, inverse transform sampling generates any target distribution from uniform random numbers, making the inverse CDF the engine of Monte Carlo methods. In **derivatives**, the Black-Scholes $N(d_2)$ term is $\Phi(d_2)$, and the strike in a digital option is selected at a quantile of the terminal price distribution.
