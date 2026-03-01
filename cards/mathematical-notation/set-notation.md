# Set Notation

**Topic:** Mathematical Notation
**Tags:** notation, sets, events, probability
**Author:** Claude Opus 4.6

---

## Definition

**Set notation** provides a formal language for describing collections of objects and the relationships between them. In probability and finance, sets represent events, sample spaces, and asset universes.

Key symbols:

- $\in$ — element of: $x \in A$ means "$x$ belongs to set $A$"
- $\subseteq$ — subset: $A \subseteq B$ means every element of $A$ is also in $B$
- $\cup$ — union: $A \cup B$ is the set of elements in $A$ **or** $B$ (or both)
- $\cap$ — intersection: $A \cap B$ is the set of elements in both $A$ **and** $B$
- $A^c$ — complement: the set of elements **not** in $A$
- $\emptyset$ — empty set: the set with no elements
- $\Omega$ — sample space: the set of all possible outcomes

## Key Formula

**De Morgan's laws** (complement distributes over union/intersection):

$$(A \cup B)^c = A^c \cap B^c$$

$$(A \cap B)^c = A^c \cup B^c$$

**Probability axioms** (Kolmogorov):

$$P(\Omega) = 1, \qquad P(A) \geq 0, \qquad P\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i) \text{ for disjoint } A_i$$

**Inclusion–exclusion** (two events):

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Conditional probability:**

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

## Example

Consider a bond portfolio. Let $D$ = {bonds that default} and $I$ = {bonds rated investment-grade}. The event "an investment-grade bond defaults" is:

$$D \cap I$$

The probability that a bond either defaults **or** is not investment-grade is:

$$P(D \cup I^c) = P(D) + P(I^c) - P(D \cap I^c)$$

If $P(D) = 0.03$, $P(I^c) = 0.20$, and $P(D \cap I^c) = 0.025$:

$$P(D \cup I^c) = 0.03 + 0.20 - 0.025 = \textbf{0.205}$$

## Remember

- Set notation is the language of **probability theory** — every probability statement is a statement about sets of outcomes within the sample space $\Omega$.
- **Bayes' theorem** is built on conditional probability $P(A \mid B) = P(A \cap B) / P(B)$, which requires understanding intersection and complement.
- In measure-theoretic probability, a **sigma-algebra** $\mathcal{F}$ is a collection of subsets of $\Omega$ that is closed under complement and countable union — the formal foundation for defining what events can be assigned probabilities.
