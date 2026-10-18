# Expectation Algebra

**Topic:** Probability
**Tags:** expectation, variance, linearity, diversification, independence, scaling
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

Expectation algebra gives the rules for how $\mathbb{E}$ and $\mathrm{Var}$ behave under scaling and addition. The variance signs are where errors occur: variance scales by the square of a constant, and variances add for both sums and differences of independent variables.

## Key Formula

$$\mathbb{E}[aX + b] = a\,\mathbb{E}[X] + b, \qquad \mathrm{Var}[aX + b] = a^2\,\mathrm{Var}[X]$$

| Quantity | Result |
|---|---|
| $\mathbb{E}[X + Y]$ | $\mathbb{E}[X] + \mathbb{E}[Y]$, always |
| $\mathrm{Var}[X + Y]$ | $\mathrm{Var}[X] + \mathrm{Var}[Y]$ if independent |
| $\mathrm{Var}[X - Y]$ | $\mathrm{Var}[X] + \mathrm{Var}[Y]$ if independent: **also a plus** |

The shift $b$ vanishes from the variance, and $\sigma$ scales by $|a|$.

## Example

If $Y = 3X - 7$ then $\mathbb{E}[Y] = 3\,\mathbb{E}[X] - 7$ and $\mathrm{Var}[Y] = 9\,\mathrm{Var}[X]$.

For $n$ independent assets each with variance $\sigma^2$, an equally weighted portfolio has

$$\mathrm{Var}\left[\frac{1}{n}\sum_{i=1}^{n} X_i\right] = \frac{1}{n^2}\cdot n\sigma^2 = \frac{\sigma^2}{n}$$

so its standard deviation falls as $\sigma/\sqrt{n}$.

## Remember

That $\sigma^2/n$ result is the whole quantitative case for diversification. The $\mathrm{Var}[X - Y]$ sign is the most commonly made error and is exactly the calculation in a long-short hedge: the risk of a spread is the sum of the variances minus twice the covariance, never a difference of variances.
