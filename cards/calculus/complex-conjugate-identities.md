# Complex Conjugate Identities

**Topic:** Calculus
**Tags:** complex conjugate, modulus, real part, fourier inversion, characteristic functions
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **complex conjugate identities** are the four core algebraic relations that connect a complex number $z$ and its conjugate $\bar{z}$, allowing the modulus, real part, and imaginary part to be expressed purely in terms of $z$ and $\bar{z}$ without trigonometry. They are indispensable whenever a complex-valued integral must be reduced to a real-valued computation.

## Key Formula

For $z = a + bi \in \mathbb{C}$, $\bar{z} = a - bi$:

$$z \bar{z} = |z|^2 \qquad \textbf{(modulus identity)}$$

$$z + \bar{z} = 2\,\text{Re}(z) \qquad \textbf{(real-part extraction)}$$

$$z - \bar{z} = 2i\,\text{Im}(z) \qquad \textbf{(imaginary-part extraction)}$$

$$\overline{z_1 z_2} = \bar{z}_1 \bar{z}_2 \qquad \textbf{(multiplicative conjugation)}$$

**Conjugate symmetry of characteristic functions:** for a real-valued random variable $X$,

$$\varphi_X(-u) = \overline{\varphi_X(u)}$$

This follows directly from the multiplicative identity: $e^{-iuX} = \overline{e^{iuX}}$, so taking expectations preserves the relation.

## Example

Evaluate the real part of the integral $I = \displaystyle\int_0^\infty e^{-iu}\cdot e^{-u^2/2}\,du$ without splitting into sine and cosine components.

Using the real-part identity:

$$\text{Re}(I) = \frac{I + \bar{I}}{2} = \frac{1}{2}\int_{-\infty}^{\infty} e^{-iuk}\cdot e^{-u^2/2}\,du \bigg|_{k=1}$$

The conjugate symmetry $\varphi(-u) = \overline{\varphi(u)}$ folds the domain: integrating from $-\infty$ to $\infty$ equals twice the real part of the integral from $0$ to $\infty$. Numerically this halves the quadrature nodes required.

## Remember

In the Carr-Madan FFT option pricing formula, the price of a European call is recovered as:

$$C(k) = \frac{e^{-\alpha k}}{\pi} \int_0^\infty e^{-iuk} \psi(u)\,du$$

where $\psi(u)$ is a damped characteristic function. Because $\psi(-u) = \overline{\psi(u)}$ (a direct consequence of the conjugate symmetry identity), the integration need only cover $u \geq 0$. Halving the domain cuts both computation time and numerical error — this single identity is why FFT-based option pricers are fast enough to use in live trading.
