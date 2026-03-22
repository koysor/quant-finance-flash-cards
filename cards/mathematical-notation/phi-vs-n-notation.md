# Phi (Φ) vs N Notation

**Topic:** Mathematical Notation
**Tags:** notation, normal distribution, CDF, convention, Black-Scholes
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Two notational conventions exist for the standard normal CDF: $\Phi(x)$ (capital phi) and $N(x)$. Both denote exactly the same function — the probability that a standard normal random variable is at most $x$. The choice is purely conventional and varies by textbook and tradition.

## Key Formula

$$\Phi(x) \equiv N(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-z^2/2}\,dz$$

Similarly, the PDF is written as either $\phi(x)$ (lowercase phi) or $N'(x)$:

$$\phi(x) \equiv N'(x) = \frac{1}{\sqrt{2\pi}}\,e^{-x^2/2}$$

| Convention | CDF | PDF | Common in |
|---|---|---|---|
| Phi | $\Phi(x)$ | $\phi(x)$ | Probability textbooks, pure statistics |
| N | $N(x)$ | $N'(x)$ | Finance texts, Hull, Wilmott, Black–Scholes literature |

A third notation, $n(x)$ for the PDF, appears in some derivatives texts (e.g. Natenberg).

## Example

The Black–Scholes call formula in both conventions:

**N convention:**

$$C = S_0\,N(d_1) - Ke^{-rT}\,N(d_2)$$

**Phi convention:**

$$C = S_0\,\Phi(d_1) - Ke^{-rT}\,\Phi(d_2)$$

These are identical — if an exam question uses $\Phi$ where you expect $N$, simply read them as the same function.

## Remember

Notation mismatches cause unnecessary confusion when moving between textbooks. Hull's *Options, Futures, and Other Derivatives* uses $N(\cdot)$, while Shreve's *Stochastic Calculus for Finance* uses $\Phi(\cdot)$. In interviews and exams, you may encounter either — or both in the same problem set. The critical skill is instant recognition that $\Phi = N$ and $\phi = N'$, so you never waste time wondering whether a different function is intended. When writing your own work, pick one convention and use it consistently.
