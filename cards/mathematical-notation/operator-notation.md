# Operator Notation

**Topic:** Mathematical Notation
**Tags:** notation, differential operators, PDE, Black-Scholes, generator
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

An **operator** is a symbol that acts on a function and returns another function. Operator notation bundles a collection of differentiation (or other) instructions into a single compact symbol, making PDEs easier to write, manipulate, and reason about. The three operators most common in quantitative finance are the differential operator $D$, the infinitesimal generator $\mathcal{L}$, and the Laplacian $\nabla^2$.

| Symbol | Name | Meaning |
|---|---|---|
| $D$ or $\frac{d}{dx}$ | Differential operator | $Df = \frac{df}{dx}$; $D^2 f = \frac{d^2 f}{dx^2}$ |
| $\mathcal{L}$ | Infinitesimal generator | Encodes drift and diffusion of a stochastic process |
| $\nabla^2$ or $\Delta$ | Laplacian | $\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \cdots$ |
| $\mathcal{L}_{BS}$ | Black-Scholes operator | The left-hand side of the Black-Scholes PDE written as a single symbol |

## Key Formula

The **infinitesimal generator** $\mathcal{L}$ of a one-dimensional Itô process $dX = a(X)\,dt + b(X)\,dW$ is:

$$\mathcal{L} = a(x)\frac{\partial}{\partial x} + \frac{1}{2}b(x)^2\frac{\partial^2}{\partial x^2}$$

Applied to a smooth function $f(x)$:

$$\mathcal{L}f = a(x)f'(x) + \frac{1}{2}b(x)^2 f''(x)$$

The **Black-Scholes operator** packages the full PDE compactly:

$$\mathcal{L}_{BS} V \equiv \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

## Example

For geometric Brownian motion $dS = \mu S\,dt + \sigma S\,dW$, the generator is:

$$\mathcal{L} = \mu S\frac{\partial}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2}{\partial S^2}$$

Apply it to $f(S) = S^2$:

$$\mathcal{L}(S^2) = \mu S \cdot 2S + \frac{1}{2}\sigma^2 S^2 \cdot 2 = 2\mu S^2 + \sigma^2 S^2 = (2\mu + \sigma^2)S^2$$

This matches Itô's lemma: $d(S^2) = (2\mu + \sigma^2)S^2\,dt + 2\sigma S^2\,dW$, confirming that $\mathcal{L}(S^2)$ gives the drift of $S^2$.

## Remember

The infinitesimal generator $\mathcal{L}$ is the continuous-time analogue of the transition operator in a discrete Markov chain. In options pricing, writing the Black-Scholes PDE as $\mathcal{L}_{BS} V = 0$ makes it immediately clear that option pricing is an eigenvalue-style problem: you are finding the function $V$ that is annihilated by the operator. This perspective underpins numerical PDE solvers (finite-difference grids), where the operator is discretised into a matrix and each time step involves a matrix equation of the form $A\mathbf{v} = \mathbf{b}$.
