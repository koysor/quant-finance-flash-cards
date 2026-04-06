# Irrational Numbers

**Topic:** Mathematical Notation
**Tags:** notation, number sets, irrational, pi, square root, continuous mathematics
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

An **irrational number** is a real number that cannot be expressed as a ratio $\frac{p}{q}$ with $p, q \in \mathbb{Z}$. Its decimal expansion is non-terminating and non-repeating. Together, the rationals and irrationals partition $\mathbb{R}$:

$$\mathbb{R} = \mathbb{Q} \cup \mathbb{Q}^c, \qquad \mathbb{Q} \cap \mathbb{Q}^c = \emptyset$$

## Key Formula

Common irrational numbers in quantitative finance:

$$\pi \approx 3.14159\ldots \qquad e \approx 2.71828\ldots \qquad \sqrt{2} \approx 1.41421\ldots$$

**Proof sketch that $\sqrt{2}$ is irrational:** assume $\sqrt{2} = \frac{p}{q}$ in lowest terms, then $2q^2 = p^2$, so $p$ is even; writing $p = 2k$ gives $q^2 = 2k^2$, so $q$ is also even — contradicting lowest terms.

The normal PDF involves two irrationals simultaneously:

$$f(x) = \frac{1}{\sqrt{2\pi}\,\sigma} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

## Example

The Black-Scholes call price for $S_0 = 100$, $K = 100$, $\sigma = 0.2$, $r = 0.05$, $T = 1$:

$$d_1 = \frac{\ln(100/100) + (0.05 + 0.02)T}{0.2\sqrt{T}} = \frac{0.07}{0.2} = 0.35$$

$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$

Both $e^{-0.05}$ and the values of $N(\cdot)$ (which involve $\pi$ via the Gaussian integral) are irrational — the final option price is an irrational number, although it is always rounded to a finite decimal for quoting.

## Remember

The two most important constants in quantitative finance — $e$ and $\pi$ — are irrational. Euler's number $e$ appears in continuous compounding ($e^{rT}$), geometric Brownian motion ($e^{\mu t + \sigma W_t}$), and the moment generating function. $\pi$ appears inside every Gaussian density via $\frac{1}{\sqrt{2\pi}}$. The irrationality of $e$ and $\pi$ means closed-form option prices are never exact rationals — they are computed numerically and quoted to a fixed number of decimal places, which is why understanding floating-point precision matters for derivatives valuation.
