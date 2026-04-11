# Unconditional Probability

**Topic:** Probability
**Tags:** unconditional probability, marginal probability, prior, baseline, total probability
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **unconditional probability** $P(A)$ is the probability of event $A$ without conditioning on any other event — computed across the entire sample space $\Omega$. It is also called the **marginal probability** or **prior probability** and represents the baseline likelihood before any additional information is incorporated.

## Key Formula

**Law of total probability** (recovering unconditional from conditionals):

$$P(A) = \sum_{i} P(A \mid B_i)\,P(B_i)$$

where $\{B_i\}$ is a partition of $\Omega$ (disjoint events covering all outcomes).

**Relationship to conditional probability:**

$$P(A) = P(A \mid B)\,P(B) + P(A \mid B^c)\,P(B^c)$$

**Marginalising a joint distribution:**

$$P(A) = \int_{-\infty}^{\infty} f_{A \mid X}(a \mid x)\,f_X(x)\,dx \quad \text{(continuous case)}$$

## Example

A bond's **unconditional default probability** over one year is $P(D) = 2\%$. This baseline ignores the current credit rating. If we learn the issuer is on negative watch:

$$P(D \mid \text{negative watch}) = 12\% \gg P(D) = 2\%$$

The unconditional probability can be recovered: with $P(\text{neg.\ watch}) = 10\%$,

$$P(D) = P(D\mid\text{neg.}) \times 0.10 + P(D\mid\text{not neg.}) \times 0.90 = 0.12(0.10) + p(0.90) = 0.02$$

Solving: $p = P(D \mid \text{not neg.}) \approx 0.89\%$.

## Remember

The unconditional probability is the answer you give when you have no additional information — the base rate. It is updated to a conditional probability when new information arrives, via Bayes' theorem: $P(A \mid B) = P(B \mid A)\,P(A) / P(B)$. In credit risk and Bayesian portfolio models, the unconditional default probability or return expectation is the prior; data or signals update it to a posterior. Confusing conditional and unconditional probabilities is a common error in risk reporting.
