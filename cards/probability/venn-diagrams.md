# Venn Diagrams

**Topic:** Probability
**Tags:** Venn diagram, set notation, union, intersection, complement, probability
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **Venn diagram** represents events as overlapping circles within a rectangle (the sample space $\Omega$). The **union** $A \cup B$ is the event that $A$ or $B$ (or both) occur; the **intersection** $A \cap B$ is the event that both occur; the **complement** $A'$ is the event that $A$ does not occur. Venn diagrams give a visual route to computing probabilities via set operations.

## Key Formula

**Addition rule:**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Complement rule:**

$$P(A') = 1 - P(A)$$

**Conditional probability from a Venn diagram:**

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

**Mutually exclusive:** $A \cap B = \emptyset \Rightarrow P(A \cup B) = P(A) + P(B)$

**Independent:** $P(A \cap B) = P(A) \cdot P(B)$

## Example

In a portfolio of 100 bonds: 30 are investment grade (IG), 20 are ESG-labelled, and 8 are both IG and ESG.

$$P(IG \cup ESG) = 0.30 + 0.20 - 0.08 = 0.42$$

$$P(IG \mid ESG) = \frac{0.08}{0.20} = 0.40$$

40% of ESG bonds are investment grade — higher than the unconditional 30%, suggesting ESG labelling is positively correlated with credit quality in this portfolio.

## Remember

Venn diagrams make the **inclusion-exclusion principle** visible, which in finance appears in **credit correlation modelling**: the joint probability of two firms defaulting ($A \cap B$) is subtracted when computing the probability that at least one defaults ($A \cup B$). Failing to subtract the overlap is a common error that overestimates portfolio loss probability. In **stress testing**, Venn diagrams also clarify overlapping scenarios — a recession scenario and a rate-spike scenario share common features (their intersection), so joint probability must account for that dependence rather than treating them as independent.
