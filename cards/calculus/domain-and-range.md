# Domain and Range

**Topic:** Calculus
**Tags:** domain, range, codomain, function, mapping, interval notation
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **domain** of a function $f$ is the complete set of input values for which $f$ is defined. The **range** (or image) is the set of all output values actually produced. The **codomain** is the declared target set, which may be larger than the range. To find the domain, exclude values that cause division by zero, negative square roots, or negative logarithms. To find the range, determine which output values are achievable by solving $y = f(x)$ for $x$.

## Key Formula

**Common domain restrictions:**

| Expression | Domain restriction |
|---|---|
| $\frac{1}{g(x)}$ | $g(x) \neq 0$ |
| $\sqrt{g(x)}$ | $g(x) \geq 0$ |
| $\ln g(x)$ | $g(x) > 0$ |

**Interval notation:** $x \in [a, b)$ means $a \leq x < b$.

**Range via inverse:** range of $f$ = domain of $f^{-1}$.

**For a composition $f \circ g$:** domain = $\{x \in \text{dom}(g) : g(x) \in \text{dom}(f)\}$.

## Example

$f(x) = \sqrt{4 - x^2}$: domain requires $4 - x^2 \geq 0 \implies x^2 \leq 4 \implies -2 \leq x \leq 2$. Domain: $[-2, 2]$.

The output is $\sqrt{4-x^2} \in [0, 2]$. Range: $[0, 2]$.

$g(x) = \ln(x - 1)$: domain requires $x - 1 > 0 \implies x > 1$. Domain: $(1, \infty)$. Range: $(-\infty, \infty)$.

## Remember

Domain and range are fundamental to **financial model validity**. Log-return models require $S_t > 0$ (the domain of $\ln$); GARCH variance equations must stay positive (domain constraint on the conditional variance); call option payoffs have range $[0, \infty)$ while put payoffs have range $[0, K]$. Domain errors in code (passing a negative number to `sqrt` or a non-positive number to `log`) are among the most common runtime failures in quantitative finance systems. In risk management, the **domain of applicability** of a model defines the scenarios for which its outputs are valid — using a model outside its domain generates spurious risk estimates.
