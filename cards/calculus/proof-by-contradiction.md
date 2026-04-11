# Proof by Contradiction

**Topic:** Calculus
**Tags:** proof by contradiction, reductio ad absurdum, irrational numbers, logic, mathematical proof
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Proof by contradiction** (reductio ad absurdum) proves a statement $P$ by assuming its negation $\neg P$ is true, then deriving a logical contradiction — a statement that is always false. Since a contradiction cannot hold, the assumption $\neg P$ must be false, so $P$ must be true. It is most powerful when the negation of $P$ has a clear, exploitable structure.

## Key Formula

**Structure:**

1. Assume $\neg P$ (the negation of what you want to prove).
2. Using valid logical steps, derive a statement $Q$ that is known to be false (or contradicts a known truth or a prior assumption).
3. Conclude: since $\neg P \implies Q$ (false), $\neg P$ must be false, therefore $P$ is true.

**Formal:** $(\neg P \implies \text{False}) \implies P$

## Example

**Prove $\sqrt{2}$ is irrational.**

Assume $\neg P$: $\sqrt{2}$ is rational, i.e. $\sqrt{2} = p/q$ in lowest terms ($p, q \in \mathbb{Z}$, $\gcd(p,q)=1$).

$$2 = \frac{p^2}{q^2} \implies p^2 = 2q^2 \implies p^2 \text{ is even} \implies p \text{ is even} \implies p = 2k$$

$$p^2 = 4k^2 = 2q^2 \implies q^2 = 2k^2 \implies q \text{ is even}$$

But then $p$ and $q$ are both even, contradicting $\gcd(p,q)=1$. **Contradiction.** $\therefore \sqrt{2}$ is irrational. $\blacksquare$

## Remember

Proof by contradiction establishes two results that underpin quantitative finance: the **irrationality of $\sqrt{2}$** (fundamental to the geometry of risk diversification — the Pythagorean relationship between variance terms produces irrational quantities) and the **infinitude of primes** (relevant to cryptographic protocols in financial system security). More directly, the **no-arbitrage principle** is proved by contradiction: assuming an arbitrage opportunity exists leads to a contradiction (an investor with zero cost can accumulate infinite wealth, violating market clearing conditions), so no such opportunity can exist in equilibrium.
