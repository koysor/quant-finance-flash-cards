# Modulus Function

**Topic:** Calculus
**Tags:** modulus, absolute value, distance, VaR, drawdown, piecewise function
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **modulus function** (or absolute value) $|x|$ returns the non-negative magnitude of a real number, stripping its sign. For a complex number $z = a + bi$, the modulus $|z|$ is the distance from the origin in the complex plane. The modulus function is continuous everywhere but not differentiable at $x = 0$.

## Key Formula

**Real modulus:**

$$|x| = \begin{cases} x & x \geq 0 \\ -x & x < 0 \end{cases}$$

**Complex modulus:**

$$|z| = |a + bi| = \sqrt{a^2 + b^2}$$

**Key properties:**

$$|xy| = |x||y|, \qquad |x + y| \leq |x| + |y| \quad \text{(triangle inequality)}$$

$$|x - y| \geq \big||x| - |y|\big| \quad \text{(reverse triangle inequality)}$$

**Derivative** (where it exists):

$$\frac{d}{dx}|x| = \text{sgn}(x) = \begin{cases} +1 & x > 0 \\ -1 & x < 0 \end{cases}$$

## Example

A portfolio's daily P&L over four days is: $+3, -5, +2, -1$ (in £000s).

The **mean absolute deviation** (MAD) measures average loss magnitude:

$$\text{MAD} = \frac{|3| + |-5| + |2| + |-1|}{4} = \frac{3 + 5 + 2 + 1}{4} = 2.75$$

The maximum drawdown uses $|\min(\text{P\&L})| = |-5| = 5$.

The modulus ensures that gains and losses are treated symmetrically in magnitude — a loss of £5k and a gain of £5k both contribute 5 to the sum.

## Remember

The modulus function is the mathematical foundation of **distance-based risk measures**. Mean Absolute Deviation (MAD) is a robust alternative to variance that uses $|r_i - \bar{r}|$ rather than $(r_i - \bar{r})^2$ — it penalises outliers less severely and is less sensitive to fat tails. The $L^1$ portfolio optimisation (minimise $\sum w_i |r_i|$) uses the modulus and produces sparser solutions than $L^2$ (mean-variance). In the complex-number setting, $|z|^2 = z\bar{z}$ converts characteristic functions to real-valued power spectra — the squared modulus appears in every Fourier-based option pricing formula.
