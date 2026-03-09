# Feynman–Kac Formula

**Topic:** Stochastic Processes
**Tags:** pde, expectation, risk-neutral pricing, black-scholes, stochastic calculus
**Created:** 2026-03-08
**Author:** Claude Sonnet 4.6

---

## Definition

The **Feynman–Kac formula** establishes that the solution to a certain class of parabolic PDEs can be represented as a conditional expectation of a functional of a stochastic process. It is the mathematical bridge between PDE methods and probabilistic (Monte Carlo) methods for pricing derivatives.

## Key Formula

Given the SDE $dX = \mu(X,t)\,dt + \sigma(X,t)\,dW$ and the PDE:

$$\frac{\partial u}{\partial t} + \mu(x,t)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(x,t)\frac{\partial^2 u}{\partial x^2} - r\,u = 0, \quad u(x,T) = \Phi(x)$$

the solution is:

$$u(x,t) = \mathbb{E}\!\left[e^{-r(T-t)}\,\Phi(X_T) \;\middle|\; X_t = x\right]$$

That is, the PDE solution equals the discounted expected terminal payoff along the SDE.

## Example

The Black-Scholes PDE for a European call (with $\mu = rS$, $\sigma_{\text{SDE}} = \sigma S$, discount $r$) satisfies the Feynman–Kac conditions exactly. The formula immediately gives:

$$C(S,t) = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}\!\left[\max(S_T - K,\, 0) \;\middle|\; S_t = S\right]$$

For $S = 100$, $K = 100$, $r = 5\%$, $\sigma = 20\%$, $T - t = 1$: this expectation evaluates (via the lognormal distribution of $S_T$) to the Black-Scholes price of approximately £10.45.

## Remember

Feynman–Kac is the reason that **solving a pricing PDE** and **running a Monte Carlo simulation** are two representations of the same answer. When the PDE is hard to solve analytically, simulate the SDE and average the discounted payoff. When simulation is noisy, switch to the PDE. Knowing which representation to use — and that they are provably equivalent — is a core skill in quantitative finance.
