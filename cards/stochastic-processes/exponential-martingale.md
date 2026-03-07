# Exponential Martingale

**Topic:** Stochastic Processes
**Tags:** martingale, exponential, ito correction, measure change, radon-nikodym
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

An **exponential martingale** is the exponential of a stochastic process, constructed so that the Itô correction term exactly cancels the drift, making the result a martingale. The key insight is that $e^{Y_t}$ is a martingale only when the drift of $Y_t$ equals $-\tfrac{1}{2}g^2(t)$, where $g$ is the diffusion coefficient.

## Key Formula

If $dY = -\tfrac{1}{2}g^2(t)\,dt + g(t)\,dX_t$, then $Z_t = e^{Y_t}$ is a martingale:

$$Z_t = Z_0\exp\!\left(-\frac{1}{2}\int_0^t g^2(s)\,ds + \int_0^t g(s)\,dX_s\right)$$

The drift condition comes from Itô's lemma applied to $e^Y$:

$$dZ = Z\!\left[\left(f + \tfrac{1}{2}g^2\right)dt + g\,dX\right]$$

Setting the drift to zero requires $f = -\tfrac{1}{2}g^2$.

## Example

Let $g(t) = \sigma$ (constant) and $Z_0 = 1$:

$$Z_t = \exp\!\left(-\frac{1}{2}\sigma^2 t + \sigma X_t\right)$$

Check: $E[Z_t] = E\!\left[e^{-\sigma^2 t/2 + \sigma X_t}\right] = e^{-\sigma^2 t/2} \cdot e^{\sigma^2 t/2} = 1$ ✓

since $E[e^{\sigma X_t}] = e^{\sigma^2 t/2}$ by the moment-generating function of $X_t \sim N(0, t)$.

## Remember

Exponential martingales are the mechanism for changing probability measures in derivative pricing. The Radon–Nikodým derivative $d\mathbb{Q}/d\mathbb{P}$ is constructed as an exponential martingale — its positivity and unit expectation ensure $\mathbb{Q}$ is a valid probability measure equivalent to $\mathbb{P}$. The characteristic $-\tfrac{1}{2}g^2$ drift term is not coincidental: it is precisely the Itô correction that exponentiation introduces, and it appears throughout quantitative finance — most visibly in the $-\tfrac{1}{2}\sigma^2$ adjustment between arithmetic and geometric returns in the lognormal model.
