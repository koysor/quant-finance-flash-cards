# Moment Generating Function

**Topic:** Probability
**Tags:** distributions, probability, moments, expectation, transforms

---

## Definition

The moment generating function (MGF) of a random variable $X$ is the function $M_X(t) = E[e^{tX}]$, defined for all values of $t$ in a neighbourhood of zero where this expectation exists. Its key property is that the $n$th derivative evaluated at $t = 0$ gives the $n$th moment of $X$, and if two random variables share the same MGF then they share the same distribution.

## Key Formula

$$M_X(t) = E[e^{tX}]$$

The $n$th moment is extracted by differentiating $n$ times and setting $t = 0$:

$$E[X^n] = M_X^{(n)}(0) = \left.\frac{d^n}{dt^n} M_X(t)\right|_{t=0}$$

For the sum of independent random variables $X + Y$, the MGF factorises:

$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$$

## Example

Let $X \sim N(\mu, \sigma^2)$ with $\mu = 3$ and $\sigma = 2$. The MGF of a normal random variable is:

$$M_X(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2} = e^{3t + 2t^2}$$

The first moment (mean): $M_X'(t) = (3 + 4t)\,e^{3t + 2t^2}$, so $M_X'(0) = 3$. This confirms $E[X] = 3$.

The second moment: $M_X''(t)$ evaluated at $t = 0$ gives $M_X''(0) = 13$. Therefore $\text{Var}(X) = E[X^2] - (E[X])^2 = 13 - 9 = 4 = \sigma^2$, as expected.

## Remember

In quantitative finance the MGF is the bridge between a distribution and its moments. When you model portfolio returns as the sum of independent asset returns, the MGF of the portfolio is the product of the individual MGFs -- this is exactly how one proves that the sum of independent normals is normal, which underpins the parametric VaR calculation $\text{VaR} = z_\alpha\,\sigma_p$. If the MGF does not exist (as for heavy-tailed distributions), it is a warning that moments may be infinite and standard risk measures may understate true tail risk.
