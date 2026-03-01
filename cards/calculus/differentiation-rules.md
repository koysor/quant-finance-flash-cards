# Differentiation Rules

**Topic:** Calculus
**Tags:** calculus, differentiation, derivatives

---

## Definition

Differentiation finds the **instantaneous rate of change** of a function. In finance, derivatives (the mathematical kind) of functions appear everywhere — from option pricing sensitivities (the Greeks) to optimisation.

## Key Formula

$$\frac{d}{dx}[x^n] = nx^{n-1} \qquad \frac{d}{dx}[c] = 0$$

$$\frac{d}{dx}[f + g] = f' + g' \qquad \frac{d}{dx}[fg] = f'g + fg'$$

$$\frac{d}{dx}\!\left[\frac{f}{g}\right] = \frac{f'g - fg'}{g^2} \qquad \frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$$

Common functions:

$$\frac{d}{dx}[e^x] = e^x \qquad \frac{d}{dx}[\ln x] = \frac{1}{x}$$

$$\frac{d}{dx}[\sin x] = \cos x \qquad \frac{d}{dx}[\cos x] = -\sin x$$

## Example

Differentiate $f(x) = e^{-x^2}$ using the chain rule.

Let $u = -x^2$, so $f = e^u$.

$$f'(x) = e^u \cdot (-2x) = -2x \, e^{-x^2}$$

At $x = 1$: $f'(1) = -2 \times e^{-1} \approx -0.736$.

This derivative appears in the normal distribution PDF.

## Remember

- The **chain rule** is essential for differentiating composite functions — used constantly when working with the Black-Scholes formula and the Greeks.
- **Delta** ($\Delta$) of an option is the partial derivative of the option price with respect to the underlying asset price: $\Delta = \partial V / \partial S$.
