# Complement Notation

**Topic:** Mathematical Notation
**Tags:** notation, complement, NOT, opposite event, survival probability
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **complement** $A^c$ is the event that $A$ does not occur — all outcomes in $\Omega$ that are not in $A$. It is the "NOT" operation on events.

| Symbol | Read as | Meaning |
|---|---|---|
| $A^c$ | "A complement" or "not A" | All outcomes where $A$ does not occur |
| $\bar{A}$ | "A bar" or "not A" | Alternative notation for $A^c$ (common in engineering) |
| $A'$ | "A prime" | Another alternative for $A^c$ (less common in finance) |
| $\Omega \setminus A$ | "omega minus A" | Set difference: $\Omega$ with $A$ removed — same as $A^c$ |
| $1 - P(A)$ | "one minus P of A" | The probability of the complement |

## Key Formula

**Complement rule:**

$$P(A^c) = 1 - P(A)$$

**De Morgan's laws:**

$$(A \cup B)^c = A^c \cap B^c \qquad \text{"not (A or B)" = "not A and not B"}$$

$$(A \cap B)^c = A^c \cup B^c \qquad \text{"not (A and B)" = "not A or not B"}$$

**Partition of $\Omega$:**

$$A \cup A^c = \Omega, \qquad A \cap A^c = \emptyset, \qquad P(A) + P(A^c) = 1$$

## Example

**Survival probability:** $D$ = {bond defaults within 5 years}. Then $D^c$ = {bond survives 5 years}. If $P(D) = 0.04$, then the survival probability $P(D^c) = 0.96$.

**Default-free portfolio:** at least one of $n$ bonds defaults is the complement of none defaulting: $P(\bigcup D_i) = 1 - P(\bigcap D_i^c)$. With $n = 100$ bonds each with $P(D_i) = 1\%$ and assuming independence: $P(\text{at least one default}) = 1 - (0.99)^{100} \approx 63.4\%$.

## Remember

The complement rule $P(A^c) = 1 - P(A)$ converts "at least one" problems into "none at all" problems, which are often easier to calculate. De Morgan's laws let you push complements through unions and intersections — essential when working with complex event algebra in credit risk, where the event of interest (joint default) may be easier to handle as the complement of the event of joint survival.
