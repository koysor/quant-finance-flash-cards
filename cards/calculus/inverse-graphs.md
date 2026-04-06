# Inverse Graphs

**Topic:** Calculus
**Tags:** inverse function, graph, reflection, symmetry, y=x line, logarithm, exponential
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The graph of $y = f^{-1}(x)$ is obtained by reflecting the graph of $y = f(x)$ in the line $y = x$. This swaps the roles of $x$ and $y$: every point $(a, b)$ on $y = f(x)$ maps to the point $(b, a)$ on $y = f^{-1}(x)$.

## Key Formula

**Reflection principle:** $(a, b) \in y = f(x) \iff (b, a) \in y = f^{-1}(x)$

**Geometric interpretation:** the line $y = x$ is the axis of symmetry between a function and its inverse.

**Key example pair:** $y = e^x$ and $y = \ln x$ are reflections of each other in $y = x$.

The domain restriction required for the inverse to exist appears graphically as the region where the original function passes the horizontal line test.

## Example

Reflect $y = e^x$ in $y = x$:

- The point $(0, 1)$ on $y = e^x$ maps to $(1, 0)$ on the inverse.
- The point $(1, e)$ maps to $(e, 1)$.
- The resulting curve is $y = \ln x$, defined only for $x > 0$, confirming the domain-range swap.

The horizontal asymptote $y = 0$ of $e^x$ as $x \to -\infty$ becomes the vertical asymptote $x = 0$ of $\ln x$.

## Remember

The graph of the **normal CDF** $\Phi(x)$ and its inverse $\Phi^{-1}(p)$ (the quantile function) are reflections in $y = x$. This geometric symmetry has a direct financial interpretation: $\Phi(x)$ converts a standardised loss $x$ into a probability $p$, while $\Phi^{-1}(p)$ converts a confidence level $p$ into a critical loss threshold. **Value at Risk** moves from the probability axis to the loss axis — it is a read-off of the inverse graph. The steepness of $\Phi^{-1}$ near $p = 1$ captures how rapidly the VaR threshold increases as confidence approaches certainty.
