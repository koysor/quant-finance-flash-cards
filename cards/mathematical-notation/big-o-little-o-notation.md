# Big-O and Little-o Notation

**Topic:** Mathematical Notation
**Tags:** notation, Landau, big-O, little-o, asymptotics, error bounds, convergence
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

The **Landau symbols** are a family of notation for describing the comparative growth of functions as an argument tends to a limit. They are used throughout quantitative finance to state error bounds, convergence rates, and which terms survive in the continuous-time limit.

| Symbol | Read as | Meaning | Intuition |
|---|---|---|---|
| $f = O(g)$ | "big-O of $g$" | $\lvert f \rvert \leq C\lvert g \rvert$ near the limit | $f$ grows **no faster than** $g$ |
| $f = o(g)$ | "little-o of $g$" | $f/g \to 0$ at the limit | $f$ grows **strictly slower than** $g$ |
| $f = \Omega(g)$ | "big-Omega of $g$" | $\lvert f \rvert \geq c\lvert g \rvert$ near the limit | $f$ grows **at least as fast as** $g$ |
| $f = \Theta(g)$ | "big-Theta of $g$" | $f = O(g)$ and $f = \Omega(g)$ | $f$ grows **at the same rate as** $g$ |
| $f \sim g$ | "$f$ asymptotic to $g$" | $f/g \to 1$ at the limit | $f$ and $g$ are **asymptotically equal** |

The limit is always specified by context: $h \to 0$ (step sizes), $n \to \infty$ (sample sizes), $k \to \infty$ (large strikes).

## Key Formula

**Hierarchy** as $h \to 0$ (most common in finance):

$$o(1) \;\supset\; O(h) \;\supset\; o(h) \;\supset\; O(h^2) \;\supset\; o(h^2) \;\supset\; \cdots$$

**Itô multiplication table** (quadratic terms in stochastic calculus):

$$dt \cdot dt = o(dt), \qquad dW_t \cdot dt = o(dt), \qquad dW_t \cdot dW_t = dt$$

**Numerical scheme convergence** (Taylor expansion remainder):

$$e^h = 1 + h + \tfrac{h^2}{2} + O(h^3)$$

$$f(x+h) = f(x) + hf'(x) + O(h^2) \qquad \text{(first-order finite difference)}$$

## Example

An Euler–Maruyama scheme for an SDE has **strong order** $O(\Delta t^{1/2})$ and **weak order** $O(\Delta t)$:

- Strong order $O(\Delta t^{1/2})$: the expected path-wise error $E[\lvert X_T^{\text{approx}} - X_T \rvert]$ scales as $\sqrt{\Delta t}$ — halving $\Delta t$ reduces path error by a factor of $\sqrt{2} \approx 1.41$.
- Weak order $O(\Delta t)$: the error in expectations $\lvert E[f(X_T^{\text{approx}})] - E[f(X_T)] \rvert$ scales as $\Delta t$ — halving $\Delta t$ halves the pricing error.

The distinction matters because **pricing** requires only weak convergence, so a scheme with better weak order (e.g. Milstein, $O(\Delta t)$ strong) is not necessarily worth its extra implementation cost over Euler.

## Remember

In Itô's lemma, the critical step is identifying which terms are $O(dt)$ and which are $o(dt)$. The term $(dW_t)^2 = dt$ is $O(dt)$ and **must be kept** — it produces the $\frac{1}{2}\sigma^2 S^2 \partial^2 V/\partial S^2$ term in the Black-Scholes PDE. The term $(dt)^2$ is $o(dt)$ and is **discarded**. Getting this wrong produces either the wrong PDE or the wrong stochastic integral. The Landau notation makes these decisions explicit and auditable: every term carries its own growth label, so the reader can verify independently which terms survive the continuous-time limit.
