# Multinomial Distribution

**Topic:** Probability
**Tags:** multinomial, categorical, generalised binomial, credit ratings, sector allocation
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **multinomial distribution** generalises the binomial to $k \geq 2$ categories. In $n$ independent trials, each trial results in outcome $i$ with probability $p_i$, where $\sum_{i=1}^k p_i = 1$. The joint distribution of the counts $(X_1, \ldots, X_k)$, where $X_i$ is the number of trials giving outcome $i$, is multinomial with parameters $n$ and $(p_1, \ldots, p_k)$.

## Key Formula

**PMF:**

$$P(X_1 = x_1, \ldots, X_k = x_k) = \frac{n!}{x_1! \cdots x_k!} p_1^{x_1} \cdots p_k^{x_k}, \quad \sum_{i=1}^k x_i = n$$

**Marginal distributions:** $X_i \sim B(n, p_i)$ for each $i$.

**Mean, variance, and covariance:**

$$\mathbb{E}[X_i] = np_i, \quad \text{Var}(X_i) = np_i(1-p_i), \quad \text{Cov}(X_i, X_j) = -np_ip_j \; (i \neq j)$$

The negative covariance reflects the constraint $\sum X_i = n$: if one count is high, others must be lower.

## Example

A credit rating agency tracks annual migrations across 3 categories: upgrade (prob 0.10), no change (0.85), downgrade (0.05) for $n = 200$ bonds.

$$\mathbb{E}[\text{upgrades}] = 20, \quad \mathbb{E}[\text{downgrades}] = 10$$

$$\text{Cov}(\text{upgrades, downgrades}) = -200 \times 0.10 \times 0.05 = -1$$

The negative covariance: years with many upgrades tend to have fewer downgrades.

## Remember

The multinomial distribution underpins the **chi-squared goodness-of-fit test**: under $H_0$, observed category counts follow a multinomial distribution, and the chi-squared statistic $\sum (O_i - E_i)^2 / E_i$ measures how far the observed multinomial is from the expected. In finance, this tests whether **observed credit rating migrations** match the historical transition matrix — a key model validation step. Portfolio sector allocations are also multinomial: the composition of a portfolio across $k$ sectors is a multinomial outcome, and tracking error to a benchmark involves analysing deviations from the expected multinomial proportions.
