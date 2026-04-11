# Composite Functions

**Topic:** Calculus
**Tags:** composite functions, composition, f of g, domain, chain rule, function
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **composite function** $f \circ g$ (read "f of g") applies $g$ first, then $f$ to the result: $(f \circ g)(x) = f(g(x))$. The output of $g$ becomes the input of $f$, so $g$'s range must be a subset of $f$'s domain. Composition is generally **not commutative**: $f \circ g \neq g \circ f$ in general.

## Key Formula

$$(f \circ g)(x) = f(g(x))$$

**Domain of $f \circ g$:** $\{x \in \text{dom}(g) : g(x) \in \text{dom}(f)\}$

**Derivative via the chain rule:**

$$(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$$

**Inverse undoes composition:** $f^{-1} \circ f = \text{id}$, so $(f^{-1} \circ f)(x) = x$.

**Iteration:** $f^n = f \circ f \circ \cdots \circ f$ ($n$ times).

## Example

Let $f(x) = \ln x$ (domain $x > 0$) and $g(x) = x^2 + 1$.

$(f \circ g)(x) = \ln(x^2 + 1)$. Domain: all $x \in \mathbb{R}$ since $x^2 + 1 > 0$ always.

$(g \circ f)(x) = (\ln x)^2 + 1$. Domain: $x > 0$.

Derivative: $(f \circ g)'(x) = \frac{1}{x^2+1} \cdot 2x = \frac{2x}{x^2+1}$.

Note $f \circ g \neq g \circ f$: $\ln(x^2+1) \neq (\ln x)^2 + 1$.

## Remember

Composite functions appear throughout quantitative finance wherever **one model feeds into another**. The Black-Scholes formula computes $\text{price} = f(g(S, K, T, r, \sigma))$ — first the $d_1, d_2$ expressions (inner function $g$), then the normal CDF (outer function $f$). The chain rule for composites is the reason the **Greeks chain**: $\partial \text{price}/\partial S$ requires differentiating the outer (normal CDF) times the inner derivative $\partial d_1/\partial S$. Risk model pipelines are another instance: raw returns → factor returns → portfolio P&L is a composition of linear maps, and the total derivative is the product of the Jacobians.
