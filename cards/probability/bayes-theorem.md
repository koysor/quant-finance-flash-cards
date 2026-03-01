# Bayes' Theorem

**Topic:** Probability
**Tags:** probability, conditional probability, Bayesian

---

## Definition

Bayes' theorem describes how to **update a probability** in light of new evidence. It relates the conditional probability of an event A given B to the reverse conditional probability of B given A.

## Key Formula

$$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$$

Where:
- **P(A)** — prior probability of A (before observing B)
- **P(B | A)** — likelihood of observing B if A is true
- **P(A | B)** — posterior probability of A given B
- **P(B)** — marginal probability of B (normalising constant)

The denominator can be expanded using the **law of total probability**:

$$P(B) = P(B \mid A)\,P(A) + P(B \mid A^c)\,P(A^c)$$

## Example

A credit model flags a borrower as high-risk. The model has:
- 5% of borrowers actually default (prior: P(Default) = 0.05)
- 90% detection rate: P(Flag | Default) = 0.90
- 10% false positive rate: P(Flag | No Default) = 0.10

What is P(Default | Flagged)?

$$P(D \mid F) = \frac{0.90 \times 0.05}{0.90 \times 0.05 + 0.10 \times 0.95} = \frac{0.045}{0.045 + 0.095} = \frac{0.045}{0.14} \approx 32\%$$

Despite the model flagging the borrower, there is only a 32% chance they will actually default.

## Remember

This result feels counterintuitive but is critical in finance: when the **base rate** (prior) of an event is low, even a good model produces many false positives. This affects credit scoring, fraud detection, and signal discovery in algorithmic trading.
