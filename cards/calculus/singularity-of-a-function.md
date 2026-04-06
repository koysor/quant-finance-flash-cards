# Singularity of a Function

**Topic:** Calculus
**Tags:** singularity, discontinuity, limits, PDE, option pricing, boundary conditions
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

A **singularity** of a function is a point at which the function is not defined or ceases to behave in a regular, well-behaved manner. At a singularity, the function may blow up to infinity, oscillate without limit, or simply not exist. Singularities are classified as **removable** (the limit exists and is finite but the function is not defined there), **poles** (the function diverges to $\pm\infty$), or **essential** (the behaviour is more wildly irregular).

## Key Formula

**Pole of order $n$ at $x = a$:** the function behaves like

$$f(x) \sim \frac{c}{(x-a)^n} \quad \text{as } x \to a, \quad c \neq 0, \; n \in \mathbb{Z}^+$$

**Removable singularity:** $\lim_{x \to a} f(x) = L$ exists and is finite, but $f(a)$ is undefined. Redefining $f(a) = L$ removes it.

**Essential singularity:** neither of the above — e.g. $e^{1/x}$ at $x = 0$, where the function oscillates between 0 and $\infty$ depending on the direction of approach.

**Logarithmic singularity:** a weaker blow-up where $f(x) \sim c \ln|x - a|$ as $x \to a$.

## Example

The function $f(x) = \dfrac{1}{x(x-1)}$ has two poles, at $x = 0$ and $x = 1$. Near $x = 0$:

$$f(x) \approx -\frac{1}{x} \quad \text{as } x \to 0$$

so $f$ has a simple pole (order 1) there. Any numerical scheme that evaluates $f$ on a grid must avoid these points, and any definite integral $\int_0^1 f(x)\,\mathrm{d}x$ is improper and must be assessed for convergence before it can be used.

## Remember

The Black-Scholes PDE has a singularity at $S = 0$: the diffusion coefficient $\tfrac{1}{2}\sigma^2 S^2$ vanishes there, and the convection term $rS \,\partial V/\partial S$ also vanishes, turning the PDE into a degenerate problem at the lower boundary. This is why finite-difference solvers for Black-Scholes do **not** place a grid point at $S = 0$ but instead impose the boundary condition $V(0, t) = 0$ (for calls) analytically, stepping the numerical grid back from the singularity. Similarly, near expiry ($T - t \to 0$) the solution of the Black-Scholes PDE for a digital option develops a near-singular spike in Gamma around the strike, which is the numerical signature of the discontinuous payoff being smoothed by the parabolic operator — a finite but very large value rather than a true singularity.
