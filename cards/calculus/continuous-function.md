# Continuous Function

**Topic:** Calculus
**Tags:** continuity, limits, differentiability, option pricing, smooth payoffs, piecewise
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A function $f$ is **continuous at a point** $x = a$ if three conditions hold: $f(a)$ is defined, $\lim_{x \to a} f(x)$ exists, and the limit equals the function value:

$$\lim_{x \to a} f(x) = f(a)$$

A function is **continuous on an interval** if it is continuous at every point in that interval. Intuitively, a continuous function can be drawn without lifting the pen — there are no jumps, holes, or vertical asymptotes.

## Key Formula

**Three conditions for continuity at $a$:**

1. $f(a)$ is defined
2. $\lim_{x \to a} f(x)$ exists (left and right limits are equal)
3. $\lim_{x \to a} f(x) = f(a)$

**Relationship to differentiability:**

$$f \text{ differentiable at } a \implies f \text{ continuous at } a$$

The converse is false: $|x|$ is continuous everywhere but not differentiable at $x = 0$.

**Intermediate Value Theorem:** if $f$ is continuous on $[a,b]$ and $f(a) \neq f(b)$, then $f$ takes every value between $f(a)$ and $f(b)$ — in particular, if $f(a)$ and $f(b)$ have opposite signs, there exists $c \in (a,b)$ with $f(c) = 0$.

## Example

The European call payoff $C_T = \max(S_T - K, 0)$ is **continuous** in $S_T$ — there is no jump at the strike — but it is **not differentiable** at $S_T = K$ (the kink). The Black-Scholes solution smooths this kink for $T > 0$: the option price $C(S, t)$ is infinitely differentiable in $S$ away from expiry, even though the terminal payoff has a corner.

By contrast, a **digital (binary) call** pays 1 if $S_T > K$ and 0 otherwise — it is **discontinuous** at the strike, creating a much harder numerical problem because the payoff cannot be resolved on a finite grid without special treatment.

## Remember

Continuity is the minimum smoothness required for the Intermediate Value Theorem to guarantee that root-finding algorithms (bisection, Newton-Raphson) will converge to a solution. In quantitative finance, **implied volatility** is a continuous function of option price (since Black-Scholes vega is always positive), so bisection is guaranteed to find $\sigma_{\text{imp}}$ given any valid market price. Discontinuous payoffs (digitals, one-touch barriers) require special numerical handling — smoothing, mesh refinement, or analytic adjustments — precisely because the standard convergence guarantees fail at the discontinuity.
