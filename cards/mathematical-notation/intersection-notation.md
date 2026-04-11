# Intersection Notation

**Topic:** Mathematical Notation
**Tags:** notation, intersection, joint probability, AND, events
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **intersection** $A \cap B$ is the event that both $A$ and $B$ occur simultaneously. In probability, it represents the joint occurrence of two events.

| Symbol | Read as | Meaning |
|---|---|---|
| $A \cap B$ | "A intersect B" or "A and B" | The event that both $A$ and $B$ occur |
| $A \cap B \cap C$ | "A and B and C" | All three events occur simultaneously |
| $\bigcap_{i=1}^{n} A_i$ | "intersection of A1 to An" | All $n$ events occur simultaneously |
| $A \cap B = \emptyset$ | "A and B are disjoint" or "mutually exclusive" | $A$ and $B$ cannot both occur |

## Key Formula

**Probability of intersection:**

$$P(A \cap B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A)$$

**Special case — independent events:**

$$A \perp\!\!\!\perp B \implies P(A \cap B) = P(A)\,P(B)$$

**Inclusion–exclusion:**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Continuous RV equivalent** (joint density):

$$P(X \leq x, Y \leq y) = \int_{-\infty}^{y}\int_{-\infty}^{x} f_{X,Y}(u,v)\,du\,dv$$

## Example

In credit risk: $D$ = {bond defaults}, $R$ = {rating downgrade occurs first}. Then $D \cap R$ = {bond is downgraded and then defaults}. The conditional probability $P(D \mid R)$ is the default probability given a prior downgrade — higher than the unconditional $P(D)$ because downgrade and default are positively associated, so $P(D \cap R) > P(D)\,P(R)$.

## Remember

The intersection $A \cap B$ is the "AND" of two events: both must happen. It appears in Bayes' theorem through $P(A \mid B) = P(A \cap B)/P(B)$, in the law of total probability through disjoint intersections, and in joint distributions where $P(X \leq x, Y \leq y)$ is the intersection event $\{X \leq x\} \cap \{Y \leq y\}$.
