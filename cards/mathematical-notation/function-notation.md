# Function Notation

**Topic:** Mathematical Notation
**Tags:** notation, function, domain, codomain, inverse, composition, mapping
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

A **function** $f: X \to Y$ is a rule that assigns to each element of the **domain** $X$ exactly one element of the **codomain** $Y$. The notation specifies both the mapping rule and the sets it operates on:

| Symbol | Read as | Meaning |
|---|---|---|
| $f: X \to Y$ | "$f$ from $X$ to $Y$" | Function with domain $X$ and codomain $Y$ |
| $f: x \mapsto f(x)$ | "$f$ maps $x$ to $f(x)$" | The rule itself (lowercase arrow for elements) |
| $f(x)$ | "$f$ of $x$" or "$f$ at $x$" | The output when the input is $x$ |
| $f^{-1}: Y \to X$ | "f inverse" | The inverse function (if $f$ is bijective) |
| $f \circ g$ | "$f$ composed with $g$" | $(f \circ g)(x) = f(g(x))$ |
| $\text{im}(f)$ or $f(X)$ | "image of $f$" | The set of all outputs: $\{f(x) : x \in X\}$ |

The **arrow $\to$** connects sets; the **mapsto arrow $\mapsto$** connects elements.

## Key Formula

**Composition:**

$$(f \circ g)(x) = f(g(x)), \qquad (f \circ g)^{-1} = g^{-1} \circ f^{-1}$$

**Inverse function theorem** (local invertibility):

If $f: \mathbb{R} \to \mathbb{R}$ is differentiable and $f'(x_0) \neq 0$, then $f^{-1}$ exists near $x_0$ with:

$$\frac{d}{dy}f^{-1}(y) = \frac{1}{f'(f^{-1}(y))}$$

**Black-Scholes as a function:**

$$C: (S, K, T, r, \sigma) \mapsto S N(d_1) - Ke^{-rT}N(d_2)$$

## Example

**Implied volatility** is a function inversion problem: the Black-Scholes formula $C = \text{BS}(S, K, T, r, \sigma)$ defines a function $\text{BS}_\sigma: \sigma \mapsto C$ holding other inputs fixed. Given a market price $C^{\text{mkt}}$, implied vol is:

$$\sigma_{\text{imp}} = \text{BS}_\sigma^{-1}(C^{\text{mkt}})$$

This inverse does not have a closed form — Newton-Raphson is used to find it numerically, exploiting that $\partial C / \partial \sigma = \text{vega} > 0$ (the function is strictly increasing in $\sigma$).

## Remember

The function notation $f: X \to Y$ is more precise than $y = f(x)$ because it makes the **domain and codomain explicit**. In finance this matters: the Black-Scholes call price function $C: \mathbb{R}_{>0} \times \mathbb{R}_{>0} \times \mathbb{R}_{>0} \times \mathbb{R} \times \mathbb{R}_{>0} \to \mathbb{R}_{>0}$ tells you immediately that negative implied volatility is outside the codomain and therefore impossible. The **composition** $f \circ g$ appears whenever a model is applied in stages — for instance, a risk factor model composed with a pricing function gives a P&L function directly from factor shocks.
