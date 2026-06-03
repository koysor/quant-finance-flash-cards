# Stochastic

**Topic:** Probability
**Tags:** stochastic, random, probability, randomness, uncertainty
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

A **stochastic** quantity or process is one that incorporates randomness — its value is not determined by initial conditions alone but depends on the outcome of a random experiment drawn from a probability space $(\Omega, \mathcal{F}, P)$. A **stochastic process** $\{X_t\}_{t \geq 0}$ is a family of random variables indexed by time, representing a system that evolves randomly.

## Key Formula

A random variable $X$ is a measurable function from a probability space to the reals:

$$X: (\Omega, \mathcal{F}, P) \to \mathbb{R}$$

A stochastic process at each time $t$ is a random variable $X_t(\omega)$, where $\omega \in \Omega$ is the particular outcome realised. Fixing $\omega$ gives a single **path** $t \mapsto X_t(\omega)$; averaging over $\Omega$ gives the **distribution** $P(X_t \leq x)$.

## Example

Consider a fair coin flipped each day. Let $X_t = $ cumulative heads minus tails after $t$ flips. For $t = 3$: if the outcomes are $\{H, T, H\}$ then $X_3 = 1$, but if the outcomes are $\{T, T, T\}$ then $X_3 = -3$. The value of $X_t$ is not known in advance — it is stochastic. As $t \to \infty$ and the flip frequency increases, this discrete process converges in distribution to Brownian motion.

## Remember

In quantitative finance, recognising that asset prices are stochastic — not deterministic — is the foundational assumption of the entire derivatives pricing framework. A deterministic model would predict one unique future stock price; a stochastic model produces a full distribution of prices. This distribution is what makes options valuable: an option on a deterministic asset with known terminal price is worth exactly its intrinsic value, so all time value comes from stochastic uncertainty.
