# Gaussian Integral

**Topic:** Probability
**Tags:** gaussian integral, normal distribution, integration, polar coordinates, normalisation
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **Gaussian integral** is the improper integral of the function $e^{-x^2}$ over the entire real line. Its value is $\sqrt{\pi}$, a result that underpins the normalisation of every normal distribution. Although $e^{-x^2}$ has no elementary antiderivative, the integral can be evaluated exactly using a polar-coordinate argument — one of the most elegant tricks in analysis.

## Key Formula

**The Gaussian integral:**

$$\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$$

**Proof sketch (polar-coordinate method):** let $I = \int_{-\infty}^{\infty} e^{-x^2}\,dx$. Then:

$$I^2 = \left(\int_{-\infty}^{\infty} e^{-x^2}\,dx\right)\!\left(\int_{-\infty}^{\infty} e^{-y^2}\,dy\right) = \iint_{\mathbb{R}^2} e^{-(x^2+y^2)}\,dx\,dy$$

Converting to polar coordinates $x = r\cos\theta$, $y = r\sin\theta$, with Jacobian $r$:

$$I^2 = \int_0^{2\pi}\!\int_0^{\infty} e^{-r^2}\,r\,dr\,d\theta = 2\pi \cdot \frac{1}{2} = \pi \implies I = \sqrt{\pi}$$

**Normalisation of the normal PDF:** substituting $x = \tfrac{t}{\sigma\sqrt{2}}$ shows:

$$\int_{-\infty}^{\infty} \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{t^2}{2\sigma^2}}\,dt = \frac{1}{\sigma\sqrt{2\pi}} \cdot \sigma\sqrt{2} \cdot \sqrt{\pi} = 1$$

## Example

Verify the standard normal PDF $\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$ integrates to 1.

Let $u = z/\sqrt{2}$, so $z = u\sqrt{2}$ and $dz = \sqrt{2}\,du$:

$$\int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-z^2/2}\,dz = \frac{\sqrt{2}}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-u^2}\,du = \frac{\sqrt{2}}{\sqrt{2\pi}} \cdot \sqrt{\pi} = \frac{\sqrt{2\pi}}{\sqrt{2\pi}} = 1$$

## Remember

The Gaussian integral is the reason the normal distribution is valid as a probability model — without it integrating to $\sqrt{\pi}$, the $\frac{1}{\sqrt{2\pi}}$ normalisation constant in the PDF would not exist. In Black-Scholes option pricing, evaluating the discounted expected payoff requires integrating the call payoff against the lognormal density; after a change of variables, this reduces to evaluating two Gaussian integrals of the form $\int e^{-u^2/2}\,du$, which produce the familiar $\Phi(d_1)$ and $\Phi(d_2)$ terms. Every option price in the Black-Scholes framework is ultimately a ratio of two Gaussian integrals.
