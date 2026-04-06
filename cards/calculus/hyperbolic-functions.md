# Hyperbolic Functions

**Topic:** Calculus
**Tags:** hyperbolic, sinh, cosh, tanh, exponential, neural networks, mean reversion
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **hyperbolic functions** are analogues of the trigonometric functions defined using the exponential function rather than the unit circle. They describe the coordinates of a point on the unit hyperbola $x^2 - y^2 = 1$ in the same way that $\cos$ and $\sin$ describe points on the unit circle $x^2 + y^2 = 1$.

## Key Formula

$$\sinh(x) = \frac{e^x - e^{-x}}{2}, \qquad \cosh(x) = \frac{e^x + e^{-x}}{2}, \qquad \tanh(x) = \frac{\sinh(x)}{\cosh(x)} = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$

**Fundamental identity** (analogous to $\sin^2 + \cos^2 = 1$):

$$\cosh^2(x) - \sinh^2(x) = 1$$

**Derivatives:**

$$\frac{d}{dx}\sinh(x) = \cosh(x), \qquad \frac{d}{dx}\cosh(x) = \sinh(x), \qquad \frac{d}{dx}\tanh(x) = \text{sech}^2(x) = 1 - \tanh^2(x)$$

**Behaviour:** $\sinh$ is odd ($\sinh(-x) = -\sinh(x)$), $\cosh$ is even ($\cosh(-x) = \cosh(x)$).

$\tanh(x) \in (-1, 1)$ for all $x$, with $\tanh(x) \to \pm 1$ as $x \to \pm\infty$.

## Example

The Black-Scholes $d_1$ in terms of hyperbolic functions: for an at-the-money forward option ($S = Ke^{rT}$), $\ln(S/K) + rT = 0$ and:

$$d_1 = \frac{\frac{1}{2}\sigma^2 T}{\sigma\sqrt{T}} = \frac{\sigma\sqrt{T}}{2}$$

The sensitivity of $d_1$ to $\sigma$ involves $\cosh$-like expressions in some affine model extensions.

More practically, $\tanh$ is the standard **activation function** in neural networks used for option pricing and volatility surface interpolation — its derivative $1 - \tanh^2(x) = \text{sech}^2(x)$ is everywhere positive and computationally convenient.

## Remember

$\tanh(x)$ is the most important hyperbolic function in modern quantitative finance because it is the **activation function** of choice in recurrent neural networks (LSTMs) used for time-series modelling and derivative pricing. Its S-shaped curve — smoothly bounded between $-1$ and $+1$, with derivative always positive — makes it ideal for learning non-linear transformations of financial data. The connection $\tanh(x) = 2\sigma(2x) - 1$ (where $\sigma$ is the sigmoid function) ties hyperbolic functions directly to logistic regression models used for default probability estimation.
