# Negative Binomial Distribution

**Topic:** Probability
**Tags:** negative binomial, count data, overdispersion, Poisson mixture, operational risk
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **negative binomial distribution** models the number of successes before a fixed number $r$ of failures in independent Bernoulli trials. Equivalently, it arises as a **Poisson–Gamma mixture**: if the Poisson rate $\lambda \sim \text{Gamma}(r, p/(1-p))$, then the resulting count distribution is negative binomial. It generalises the geometric distribution ($r = 1$) and is used for **overdispersed count data** where variance exceeds the mean.

## Key Formula

**PMF** (number of successes $k$ before $r$ failures):

$$P(X = k) = \binom{k+r-1}{k} p^k (1-p)^r, \quad k = 0, 1, 2, \ldots$$

**Mean and variance:**

$$\mathbb{E}[X] = \frac{rp}{1-p}, \qquad \text{Var}(X) = \frac{rp}{(1-p)^2}$$

**Overdispersion:** $\text{Var}(X) > \mathbb{E}[X]$ always (unlike Poisson where they are equal).

**Poisson limit:** as $r \to \infty$, $p \to 0$ with $rp/(1-p) \to \lambda$, the distribution approaches $\text{Poisson}(\lambda)$.

## Example

Operational risk loss events occur with overdispersed frequency. A Poisson model ($\lambda = 5$ per year) predicts Var = 5, but observed Var = 12. Fitting $\text{NegBin}(r, p)$:

$$\frac{rp}{1-p} = 5, \quad \frac{rp}{(1-p)^2} = 12 \implies 1-p = 5/12, \; r = 5 \times (7/12)/(5/12) = 7$$

The heavier tail of the negative binomial gives higher capital estimates than the Poisson model.

## Remember

The negative binomial distribution is the standard **frequency distribution in operational risk** capital models (Basel AMA). Real-world event frequencies are overdispersed — clustering of events (system outages, fraud waves) means variance exceeds the mean, violating the Poisson assumption. The Poisson–Gamma mixture interpretation is also important: it models the situation where the underlying event rate $\lambda$ is itself uncertain (Gamma-distributed), reflecting model uncertainty. The compound negative binomial distribution (negative binomial frequency × severity) generates the heavy-tailed total loss distributions that drive large operational risk capital requirements.
