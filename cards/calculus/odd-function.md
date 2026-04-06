# Odd Function

**Topic:** Calculus
**Tags:** odd function, symmetry, integration, antisymmetry, moments, probability distributions
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A function $f$ is **odd** if it is symmetric about the origin: $f(-x) = -f(x)$ for all $x$ in its domain. Rotating the graph by 180° about the origin leaves it unchanged. Every odd function satisfies $f(0) = 0$ (provided $0$ is in the domain).

## Key Formula

**Antisymmetry condition:**

$$f(-x) = -f(x) \quad \text{for all } x$$

**Integration over a symmetric interval — the key result:**

$$\int_{-a}^{a} f(x)\, dx = 0 \qquad (f \text{ odd})$$

This holds for $a = \infty$ provided the integral converges absolutely.

Common odd functions: $x,\; x^3,\; \sin x,\; \sinh x,\; x\,e^{-x^2}$

**Product rules for parity:**

$$\text{odd} \times \text{odd} = \text{even}, \qquad \text{odd} \times \text{even} = \text{odd}, \qquad \text{even} \times \text{even} = \text{even}$$

## Example

The third central moment (skewness numerator) of a symmetric distribution is:

$$E[(X - \mu)^3] = \int_{-\infty}^{\infty} (x - \mu)^3 \phi(x - \mu)\, dx$$

The integrand $(x - \mu)^3 \phi(x - \mu)$ is the product of an odd function ($(x-\mu)^3$) and an even function ($\phi$), so it is odd. The integral over the symmetric domain $(-\infty, \infty)$ is therefore exactly zero — confirming that the normal distribution has zero skewness without computing the integral.

## Remember

The vanishing integral of odd functions over symmetric domains is a structural result that saves computation throughout quantitative finance. It confirms zero mean for a centred normal, zero skewness for any symmetric distribution, and zero contribution from imaginary-part integrands in Fourier-based option pricing. Whenever you need to show that a moment or integral is zero, check whether the integrand is odd before reaching for a calculator — parity symmetry is often the fastest proof.
