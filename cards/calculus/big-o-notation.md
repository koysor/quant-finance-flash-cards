# Big-O Notation

**Topic:** Calculus
**Tags:** asymptotics, approximation, convergence, error bounds, numerical methods
**Created:** 2026-03-15
**Author:** Claude Opus 4.6

---

## Definition

Big-O notation describes an upper bound on how quickly a function grows (or shrinks) relative to another function as the argument tends to a limit. Writing $f(x) = O(g(x))$ as $x \to a$ means there exist constants $C > 0$ and $\delta > 0$ such that $|f(x)| \leq C\,|g(x)|$ for all $x$ satisfying $0 < |x - a| < \delta$. In quantitative finance it most commonly appears in truncation errors: when a Taylor expansion is cut after the quadratic term, the remainder is $O(h^3)$, meaning the error shrinks at least as fast as the cube of the step size.

## Key Formula

$$f(x) = O\bigl(g(x)\bigr) \text{ as } x \to a \;\;\Longleftrightarrow\;\; \exists\, C > 0,\;\delta > 0 \;\text{ such that }\; |f(x)| \leq C\,|g(x)| \;\;\forall\; 0 < |x - a| < \delta$$

A common application — the Taylor remainder:

$$f(x) = f(a) + f'(a)(x-a) + \tfrac{1}{2}f''(a)(x-a)^2 + O\bigl((x-a)^3\bigr)$$

## Example

Suppose we approximate $e^h$ by its second-order Taylor expansion around $h = 0$:

$$e^h \approx 1 + h + \tfrac{h^2}{2}$$

The exact error is $e^h - (1 + h + \tfrac{h^2}{2}) = \tfrac{h^3}{6} + \tfrac{h^4}{24} + \cdots$

For $h = 0.01$: the error is approximately $\tfrac{(0.01)^3}{6} \approx 1.667 \times 10^{-7}$.

We write this remainder as $O(h^3)$ because the dominant error term scales with the cube of $h$ — halving $h$ reduces the error roughly eightfold.

## Remember

Big-O notation is how practitioners communicate the accuracy of numerical schemes. When the Euler–Maruyama discretisation of a stochastic differential equation is described as having $O(\Delta t)$ weak convergence, it tells you that halving the time step roughly halves the pricing error — so you can judge whether the computational cost of a finer grid is worthwhile. Similarly, the Black–Scholes PDE solver's finite-difference error being $O(\Delta x^2)$ means doubling the spatial grid points cuts the error by a factor of four, guiding the trade-off between speed and accuracy in real-time options pricing.
