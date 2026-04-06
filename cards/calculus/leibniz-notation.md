# Leibniz Notation

**Topic:** Calculus
**Tags:** calculus, differentiation, notation, derivatives, chain rule
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

Leibniz notation expresses derivatives as fractions of infinitesimal quantities: $\frac{dy}{dx}$ for the first derivative of $y$ with respect to $x$, and $\frac{d^n y}{dx^n}$ for higher-order derivatives. Unlike prime notation ($f'$), Leibniz notation makes the independent variable explicit, which is essential when working with functions of several variables or applying the chain rule.

## Key Formula

First derivative:

$$\frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}$$

Second derivative:

$$\frac{d^2 y}{dx^2} = \frac{d}{dx}\!\left(\frac{dy}{dx}\right)$$

Chain rule in Leibniz form — if $y$ depends on $u$, which depends on $x$:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

Partial derivative notation (holding other variables fixed):

$$\frac{\partial f}{\partial x}, \qquad \frac{\partial^2 f}{\partial x^2}, \qquad \frac{\partial^2 f}{\partial y \, \partial x}$$

## Example

The price of a European call option $V$ depends on the underlying price $S$ and time $t$. Using Leibniz notation, Delta and Gamma are written:

$$\Delta = \frac{\partial V}{\partial S} \approx \frac{0.55 - 0.45}{101 - 99} = 0.05 \text{ per £1 move}$$

At $S = 100$, if $V = 5.00$ and at $S = 101$, $V = 5.05$, then $\frac{\partial V}{\partial S} \approx 0.05$. The second-order term $\frac{\partial^2 V}{\partial S^2}$ (Gamma) captures the curvature of this relationship.

## Remember

The entire language of option pricing is written in Leibniz notation. The Black-Scholes PDE

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

is unreadable without it. Each term corresponds directly to a Greek: $\Theta$, $\Gamma$, and $\Delta$ respectively. Recognising that $\frac{dy}{du} \cdot \frac{du}{dx}$ is the chain rule in disguise is also the first step to understanding Itô's Lemma, where the extra $\frac{1}{2}\sigma^2\frac{\partial^2 f}{\partial x^2}$ term arises from the stochastic analogue of the same cancellation.
