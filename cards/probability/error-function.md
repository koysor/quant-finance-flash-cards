# Error Function

**Topic:** Probability
**Tags:** erf, normal distribution, phi, numerical methods, special functions
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

The **error function** $\operatorname{erf}(x)$ is a special function that measures the probability of a standard normal variable falling within $\pm x\sqrt{2}$ of the mean. It arises naturally from the Gaussian integral and provides the mathematical link between the raw Gaussian integral and the standardised normal CDF $\Phi(z)$.

## Key Formula

$$\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2}\,dt$$

**Relation to $\Phi$:**

$$\Phi(z) = \frac{1}{2}\left[1 + \operatorname{erf}\!\left(\frac{z}{\sqrt{2}}\right)\right]$$

**Complementary error function:**

$$\operatorname{erfc}(x) = 1 - \operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_x^{\infty} e^{-t^2}\,dt$$

| $x$ | $\operatorname{erf}(x)$ |
|---|---|
| $0$ | $0$ |
| $0.5$ | $0.5205$ |
| $1.0$ | $0.8427$ |
| $2.0$ | $0.9953$ |

## Example

Compute $\Phi(1.0)$ using the error function:

$$\Phi(1.0) = \frac{1}{2}\left[1 + \operatorname{erf}\!\left(\frac{1.0}{\sqrt{2}}\right)\right] = \frac{1}{2}\left[1 + \operatorname{erf}(0.7071)\right]$$

From tables, $\operatorname{erf}(0.7071) \approx 0.6827$, so:

$$\Phi(1.0) \approx \frac{1}{2}(1 + 0.6827) = 0.8414$$

This confirms the familiar result that roughly 84.1% of a standard normal distribution lies below one standard deviation.

## Remember

Every numerical library computes $\Phi(z)$ by calling the error function internally — Python's `scipy.stats.norm.cdf`, Excel's `NORM.S.DIST`, and C++'s `std::erfc` all reduce to highly optimised $\operatorname{erf}$ implementations. In quantitative finance, when you price options via Black–Scholes or compute parametric VaR, the computational bottleneck is evaluating $\operatorname{erf}$ millions of times across a grid of strikes and maturities. Understanding this link matters when you need to implement fast, accurate pricing engines — rational polynomial approximations to $\operatorname{erf}$ (such as Abramowitz and Stegun's formula) are standard practice in production quant libraries.
