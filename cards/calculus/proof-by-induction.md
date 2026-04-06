# Proof by Induction

**Topic:** Calculus
**Tags:** proof by induction, mathematical induction, base case, inductive step, series, sequences
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Mathematical induction** is a proof technique for statements $P(n)$ that hold for all positive integers $n$. It consists of two steps: proving $P(1)$ is true (the **base case**), then proving that $P(k) \Rightarrow P(k+1)$ for all $k \geq 1$ (the **inductive step**). Together these guarantee $P(n)$ for all $n \in \mathbb{N}$.

## Key Formula

**Structure of an induction proof:**

1. **Base case:** verify $P(1)$ directly.
2. **Inductive hypothesis:** assume $P(k)$ holds for some $k \geq 1$.
3. **Inductive step:** using the hypothesis, prove $P(k+1)$.
4. **Conclusion:** $P(n)$ holds for all $n \geq 1$.

**Analogy:** an infinite row of dominoes — if the first falls (base case) and each falling domino knocks over the next (inductive step), then all dominoes fall.

## Example

Prove $\displaystyle\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$.

**Base case ($n = 1$):** LHS $= 1$, RHS $= \frac{1 \cdot 2}{2} = 1$. ✓

**Inductive step:** Assume $\sum_{i=1}^k i = \frac{k(k+1)}{2}$.

$$\sum_{i=1}^{k+1} i = \sum_{i=1}^k i + (k+1) = \frac{k(k+1)}{2} + (k+1) = \frac{(k+1)(k+2)}{2}$$

This is $P(k+1)$. ✓ By induction, the formula holds for all $n \geq 1$.

## Remember

Proof by induction establishes the closed-form formulas that underpin quantitative finance calculations. The **arithmetic series** formula $\sum i = n(n+1)/2$ is proved by induction — and this formula appears in the calculation of total coupon payments and accrued interest. The **geometric series** formula $\sum r^k = (1-r^{n+1})/(1-r)$ is likewise proved by induction — and this is the annuity formula that prices every bond and fixed-rate loan. Understanding induction means understanding why these formulas are *certain*, not just empirically observed.
