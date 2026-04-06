# Indicator Function Notation

**Topic:** Mathematical Notation
**Tags:** notation, indicator function, positive part, events, payoff
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

The **indicator function** $\mathbf{1}_A$ (also written $\mathbb{1}_A$ or $\mathbf{1}[A]$) equals 1 if the event or condition $A$ holds and 0 otherwise. It converts a set-membership question into a number.

| Symbol | Meaning |
|---|---|
| $\mathbf{1}_A$ or $\mathbf{1}[A]$ | 1 if event $A$ occurs, 0 otherwise |
| $\mathbf{1}_{x > 0}$ | 1 if $x > 0$, 0 if $x \leq 0$ |
| $[x]_+$ or $(x)^+$ | Positive part: $\max(x, 0)$ |
| $[x]_-$ or $(x)^-$ | Negative part: $\max(-x, 0)$ |

The positive part can be expressed as $[x]_+ = x \cdot \mathbf{1}_{x > 0}$.

## Key Formula

**Decomposition identity:**

$$x = [x]_+ - [x]_-, \qquad |x| = [x]_+ + [x]_-$$

**Call option payoff** at expiry:

$$C_T = (S_T - K)^+ = (S_T - K)\,\mathbf{1}_{S_T > K}$$

**Expected value via indicator:**

$$E[\mathbf{1}_A] = P(A)$$

**Indicator of intersection:**

$$\mathbf{1}_{A \cap B} = \mathbf{1}_A \cdot \mathbf{1}_B$$

## Example

A digital (binary) call option pays £1 if $S_T > K$, else £0:

$$\text{Payoff} = \mathbf{1}_{S_T > K}$$

Under the risk-neutral measure $\mathbb{Q}$, its price is:

$$V_0 = e^{-rT}\,E^{\mathbb{Q}}[\mathbf{1}_{S_T > K}] = e^{-rT}\,\mathbb{Q}(S_T > K) = e^{-rT}\,N(d_2)$$

where $N(d_2)$ is the standard normal CDF evaluated at $d_2$ — a direct consequence of the identity $E[\mathbf{1}_A] = P(A)$.

## Remember

The **positive part** $(S_T - K)^+$ is the universal option payoff building block. Every vanilla European option is either $(S_T - K)^+$ (call) or $(K - S_T)^+$ (put). Exotic products such as barrier options, CLO tranches, and credit-linked notes are all constructed from sums and products of indicator functions applied to threshold conditions. Understanding $\mathbf{1}_A$ as an expectation under a probability measure — specifically $E[\mathbf{1}_A] = P(A)$ — is the direct link between option pricing and risk-neutral probabilities.
