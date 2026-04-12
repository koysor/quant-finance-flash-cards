# Sample Space

**Topic:** Probability
**Tags:** sample space, events, outcomes, probability axioms, omega, probability space
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

The **sample space** $\Omega$ is the complete set of all possible outcomes of a random experiment. Each element $\omega \in \Omega$ is a single outcome; an **event** is any subset $A \subseteq \Omega$ to which a probability can be assigned. Together with a collection of events $\mathcal{F}$ and a probability measure $\mathbb{P}$, the triple $(\Omega, \mathcal{F}, \mathbb{P})$ is called a **probability space**.

| Symbol | Read as | Meaning |
|---|---|---|
| $\Omega$ | "omega" | The sample space — the universal set of all outcomes |
| $\omega$ | "lowercase omega" | A single outcome: one element of $\Omega$ |
| $A \subseteq \Omega$ | "$A$ is an event" | A subset of outcomes; we assign probability $P(A)$ to it |
| $\emptyset$ | "empty set" | The impossible event: $P(\emptyset) = 0$ |
| $(\Omega, \mathcal{F}, \mathbb{P})$ | "probability space" | The complete formal structure for a probability model |

## Key Formula

**Kolmogorov's three axioms** — the foundation from which every probability rule follows:

$$P(\Omega) = 1 \qquad (\text{some outcome always occurs})$$

$$P(A) \geq 0 \quad \text{for all events } A \subseteq \Omega$$

$$P(A \cup B) = P(A) + P(B) \quad \text{whenever } A \cap B = \emptyset \quad (\text{countable additivity})$$

**Complement rule** (derived from the axioms):

$$P(A^c) = 1 - P(A), \qquad A^c = \Omega \setminus A$$

## Example

**Discrete:** a credit analyst assesses whether a bond defaults this year.

$$\Omega = \{\text{default},\, \text{survive}\}$$

The event "bond defaults" is $A = \{\text{default}\}$ with $P(A) = 0.03$ (a 3% probability of default). By the complement rule, $P(\text{survive}) = 1 - 0.03 = 0.97$.

**Continuous:** tomorrow's log-return on an equity. $\Omega = \mathbb{R}$ — every real number is a conceivable return. The event "loss exceeds 2%" is $A = \{r < -0.02\} \subseteq \mathbb{R}$, and $P(A) = F(-0.02)$ where $F$ is the CDF.

## Remember

In a **Monte Carlo VaR calculation**, the simulator explicitly constructs a finite $\Omega$: each of the $N$ simulated market scenarios is one $\omega_i \in \Omega$, and VaR at the 99th percentile is simply the loss at the $0.01 \times N$-th order statistic across $\Omega$. The risk-neutral measure $\mathbb{Q}$ and real-world measure $\mathbb{P}$ are two different probability measures defined on the *same* $\Omega$ — they disagree on how likely each outcome is, not on which outcomes are possible.
