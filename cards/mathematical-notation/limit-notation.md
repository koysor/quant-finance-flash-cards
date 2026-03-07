# Limit Notation

**Topic:** Mathematical Notation
**Tags:** notation, limits, convergence, infinity, asymptotic, calculus
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

**Limit notation** describes the value that a function or sequence approaches as its argument tends to some target. The notation specifies the variable, the target, and optionally the direction of approach.

| Symbol | Read as | Meaning |
|---|---|---|
| $\displaystyle\lim_{x \to a} f(x) = L$ | "limit as $x$ tends to $a$ of $f(x)$ equals $L$" | $f(x)$ approaches $L$ as $x$ approaches $a$ |
| $x \to \infty$ | "$x$ tends to infinity" | $x$ grows without bound |
| $x \to 0^+$ | "$x$ tends to zero from above" | $x$ approaches 0 through positive values |
| $x \to 0^-$ | "$x$ tends to zero from below" | $x$ approaches 0 through negative values |
| $O(h^2)$ | "big-O of $h$ squared" | Bounded above by a constant times $h^2$ as $h \to 0$ |
| $o(h)$ | "little-o of $h$" | Grows slower than $h$; i.e. $o(h)/h \to 0$ |

## Key Formula

**Definition of the derivative:**

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

**Continuous compounding** as the limit of discrete compounding:

$$\lim_{n \to \infty}\left(1 + \frac{r}{n}\right)^{n} = e^r$$

**Big-O in Taylor expansion** — terms beyond the kept terms:

$$f(x + h) = f(x) + f'(x)h + \tfrac{1}{2}f''(x)h^2 + O(h^3)$$

## Example

Show that continuous compounding arises from the limit. At $r = 10\%$:

| $n$ (compoundings/year) | $\left(1 + 0.1/n\right)^n$ |
|---|---|
| 1 | 1.10000 |
| 12 | 1.10471 |
| 365 | 1.10516 |
| $\infty$ | $e^{0.1} = 1.10517$ |

## Remember

Limit notation appears everywhere in quantitative finance, usually at the boundary between discrete and continuous models. The binomial tree converges to Black–Scholes as the number of time steps $n \to \infty$. Discrete compounding becomes continuous compounding as $n \to \infty$. The big-O and little-o notations are essential for Itô calculus, where the key insight is that $(dW)^2 = O(dt)$ (it behaves like $dt$) while $(dt)^2 = o(dt)$ (it vanishes faster than $dt$) — this asymptotic distinction is precisely what produces the Itô correction term.
