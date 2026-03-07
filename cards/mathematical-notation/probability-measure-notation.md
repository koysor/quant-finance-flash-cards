# Probability Measure Notation

**Topic:** Mathematical Notation
**Tags:** notation, measure theory, filtration, sigma-algebra, probability space
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

**Probability measure notation** provides the formal language for describing probability spaces, information structures, and measure changes — the mathematical foundations of stochastic finance.

| Symbol | Read as | Meaning |
|---|---|---|
| $(\Omega, \mathcal{F}, \mathbb{P})$ | "the probability space omega, F, P" | Sample space, sigma-algebra, probability measure |
| $\Omega$ | "omega" | The set of all possible outcomes |
| $\mathcal{F}$ | "script F" or "the sigma-algebra" | Collection of events that can be assigned probabilities |
| $\mathbb{P}$ | "P" (blackboard bold) | The real-world (physical) probability measure |
| $\mathbb{Q}$ | "Q" | The risk-neutral probability measure |
| $\mathcal{F}_t$ | "F sub t" or "the filtration at time $t$" | Information available up to time $t$ |
| $\{\mathcal{F}_t\}_{t \geq 0}$ | "the filtration" | The growing family of information sets |
| $d\mathbb{Q}/d\mathbb{P}$ | "dQ dP" | Radon–Nikodým derivative; density for measure change |

## Key Formula

**Risk-neutral pricing formula** (ties all the notation together):

$$V_0 = E^{\mathbb{Q}}\!\left[e^{-rT} \, \text{payoff}(S_T) \;\middle|\; \mathcal{F}_0\right]$$

This reads: "the price today equals the discounted expected payoff under the risk-neutral measure $\mathbb{Q}$, conditional on information at time 0."

**Adapted process:** $X_t$ is $\mathcal{F}_t$-measurable means $X_t$ depends only on information available at time $t$ — no looking into the future.

## Example

In a two-period binomial model: $\Omega = \{uu, ud, du, dd\}$ (sequences of up/down moves).

- $\mathcal{F}_0 = \{\emptyset, \Omega\}$ — at time 0 you know nothing
- $\mathcal{F}_1 = \{\emptyset, \{uu, ud\}, \{du, dd\}, \Omega\}$ — after one step, you know the first move
- $\mathcal{F}_2 = $ all subsets of $\Omega$ — after two steps, you know everything

The filtration $\mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \mathcal{F}_2$ models information arriving over time.

## Remember

This notation appears dense but encodes a simple idea: **who knows what, and when**. The filtration $\mathcal{F}_t$ is the mathematical model of information flow — at each time $t$, you can distinguish between certain outcomes but not others. The condition "$X_t$ is $\mathcal{F}_t$-adapted" means your trading strategy cannot use future information (no insider trading, mathematically enforced). The two measures $\mathbb{P}$ and $\mathbb{Q}$ see the same events as possible but weight them differently — $\mathbb{P}$ for forecasting real-world probabilities, $\mathbb{Q}$ for pricing derivatives as discounted expected payoffs.
