# Law of Iterated Expectations

**Topic:** Probability
**Tags:** iterated expectations, conditional expectation, tower property, risk-neutral pricing, probability
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **law of iterated expectations** (also called the tower property) states that the unconditional expectation of a random variable equals the expectation of its conditional expectation. In other words, you can compute $E[X]$ in two stages: first condition on some other variable $Y$, then average over $Y$.

$$E[X] = E\!\left[E[X \mid Y]\right]$$

## Key Formula

**Tower property (general form):**

$$E[X] = E\!\left[E[X \mid Y]\right]$$

**Iterated conditioning** — if $Z$ contains more information than $Y$ (i.e. $Y$ is determined by $Z$):

$$E\!\left[E[X \mid Z] \mid Y\right] = E[X \mid Y]$$

**Conditional version:**

$$E[X \mid Y] = E\!\left[E[X \mid Y, Z] \mid Y\right]$$

## Example

A bond pays £100 if it does not default. Default probability depends on the credit regime: in a "good" economy (probability 0.7), the default probability is 5%; in a "bad" economy (probability 0.3), it is 20%.

Let $R$ = regime, $P$ = payoff. Compute expected payoff:

$$E[P \mid R = \text{good}] = 0.95 \times 100 = 95, \quad E[P \mid R = \text{bad}] = 0.80 \times 100 = 80$$

$$E[P] = E\!\left[E[P \mid R]\right] = 0.7 \times 95 + 0.3 \times 80 = 66.5 + 24 = 90.5$$

## Remember

In risk-neutral pricing, the law of iterated expectations guarantees that the price of a derivative today equals the discounted expectation of its price tomorrow — chained across all future time steps. This is the foundation of backward induction in binomial trees and the martingale property of discounted asset prices: $S_t = E^Q[S_{t+1}/(1+r) \mid \mathcal{F}_t]$. Without this law, multi-period pricing would not be self-consistent.
