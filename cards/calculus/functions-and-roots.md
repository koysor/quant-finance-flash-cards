# Functions and Roots

**Topic:** Calculus
**Tags:** function, root, zero, domain, range, f(x), composite function
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **function** $f: A \to B$ assigns to each element of the domain $A$ exactly one element of the codomain $B$. A **root** (or zero) of $f$ is a value $x$ in the domain such that $f(x) = 0$. Finding roots is the core problem in equation solving and numerical methods.

## Key Formula

**Function composition:** $(g \circ f)(x) = g(f(x))$ — apply $f$ first, then $g$.

**Root-finding condition:** $f(x) = 0$.

**Fundamental Theorem of Algebra:** a polynomial of degree $n$ has exactly $n$ roots in $\mathbb{C}$ (counting multiplicity).

**Sign-change rule (IVT):** if $f$ is continuous and $f(a) < 0 < f(b)$, then $f$ has at least one root in $(a, b)$.

## Example

Let $f(x) = x^3 - x - 1$.

Check: $f(1) = -1 < 0$ and $f(2) = 5 > 0$.

By the Intermediate Value Theorem, $f$ has a root in $(1, 2)$.

Newton-Raphson from $x_0 = 1.5$: $x_1 = 1.5 - f(1.5)/f'(1.5) = 1.5 - (0.875)/(5.75) \approx 1.3478$.

Continuing converges to $x \approx 1.3247$.

## Remember

Root-finding is central to derivative pricing: **implied volatility** is the root of the equation $\text{Black-Scholes}(\sigma) - \text{market price} = 0$. Given a traded option price and the Black-Scholes formula as $f(\sigma)$, finding $\sigma_\text{impl}$ is a one-dimensional root-finding problem. The sign-change bracketing (IVT) locates an initial interval; Newton-Raphson or Brent's method converges to the implied vol. Every Bloomberg terminal applies this root-finding algorithm billions of times daily to compute the implied volatility surface.
