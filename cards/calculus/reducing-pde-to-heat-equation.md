# Reducing a PDE to the Heat Equation

**Topic:** Calculus
**Tags:** PDE, heat equation, substitution, Black-Scholes, parabolic
**Author:** Claude Opus 4.6

---

## Definition

Many linear parabolic PDEs — including the Black-Scholes equation — can be **reduced to the heat equation** via an exponential substitution. This is valuable because the heat equation has well-known analytical solutions (Gaussian kernels), so reducing to it gives access to closed-form results.

The technique works on any PDE of the form:

$$\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2} + a\frac{\partial u}{\partial x} + bu$$

where $a$ and $b$ are constants. The goal is to eliminate the first-order and zeroth-order terms, leaving the pure heat equation.

## Key Formula

**The substitution:**

$$u(x, t) = e^{\alpha x + \beta t}\,v(x, t)$$

Substituting into the PDE and choosing $\alpha$ and $\beta$ to kill the unwanted terms:

$$\alpha = -\frac{a}{2}, \qquad \beta = b - \frac{a^2}{4}$$

**The result:**

$$\frac{\partial v}{\partial t} = \frac{\partial^2 v}{\partial x^2}$$

This is the **heat equation** — one of the most studied PDEs in mathematics.

## Example

Consider $\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2} + 3\frac{\partial u}{\partial x} - 2u$, so $a = 3$ and $b = -2$.

Compute the substitution parameters:

$$\alpha = -\frac{3}{2}, \qquad \beta = -2 - \frac{9}{4} = -\frac{17}{4}$$

Set $u(x, t) = e^{-\frac{3}{2}x - \frac{17}{4}t}\,v(x, t)$. Then $v$ satisfies the heat equation $v_t = v_{xx}$, whose solution with initial data $v(x, 0)$ is:

$$v(x, t) = \frac{1}{\sqrt{4\pi t}} \int_{-\infty}^{\infty} v(\xi, 0)\,e^{-(x - \xi)^2 / 4t}\,d\xi$$

## Remember

- This substitution is the **key trick behind the Black-Scholes closed-form solution**. After changing variables from $(S, t)$ to $(x, \tau)$ using $S = Ke^x$ and $\tau = T - t$, the Black-Scholes PDE becomes a linear parabolic PDE with constant coefficients, which the exponential substitution reduces to the heat equation.
- The heat equation's solution is a convolution with the **Gaussian kernel** $\frac{1}{\sqrt{4\pi t}}e^{-x^2/4t}$ — this is why the Black-Scholes formula involves the cumulative normal distribution $N(d_1)$ and $N(d_2)$.
- The same reduction technique applies to bond pricing PDEs (Vasicek, Hull–White) and any other linear parabolic PDE with constant coefficients encountered in quantitative finance.
