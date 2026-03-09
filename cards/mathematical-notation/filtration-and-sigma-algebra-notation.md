# Filtration and Sigma-Algebra Notation

**Topic:** Mathematical Notation
**Tags:** filtration, sigma-algebra, information set, probability space, stochastic processes
**Created:** 2026-03-09
**Author:** Claude Sonnet 4.6

---

## Definition

A **probability space** $(\Omega, \mathcal{F}, \mathbb{P})$ consists of a sample space $\Omega$, a sigma-algebra $\mathcal{F}$ (the collection of measurable events), and a probability measure $\mathbb{P}$. A **filtration** $\{\mathcal{F}_t\}_{t \geq 0}$ is an increasing family of sigma-algebras that models the accumulation of information over time: if $s \leq t$ then $\mathcal{F}_s \subseteq \mathcal{F}_t$.

| Symbol | Read as | Meaning |
|---|---|---|
| $\Omega$ | "omega" | The set of all possible outcomes (sample space) |
| $\mathcal{F}$ | "script F" | Sigma-algebra: the collection of events we can assign probabilities to |
| $\mathbb{P}$ | "P" | Probability measure on $(\Omega, \mathcal{F})$ |
| $\mathcal{F}_t$ | "F sub t" | The information available at time $t$ |
| $\{\mathcal{F}_t\}_{t \geq 0}$ | "the filtration" | The full history of information as $t$ grows |
| $X \in \mathcal{F}_t$ | "X is $\mathcal{F}_t$-measurable" | $X$ is known (determined) by time $t$ |

## Key Formula

The **adaptedness** condition for a stochastic process $(X_t)_{t \geq 0}$:

$$X_t \text{ is } \mathcal{F}_t\text{-measurable for all } t \geq 0$$

The **increasing** property of a filtration:

$$s \leq t \implies \mathcal{F}_s \subseteq \mathcal{F}_t$$

Combined with $\mathbb{P}$, the filtered probability space is written $(\Omega, \mathcal{F}, \{\mathcal{F}_t\}_{t \geq 0}, \mathbb{P})$.

## Example

Consider a stock observed daily over two days. At time 0: $\mathcal{F}_0 = \{\emptyset, \Omega\}$ (trivial — no information). At time 1: $\mathcal{F}_1$ contains events like $\{S_1 > 100\}$ — the first day's price is now known. At time 2: $\mathcal{F}_2 \supseteq \mathcal{F}_1$ and additionally contains events like $\{S_2 > 110\}$. The stock price $S_t$ is $\mathcal{F}_t$-measurable (you know today's price today), but tomorrow's price $S_{t+1}$ is not $\mathcal{F}_t$-measurable (it is unknown).

## Remember

Every formula in derivatives pricing that writes $E[\cdot \mid \mathcal{F}_t]$ is implicitly using a filtration. The sigma-algebra $\mathcal{F}_t$ is not just abstract algebra — it is the precise mathematical encoding of "market information up to time $t$". When a trading strategy is described as **adapted**, it means the trader cannot look into the future: each decision $H_t$ belongs to $\mathcal{F}_t$. This no-future-peeking requirement is what makes a hedging strategy physically realisable.
