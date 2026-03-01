# Fundamental Theorem of Calculus

**Topic:** Calculus
**Tags:** calculus, integration, antiderivative, FTC

---

## Definition

The Fundamental Theorem of Calculus (FTC) links the two central operations of calculus — differentiation and integration — and shows they are inverses of each other.

**Part 1 (Derivative of an Integral):** If $f$ is continuous on $[a, b]$ and we define

$$F(x) = \int_a^x f(t)\,dt$$

then $F$ is differentiable on $(a, b)$ and $F'(x) = f(x)$. In words, differentiating the integral recovers the original integrand.

**Part 2 (Evaluating a Definite Integral):** If $f$ is continuous on $[a, b]$ and $F$ is any antiderivative of $f$ (i.e. $F' = f$), then

$$\int_a^b f(x)\,dx = F(b) - F(a)$$

This transforms the problem of computing an area under a curve into simple evaluation of an antiderivative at two points.

## Key Formula

$$\frac{d}{dx}\int_a^x f(t)\,dt = f(x) \qquad \text{(Part 1)}$$

$$\int_a^b f(x)\,dx = F(b) - F(a), \quad F' = f \qquad \text{(Part 2)}$$

## Example

Evaluate $\displaystyle\int_1^3 2x\,dx$.

**Step 1 — Find an antiderivative:** Since $\frac{d}{dx}[x^2] = 2x$, we have $F(x) = x^2$.

**Step 2 — Apply Part 2:**

$$\int_1^3 2x\,dx = F(3) - F(1) = 3^2 - 1^2 = 9 - 1 = 8$$

**Verification via Part 1:** Define $G(x) = \int_1^x 2t\,dt$. By Part 1, $G'(x) = 2x$, confirming that differentiation undoes the integration.

## Remember

- The CDF is the integral of the PDF: $F_X(x) = \int_{-\infty}^{x} f_X(t)\,dt$, and by Part 1 we recover $f_X(x) = F_X'(x)$. This relationship underpins every probability calculation in quantitative finance.
- Continuous compounding uses the exponential integral. The accumulated return over $[0, T]$ satisfies $\ln\!\bigl(S(T)/S(0)\bigr) = \int_0^T r(t)\,dt$, and Part 2 lets us evaluate this when the instantaneous rate $r(t)$ has a known antiderivative.
- In Black-Scholes pricing, the option value is an integral over the risk-neutral density. Understanding that integration and differentiation are inverses is what lets us move freely between cumulative probabilities ($N(d_2)$) and the density ($n(d_2)$) when computing Greeks.
