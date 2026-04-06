# Leibniz Rule

**Topic:** Calculus
**Tags:** calculus, differentiation, integration, leibniz-rule, parameter-differentiation
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **Leibniz integral rule** (differentiation under the integral sign) states that when an integral depends on a parameter, you can differentiate the entire expression by moving the derivative inside the integral and also accounting for any dependence of the limits on that parameter.

For a parameter $\theta$, lower limit $a(\theta)$, upper limit $b(\theta)$, and integrand $f(x, \theta)$:

$$\frac{d}{d\theta}\int_{a(\theta)}^{b(\theta)} f(x,\theta)\,dx = f\bigl(b(\theta),\theta\bigr)\,b'(\theta) - f\bigl(a(\theta),\theta\bigr)\,a'(\theta) + \int_{a(\theta)}^{b(\theta)} \frac{\partial f}{\partial \theta}(x,\theta)\,dx$$

When the limits are constant (do not depend on $\theta$), the boundary terms vanish and the rule simplifies to:

$$\frac{d}{d\theta}\int_a^b f(x,\theta)\,dx = \int_a^b \frac{\partial f}{\partial \theta}(x,\theta)\,dx$$

## Key Formula

Full form with variable limits:

$$\frac{d}{d\theta}\int_{a(\theta)}^{b(\theta)} f(x,\theta)\,dx = f\bigl(b(\theta),\theta\bigr)\,b'(\theta) - f\bigl(a(\theta),\theta\bigr)\,a'(\theta) + \int_{a(\theta)}^{b(\theta)} \frac{\partial f}{\partial \theta}\,dx$$

Simplified form with constant limits:

$$\frac{d}{d\theta}\int_a^b f(x,\theta)\,dx = \int_a^b \frac{\partial f}{\partial \theta}\,dx$$

## Example

Differentiate $I(\theta) = \displaystyle\int_0^1 x^\theta\,dx$ with respect to $\theta$ (where $\theta > -1$).

**Direct evaluation:** $I(\theta) = \dfrac{x^{\theta+1}}{\theta+1}\Bigg|_0^1 = \dfrac{1}{\theta+1}$, so $I'(\theta) = -\dfrac{1}{(\theta+1)^2}$.

**Leibniz rule (limits constant):**

$$I'(\theta) = \int_0^1 \frac{\partial}{\partial \theta}\,x^\theta\,dx = \int_0^1 x^\theta \ln x\,dx$$

Both methods must agree: $\displaystyle\int_0^1 x^\theta \ln x\,dx = -\frac{1}{(\theta+1)^2}$, which can be verified independently.

## Remember

In quantitative finance the Leibniz rule lets you differentiate option prices and risk measures expressed as expectations (integrals over a risk-neutral density). For example, the Black-Scholes call price is an integral of the payoff against a lognormal density that depends on parameters such as $\sigma$ and $r$. Differentiating inside the integral immediately yields Vega and Rho without needing to re-derive the closed form from scratch. More generally, whenever a price or risk metric is written as $V(\theta) = \int f(x,\theta)\,p(x)\,dx$, the Leibniz rule justifies swapping the order of differentiation and expectation — a step that appears constantly in sensitivity analysis and in deriving Greeks for exotic products.
