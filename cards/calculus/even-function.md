# Even Function

**Topic:** Calculus
**Tags:** even function, symmetry, integration, Fourier transform, probability distributions
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A function $f$ is **even** if it is symmetric about the $y$-axis: $f(-x) = f(x)$ for all $x$ in its domain. The graph of an even function is a mirror image of itself when reflected in the vertical axis. In contrast, an **odd** function satisfies $f(-x) = -f(x)$ and is symmetric about the origin.

## Key Formula

**Symmetry condition:**

$$f(-x) = f(x) \quad \text{for all } x$$

**Integration over a symmetric interval** — the most important consequence:

$$\int_{-a}^{a} f(x)\, dx = 2\int_{0}^{a} f(x)\, dx \qquad (f \text{ even})$$

$$\int_{-a}^{a} g(x)\, dx = 0 \qquad (g \text{ odd})$$

Common even functions: $x^2,\; x^4,\; |x|,\; \cos x,\; e^{-x^2}$

A general function decomposes uniquely into even and odd parts:

$$f(x) = \underbrace{\frac{f(x)+f(-x)}{2}}_{\text{even part}} + \underbrace{\frac{f(x)-f(-x)}{2}}_{\text{odd part}}$$

## Example

The standard normal PDF $\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ is even: $\phi(-x) = \phi(x)$.

This symmetry immediately gives $E[Z] = 0$ for a standard normal $Z$, because:

$$E[Z] = \int_{-\infty}^{\infty} x \cdot \phi(x)\, dx = 0$$

The integrand $x\phi(x)$ is odd (odd $\times$ even = odd), so the integral over the symmetric domain $(-\infty, \infty)$ is zero — no calculation required.

## Remember

Recognising even and odd integrands is a powerful shortcut in quantitative finance. The normal PDF is even, so any integral of an odd function against it vanishes — this is why all odd central moments of the normal distribution (mean, skewness, and all odd cumulants) are zero without needing to evaluate the integrals. The same symmetry argument applies in Fourier-based option pricing: the imaginary part of the characteristic function integrand is often odd, and its integral over $\mathbb{R}$ drops out, halving the numerical work.
