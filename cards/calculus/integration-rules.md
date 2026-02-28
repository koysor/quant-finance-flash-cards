# Integration Rules

**Topic:** Calculus
**Tags:** calculus, integration, antiderivative, substitution, by-parts
**Created:** 2026-02-28 20:46:20
**Author:** Claude Opus 4.6

---

## Definition

Integration is the reverse of differentiation. It finds the **accumulated quantity** — the area under a curve — given a rate of change. An **indefinite integral** yields a family of antiderivatives (plus a constant $C$), while a **definite integral** evaluates the net signed area between two bounds. In finance, integration converts densities into probabilities, continuous cash-flow rates into present values, and payoff functions into option prices.

## Key Formula

**Power rule** (for $n \neq -1$):

$$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$$

**Substitution** (reverse chain rule) — if $u = g(x)$:

$$\int f\bigl(g(x)\bigr) \, g'(x) \, dx = \int f(u) \, du$$

**Integration by parts** (reverse product rule):

$$\int u \, dv = uv - \int v \, du$$

**Definite integral** (Fundamental Theorem of Calculus):

$$\int_a^b f(x) \, dx = F(b) - F(a), \qquad \text{where } F'(x) = f(x)$$

**Common antiderivatives:**

| Function | Integral |
|---|---|
| $e^{ax}$ | $\frac{1}{a} e^{ax} + C$ |
| $\frac{1}{x}$ | $\ln\lvert x \rvert + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sin x$ | $-\cos x + C$ |

## Example

Evaluate $\displaystyle \int_0^1 x \, e^{x^2} \, dx$ using substitution.

**Step 1 — choose substitution:** Let $u = x^2$, so $du = 2x \, dx$, hence $x \, dx = \tfrac{1}{2} \, du$.

**Step 2 — change bounds:** when $x = 0$, $u = 0$; when $x = 1$, $u = 1$.

**Step 3 — rewrite and integrate:**

$$\int_0^1 x \, e^{x^2} \, dx = \frac{1}{2} \int_0^1 e^u \, du = \frac{1}{2} \bigl[ e^u \bigr]_0^1 = \frac{1}{2}(e - 1) \approx 0.8591$$

## Remember

- The **cumulative distribution function** $F(x) = \int_{-\infty}^{x} f(t) \, dt$ is an integral of the probability density — every probability you compute from a continuous distribution is an integration problem.
- The **present value of a continuous cash-flow stream** $c(t)$ discounted at rate $r$ is $PV = \int_0^T c(t) \, e^{-rt} \, dt$ — the continuous analogue of summing discounted discrete payments.
- The **Black-Scholes call price** is derived by integrating the discounted payoff $\max(S_T - K, 0)$ over the risk-neutral lognormal density, which ultimately reduces to integrals of the standard normal CDF $\Phi(d)$.
- Integration by parts is the tool behind deriving the **Fokker-Planck equation**, which governs how probability densities evolve through time in diffusion models.
