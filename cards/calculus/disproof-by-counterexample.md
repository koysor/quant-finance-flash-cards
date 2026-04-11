# Disproof by Counterexample

**Topic:** Calculus
**Tags:** counterexample, disproof, universal statement, conjecture, mathematical proof
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **universal statement** of the form "for all $x$, $P(x)$ is true" ($\forall x: P(x)$) is disproved by exhibiting a single **counterexample** — one specific value $x_0$ for which $P(x_0)$ is false. A single counterexample is sufficient to disprove a universal claim entirely, no matter how often the statement holds for other values.

## Key Formula

To disprove $\forall x \in S: P(x)$, find one $x_0 \in S$ such that $P(x_0)$ is false.

**Logical structure:** $\neg(\forall x: P(x)) \equiv \exists x: \neg P(x)$

**Common approach:** try small integers, fractions, negatives, zero, or boundary cases as candidates.

## Example

**Conjecture:** $n^2 + n + 41$ is prime for all positive integers $n$.

Check: $n=1: 43$ ✓, $n=2: 47$ ✓, ..., $n=40: 1681 = 41^2$ ✗

**Counterexample:** $n = 40 \implies n^2 + n + 41 = 1681 = 41^2$, which is not prime.

The conjecture is false, despite holding for 39 consecutive values.

**Second example:** disprove "$a^2 > a$ for all real $a$". Counterexample: $a = 0.5 \implies 0.25 < 0.5$. ✗

## Remember

Disproof by counterexample is how **risk model failures are identified in practice**. The statement "value-at-risk is sub-additive for all portfolios" was a long-held conjecture, and a single counterexample (two portfolios whose combined VaR exceeds the sum of individual VaRs) disproved it — leading to the development of **Expected Shortfall (CVaR)** as a coherent risk measure. In model validation, finding one scenario where a model produces an absurd result (negative prices, probability > 1, infinite Greeks) is sufficient to identify a model deficiency, regardless of how well the model performs elsewhere.
