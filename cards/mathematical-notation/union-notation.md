# Union Notation

**Topic:** Mathematical Notation
**Tags:** notation, union, OR, events, inclusion-exclusion
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **union** $A \cup B$ is the event that at least one of $A$ or $B$ occurs. It is the "OR" operation on events.

| Symbol | Read as | Meaning |
|---|---|---|
| $A \cup B$ | "A union B" or "A or B" | At least one of $A$ or $B$ occurs |
| $A \cup B \cup C$ | "A or B or C" | At least one of the three events occurs |
| $\bigcup_{i=1}^{n} A_i$ | "union of A1 to An" | At least one of $n$ events occurs |
| $\bigcup_{i=1}^{\infty} A_i$ | "countable union" | At least one event in the infinite sequence occurs |
| $A \cup A^c = \Omega$ | "A union its complement is certain" | Either $A$ happens or it doesn't — one is guaranteed |

## Key Formula

**Inclusion–exclusion (two events):**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Mutually exclusive events** ($A \cap B = \emptyset$):

$$P(A \cup B) = P(A) + P(B)$$

**Union bound (Boole's inequality):**

$$P\!\left(\bigcup_{i=1}^{n} A_i\right) \leq \sum_{i=1}^{n} P(A_i)$$

**Countable additivity** (Kolmogorov axiom — for pairwise disjoint events):

$$P\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$

## Example

In a two-bond portfolio: $D_1$ = {bond 1 defaults}, $D_2$ = {bond 2 defaults}. Portfolio loss occurs if at least one defaults: $P(D_1 \cup D_2) = P(D_1) + P(D_2) - P(D_1 \cap D_2)$. With $P(D_1) = P(D_2) = 3\%$ and $P(D_1 \cap D_2) = 0.5\%$ (correlated defaults): $P(\text{loss}) = 3 + 3 - 0.5 = 5.5\%$. If defaults were independent: $P(D_1 \cap D_2) = 0.09\%$, giving $P(\text{loss}) = 5.91\%$.

## Remember

The inclusion–exclusion formula $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ subtracts $P(A \cap B)$ because the joint event is counted twice when adding $P(A)$ and $P(B)$. The union bound $P(\bigcup A_i) \leq \sum P(A_i)$ is used throughout finance to derive conservative upper bounds on portfolio loss probabilities without needing to compute all pairwise intersections.
