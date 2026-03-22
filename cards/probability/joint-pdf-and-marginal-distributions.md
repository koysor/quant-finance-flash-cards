# Joint PDF and Marginal Distributions

**Topic:** Probability
**Tags:** joint distribution, marginal distribution, multivariate, correlation, independence
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A **joint PDF** $f_{X,Y}(x, y)$ describes the simultaneous probability structure of two (or more) continuous random variables. The **marginal distribution** of one variable is obtained by integrating ("summing out") the other from the joint density, recovering the univariate PDF as if the other variable did not exist.

## Key Formula

**Joint probability over a region:**

$$P(a < X \le b, \; c < Y \le d) = \int_a^b \int_c^d f_{X,Y}(x,y)\,dy\,dx$$

**Marginal PDFs** from the joint:

$$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dy, \qquad f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dx$$

**Independence** holds if and only if the joint factors:

$$f_{X,Y}(x,y) = f_X(x)\,f_Y(y) \quad \text{for all } x, y$$

For the **bivariate normal** with correlation $\rho$:

$$f_{X,Y}(x,y) = \frac{1}{2\pi\sigma_X\sigma_Y\sqrt{1-\rho^2}} \exp\!\left(-\frac{1}{2(1-\rho^2)}\left[\frac{(x-\mu_X)^2}{\sigma_X^2} - \frac{2\rho(x-\mu_X)(y-\mu_Y)}{\sigma_X\sigma_Y} + \frac{(y-\mu_Y)^2}{\sigma_Y^2}\right]\right)$$

## Example

Two stock returns $X$ and $Y$ follow a bivariate normal with $\mu_X = \mu_Y = 0$, $\sigma_X = \sigma_Y = 1$, and $\rho = 0.6$.

What is $P(X > 1, Y > 1)$?

Each marginal gives $P(X > 1) = 1 - \Phi(1) = 0.159$. If independent, $P(X > 1, Y > 1)$ would be $0.159^2 = 0.025$.

With $\rho = 0.6$, the joint probability is approximately **0.067** — nearly three times higher than the independent case — because positive correlation makes simultaneous large moves more likely.

## Remember

Portfolio risk depends entirely on the joint distribution of asset returns, not just the marginals. Two assets can each have well-behaved normal marginals yet exhibit dangerous joint tail behaviour if the dependence structure (captured by copulas or the correlation matrix) concentrates probability in the extremes. The bivariate normal's joint PDF shows how $\rho$ controls the elliptical contours of equal density — but in practice, financial returns often exhibit **tail dependence** beyond what $\rho$ captures, which is why copula models are used for more realistic joint modelling in risk management.
