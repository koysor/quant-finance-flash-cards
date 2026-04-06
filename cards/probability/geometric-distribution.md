# Geometric Distribution

**Topic:** Probability
**Tags:** geometric distribution, first success, memoryless, waiting time, Bernoulli trials
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **geometric distribution** models the number of independent Bernoulli trials needed to obtain the **first success**. It is the only discrete distribution with the **memoryless property**: the number of additional trials needed is independent of how many trials have already failed. Two conventions exist: $X$ = number of trials until first success (supported on $\{1, 2, \ldots\}$) or $Y = X - 1$ = number of failures before first success (supported on $\{0, 1, 2, \ldots\}$).

## Key Formula

**PMF** (number of trials to first success):

$$P(X = k) = (1-p)^{k-1} p, \quad k = 1, 2, 3, \ldots$$

**Mean and variance:**

$$\mathbb{E}[X] = \frac{1}{p}, \qquad \text{Var}(X) = \frac{1-p}{p^2}$$

**Memoryless property:**

$$P(X > m + n \mid X > m) = P(X > n)$$

**CDF:** $P(X \leq k) = 1 - (1-p)^k$

## Example

A credit analyst checks a bond portfolio daily for the first default event. Each bond has daily default probability $p = 0.001$.

$$\mathbb{E}[X] = 1/0.001 = 1000 \text{ days}, \qquad \sigma = \sqrt{999}/0.001 \approx 999 \text{ days}$$

The probability of no default in the first 500 days: $P(X > 500) = (1-0.001)^{500} \approx e^{-0.5} \approx 60.7\%$.

## Remember

The geometric distribution is the **discrete analogue of the exponential distribution** — both share the memoryless property. In credit risk, it models **time to default** when default probability is constant each period. The memoryless property matters for **credit portfolio management**: knowing that a bond has survived 5 years tells you nothing extra about whether it will default next year (under a constant hazard model). The geometric distribution is also the basis of the **run-length distribution in backtesting** — the number of consecutive VaR non-exceedances follows a geometric distribution if the model is correctly specified.
