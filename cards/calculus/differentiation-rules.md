# Differentiation Rules

**Topic:** Calculus
**Tags:** calculus, differentiation, derivatives
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

Differentiation finds the **instantaneous rate of change** of a function. In finance, derivatives (the mathematical kind) of functions appear everywhere — from option pricing sensitivities (the Greeks) to optimisation.

## Key Rules

| Rule | Formula |
|---|---|
| Power rule | d/dx [xⁿ] = nxⁿ⁻¹ |
| Constant | d/dx [c] = 0 |
| Sum rule | d/dx [f + g] = f' + g' |
| Product rule | d/dx [fg] = f'g + fg' |
| Quotient rule | d/dx [f/g] = (f'g − fg') / g² |
| Chain rule | d/dx [f(g(x))] = f'(g(x)) · g'(x) |

**Common functions:**

| Function | Derivative |
|---|---|
| eˣ | eˣ |
| ln(x) | 1/x |
| sin(x) | cos(x) |
| cos(x) | −sin(x) |

## Example (Chain Rule)

Differentiate f(x) = e^(−x²):

Let u = −x², so f = eᵘ.

f'(x) = eᵘ · (−2x) = **−2x · e^(−x²)**

This appears in the normal distribution PDF.

## Remember

- The **chain rule** is essential for differentiating composite functions — used constantly when working with the Black-Scholes formula and the Greeks.
- **Delta** (Δ) of an option is the partial derivative of the option price with respect to the underlying asset price: Δ = ∂V/∂S.
