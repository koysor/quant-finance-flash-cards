# Numerical Greeks by Finite Difference

**Topic:** Computational Finance
**Tags:** python, greeks, finite difference, delta, gamma, sensitivity
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Numerical Greeks** are option sensitivities computed by bumping an input parameter by a small amount and measuring the resulting change in price, rather than deriving an analytical formula. This finite-difference approach works for *any* pricing model — including Monte Carlo and PDE solvers where closed-form Greeks do not exist — making it the universal method on trading desks.

## Key Formula

**Central difference approximation:**

$$\Delta \approx \frac{V(S + h) - V(S - h)}{2h}$$

$$\Gamma \approx \frac{V(S + h) - 2V(S) + V(S - h)}{h^2}$$

**Python implementation:**

```python
def numerical_delta(pricer, S, h=0.01):
    return (pricer(S + h) - pricer(S - h)) / (2 * h)

def numerical_gamma(pricer, S, h=0.01):
    return (pricer(S + h) - 2 * pricer(S) + pricer(S - h)) / h**2
```

## Example

Compute delta and gamma for a European call using a Black-Scholes pricer:

```python
pricer = lambda S: bs_call(S, K=100, r=0.05, sigma=0.20, T=1.0)

delta = numerical_delta(pricer, S=100, h=0.50)
gamma = numerical_gamma(pricer, S=100, h=0.50)
# delta ≈ 0.637 (analytical: 0.637)
# gamma ≈ 0.019 (analytical: 0.019)
```

The bump size $h$ balances truncation error (large $h$) against floating-point noise (small $h$). For equity options, $h = £0.50$ is a common choice.

## Remember

On a real trading desk, most Greeks are computed numerically, not analytically. Analytical Greeks exist only for simple models (Black-Scholes, Bachelier); exotic products priced by Monte Carlo or PDE methods have no closed-form sensitivities. The finite-difference approach is model-agnostic: the same bumping code works whether the underlying pricer is Black-Scholes, Heston, or a full Monte Carlo engine. The main cost is that each Greek requires re-pricing — delta needs two extra pricings, a full set of Greeks (delta, gamma, vega, theta, rho) needs roughly ten — so efficient pricer implementation is essential. Central differences are preferred over forward differences because the error is $O(h^2)$ rather than $O(h)$.
