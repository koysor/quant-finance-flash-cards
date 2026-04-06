# L'Hôpital's Rule

**Topic:** Calculus
**Tags:** L'Hôpital, limits, indeterminate forms, derivatives, Greeks, small-time asymptotics
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

**L'Hôpital's Rule** resolves limits of the form $\frac{0}{0}$ or $\frac{\infty}{\infty}$ — called **indeterminate forms** — by replacing the ratio with the ratio of the derivatives. If $\lim_{x \to a} f(x) = 0$ and $\lim_{x \to a} g(x) = 0$ (or both are $\pm\infty$), and $g'(x) \neq 0$ near $a$, then:

$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

provided the right-hand limit exists. The rule may be applied repeatedly if the result remains indeterminate.

## Key Formula

**Applicable indeterminate forms:** $\frac{0}{0}$, $\frac{\infty}{\infty}$, $0 \cdot \infty$, $\infty - \infty$, $0^0$, $1^\infty$, $\infty^0$

The last four are reduced to $\frac{0}{0}$ or $\frac{\infty}{\infty}$ by algebraic manipulation before applying the rule.

**Standard result:**

$$\lim_{x \to 0} \frac{\sin x}{x} = \lim_{x \to 0} \frac{\cos x}{1} = 1$$

**Exponential growth dominates polynomials:**

$$\lim_{x \to \infty} \frac{x^n}{e^x} = 0 \quad \text{for any } n$$

(Apply the rule $n$ times; the numerator eventually becomes a constant while the denominator remains $e^x$.)

## Example

In the Black-Scholes model, as time to expiry $T \to 0$ with the option at-the-money ($S = K$):

$$d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}} \xrightarrow[S=K]{} \frac{(r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}} = \frac{(r + \frac{1}{2}\sigma^2)\sqrt{T}}{\sigma} \to 0$$

This $\frac{0}{0}$ form (numerator and denominator both $\to 0$) can be handled by L'Hôpital. The result $d_1 \to 0$ confirms that at-the-money options near expiry have $\Delta \approx N(0) = 0.5$, a key sanity check for option pricing models.

## Remember

L'Hôpital's Rule is the standard tool for evaluating **small-time and large-strike asymptotics** in options pricing. The short-maturity behaviour of implied volatility — how $\sigma_{\text{imp}}(T)$ behaves as $T \to 0$ — involves limits of the form $\frac{0}{0}$ that require L'Hôpital to resolve. Similarly, large-strike asymptotics (Lee's moment formula) involve $\frac{\infty}{\infty}$ forms. Whenever a pricing or risk formula produces an indeterminate form at a boundary, L'Hôpital's Rule is the first tool to reach for.
