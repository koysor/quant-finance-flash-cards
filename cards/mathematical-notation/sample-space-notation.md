# Sample Space Notation

**Topic:** Mathematical Notation
**Tags:** notation, sample space, omega, events, probability space
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **sample space** $\Omega$ is the set of all possible outcomes of a random experiment. Every probability statement is ultimately a statement about subsets of $\Omega$.

| Symbol | Read as | Meaning |
|---|---|---|
| $\Omega$ | "omega" | The sample space — the universal set of all outcomes |
| $\omega$ | "lowercase omega" | A single outcome: one element of $\Omega$ |
| $A \subseteq \Omega$ | "A is a subset of omega" | An **event** — a collection of outcomes we assign a probability to |
| $\emptyset$ | "empty set" | The impossible event: $P(\emptyset) = 0$ |
| $\Omega$ itself | "the certain event" | $P(\Omega) = 1$ — some outcome always occurs |
| $(\Omega, \mathcal{F}, \mathbb{P})$ | "the probability space" | Sample space + sigma-algebra + probability measure |

## Key Formula

**Kolmogorov's axioms** (the three rules all probabilities obey):

$$P(\Omega) = 1, \qquad P(A) \geq 0 \text{ for all } A \subseteq \Omega$$

$$P\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i) \quad \text{for pairwise disjoint events } A_i$$

**Partition of $\Omega$** (events $A_1, A_2, \ldots$ are a partition if):

$$A_i \cap A_j = \emptyset \text{ for } i \neq j, \qquad \bigcup_{i} A_i = \Omega$$

**Law of total probability** (using a partition $\{A_i\}$):

$$P(B) = \sum_{i} P(B \mid A_i)\,P(A_i)$$

## Example

**Discrete:** roll a fair die. $\Omega = \{1, 2, 3, 4, 5, 6\}$, each outcome $\omega \in \Omega$ has $P(\{\omega\}) = 1/6$. The event "even number" is $A = \{2, 4, 6\} \subseteq \Omega$ with $P(A) = 1/2$.

**Continuous:** tomorrow's log-return on an equity. $\Omega = \mathbb{R}$ (any real value is conceivable), $\omega$ is a specific return realisation, and the event "loss exceeds 5%" is $A = \{r < -0.05\} \subseteq \mathbb{R}$. $P(A) = F(-0.05)$ where $F$ is the CDF.

**Finance:** a Monte Carlo simulation of 10,000 scenarios defines a finite $\Omega = \{\omega_1, \ldots, \omega_{10000}\}$. Each scenario $\omega_i$ is one possible path of asset prices; the VaR estimate is the order statistic of losses across $\Omega$.

## Remember

$\Omega$ is the silent backdrop of every probability calculation — it sets the boundary of what is possible. In derivatives pricing, $\Omega$ contains all possible price paths; the risk-neutral measure $\mathbb{Q}$ and real-world measure $\mathbb{P}$ are two different ways of assigning probabilities to the *same* events in the *same* $\Omega$. When two models disagree, they usually differ in how they weight outcomes of $\Omega$, not in what $\Omega$ is.
