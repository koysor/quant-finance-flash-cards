# Conditional Probability

**Topic:** Probability
**Tags:** conditional probability, independence, multiplication rule, P(A|B), joint probability
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **conditional probability** of event $A$ given that event $B$ has occurred is the probability of $A$ restricted to the sub-universe where $B$ is known to be true. It is defined whenever $P(B) > 0$. Two events are **independent** if knowing $B$ provides no information about $A$.

## Key Formula

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0$$

**Multiplication rule** (rearrangement):

$$P(A \cap B) = P(A \mid B)\, P(B) = P(B \mid A)\, P(A)$$

**Independence:** $A \perp B \iff P(A \mid B) = P(A) \iff P(A \cap B) = P(A)\,P(B)$

**Law of total probability:**

$$P(A) = \sum_{i} P(A \mid B_i)\, P(B_i)$$

where $\{B_i\}$ is a partition of the sample space.

## Example

In a bond portfolio, 5% of bonds default in a given year, but given a recession the default rate rises to 18%.

$$P(\text{default}) = 0.05, \qquad P(\text{default} \mid \text{recession}) = 0.18$$

If $P(\text{recession}) = 0.20$:

$$P(\text{default} \cap \text{recession}) = 0.18 \times 0.20 = 0.036$$

The joint probability of recession and default is 3.6% — far higher than if the two events were independent ($0.05 \times 0.20 = 1.0\%$), quantifying the dependence between credit and macro risk.

## Remember

Conditional probability is the foundation of every credit risk model. The **conditional probability of default (CPD)** given a macro state (recession, expansion) is the core quantity in stress testing and IFRS 9 Expected Credit Loss models — banks must estimate PD conditional on forward-looking macro scenarios, not the unconditional historical average. The multiplication rule $P(A \cap B) = P(A \mid B) P(B)$ also underlies the **copula approach** to CDO pricing: decomposing joint default probabilities into marginal PDs and a dependence structure (the copula) is exactly the conditional probability multiplication rule applied in reverse.
