# Little-o Notation

**Topic:** Calculus
**Tags:** asymptotics, approximation, convergence, limits, error analysis
**Created:** 2026-03-15
**Author:** Claude Opus 4.6

---

## Definition

Little-o notation describes a function that becomes negligible relative to another function as the argument tends to a limit. Writing $f(x) = o(g(x))$ as $x \to a$ means the ratio $f(x)/g(x) \to 0$. Where Big-O says "grows no faster than", little-o says "grows strictly slower than". In quantitative finance, little-o terms are the parts of an expansion that vanish so quickly they can be safely discarded — for instance, when deriving Ito's lemma the higher-order terms in $dt$ are $o(dt)$ and are dropped to obtain the final stochastic differential.

## Key Formula

$$f(x) = o\bigl(g(x)\bigr) \text{ as } x \to a \;\;\Longleftrightarrow\;\; \lim_{x \to a} \frac{f(x)}{g(x)} = 0$$

Equivalently, for any $\varepsilon > 0$ there exists $\delta > 0$ such that $|f(x)| \leq \varepsilon\,|g(x)|$ for all $0 < |x - a| < \delta$.

A common application — the Taylor expansion with little-o remainder:

$$f(x) = f(a) + f'(a)(x - a) + \tfrac{1}{2}f''(a)(x - a)^2 + o\bigl((x - a)^2\bigr)$$

## Example

Consider $f(h) = h^2$ and $g(h) = h$ as $h \to 0$:

$$\frac{f(h)}{g(h)} = \frac{h^2}{h} = h \;\xrightarrow{h \to 0}\; 0$$

So $h^2 = o(h)$. Concretely, at $h = 0.01$: $h = 0.01$ but $h^2 = 0.0001$ — the squared term is 100 times smaller and becomes negligible.

This is why, in the derivation of Ito's lemma, the term $\tfrac{1}{2}f''(S)\,(\Delta S)^2\,\Delta t$ is $o(\Delta t)$ and is discarded: it shrinks faster than $\Delta t$ itself as the time step tends to zero.

## Remember

Little-o notation is the formal justification for dropping "small" terms in stochastic calculus. When deriving the Black–Scholes equation from Ito's lemma, terms like $(\Delta t)^{3/2}$ and $(\Delta t)^2$ are $o(\Delta t)$ — they vanish faster than $\Delta t$ as the time step shrinks to zero. Recognising which terms are $o(\Delta t)$ versus $O(\Delta t)$ is precisely what determines which parts of a Taylor expansion survive in the continuous-time limit, and therefore which terms appear in the final pricing PDE.
