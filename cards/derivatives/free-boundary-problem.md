# Free Boundary Problem

**Topic:** Derivatives
**Tags:** free boundary problem, american option, optimal stopping, linear complementarity, real options, pde
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **free boundary problem** is a PDE problem in which part of the domain boundary is unknown and must be determined as part of the solution. In quantitative finance, free boundary problems arise whenever a decision-maker acts optimally at a threshold that depends on the current state — the threshold is free to move and must be found simultaneously with the value function.

## Key Formula

The general finance free boundary problem on a domain $\Omega(t)$ with free boundary $\partial\Omega^*(t)$:

$$\mathcal{L}V = 0 \quad \text{in the continuation region } \Omega(t)$$

$$V = h \quad \text{on the fixed boundary } \partial\Omega$$

At the **free boundary** $\partial\Omega^*(t)$, two conditions must both hold:

$$V\big|_{\partial\Omega^*} = h\big|_{\partial\Omega^*} \quad\text{(value matching)}$$

$$\nabla V\big|_{\partial\Omega^*} = \nabla h\big|_{\partial\Omega^*} \quad\text{(smooth pasting)}$$

These two conditions together determine both $V$ and the location of $\partial\Omega^*$. Equivalently, the whole problem can be written as the **linear complementarity problem**: $\min(\mathcal{L}V,\; V - h) = 0$.

## Example

The same mathematical structure governs several distinct financial problems:

| Problem | Decision | Free boundary |
|---------|----------|---------------|
| American put | Exercise | Critical stock price $S^*(t)$ |
| Callable bond | Issuer calls | Interest rate threshold $r^*(t)$ |
| Real option: invest | Invest now | Project value threshold $V^*$ |
| Merton optimal dividends | Pay dividend | Cash reserve level $x^*$ |

For the American put with $K = 100$, $r = 5\%$, $\sigma = 25\%$, the free boundary at 6 months to expiry is $S^*(0.5) \approx \pounds80$: the option satisfies the PDE for $S > 80$ and equals $100 - S$ for $S \leq 80$.

## Remember

The free boundary structure is the unifying mathematical idea behind seemingly unrelated finance decisions. A portfolio manager deciding when to harvest a tax loss, a firm deciding when to default, and an investor deciding when to exercise an American put are all solving the same class of problem — find the threshold, then the value follows. The practical consequence is that any pricing model for an instrument with an embedded decision must solve a free boundary problem, either explicitly (PDE with projected iteration) or implicitly (Longstaff-Schwartz regression). Misidentifying the domain as fixed when it is free is the root cause of systematic mispricing in American-style options.
