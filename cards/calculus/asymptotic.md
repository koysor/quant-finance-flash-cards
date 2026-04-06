# Asymptotic

**Topic:** Calculus
**Tags:** asymptote, asymptotic, limits, tail behaviour, option pricing, large strike
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

An **asymptote** is a line (or curve) that a function approaches arbitrarily closely but never reaches. A function is **asymptotic** to a line $y = L$ if $\lim_{x \to \infty} f(x) = L$ (horizontal asymptote) or to $x = a$ if $\lim_{x \to a} f(x) = \pm\infty$ (vertical asymptote). **Asymptotic analysis** studies the behaviour of functions in limiting regimes.

## Key Formula

**Horizontal asymptote:** $\lim_{x \to \pm\infty} f(x) = L$

**Vertical asymptote:** $\lim_{x \to a^\pm} f(x) = \pm\infty$

**Asymptotic equivalence:** $f(x) \sim g(x)$ as $x \to a$ means $\lim_{x \to a} \frac{f(x)}{g(x)} = 1$

**Asymptotic expansion** — approximating $f$ for large $x$:

$$f(x) \sim a_0 + \frac{a_1}{x} + \frac{a_2}{x^2} + \cdots \quad \text{as } x \to \infty$$

**Lee's moment formula** (large-strike asymptotic for implied vol $\sigma_{\text{imp}}$):

$$\sigma_{\text{imp}}^2(k) \sim \frac{|k|}{T} \quad \text{as } k = \ln(K/F) \to \pm\infty$$

where the slope of $\sigma_{\text{imp}}^2$ against log-moneyness $|k|$ is bounded above by the moment index of the distribution.

## Example

The Black-Scholes call price has two asymptotes:

As $S \to 0$: $C \to 0$ (horizontal asymptote at zero — deep out-of-the-money call is worthless).

As $S \to \infty$: $C \sim S - Ke^{-rT}$ (the call price approaches the forward price minus the discounted strike — it behaves like a forward contract when deep in-the-money).

These two asymptotic regimes define the boundary conditions for numerical PDE solvers — the grid must be large enough that the asymptotic approximation is accurate at the boundaries.

## Remember

Asymptotic analysis is the standard tool for validating option pricing models at the extremes of strike and maturity. **Roger Lee's moment formula** links the large-strike behaviour of the implied volatility smile to the moments of the risk-neutral distribution — if the $p$-th moment of $S_T$ is finite, the smile cannot grow faster than $\sqrt{|k|}$ at large log-strikes. This gives a model-free constraint on any implied vol surface: checking that the wings decay at the correct asymptotic rate is a standard arbitrage check for calibrated models.
