# Cauchy Distribution

**Topic:** Probability
**Tags:** Cauchy, heavy tails, undefined mean, pathological, stable distribution, ratio
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Cauchy distribution** is a continuous, symmetric distribution with location $x_0$ and scale $\gamma > 0$. It has extremely heavy tails: no finite mean, variance, or higher moments exist. The Cauchy arises as the ratio of two independent standard normal random variables, and as a special case of the Student-$t$ distribution with 1 degree of freedom. Despite having no finite moments, it is the canonical example of a distribution where the Law of Large Numbers fails — the sample mean does not converge.

## Key Formula

**PDF:**

$$f(x; x_0, \gamma) = \frac{1}{\pi\gamma\left[1 + \left(\frac{x-x_0}{\gamma}\right)^2\right]}$$

**CDF:**

$$F(x) = \frac{1}{2} + \frac{1}{\pi}\arctan\!\left(\frac{x-x_0}{\gamma}\right)$$

**Moments:** $\mathbb{E}[X]$ and $\text{Var}(X)$ do not exist.

**Ratio:** if $X, Y \overset{\text{iid}}{\sim} N(0,1)$, then $X/Y \sim \text{Cauchy}(0,1)$.

## Example

Portfolio performance ratios such as information ratio or Sharpe ratio involve dividing a return (numerator) by a standard deviation estimate (denominator). When estimated from short samples, both are noisy — the ratio of two approximately normal estimates has Cauchy-like tail behaviour, explaining why **Sharpe ratios are highly unreliable over short periods** and can take extreme values.

Over 12 months: sample Sharpe ratio standard error $\approx \sqrt{(1 + \text{SR}^2/2)/12}$, so a true SR of 0.5 has SE $\approx 0.29$ — the estimate is very noisy.

## Remember

The Cauchy distribution is the theoretical warning against **moment-based risk measures for extreme risk**. Any distribution with tail index $\alpha \leq 1$ (like Cauchy) has no finite mean — standard expected return calculations become meaningless. In practice, financial returns have $\alpha \approx 2$–$4$, so moments exist but are heavily influenced by extremes. The Cauchy also illustrates why **averaging does not always help**: the sample mean of $n$ Cauchy observations has the same Cauchy distribution regardless of $n$ — adding more data does not reduce uncertainty, which is the limiting case of extremely fat-tailed financial returns.
