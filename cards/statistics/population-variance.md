# Population Variance

**Topic:** Statistics
**Tags:** variance, population, standard deviation, dispersion, risk
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **population variance** $\sigma^2$ measures the average squared deviation of every observation in the population from the population mean $\mu$. It is the true, theoretical variance of the data-generating process — never directly observable, but estimable from samples.

$$\sigma^2 = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2 \quad \text{(finite population)}$$

$$\sigma^2 = E\!\left[(X - \mu)^2\right] = E[X^2] - \mu^2 \quad \text{(random variable)}$$

## Key Formula

**Finite population:**

$$\sigma^2 = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2$$

**Equivalent computational form:**

$$\sigma^2 = E[X^2] - (E[X])^2$$

**Standard deviation:**

$$\sigma = \sqrt{\sigma^2}$$

**Scaling:**

$$\text{Var}(aX + b) = a^2\sigma^2$$

## Example

A stock has annual returns drawn from $N(\mu, \sigma^2)$ with $\sigma = 20\%$ per year. The population variance is $\sigma^2 = 0.04$. Over a horizon of $T$ years (assuming i.i.d. returns), the cumulative return variance is $T\sigma^2$ and the volatility scales as $\sigma\sqrt{T}$ — so a 2-year investment has annual equivalent volatility $20\%\sqrt{2} \approx 28.3\%$.

If instead the daily population variance is $\sigma_d^2$, the annual variance is $252\,\sigma_d^2$ under i.i.d. returns (the square-root-of-time rule for volatility).

## Remember

The population variance $\sigma^2$ is the theoretical object that risk models are trying to estimate. VaR, tracking error, and Sharpe ratio calculations all depend on it. Because $\sigma^2$ is unobservable, practitioners must choose an estimator — historical (sample variance with $n-1$), EWMA, or GARCH — each making different assumptions about how the true variance evolves over time. The choice of estimator is a modelling decision with real consequences: underestimating $\sigma^2$ leads directly to underestimating required capital and risk limits.
