# Fokker-Planck Equation

**Topic:** Stochastic Processes
**Level:** A Level Mathematics
**Tags:** Fokker-Planck, probability density, PDE, diffusion, Kolmogorov, transition density
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

The **Fokker-Planck equation** (also called the Kolmogorov forward equation) is a partial differential equation that describes how the probability density function of a stochastic process evolves over time. Rather than tracking individual sample paths, it tells you how the entire distribution of possible values spreads and shifts.

## Key Formula

For the SDE $dX = a(X) \, dt + b(X) \, dW$, the probability density $p(x, t)$ satisfies:

$$\frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}\bigl[a(x) \, p\bigr] + \frac{1}{2}\frac{\partial^2}{\partial x^2}\bigl[b(x)^2 \, p\bigr]$$

For GBM with $a(S) = \mu S$ and $b(S) = \sigma S$:

$$\frac{\partial p}{\partial t} = -\frac{\partial}{\partial S}(\mu S \, p) + \frac{1}{2}\frac{\partial^2}{\partial S^2}(\sigma^2 S^2 \, p)$$

The solution confirms that $S(T)$ is **lognormally distributed**.

## Example

For standard Brownian motion ($a = 0$, $b = 1$), the Fokker-Planck equation reduces to the **heat equation**:

$$\frac{\partial p}{\partial t} = \frac{1}{2}\frac{\partial^2 p}{\partial x^2}$$

Starting from a point mass at $x = 0$, the solution is the familiar Gaussian:

$$p(x, t) = \frac{1}{\sqrt{2\pi t}} \exp\!\left(-\frac{x^2}{2t}\right)$$

At $t = 1$, approximately 68% of probability lies within $|x| < 1$ and 95% within $|x| < 2$.

## Remember

The Fokker-Planck equation is the **dual** of the Black-Scholes PDE — both are second-order parabolic PDEs driven by the same drift and diffusion coefficients, but they describe different things. Black-Scholes evolves the option price backwards from expiry; Fokker-Planck evolves the probability density forwards from today. Understanding this duality is essential for pricing path-dependent derivatives and for calibrating models to observed return distributions.
