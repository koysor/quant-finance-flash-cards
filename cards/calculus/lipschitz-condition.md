# Lipschitz Condition

**Topic:** Calculus
**Tags:** lipschitz, continuity, ode, existence uniqueness, sde
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

A function $f$ satisfies a **Lipschitz condition** with constant $L > 0$ if the absolute change in output is uniformly bounded by $L$ times the absolute change in input, for all points in the domain. It is a uniform continuity condition that prevents the function from having arbitrarily steep slopes, and is the key hypothesis guaranteeing that differential equations have unique solutions.

## Key Formula

$$\lvert f(x) - f(y) \rvert \leq L \lvert x - y \rvert \quad \text{for all } x, y \in \text{dom}(f)$$

Every differentiable function with bounded derivative is Lipschitz: if $\lvert f'(x) \rvert \leq L$ for all $x$, then by the mean value theorem, $\lvert f(x) - f(y) \rvert \leq L \lvert x - y \rvert$.

The **Picard–Lindelöf theorem** states that if $f(t, x)$ is Lipschitz in $x$, the ODE $\dot{x} = f(t, x)$ has a unique local solution.

## Example

$f(x) = x^2$ is **not** globally Lipschitz: for $x = n$, $y = n + 1$, $\lvert f(x) - f(y) \rvert = 2n + 1$, which grows without bound. However, $f(x) = x^2$ **is** Lipschitz on any bounded interval $[-M, M]$ with constant $L = 2M$.

$f(x) = \sqrt{x}$ is not Lipschitz near $x = 0$: the derivative $\frac{1}{2\sqrt{x}} \to \infty$ as $x \to 0$.

$f(x) = \sigma x$ (linear, as in Black–Scholes diffusion) is globally Lipschitz with $L = \lvert \sigma \rvert$.

## Remember

In quantitative finance, the Lipschitz condition is what makes Black–Scholes and Vasicek SDEs mathematically well-posed. The coefficients $\mu(S) = \mu S$ and $\sigma(S) = \sigma S$ of GBM are locally Lipschitz (and satisfy a linear growth condition), guaranteeing a unique strong solution via the Picard–Lindelöf–type theorem for SDEs. When a practitioner proposes a novel SDE for volatility or rates, verifying Lipschitz continuity of its coefficients is the first check confirming the model is internally consistent.
