# Linear Equation

**Topic:** Calculus
**Tags:** linear equation, straight line, gradient, intercept, regression, yield curve
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A **linear equation** in one variable has the form $ax + b = 0$ with $a \neq 0$, and has exactly one solution $x = -b/a$. In two variables it defines a straight line: $y = mx + c$, where $m$ is the **gradient** (slope) and $c$ is the **$y$-intercept**. The relationship between $x$ and $y$ is proportional — equal changes in $x$ produce equal changes in $y$.

## Key Formula

**Slope-intercept form:**

$$y = mx + c$$

**Gradient** between two points $(x_1, y_1)$ and $(x_2, y_2)$:

$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$$

**Solution** of $ax + b = 0$:

$$x = -\frac{b}{a}$$

**General form:** $ax + by + c = 0$, where not both $a$ and $b$ are zero.

## Example

A simple linear yield curve model assumes that the spot rate rises linearly with maturity:

$$r(T) = 0.02 + 0.005 \cdot T$$

At $T = 2$: $r = 0.03$; at $T = 5$: $r = 0.045$. The gradient $m = 0.005$ means the yield increases by 50 basis points per year of additional maturity.

The price of a zero-coupon bond is $P = e^{-r(T) \cdot T}$, which is a non-linear function of $T$ even though the underlying rate model is linear.

## Remember

Simple linear regression fits the linear equation $y = \beta_0 + \beta_1 x$ to data by minimising the sum of squared residuals. In finance, this produces the **beta** of a stock — the slope $\beta_1$ of the regression of excess stock returns on excess market returns. A beta of 1.2 means a 1% market move is associated with a 1.2% stock move on average. The intercept $\beta_0$ is Jensen's alpha. Every factor model regression reduces to fitting linear equations, making this the most frequently used mathematical structure in empirical finance.
