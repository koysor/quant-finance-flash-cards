# Modulus Transformations

**Topic:** Calculus
**Tags:** modulus, transformations, graph, absolute value, reflection, piecewise, payoff
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Modulus transformations** alter the graph of $y = f(x)$ using the absolute value. Two key transformations:

- $y = |f(x)|$: reflect any portion of the graph where $f(x) < 0$ above the $x$-axis.
- $y = f(|x|)$: replace the left half of the graph ($x < 0$) with a mirror of the right half.

## Key Formula

$$y = |f(x)|: \quad \text{keep } f(x) \text{ where } f(x) \geq 0; \text{ reflect where } f(x) < 0$$

$$y = f(|x|): \quad \text{set } y = f(x) \text{ for } x \geq 0; \text{ mirror about the } y\text{-axis for } x < 0$$

**Gradient at the fold:** $y = |f(x)|$ is not differentiable at points where $f(x) = 0$ and $f'(x) \neq 0$ — there is a corner (kink) in the graph at these points.

## Example

Sketch $y = |x^2 - 4|$.

The base curve $y = x^2 - 4$ is negative for $-2 < x < 2$. Apply $|\cdot|$: reflect this negative section upward.

Result: a curve that touches the $x$-axis at $x = \pm 2$, with a "W" shape — the central valley is folded up to a peak at $(0, 4)$.

## Remember

Option payoff diagrams are modulus transformations. A **call option** payoff $\max(S - K, 0)$ is the positive-part function, equivalent to $|f(S)|$ where $f(S) = S - K$, keeping only $f(S) \geq 0$. A **straddle** payoff — long a call and a put at the same strike — is $|S - K|$: the classic "V" shape of a modulus graph. Every structured product payoff diagram that has a kink, a fold, or a reflected section corresponds geometrically to a modulus transformation of a simpler curve.
