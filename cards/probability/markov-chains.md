# Markov Chains

**Topic:** Probability
**Tags:** Markov chain, transition matrix, steady state, credit ratings, discrete time, absorbing state
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **Markov chain** is a discrete-time stochastic process $\{X_n\}$ taking values in a finite or countable state space $S$, where the future state depends only on the present state — not on the history. This is the **Markov property**. The process is fully characterised by its **transition matrix** $P$, where $P_{ij} = P(X_{n+1} = j \mid X_n = i)$.

## Key Formula

**Transition matrix** (rows sum to 1):

$$P = \begin{pmatrix} p_{11} & p_{12} & \cdots \\ p_{21} & p_{22} & \cdots \\ \vdots & & \ddots \end{pmatrix}, \qquad \sum_j p_{ij} = 1 \; \forall\, i$$

**$n$-step transition probabilities:**

$$P(X_{n+k} = j \mid X_k = i) = (P^n)_{ij}$$

**Steady-state distribution** $\boldsymbol{\pi}$ satisfies:

$$\boldsymbol{\pi} P = \boldsymbol{\pi}, \qquad \sum_i \pi_i = 1$$

## Example

Moody's publishes annual credit rating transition matrices. A simplified 3-state matrix (Investment Grade IG, High Yield HY, Default D):

$$P = \begin{pmatrix} 0.90 & 0.09 & 0.01 \\ 0.05 & 0.88 & 0.07 \\ 0 & 0 & 1 \end{pmatrix}$$

Default is an **absorbing state** ($p_{DD} = 1$). The 5-year default probability from IG is found from $(P^5)_{ID}$, computed by matrix multiplication.

## Remember

Credit rating transition matrices are the most important application of Markov chains in finance. Basel IRB and CDS pricing both require **multi-year default probabilities**: the probability that an A-rated issuer defaults within 5 years is read off $P^5$, the fifth power of the annual transition matrix — a direct Markov chain calculation. The steady-state distribution $\boldsymbol{\pi}$ gives the long-run fraction of time spent in each rating, providing a sanity check on the matrix. Markov chains also underlie **regime-switching models**: a hidden Markov model (HMM) uses a latent Markov chain to represent market regimes (bull/bear), with each regime generating returns with different drift and volatility.
