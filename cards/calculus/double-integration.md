# Double Integration

**Topic:** Calculus
**Tags:** calculus, integration, iterated integrals, joint density, multivariable
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

A **double integral** extends single-variable integration to functions of two variables, computing the volume under a surface $f(x, y)$ over a two-dimensional region $R$. In practice it is evaluated as an **iterated integral** — integrating first with respect to one variable (treating the other as constant) and then with respect to the second. This is directly analogous to performing two successive single integrations.

## Key Formula

For a rectangular region $a \leq x \leq b$, $c \leq y \leq d$:

$$\iint_R f(x, y) \, dA = \int_a^b \int_c^d f(x, y) \, dy \, dx$$

**Fubini's theorem** guarantees that, provided $f$ is continuous on $R$, the order of integration may be swapped without changing the result:

$$\int_a^b \int_c^d f(x, y) \, dy \, dx = \int_c^d \int_a^b f(x, y) \, dx \, dy$$

For a **joint probability density function** $f(x, y)$ of two continuous random variables $X$ and $Y$, the probability that $(X, Y)$ falls in region $R$ is:

$$P\bigl((X, Y) \in R\bigr) = \iint_R f(x, y) \, dA$$

and the marginal density of $X$ is recovered by integrating out $Y$:

$$f_X(x) = \int_{-\infty}^{\infty} f(x, y) \, dy$$

## Example

Suppose the joint density of two correlated log-returns is uniform on the square $[0, 2] \times [0, 2]$, so $f(x, y) = \tfrac{1}{4}$. Find the probability that both returns are positive and less than 1.

$$P(0 \leq X \leq 1,\ 0 \leq Y \leq 1) = \int_0^1 \int_0^1 \frac{1}{4} \, dy \, dx$$

**Inner integral** (with respect to $y$):

$$\int_0^1 \frac{1}{4} \, dy = \frac{1}{4}$$

**Outer integral** (with respect to $x$):

$$\int_0^1 \frac{1}{4} \, dx = \frac{1}{4}$$

So the probability is $0.25$ — exactly one quarter of the total probability mass, as expected from symmetry.

## Remember

Double integration is the mathematical engine behind **joint distribution models** in multi-asset derivatives. The price of a **spread option** (payoff: $\max(S_1 - S_2 - K, 0)$) requires integrating the joint lognormal density of two correlated assets over the exercise region — a two-dimensional integral that generally has no closed form and must be evaluated numerically. Mastering iterated integrals and the ability to change integration order (Fubini) is essential for deriving marginal distributions, computing covariances, and understanding how correlation enters option pricing models.
