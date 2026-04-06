# Integration by Substitution

**Topic:** Calculus
**Tags:** calculus, integration, substitution, u-substitution, chain-rule, antiderivative
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

Integration by substitution (u-substitution) is a technique for evaluating integrals by replacing a complicated expression with a single new variable, simplifying the integrand into a recognisable form. It is the integration counterpart of the chain rule for differentiation: wherever you see a function composed with another function multiplied by the inner function's derivative, substitution will simplify the integral.

## Key Formula

Given $u = g(x)$, so $\dfrac{du}{dx} = g'(x)$ and therefore $du = g'(x)\,dx$:

$$\int f\!\bigl(g(x)\bigr)\,g'(x)\,dx = \int f(u)\,du$$

For a **definite integral**, the limits must be converted from $x$-values to $u$-values:

$$\int_{a}^{b} f\!\bigl(g(x)\bigr)\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$$

## Example

Evaluate the present value of a continuous cash-flow stream with exponentially decaying payments:

$$PV = \int_0^2 e^{-0.05t} \cdot (-0.05)\,e^{-0.05t}\,dt$$

Actually, consider the simpler integral $\displaystyle\int_0^T t\,e^{-\frac{t^2}{2\sigma^2}}\,dt$ which appears when computing expected shortfall over a volatility-weighted horizon with $\sigma = 1$, $T = 2$:

**Step 1 — choose substitution:** let $u = \dfrac{t^2}{2}$, so $du = t\,dt$.

**Step 2 — convert limits:** when $t = 0$, $u = 0$; when $t = 2$, $u = 2$.

**Step 3 — rewrite and integrate:**

$$\int_0^2 t\,e^{-t^2/2}\,dt = \int_0^2 e^{-u}\,du = \bigl[-e^{-u}\bigr]_0^2 = 1 - e^{-2} \approx 0.8647$$

## Remember

The Black-Scholes formula is derived by integrating the discounted call payoff $\max(S_T - K,\,0)$ over the risk-neutral lognormal density. The key step uses substitution to convert the integral into the form $\int e^{-z^2/2}\,dz$, which evaluates to the standard normal CDF $\Phi(d)$. Every time you see $\Phi(d_1)$ or $\Phi(d_2)$ in an option pricing formula, substitution is the mechanism that produced it.
