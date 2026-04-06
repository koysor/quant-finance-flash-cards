# Linearity of Differentiation

**Topic:** Calculus
**Tags:** calculus, differentiation, linearity, superposition, derivatives
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

Differentiation is a **linear operator**: it preserves addition and scalar multiplication. If $f$ and $g$ are differentiable functions and $a$, $b$ are constants, then the derivative of any linear combination of $f$ and $g$ equals the same linear combination of their derivatives.

## Key Formula

$$\frac{d}{dx}\bigl[a\,f(x) + b\,g(x)\bigr] = a\,f'(x) + b\,g'(x)$$

Two special cases follow directly:

$$\frac{d}{dx}\bigl[c\,f(x)\bigr] = c\,f'(x) \qquad \text{(constant multiple rule)}$$

$$\frac{d}{dx}\bigl[f(x) + g(x)\bigr] = f'(x) + g'(x) \qquad \text{(sum rule)}$$

## Example

A portfolio value is modelled as $V(S) = 2S^3 - 5S + 7$, where $S$ is the asset price.

Using linearity:

$$V'(S) = 2 \cdot 3S^2 - 5 \cdot 1 + 0 = 6S^2 - 5$$

At $S = 10$: $V'(10) = 6(100) - 5 = 595$.

Each term is differentiated independently — no term "interferes" with the others.

## Remember

Linearity of differentiation underlies the additivity of the Greeks: the delta of a portfolio is the sum of the deltas of its individual positions. If you hold $a$ units of option $A$ and $b$ units of option $B$, the portfolio delta is $a\,\Delta_A + b\,\Delta_B$, which makes hedging calculations straightforward and scalable.
