# Convergence

**Topic:** Calculus
**Tags:** convergence, radius of convergence, power series, interval of convergence, Taylor series, approximation
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A power series $\sum_{n=0}^{\infty} a_n x^n$ **converges** for values of $x$ within its **radius of convergence** $R$ — the largest value such that the series sums to a finite limit for all $|x| < R$. Outside this radius the series diverges. The radius is found using the ratio test and determines where a Taylor or Maclaurin series provides a valid approximation.

## Key Formula

**Radius of convergence** (ratio test):

$$R = \lim_{n \to \infty} \left|\frac{a_n}{a_{n+1}}\right|$$

**Interval of convergence:** $(-R, R)$ — check endpoints separately.

**Special cases:**

| Series | $R$ | Converges for |
|---|---|---|
| $e^x = \sum x^n/n!$ | $\infty$ | all $x$ |
| $\sin x$, $\cos x$ | $\infty$ | all $x$ |
| $\ln(1+x) = \sum (-1)^{n+1}x^n/n$ | $1$ | $-1 < x \leq 1$ |
| $\frac{1}{1-x} = \sum x^n$ | $1$ | $|x| < 1$ |

## Example

Find the radius of convergence of $\displaystyle\sum_{n=1}^{\infty} \frac{x^n}{n}$.

Here $a_n = 1/n$, so:

$$R = \lim_{n\to\infty} \frac{1/n}{1/(n+1)} = \lim_{n\to\infty} \frac{n+1}{n} = 1$$

The series converges for $|x| < 1$. Checking endpoints: at $x = 1$ this is the harmonic series (diverges); at $x = -1$ it is the alternating harmonic series (converges). Interval: $-1 \leq x < 1$.

## Remember

Convergence is the hidden constraint in every Taylor-series-based approximation in finance. The **delta-gamma approximation** $\Delta V \approx \Delta\cdot\delta S + \tfrac{1}{2}\Gamma\cdot(\delta S)^2$ is a truncated Taylor series valid only for small $\delta S$ — it is accurate within the radius of convergence of the option price series in $\delta S$. For large market moves (gap risk, flash crashes), $\delta S$ leaves this region and the approximation breaks down. **Stressed VaR** and scenario analysis exist precisely because the linear-quadratic Taylor approximation converges too slowly in the tails of the return distribution.
