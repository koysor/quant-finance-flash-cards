# Probability Measure

**Topic:** Probability
**Tags:** measure theory, kolmogorov axioms, risk-neutral measure, radon-nikodym, change of measure, sigma-algebra
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

A **probability measure** $P$ is a function $P: \mathcal{F} \to [0,1]$ defined on a sigma-algebra $\mathcal{F}$ of subsets of a sample space $\Omega$, satisfying Kolmogorov's three axioms:

1. **Non-negativity:** $P(A) \geq 0$ for all $A \in \mathcal{F}$
2. **Normalisation:** $P(\Omega) = 1$
3. **Countable additivity:** for any countable collection of disjoint events $A_1, A_2, \ldots$,

$$P\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$

The triple $(\Omega, \mathcal{F}, P)$ is called a **probability space**. Multiple distinct probability measures can be defined on the same measurable space $(\Omega, \mathcal{F})$.

## Key Formula

Two probability measures $P$ and $Q$ on $(\Omega, \mathcal{F})$ are **equivalent** (mutually absolutely continuous) if they assign zero probability to exactly the same events. When $P \sim Q$, the **Radon-Nikodym theorem** guarantees a strictly positive density:

$$\frac{dQ}{dP} = \xi, \qquad Q(A) = \int_A \xi \, dP \quad \forall A \in \mathcal{F}$$

The random variable $\xi = dQ/dP$ is called the **Radon-Nikodym derivative** (or **likelihood ratio**). It converts expectations under $P$ to expectations under $Q$:

$$\mathbb{E}^Q[X] = \mathbb{E}^P\!\left[\frac{dQ}{dP} \cdot X\right]$$

## Example

Consider a one-step binomial model. Stock $S_0 = 100$ moves to $S_u = 110$ (up) or $S_d = 95$ (down). Suppose the real-world probabilities are $P(u) = 0.6$, $P(d) = 0.4$ and the risk-free rate $r = 0.02$.

The risk-neutral probabilities satisfying $S_0 = e^{-r}\mathbb{E}^Q[S_1]$ are:

$$q = \frac{S_0 e^r - S_d}{S_u - S_d} = \frac{100 \times 1.02 - 95}{110 - 95} = \frac{7}{15} \approx 0.467$$

The Radon-Nikodym derivative at each outcome:

$$\frac{dQ}{dP}(\text{up}) = \frac{q}{P(u)} \approx \frac{0.467}{0.6} \approx 0.778, \qquad \frac{dQ}{dP}(\text{down}) = \frac{1-q}{P(d)} \approx \frac{0.533}{0.4} \approx 1.333$$

Both $P$ and $Q$ assign positive probability to each outcome, so they are equivalent measures on the same $(\Omega, \mathcal{F})$.

## Remember

In derivatives pricing, the **real-world measure $P$** reflects observed statistical frequencies — it governs how asset prices actually evolve and is used in risk management and scenario analysis. The **risk-neutral measure $Q$** is a different probability measure on the same sample space, constructed so that all discounted asset prices are martingales; option prices are simply discounted expectations under $Q$.

The Radon-Nikodym derivative $dQ/dP$ is the mathematical bridge between them — in continuous time, this is the **Girsanov kernel**, and the change of measure shifts the drift of Brownian motion from the real-world drift $\mu$ to the risk-free rate $r$. Confusing $P$ and $Q$ — for instance, discounting at $r$ but using real-world drift $\mu$ — is a fundamental pricing error that the measure-theoretic framework makes impossible to overlook.
