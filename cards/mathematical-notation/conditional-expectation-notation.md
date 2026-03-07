# Conditional Expectation Notation

**Topic:** Mathematical Notation
**Tags:** notation, conditional expectation, filtration, information, probability
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

**Conditional expectation notation** expresses the expected value of a random variable given partial information. The conditioning can be on a specific event, a random variable, or a filtration (information set) — each form appears throughout stochastic finance.

| Symbol | Read as | Meaning |
|---|---|---|
| $E[X \mid A]$ | "expectation of $X$ given event $A$" | Expected value restricted to outcomes where $A$ occurs |
| $E[X \mid Y]$ | "expectation of $X$ given $Y$" | A function of $Y$: the best prediction of $X$ knowing $Y$ |
| $E[X \mid Y = y]$ | "expectation of $X$ given $Y$ equals $y$" | A specific number for each value $y$ |
| $E[X \mid \mathcal{F}_t]$ | "expectation of $X$ given $\mathcal{F}_t$" | Best prediction of $X$ using all information available at time $t$ |
| $E_t[X]$ | "time-$t$ expectation of $X$" | Shorthand for $E[X \mid \mathcal{F}_t]$ |

## Key Formula

**Tower property** (iterated expectations):

$$E\!\big[E[X \mid \mathcal{F}_t] \mid \mathcal{F}_s\big] = E[X \mid \mathcal{F}_s], \qquad s \leq t$$

**Martingale property** written in this notation:

$$E[M_t \mid \mathcal{F}_s] = M_s$$

**Risk-neutral pricing:**

$$V_t = e^{-r(T-t)}\,E^{\mathbb{Q}}[\text{payoff} \mid \mathcal{F}_t]$$

## Example

A stock at time 1 is $S_1 = £110$. Under the risk-neutral measure, $E^{\mathbb{Q}}[S_2 \mid \mathcal{F}_1]$ means "the expected stock price at time 2, given everything known at time 1."

If discounted prices are martingales: $E^{\mathbb{Q}}[e^{-r}S_2 \mid \mathcal{F}_1] = S_1$, so:

$$E^{\mathbb{Q}}[S_2 \mid \mathcal{F}_1] = S_1 \cdot e^{r} = 110 \times e^{0.05} = \text{£}115.64$$

The conditioning on $\mathcal{F}_1$ means the expectation uses the known price path up to time 1 — not just $S_1$ but all observed information.

## Remember

The bar "$\mid$" in $E[X \mid \mathcal{F}_t]$ is the most important piece of notation in stochastic finance. It separates what you are predicting (left of the bar) from what you know (right of the bar). Conditioning on a filtration $\mathcal{F}_t$ rather than a single variable means you use *all* market information up to time $t$, not just one price. This is why the result $E[X \mid \mathcal{F}_t]$ is itself a random variable — it depends on which path the market has taken so far. Every derivative pricing formula, every hedging argument, and every martingale condition is ultimately a statement about conditional expectations.
