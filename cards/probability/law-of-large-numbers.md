# Law of Large Numbers

**Topic:** Probability
**Tags:** law of large numbers, convergence, sample mean, Monte Carlo, simulation, expectation
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Law of Large Numbers** (LLN) states that the sample mean of independent, identically distributed random variables converges to the population mean as the sample size grows. The **Weak LLN** gives convergence in probability; the **Strong LLN** gives almost sure convergence.

## Key Formula

Let $X_1, X_2, \ldots$ be i.i.d. with mean $\mu = \mathbb{E}[X]$ and finite variance $\sigma^2$. Define the sample mean $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$.

**Weak LLN:**

$$\bar{X}_n \xrightarrow{P} \mu \quad \text{as } n \to \infty, \qquad \text{i.e.} \quad P\!\left(|\bar{X}_n - \mu| > \varepsilon\right) \to 0 \;\; \forall\, \varepsilon > 0$$

**Strong LLN:**

$$P\!\left(\lim_{n\to\infty} \bar{X}_n = \mu\right) = 1$$

**Rate of convergence** (from Chebyshev's inequality):

$$P\!\left(|\bar{X}_n - \mu| > \varepsilon\right) \leq \frac{\sigma^2}{n\varepsilon^2}$$

## Example

Estimate the fair value of a call option by Monte Carlo. Simulate $n$ stock price paths; for each compute the discounted payoff $Y_i = e^{-rT}\max(S_T^{(i)} - K, 0)$.

By the LLN, $\bar{Y}_n \to \mathbb{E}[e^{-rT}\max(S_T - K, 0)]$ as $n \to \infty$.

With $n = 10{,}000$ paths and $\sigma_{Y} = 5$, the standard error is $\sigma_Y/\sqrt{n} = 5/100 = 0.05$ — the estimate is within £0.05 of the true price with high probability.

## Remember

The LLN is the **theoretical guarantee that Monte Carlo simulation works**. Every Monte Carlo pricer — from simple European calls to XVA calculations on a million-path book — relies on the LLN: the average of $n$ discounted payoffs converges to the true option price. The rate of convergence $O(1/\sqrt{n})$ is also the source of the simulation's main practical limitation: to halve the Monte Carlo error requires quadrupling the number of paths. Variance reduction techniques (antithetic variates, control variates, importance sampling) all aim to reduce $\sigma_Y^2$ so that the same accuracy is achieved with fewer paths.
