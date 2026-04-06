# Euler's Identity

**Topic:** Calculus
**Tags:** euler's identity, complex exponential, irrational numbers, pi, mathematical constants
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Euler's identity** is the special case of Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ evaluated at $\theta = \pi$, giving $e^{i\pi} = -1$, or equivalently $e^{i\pi} + 1 = 0$. It unites the five most fundamental mathematical constants — the additive identity $0$, the multiplicative identity $1$, the base of natural logarithms $e \approx 2.718$, the imaginary unit $i$ (where $i^2 = -1$), and the circle constant $\pi \approx 3.14159$ — in a single compact equation.

## Key Formula

$$e^{i\pi} + 1 = 0$$

This is the special case $\theta = \pi$ of Euler's formula:

$$e^{i\theta} = \cos\theta + i\sin\theta \xrightarrow{\;\theta = \pi\;} e^{i\pi} = \cos\pi + i\sin\pi = -1 + 0i = -1$$

**Equivalent rearrangements:**

$$e^{i\pi} = -1 \qquad \Longleftrightarrow \qquad e^{i\pi} + 1 = 0 \qquad \Longleftrightarrow \qquad \ln(-1) = i\pi$$

**Half-rotation interpretation:** multiplying any complex number $z$ by $e^{i\pi}$ rotates it by $180°$ (half a full turn of $2\pi$), mapping $z \to -z$. In particular, multiplying $1$ by $e^{i\pi}$ gives $-1$, which is the geometric meaning of the identity.

## Example

Verify using the Taylor series for $e^x$ with $x = i\pi$:

$$e^{i\pi} = 1 + i\pi + \frac{(i\pi)^2}{2!} + \frac{(i\pi)^3}{3!} + \frac{(i\pi)^4}{4!} + \cdots$$

$$= \underbrace{\left(1 - \frac{\pi^2}{2} + \frac{\pi^4}{24} - \cdots\right)}_{\cos\pi\; =\; -1} + i\underbrace{\left(\pi - \frac{\pi^3}{6} + \frac{\pi^5}{120} - \cdots\right)}_{\sin\pi\; =\; 0}$$

Taking the first few terms numerically: $1 - \frac{9.870}{2} + \frac{97.41}{24} \approx 1 - 4.935 + 4.058 \approx -0.999\ldots \to -1$ as more terms are added. So $e^{i\pi} + 1 = 0$ is confirmed as the series converge.

## Remember

The identity $e^{i\pi} = -1$ is the $\theta = \pi$ instance of the more general relation $|e^{i\theta}| = 1$, which tells quants that a complex exponential always has modulus 1. This property is what guarantees that the **characteristic function** $\varphi_X(u) = E[e^{iuX}]$ always converges: $|e^{iuX}| = 1$ regardless of the distribution of $X$, so the expectation is automatically finite. Euler's identity is therefore not just a mathematical curiosity — it is the geometric cornerstone that makes Fourier-based derivative pricing (Carr-Madan FFT, Heston model semi-analytics) analytically tractable for any log-return distribution, including fat-tailed ones where the moment generating function diverges.
