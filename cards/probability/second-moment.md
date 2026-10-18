# The Second Moment

**Topic:** Probability
**Tags:** second moment, variance, expectation, moments, computational formula
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

The **second moment** $\mathbb{E}[X^2]$ is the expected value of the square of a random variable. It is not the variance: it also contains the square of the mean. The two are linked by the most-used rearrangement in probability.

## Key Formula

$$\mathbb{E}[X^2] = \mathrm{Var}[X] + \bigl(\mathbb{E}[X]\bigr)^2 \qquad\Longleftrightarrow\qquad \mathrm{Var}[X] = \mathbb{E}[X^2] - \bigl(\mathbb{E}[X]\bigr)^2$$

Since variance is non-negative, $\mathbb{E}[X^2] \geq (\mathbb{E}[X])^2$, with equality only if $X$ is constant.

## Example

If $X \sim \mathcal{N}(4, 2^2)$ then $\mathbb{E}[X^2] = 4 + 4^2 = 20$.

Given $\mathbb{E}[X] = 3$ and $\mathrm{Var}[X] = 5$:

$$\mathbb{E}[X^2] = 5 + 9 = 14, \qquad \mathbb{E}[2X + 1] = 7, \qquad \mathrm{Var}[2X + 1] = 4 \times 5 = 20$$

## Remember

Variance is almost always computed this way: realised variance of returns is the mean of squared returns minus the square of the mean return. For daily returns the mean is tiny, so the second moment is almost all variance, which is why volatility estimators often use squared returns directly. The same $\mathbb{E}[X^2]$ appears in the Itô isometry and in the variance of a lognormal price.
