# Mill's Ratio

**Topic:** Probability
**Tags:** normal distribution, tail probability, hazard rate, barrier options, asymptotics
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

**Mill's ratio** for the standard normal distribution is the ratio of the PDF $\phi(z)$ to the survival function $1 - \Phi(z)$. It measures how rapidly the tail probability decays relative to the density, and is the reciprocal of the hazard rate. For large $z$, Mill's ratio approaches $1/z$, giving a simple approximation for tail probabilities.

## Key Formula

$$M(z) = \frac{\phi(z)}{1 - \Phi(z)}$$

where $\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$.

**Tail approximation** (for large $z > 0$):

$$1 - \Phi(z) \approx \frac{\phi(z)}{z}$$

**Tighter bound** (for $z > 0$):

$$\frac{z}{z^2 + 1}\,\phi(z) \leq 1 - \Phi(z) \leq \frac{1}{z}\,\phi(z)$$

| $z$ | $\phi(z)/z$ | $1 - \Phi(z)$ | Relative error |
|---|---|---|---|
| $2$ | $0.02700$ | $0.02275$ | $18.7\%$ |
| $3$ | $0.01477$ | $0.01350$ | $9.4\%$ |
| $4$ | $0.00033$ | $0.00003$ | $4.7\%$ |

## Example

Estimate the probability that a standard normal variable exceeds $z = 3$ using Mill's ratio:

$$1 - \Phi(3) \approx \frac{\phi(3)}{3} = \frac{1}{3} \times \frac{1}{\sqrt{2\pi}} e^{-9/2} = \frac{1}{3} \times 0.004432 = 0.001477$$

The exact value is $0.001350$, so the approximation is about 9.4% too high — but it captures the correct order of magnitude with a simple mental calculation.

## Remember

Mill's ratio is a practical tool for reasoning about extreme events in quantitative finance. When computing the probability of a 5-sigma market crash, exact $\Phi$ tables are often unavailable and the approximation $1 - \Phi(z) \approx \phi(z)/z$ gives a quick estimate. In barrier option pricing, the probability of breaching a far-out-of-the-money barrier involves deep tail evaluations where Mill's ratio provides the leading-order behaviour. The ratio also appears in truncated normal distributions used for censored return data and in the Heckman correction for selection bias in financial econometrics.
