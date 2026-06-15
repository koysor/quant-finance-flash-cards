# Detailed Balance

**Topic:** Stochastic Processes
**Tags:** detailed balance, reversibility, stationary distribution, Metropolis-Hastings, MCMC, Markov chain
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

A Markov chain satisfies detailed balance with respect to a distribution $\pi$ if the probability flux from state $x$ to state $y$ equals the flux from $y$ to $x$ under $\pi$. It is a sufficient condition for $\pi$ to be the stationary distribution, and it implies the chain is time-reversible: running it forwards and backwards in time looks statistically identical.

## Key Formula

Detailed balance condition:

$$\pi(x)\, P(x, y) = \pi(y)\, P(y, x) \quad \text{for all states } x, y$$

Summing over $y$ gives $\sum_y \pi(x)P(x,y) = \sum_y \pi(y)P(y,x)$, which is exactly $(\pi P)_x = \pi_x$ — confirming $\pi$ is stationary. The **Metropolis–Hastings** acceptance probability is designed to enforce detailed balance:

$$\alpha(\theta \to \theta^*) = \min\!\left(1,\; \frac{\pi(\theta^*)\, q(\theta \mid \theta^*)}{\pi(\theta)\, q(\theta^* \mid \theta)}\right)$$

so that $\pi(\theta)\cdot P(\theta \to \theta^*) = \pi(\theta^*)\cdot P(\theta^* \to \theta)$ holds by construction.

## Example

Suppose $\pi(A) = 0.4$, $\pi(B) = 0.6$, and the symmetric proposal $q(\cdot \mid \cdot) = 0.5$ proposes moves in both directions equally. Detailed balance requires $P(A \to B)$ and $P(B \to A)$ to satisfy $0.4 \cdot P(A\to B) = 0.6 \cdot P(B\to A)$. The Metropolis acceptance step sets $\alpha(A \to B) = \min(1, 0.6/0.4) = 1$ and $\alpha(B \to A) = \min(1, 0.4/0.6) = 0.667$, which enforces the balance equation exactly.

## Remember

The Metropolis–Hastings algorithm is constructed to satisfy detailed balance with the desired posterior as the stationary distribution. This is the mathematical guarantee that makes Bayesian calibration of derivatives models work: no matter what proposal distribution a practitioner uses, the acceptance step corrects the transition probabilities so the chain's long-run samples come from the correct posterior over model parameters.
