# CDF vs PDF

**Topic:** Probability
**Tags:** CDF, PDF, distributions, probability, integration, differentiation
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **probability density function** (PDF) $f(x)$ gives the rate of probability per unit of $x$ — it describes the shape of a distribution but is not itself a probability. The **cumulative distribution function** (CDF) $F(x) = P(X \le x)$ gives the accumulated probability up to $x$. They are linked by integration and differentiation: the CDF is the integral of the PDF, and the PDF is the derivative of the CDF.

## Key Formula

$$F(x) = \int_{-\infty}^{x} f(t)\,dt \qquad \Longleftrightarrow \qquad f(x) = \frac{dF}{dx}$$

**Probability over an interval** (requires both functions):

$$P(a < X \le b) = F(b) - F(a) = \int_a^b f(t)\,dt$$

**Key contrasts:**

| Property | PDF $f(x)$ | CDF $F(x)$ |
|---|---|---|
| Range | $f(x) \ge 0$, can exceed 1 | $0 \le F(x) \le 1$ |
| At a single point | Not a probability | $P(X \le x)$ |
| Shape | Bell, skewed, multi-modal | Always non-decreasing, S-shaped |
| Total area / limit | $\int f = 1$ | $F(\infty) = 1$ |

## Example

A stock's annual log-return $X \sim N(0.08, 0.20^2)$ has PDF and CDF:

$$f(x) = \frac{1}{0.20\sqrt{2\pi}}\,\exp\!\left(-\frac{(x - 0.08)^2}{2(0.04)}\right)$$

**What is the probability of a negative return?**

Using the CDF: $P(X < 0) = F(0)$.

Standardise: $z = \frac{0 - 0.08}{0.20} = -0.40$, so $F(0) = N(-0.40) = 0.345$.

**Using the PDF:** this same answer equals $\int_{-\infty}^{0} f(x)\,dx = 0.345$ — the area under the bell curve to the left of zero.

The CDF gives the answer in one lookup; the PDF requires integration to get the same result.

## Remember

In quantitative finance, the CDF and PDF answer different questions and appear in different contexts. The **CDF** is used directly in option pricing ($N(d_1)$, $N(d_2)$ in Black–Scholes), VaR calculation (the quantile is the inverse CDF), and Monte Carlo simulation (inverse transform sampling). The **PDF** appears in Greek calculations ($N'(d_1)$ in gamma and vega), maximum likelihood estimation, and density forecasting. The key insight is that the CDF accumulates probability (answering "what is the chance of being below $x$?"), while the PDF describes where probability is concentrated (answering "where are outcomes most likely?"). Confusing the two — or forgetting that $f(x)$ is not a probability — is a common source of errors.
