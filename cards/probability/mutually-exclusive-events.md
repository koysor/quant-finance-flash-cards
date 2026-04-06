# Mutually Exclusive Events

**Topic:** Probability
**Tags:** mutually exclusive, independent, addition rule, disjoint, probability
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

Two events $A$ and $B$ are **mutually exclusive** (disjoint) if they cannot both occur: $A \cap B = \emptyset$. Two events are **independent** if the occurrence of one does not change the probability of the other: $P(A \mid B) = P(A)$. These are distinct concepts — mutually exclusive events with positive probability are **never** independent, because knowing $B$ occurred tells you $A$ cannot occur.

## Key Formula

**Mutually exclusive addition rule:**

$$P(A \cup B) = P(A) + P(B) \quad \text{(when } A \cap B = \emptyset\text{)}$$

**Independence condition:**

$$A \perp B \iff P(A \cap B) = P(A) \cdot P(B)$$

**Mutually exclusive implies not independent** (when $P(A) > 0$ and $P(B) > 0$):

$$P(A \cap B) = 0 \neq P(A) \cdot P(B) \implies A \text{ and } B \text{ are dependent}$$

## Example

Roll a fair die. Let $A = \{1, 2\}$ and $B = \{3, 4\}$.

$A \cap B = \emptyset$: mutually exclusive. $P(A \cup B) = 1/3 + 1/3 = 2/3$.

Now let $C = \{1, 2, 3\}$ and $D = \{3, 4, 5, 6\}$.

$P(C \cap D) = P(\{3\}) = 1/6 = 1/2 \times 1/3 = P(C) \cdot P(D)$: $C$ and $D$ are independent (not mutually exclusive).

## Remember

The distinction between mutual exclusivity and independence is critical in **scenario analysis and stress testing**. Market regimes (e.g. low-vol vs high-vol) are approximately mutually exclusive — the market is in one regime at a time — but two stocks' daily returns can be independent within a regime. Confusing the two leads to errors in **Monte Carlo simulation**: treating correlated risk factors as independent underestimates joint tail losses. In credit, assuming defaults are mutually exclusive (which they are not) dramatically underestimates the probability of multiple defaults, as the 2008 financial crisis demonstrated.
