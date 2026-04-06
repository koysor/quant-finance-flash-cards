# Differentiation of Trigonometric Functions

**Topic:** Calculus
**Tags:** differentiation, trigonometry, sine, cosine, chain-rule, calculus
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

Differentiating a trigonometric function gives the instantaneous rate of change of that oscillatory quantity with respect to its argument. The six standard trig functions each have a closed-form derivative expressible in terms of the same family of functions.

## Key Formula

**Primary derivatives:**

$$\frac{d}{dx}\sin x = \cos x \qquad \frac{d}{dx}\cos x = -\sin x \qquad \frac{d}{dx}\tan x = \sec^2 x$$

**Reciprocal function derivatives:**

$$\frac{d}{dx}\csc x = -\csc x \cot x \qquad \frac{d}{dx}\sec x = \sec x \tan x \qquad \frac{d}{dx}\cot x = -\csc^2 x$$

**With chain rule** — for a composite argument $g(x)$:

$$\frac{d}{dx}\sin(g(x)) = g'(x)\cos(g(x)) \qquad \frac{d}{dx}\cos(g(x)) = -g'(x)\sin(g(x))$$

**Key limit underpinning both primary results:**

$$\lim_{h \to 0} \frac{\sin h}{h} = 1 \qquad \lim_{h \to 0} \frac{\cos h - 1}{h} = 0$$

## Example

Differentiate $f(t) = A\sin(\omega t + \phi)$, a sinusoidal price oscillation with amplitude $A$, angular frequency $\omega$, and phase $\phi$.

Let $g(t) = \omega t + \phi$, so $g'(t) = \omega$.

$$f'(t) = A \cdot \omega \cos(\omega t + \phi)$$

At $t = 0$ with $A = 2$, $\omega = \pi$, $\phi = 0$:

$$f'(0) = 2\pi\cos(0) = 2\pi \approx 6.28$$

The derivative is another sinusoid shifted by $\tfrac{\pi}{2}$, with amplitude scaled by $\omega$.

## Remember

Trig differentiation is foundational to **Fourier-based option pricing** (e.g. the Carr–Madan method). The characteristic function $\varphi(\omega) = E[e^{i\omega X}]$ is differentiated term by term using $\tfrac{d}{d\omega}e^{i\omega x} = ix\,e^{i\omega x}$, which is essentially the chain rule applied to $\cos(\omega x) + i\sin(\omega x)$. Understanding how the derivative of $\sin$ and $\cos$ shifts phase by $\tfrac{\pi}{2}$ also explains why Greeks like **Vega** and **Delta** peak near the money — the sensitivity is greatest where the option-value curve bends most sharply, analogous to where $|\cos x|$ is largest relative to $|\sin x|$.
