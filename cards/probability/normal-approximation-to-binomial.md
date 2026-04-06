# Normal Approximation to the Binomial

**Topic:** Probability
**Tags:** normal approximation, binomial, continuity correction, central limit theorem, large sample
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

When $n$ is large and $p$ is not too close to 0 or 1, the binomial distribution $X \sim B(n, p)$ can be approximated by a normal distribution. The approximation improves as $n$ increases and is generally considered adequate when $np > 5$ and $n(1-p) > 5$. A **continuity correction** is applied because we are approximating a discrete distribution with a continuous one: a discrete value $x$ is replaced by the interval $(x - 0.5, x + 0.5)$.

## Key Formula

**Approximation:**

$$X \sim B(n,p) \approx N(\mu, \sigma^2), \quad \mu = np, \quad \sigma^2 = np(1-p)$$

**Continuity correction:**

$$P(X \leq k) \approx P\!\left(Z \leq \frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right)$$

$$P(X \geq k) \approx P\!\left(Z \geq \frac{k - 0.5 - np}{\sqrt{np(1-p)}}\right)$$

$$P(X = k) \approx P\!\left(\frac{k - 0.5 - np}{\sqrt{np(1-p)}} \leq Z \leq \frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right)$$

## Example

A trader executes 200 independent trades, each with a 55% win probability. Find the approximate probability of winning more than 120 trades.

$$\mu = 200 \times 0.55 = 110, \quad \sigma = \sqrt{200 \times 0.55 \times 0.45} = \sqrt{49.5} \approx 7.04$$

$$P(X > 120) \approx P\!\left(Z > \frac{120.5 - 110}{7.04}\right) = P(Z > 1.492) \approx 1 - 0.9322 = 0.068$$

Without the continuity correction ($P(Z > 1.42) \approx 0.078$) the answer differs by about 1 percentage point.

## Remember

The normal approximation to the binomial is an application of the **Central Limit Theorem**: the sum of many independent Bernoulli trials converges to normality. In quantitative finance this underpins the **Black-Scholes model** — the log-return of a stock over $n$ periods is the sum of $n$ small i.i.d. shocks, which by the CLT is approximately normal. The continuity correction is a reminder that financial data is often **discretely quoted** (prices tick in £0.01 increments) even when modelled continuously.
