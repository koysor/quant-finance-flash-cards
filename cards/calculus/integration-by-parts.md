# Integration by Parts

**Topic:** Calculus
**Tags:** calculus, integration, by-parts, product rule, option pricing, probability
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

Integration by parts is a technique for evaluating integrals of products of functions. It is the integral counterpart of the product rule for differentiation: if one factor is easier to differentiate and the other is easier to integrate, the technique converts a hard integral into a simpler one.

## Key Formula

Choose $u$ and $dv$ from the integrand, then apply:

$$\int u \, dv = uv - \int v \, du$$

where $du = u'(x) \, dx$ and $v = \int dv$.

For a definite integral over $[a, b]$:

$$\int_a^b u \, dv = \bigl[uv\bigr]_a^b - \int_a^b v \, du$$

**LIATE rule** (choose $u$ in this priority order): **L**ogarithmic, **I**nverse trig, **A**lgebraic, **T**rigonometric, **E**xponential.

## Example

Evaluate $\displaystyle \int_0^\infty x \, e^{-rx} \, dx$ — the expected time to payment when $x$ is exponentially distributed with rate $r > 0$.

**Step 1 — assign parts:** Let $u = x$ and $dv = e^{-rx} \, dx$, so $du = dx$ and $v = -\tfrac{1}{r} e^{-rx}$.

**Step 2 — apply the formula:**

$$\int_0^\infty x \, e^{-rx} \, dx = \Bigl[-\frac{x}{r} e^{-rx}\Bigr]_0^\infty + \frac{1}{r} \int_0^\infty e^{-rx} \, dx$$

**Step 3 — evaluate:** The boundary term vanishes (since $x \, e^{-rx} \to 0$ as $x \to \infty$), giving:

$$= \frac{1}{r} \cdot \frac{1}{r} = \frac{1}{r^2}$$

So the mean of an exponential distribution with rate $r$ is $1/r$.

## Remember

Integration by parts appears in several key quant finance derivations. Pricing a European call requires integrating $\max(S_T - K, 0)$ against the risk-neutral density; integration by parts converts that expression into $S_0 \Phi(d_1) - K e^{-rT} \Phi(d_2)$, the familiar Black-Scholes formula. It also underpins the derivation of the Fokker-Planck equation, where integration by parts shifts spatial derivatives from the probability density onto test functions to obtain the forward equation governing how option prices evolve.
