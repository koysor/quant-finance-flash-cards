# Moment Notation

**Topic:** Mathematical Notation
**Tags:** notation, moments, central moments, skewness, kurtosis, raw moments
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Moment notation** provides a compact way to describe the shape of a probability distribution. Raw moments measure about zero; central moments measure about the mean; standardised moments are scale-free shape statistics.

| Symbol | Read as | Definition | Meaning |
|---|---|---|---|
| $\mu_k'$ | "k-th raw moment" | $E[X^k]$ | Moment about zero |
| $\mu_k$ | "k-th central moment" | $E[(X - \mu)^k]$ | Moment about the mean |
| $\mu_1'$ | "first raw moment" | $E[X] = \mu$ | Mean |
| $\mu_2$ | "second central moment" | $E[(X-\mu)^2] = \sigma^2$ | Variance |
| $\mu_3$ | "third central moment" | $E[(X-\mu)^3]$ | Asymmetry (related to skewness) |
| $\mu_4$ | "fourth central moment" | $E[(X-\mu)^4]$ | Tail weight (related to kurtosis) |

## Key Formula

**Standardised moments** (dimensionless, scale-invariant):

$$\tilde{\mu}_k = \frac{\mu_k}{\sigma^k} = \frac{E[(X-\mu)^k]}{\left(E[(X-\mu)^2]\right)^{k/2}}$$

| Standardised moment | Symbol | Value for $N(\mu,\sigma^2)$ |
|---|---|---|
| 3rd ($k=3$) | $\gamma_1 = \tilde{\mu}_3$ (skewness) | 0 |
| 4th ($k=4$) | $\gamma_2 = \tilde{\mu}_4$ (kurtosis) | 3 |
| Excess kurtosis | $\gamma_2 - 3$ | 0 |

## Example

For a $\text{Normal}(\mu, \sigma^2)$ distribution: $\mu_1' = \mu$, $\mu_2 = \sigma^2$, $\mu_3 = 0$ (symmetric), $\mu_4 = 3\sigma^4$ (so $\gamma_2 = 3$).

For a Student's $t$ with $\nu = 5$ degrees of freedom: $\mu_4 = 3\sigma^4 \cdot \frac{\nu-2}{\nu-4} = 3\sigma^4 \cdot 3 = 9\sigma^4$, giving $\gamma_2 = 9 > 3$ — heavier tails than normal.

## Remember

In quantitative finance, the 3rd and 4th standardised moments — skewness ($\gamma_1$) and excess kurtosis ($\gamma_2 - 3$) — are the two statistics that most visibly distinguish real asset return distributions from the normal distribution. Equity returns typically show negative skewness (large losses are more common than large gains) and positive excess kurtosis (fat tails). These deviations from normality are precisely what VaR models underestimate and why CVaR is preferred.
