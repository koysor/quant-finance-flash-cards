# Trigonometric Identities

**Topic:** Calculus
**Tags:** trig identities, double angle, compound angle, Pythagorean, simplification, integration
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Trigonometric identities** are equations involving trig functions that are true for all values of the variable. They are used to simplify expressions, rewrite integrands into integrable forms, and prove other results. The three families are: Pythagorean identities, compound angle formulas, and double angle formulas.

## Key Formula

**Pythagorean:**

$$\sin^2\theta + \cos^2\theta = 1, \qquad 1 + \tan^2\theta = \sec^2\theta, \qquad 1 + \cot^2\theta = \csc^2\theta$$

**Compound angle:**

$$\sin(A \pm B) = \sin A\cos B \pm \cos A\sin B$$

$$\cos(A \pm B) = \cos A\cos B \mp \sin A\sin B$$

**Double angle:**

$$\sin 2\theta = 2\sin\theta\cos\theta, \qquad \cos 2\theta = \cos^2\theta - \sin^2\theta = 1 - 2\sin^2\theta = 2\cos^2\theta - 1$$

## Example

Integrate $\int \sin^2 x\, dx$.

Using the identity $\cos 2x = 1 - 2\sin^2 x$ → $\sin^2 x = \frac{1 - \cos 2x}{2}$:

$$\int \sin^2 x\, dx = \int \frac{1 - \cos 2x}{2}\, dx = \frac{x}{2} - \frac{\sin 2x}{4} + C$$

Without the identity this integral has no simple form.

## Remember

The double angle formula $\cos 2\theta = 1 - 2\sin^2\theta$ is the half-angle substitution that converts powers of trig functions into first-order terms — a technique used in **closed-form option pricing** under stochastic volatility. When computing $E[\cos(\omega \ln S_T)]$ for a lognormal asset, expanding via compound angle formulas and matching moment-generating function terms lets quants derive analytical expressions for option prices. The Pythagorean identity $\sin^2 + \cos^2 = 1$ is also the complex-number norm identity $|e^{i\theta}|^2 = 1$, underpinning the unit-modulus property of characteristic functions evaluated on the real axis.
