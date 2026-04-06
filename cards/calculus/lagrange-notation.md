# Lagrange Notation

**Topic:** Calculus
**Tags:** calculus, differentiation, notation, derivatives, higher-order derivatives
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

Lagrange notation expresses derivatives using prime symbols — $f'(x)$, $f''(x)$, $f'''(x)$ — rather than the $\frac{d}{dx}$ symbol introduced by Leibniz. It is compact and convenient for writing higher-order derivatives and is widely used in optimisation and function analysis.

## Key Formula

First derivative (rate of change):

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

Higher-order derivatives:

$$f''(x) = \frac{d^2 f}{dx^2}, \qquad f'''(x) = \frac{d^3 f}{dx^3}, \qquad f^{(n)}(x) = \frac{d^n f}{dx^n}$$

The prime notation and Leibniz notation are interchangeable:

$$f'(x) \equiv \frac{df}{dx}, \qquad f''(x) \equiv \frac{d^2 f}{dx^2}$$

## Example

Let $f(x) = x^3 - 4x^2 + 5$.

$$f'(x) = 3x^2 - 8x$$

$$f''(x) = 6x - 8$$

To find the minimum, set $f'(x) = 0$: $3x^2 - 8x = 0 \Rightarrow x(3x - 8) = 0$, so $x = 0$ or $x = \tfrac{8}{3}$.

Check second-order condition: $f''(\tfrac{8}{3}) = 6 \times \tfrac{8}{3} - 8 = 16 - 8 = 8 > 0$, confirming a local minimum at $x = \tfrac{8}{3}$.

## Remember

In quantitative finance, Lagrange notation appears in the **second-order condition for portfolio optimisation**. When minimising portfolio variance $\sigma_p^2(w)$ with respect to weights $w$, the first-order condition $\sigma_p'(w) = 0$ identifies the critical point, and the second-order condition $\sigma_p''(w) > 0$ confirms it is a minimum rather than a maximum. The prime notation is also used when writing the **Taylor expansion of an option price** compactly: $V(S + \Delta S) \approx V(S) + V'(S)\,\Delta S + \tfrac{1}{2}V''(S)\,(\Delta S)^2$, where $V'(S) = \Delta$ (Delta) and $V''(S) = \Gamma$ (Gamma).
