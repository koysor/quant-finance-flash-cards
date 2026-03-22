# Survival Function

**Topic:** Probability
**Tags:** survival function, CDF, tail probability, credit risk, hazard rate
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **survival function** $S(x) = 1 - F(x) = P(X > x)$ gives the probability that a random variable exceeds a given value. It is the complement of the CDF and is always non-increasing from 1 to 0. In quantitative finance, it appears naturally whenever we ask "what is the probability of surviving beyond time $t$?" — for example, the probability that a bond issuer has not defaulted by time $t$.

## Key Formula

$$S(x) = 1 - F(x) = P(X > x) = \int_x^{\infty} f(t)\,dt$$

**Relationship to the hazard rate** $h(x)$:

$$h(x) = \frac{f(x)}{S(x)} = -\frac{d}{dx}\ln S(x)$$

$$S(x) = \exp\!\left(-\int_0^x h(t)\,dt\right) = e^{-H(x)}$$

where $H(x) = \int_0^x h(t)\,dt$ is the **cumulative hazard**.

For the **exponential distribution** (constant hazard $\lambda$):

$$S(t) = e^{-\lambda t}$$

## Example

A corporate bond has a constant annual hazard rate of $\lambda = 2\%$. What is the probability the issuer survives (does not default) beyond 5 years?

$$S(5) = e^{-0.02 \times 5} = e^{-0.10} = 0.9048$$

There is a 90.5% probability of no default in the first 5 years.

The probability of default in the first 5 years is:

$$F(5) = 1 - S(5) = 1 - 0.9048 = 0.0952 \approx 9.5\%$$

## Remember

The survival function is the natural language of credit risk. CDS pricing, bond default probabilities, and Basel regulatory capital formulae are all expressed in terms of survival probabilities rather than CDFs. The key identity $S(t) = e^{-H(t)}$ connects survival to the cumulative hazard, which can be estimated from market CDS spreads — a 100 bps annual CDS spread implies roughly a 1% annual hazard rate. Whenever you see $P(\tau > t)$ in a credit model, you are looking at a survival function.
