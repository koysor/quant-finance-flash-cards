# The Birthday and Monty Hall Problems

**Topic:** Probability
**Tags:** probability, birthday problem, Monty Hall, conditional probability, intuition
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

Two classic problems in which the intuitive answer is confidently wrong. The **birthday problem** asks how many people are needed for a shared birthday to be likely; the **Monty Hall problem** asks whether to switch doors after the host reveals a goat.

## Key Formula

$$P(\text{shared birthday among } n) = 1 - \frac{365!}{(365 - n)!\;365^{\,n}}$$

For Monty Hall, switching wins with probability $\tfrac{2}{3}$ and staying wins with probability $\tfrac{1}{3}$.

## Example

For $n = 23$ the probability of a shared birthday is just over $50\%$ (about $0.507$). There are $\binom{23}{2} = 253$ **pairs**, not 23 people, and each pair is a chance of a match.

Monty Hall by tree: your first pick is the car with probability $\tfrac{1}{3}$, in which case switching loses; it is a goat with probability $\tfrac{2}{3}$, and the host then *must* open the other goat, so switching wins. With 100 doors and the host opening 98 goats, switching wins with probability $\tfrac{99}{100}$.

## Remember

Both are calibration exercises for intuition. The host's choice is not random, so it carries information: this is conditional probability, and Bayes' theorem is the general tool. Quantitative finance is full of situations where the naive answer and the correct one differ by a large factor, such as the chance that some pair among many correlated assets breaches a limit at the same time.
