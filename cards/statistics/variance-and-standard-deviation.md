# Variance and Standard Deviation

**Topic:** Statistics
**Level:** A Level Mathematics
**Tags:** statistics, descriptive stats, risk, spread

---

## Definition

**Variance** measures the average squared deviation of a random variable from its mean. It quantifies **spread** or **dispersion**.

**Standard deviation** is the square root of variance, expressed in the same units as the data — making it more interpretable.

In finance, standard deviation of returns is the primary measure of **volatility**.

## Key Formula

**Population variance:**

$$\sigma^2 = E\!\left[(X - \mu)^2\right] = E[X^2] - (E[X])^2$$

**Sample variance** (unbiased, using Bessel's correction):

$$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

**Standard deviation:** σ = √(σ²)

## Key Properties

- Var(aX + b) = a² Var(X)
- Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X, Y)
- For **independent** X and Y: Var(X + Y) = Var(X) + Var(Y)

## Example

Daily returns: 1%, −2%, 3%, 0%, −1%

Mean: x̄ = (1 − 2 + 3 + 0 − 1) / 5 = 0.2%

Sample variance: s² = [(0.8² + 2.2² + 2.8² + 0.2² + 1.2²)] / 4 = [0.64 + 4.84 + 7.84 + 0.04 + 1.44] / 4 = 14.8 / 4 = 3.7 (%²)

Standard deviation: s = √3.7 ≈ **1.92%**

## Remember

- Standard deviation (volatility) is the most widely used risk measure in finance, but it treats upside and downside equally — it **does not distinguish** between good and bad volatility.
- **Annualising:** multiply daily σ by √252 (trading days per year).
