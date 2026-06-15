# Riemann Sum

**Topic:** Calculus
**Tags:** riemann sum, numerical integration, discretisation, definite integral, approximation
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **Riemann sum** approximates the area under a curve by partitioning an interval $[a, b]$ into $n$ subintervals and replacing the function on each subinterval with a constant — the function's value at the left endpoint, right endpoint, or midpoint. As $n \to \infty$ and the subinterval widths shrink to zero, the sum converges to the definite integral.

## Key Formula

For a uniform partition with step $h = (b - a)/n$ and nodes $x_i = a + ih$:

**Left Riemann sum:**
$$L_n = h\sum_{i=0}^{n-1} f(x_i)$$

**Right Riemann sum:**
$$R_n = h\sum_{i=1}^{n} f(x_i)$$

The error is $O(h)$ for left/right rules and $O(h^2)$ for the midpoint rule. Convergence requires:

$$\int_a^b f(x)\,dx = \lim_{n \to \infty} L_n = \lim_{n \to \infty} R_n$$

## Example

Approximate $\int_0^1 e^x\,dx$ with a left Riemann sum using $n = 4$ equal subintervals ($h = 0.25$):

$$L_4 = 0.25\,(e^{0} + e^{0.25} + e^{0.5} + e^{0.75}) = 0.25\,(1.000 + 1.284 + 1.649 + 2.117) = 1.513$$

Exact value: $e - 1 \approx 1.718$. The error is $0.205$, which halves each time $n$ doubles — confirming $O(h)$ convergence.

## Remember

Monte Carlo simulation is a **randomised Riemann sum**: each simulated path contributes one rectangle of height $f(\omega_i)$ and "width" $1/n$, so the sample mean $\hat{\mu} = n^{-1}\sum_i f(\omega_i)$ is exactly a Riemann sum with randomly placed nodes. The deterministic Riemann sum converges at rate $O(1/n)$; Monte Carlo converges at the slower rate $O(1/\sqrt{n})$ but works in high dimensions where regular grids are impractical — the key trade-off in numerical integration for derivatives pricing.
