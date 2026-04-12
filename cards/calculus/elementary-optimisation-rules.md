# Elementary Optimisation Rules

**Topic:** Calculus
**Tags:** optimisation, minimax duality, affine invariance, objective function, mean-variance optimisation, portfolio theory
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

Two fundamental rules that let you rewrite any optimisation problem into a more convenient form without changing the solution.

**Rule 1 — Min/Max Duality:** any maximisation problem can be converted to a minimisation problem by negating the objective. The two problems share the same optimal point $x^*$.

**Rule 2 — Affine Transformation Invariance:** for constants $a$ and $b > 0$, scaling or shifting the objective never changes the optimal point. The maximiser of $a + b \cdot f(x)$ is identical to the maximiser of $f(x)$.

## Key Formula

**Rule 1:**

$$\max_x f(x) \equiv -\min_x \bigl(-f(x)\bigr)$$

**Rule 2:** for constants $a \in \mathbb{R}$, $b > 0$,

$$\operatorname*{arg\,max}_x \bigl(a + b \cdot f(x)\bigr) = \operatorname*{arg\,max}_x f(x)$$

**Mean-variance equivalence** (combining both rules):

$$\max_w \Bigl[w^\top\mu - \tfrac{\lambda}{2}\,w^\top\Sigma w\Bigr] \;\equiv\; \min_w \Bigl[\tfrac{\lambda}{2}\,w^\top\Sigma w - w^\top\mu\Bigr]$$

Both share the same optimal weights $w^*$; $\lambda > 0$ is the risk-aversion coefficient.

## Example

Show that maximising $U(w) = w^\top\mu - \tfrac{\lambda}{2}\,w^\top\Sigma w$ is equivalent to the standard minimisation form of MVO.

Negate the objective (Rule 1):

$$\max_w U(w) \equiv -\min_w \bigl(-U(w)\bigr) = -\min_w \Bigl[-w^\top\mu + \tfrac{\lambda}{2}\,w^\top\Sigma w\Bigr]$$

The outer negation does not affect $w^*$, so solving

$$\min_w \Bigl[\tfrac{\lambda}{2}\,w^\top\Sigma w - w^\top\mu\Bigr]$$

gives the same optimal portfolio. Neither the additive constant nor the positive scalar $\lambda$ alters the solution (Rule 2).

## Remember

The **mean-variance optimisation (MVO)** problem appears in two equivalent forms in textbooks and software: a utility-maximisation form and a variance-minimisation form. Elementary optimisation rules explain why both give the same portfolio $w^*$. In practice, solvers are written for minimisation (e.g. `scipy.optimize.minimize`), so Rule 1 lets you pass any mean-variance objective directly without reformulating by hand. Rule 2 means you can absorb $\lambda$ into the objective freely — a useful trick when deriving the closed-form solution $w^* = \tfrac{1}{\lambda}\Sigma^{-1}\mu$ for unconstrained MVO.
