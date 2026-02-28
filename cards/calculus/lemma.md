# Lemma

**Topic:** Calculus
**Tags:** lemma, proof, theorem, mathematical reasoning, logic
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

A **lemma** is a proven mathematical statement that serves as a stepping stone towards proving a larger theorem. Lemmas break complex proofs into smaller, manageable pieces and are often reused across multiple proofs. Once proved, a lemma carries the same certainty as a theorem — the distinction is one of role, not rigour.

## Key Formula

A lemma follows the standard structure of a mathematical proof:

$$\text{If } P \text{ (hypotheses), then } Q \text{ (conclusion)}$$

For example, a lemma might establish that for any twice-differentiable function $f$ and small increment $h$:

$$f(x + h) = f(x) + f'(x)h + \frac{1}{2}f''(x)h^2 + O(h^3)$$

This Taylor expansion lemma is then used inside larger proofs without repeating its derivation each time.

## Example

**Lemma:** If $X$ and $Y$ are independent random variables, then $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$.

**Proof:** $\operatorname{Var}(X + Y) = E[(X+Y)^2] - (E[X+Y])^2$. Expanding and using independence ($E[XY] = E[X]E[Y]$):

$$= E[X^2] + 2E[X]E[Y] + E[Y^2] - (E[X])^2 - 2E[X]E[Y] - (E[Y])^2$$

$$= \operatorname{Var}(X) + \operatorname{Var}(Y)$$

This lemma underpins the square-root rule: if daily returns are independent with equal variance $\sigma^2$, then $n$-day variance is $n\sigma^2$ and $n$-day volatility is $\sigma\sqrt{n}$.

## Remember

In quantitative finance, the most famous lemma is **Itô's Lemma**, which extends the chain rule to stochastic processes and is the key stepping stone to deriving the Black-Scholes PDE. Recognising that a lemma is a reusable building block helps you understand why Itô's result appears in nearly every continuous-time derivation — it was proved once, and every subsequent proof simply invokes it.
