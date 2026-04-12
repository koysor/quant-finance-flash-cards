# Event

**Topic:** Probability
**Tags:** event, sample space, set theory, probability axioms, union, complement
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

An **event** is any subset $A \subseteq \Omega$ of the sample space to which a probability can be assigned. Events are the fundamental objects that probability measures act on.

| Type | Notation | Meaning |
|---|---|---|
| Elementary event | $\{\omega\}$ | A singleton — exactly one outcome occurs |
| Compound event | $A \subseteq \Omega,\; \lvert A \rvert > 1$ | Multiple outcomes are grouped together |
| Impossible event | $\emptyset$ | No outcome in the event occurs; $P(\emptyset) = 0$ |
| Certain event | $\Omega$ | Some outcome always occurs; $P(\Omega) = 1$ |

Events can be combined using standard **set operations**:

- **Union** $A \cup B$: at least one of $A$ or $B$ occurs
- **Intersection** $A \cap B$: both $A$ and $B$ occur simultaneously
- **Complement** $A^c = \Omega \setminus A$: $A$ does not occur

## Key Formula

$$P(A \cup B) = P(A) + P(B) - P(A \cap B) \qquad \text{(inclusion–exclusion)}$$

$$P(A^c) = 1 - P(A) \qquad \text{(complement rule)}$$

$$P(\emptyset) = 0, \qquad P(\Omega) = 1$$

If $A$ and $B$ are **mutually exclusive** ($A \cap B = \emptyset$):

$$P(A \cup B) = P(A) + P(B)$$

## Example

A credit portfolio contains three bonds: X, Y, Z. The sample space of default events is:

$$\Omega = \{\emptyset, X, Y, Z, XY, XZ, YZ, XYZ\}$$

Define the event "at least one bond defaults" as $A = \Omega \setminus \{\emptyset\}$. Define $B = \{XY, XZ, YZ, XYZ\}$ as "at least two bonds default". Then:

$$A \cap B = B, \qquad A \cup B = A, \qquad B^c = \{\emptyset, X, Y, Z\}$$

If each bond defaults independently with probability $p = 0.02$:

$$P(A) = 1 - P(\emptyset) = 1 - (1-0.02)^3 \approx 0.0588$$

## Remember

In **credit risk**, a portfolio loss model assigns a probability to every event in $\Omega$ — the set of all possible default combinations. The **Value at Risk (VaR)** at 99% confidence is the boundary of the event "portfolio loss exceeds $L$": you find the smallest $L$ such that $P(\text{loss} > L) \leq 0.01$. The complement rule means that controlling the tail event (the 1% worst outcomes) is equivalent to characterising the 99% central event — this duality underpins every VaR and CVaR calculation.
