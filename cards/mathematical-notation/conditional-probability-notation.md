# Conditional Probability Notation

**Topic:** Mathematical Notation
**Tags:** notation, conditional probability, given, Bayes, posterior
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **conditional probability** $P(A \mid B)$ is the probability of event $A$ given that event $B$ is known to have occurred. The vertical bar $\mid$ is read "given" and restricts the sample space to outcomes where $B$ holds.

| Symbol | Read as | Meaning |
|---|---|---|
| $P(A \mid B)$ | "probability of A given B" | Updated probability of $A$ when $B$ is known to occur |
| $f_{X \mid Y}(x \mid y)$ | "conditional density of X given Y equals y" | $f_{X,Y}(x,y)/f_Y(y)$ — restricting to where $Y = y$ |
| $P(A \mid B, C)$ | "probability of A given B and C" | Conditioning on two pieces of information simultaneously |
| $\mid$ | "given" or "conditioned on" | The bar separates the event from the conditioning information |

## Key Formula

**Definition of conditional probability:**

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0$$

**Multiplication rule** (rearranging the definition):

$$P(A \cap B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A)$$

**Bayes' theorem:**

$$P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}$$

**Law of total probability** (for a partition $\{A_i\}$):

$$P(B) = \sum_{i} P(B \mid A_i)\,P(A_i)$$

## Example

**Credit risk:** $U$ = {company is in financial distress}, $D$ = {bond defaults}. Historical data give $P(D) = 2\%$, $P(U) = 5\%$, $P(U \mid D) = 60\%$.

Bayes' theorem: $P(D \mid U) = \frac{P(U \mid D)\,P(D)}{P(U)} = \frac{0.60 \times 0.02}{0.05} = 24\%$. A bond in financial distress is 12 times more likely to default than the average bond.

## Remember

The notation $P(A \mid B)$ is a completely new probability measure — not $P(A)$ divided by $P(B)$ in the sense of adjusting a prior, but rather the probability in the restricted universe where $B$ has occurred. Bayes' theorem inverts the conditioning: if you know $P(D \mid U)$ (how likely distress precedes default) you can compute $P(U \mid D)$ (how likely distress given default) using the base rates. This reversal is the foundation of Bayesian inference and the Black-Litterman model.
