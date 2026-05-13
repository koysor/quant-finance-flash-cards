# Automatic Differentiation

**Topic:** Computational Finance
**Tags:** automatic differentiation, adjoint, AAD, greeks, machine learning, backpropagation
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

Automatic differentiation (AD) computes exact derivatives of any function implemented in code, to machine precision, by systematically applying the chain rule to each arithmetic operation. It is not symbolic differentiation (algebraic) nor finite differences (approximate) — it works directly on the numerical computation graph and is exact up to floating-point precision.

## Key Formula

For a function $f: \mathbb{R}^n \to \mathbb{R}^m$ computed as a sequence of elementary operations, the chain rule gives the Jacobian. Two modes exist:

**Forward mode** — propagates derivative alongside the primal computation:

$$\dot{v}_i = \frac{\partial v_i}{\partial x_j} \quad \text{(cost: } n \text{ forward passes for } n \text{ inputs)}$$

**Reverse mode (adjoint / backpropagation)** — propagates sensitivity backwards from output:

$$\bar{v}_i = \frac{\partial f}{\partial v_i} \quad \text{(cost: 1 forward + 1 backward pass, regardless of } n\text{)}$$

For $f: \mathbb{R}^n \to \mathbb{R}$ (a scalar loss or P&L), reverse mode computes **all** $n$ partial derivatives in a single backward pass — $O(1)$ cost vs $O(n)$ for finite differences.

**Python (JAX):**

```python
import jax
import jax.numpy as jnp

def bs_call(params):
    S, K, r, sigma, T = params
    d1 = (jnp.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*jnp.sqrt(T))
    d2 = d1 - sigma*jnp.sqrt(T)
    from jax.scipy.stats import norm
    return S*norm.cdf(d1) - K*jnp.exp(-r*T)*norm.cdf(d2)

greeks = jax.grad(bs_call)([100., 100., 0.05, 0.20, 1.0])
# Returns [delta, -delta_K, rho, vega, theta] simultaneously
```

## Example

A bank's XVA engine computes sensitivities of a £10bn portfolio's credit valuation adjustment (CVA) to 500 market risk factors. Finite differences require 500 re-pricings per scenario. Adjoint AD (AAD) computes all 500 sensitivities in a **single backward pass** — the same cost as one forward pricing. Banks including Goldman Sachs and Barclays have rebuilt risk engines around AAD, reducing daily Greeks computation from hours to minutes.

## Remember

AAD is the reason that deep learning is computationally feasible — backpropagation is simply reverse-mode automatic differentiation applied to neural network loss functions. In quantitative finance, AAD is replacing Monte Carlo Greeks and finite-difference bumping for XVA, SIMM (ISDA initial margin), and regulatory capital sensitivities. The key constraint is **memory**: reverse mode must store the entire forward computation graph to backpropagate, which can be prohibitive for long Monte Carlo paths — checkpointing strategies trade memory for recomputation time.
