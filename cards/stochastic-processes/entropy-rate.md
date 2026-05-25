# Entropy Rate

**Topic:** Stochastic Processes
**Tags:** entropy rate, stochastic process, markov chain, information theory, market efficiency, regime
**Created:** 2026-05-25
**Author:** Claude Sonnet 4.6

---

## Definition

The **entropy rate** $h(\mathbf{X})$ of a stationary stochastic process $\{X_t\}$ measures the average uncertainty generated per time step as the process evolves. It is the per-symbol Shannon entropy in the limit of long sequences, and quantifies how much new information the process produces at each step.

## Key Formula

$$h(\mathbf{X}) = \lim_{n \to \infty} \frac{1}{n} H(X_1, X_2, \ldots, X_n)$$

Equivalently (via the chain rule of entropy):

$$h(\mathbf{X}) = \lim_{n \to \infty} H(X_n \mid X_{n-1}, \ldots, X_1)$$

For a **time-homogeneous Markov chain** with stationary distribution $\boldsymbol{\pi}$ and transition matrix $P$:

$$h(\mathbf{X}) = -\sum_{i} \pi_i \sum_{j} P_{ij} \log P_{ij}$$

This is the entropy of the next state, averaged over the stationary distribution of the current state.

## Example

A two-state regime model: bull ($B$) and bear ($R$) markets, with transition matrix:

$$P = \begin{pmatrix} 0.95 & 0.05 \\ 0.10 & 0.90 \end{pmatrix}$$

Stationary distribution: $\pi_B = 2/3$, $\pi_R = 1/3$.

$$h = -\tfrac{2}{3}\bigl(0.95\log 0.95 + 0.05\log 0.05\bigr) - \tfrac{1}{3}\bigl(0.10\log 0.10 + 0.90\log 0.90\bigr) \approx 0.234 \text{ bits/day}$$

A model with equal transition probabilities ($P_{ij} = 0.5$) would have entropy rate $1$ bit/day — maximally unpredictable. The low entropy rate here (0.234) reflects strong regime persistence.

## Remember

The entropy rate of a market process is an empirical measure of **regime persistence versus randomness**. A low entropy rate signals that the process has memory — today's regime strongly predicts tomorrow's — which creates tradeable structure: momentum strategies profit from this predictability. A high entropy rate, approaching the theoretical maximum of $\log K$ bits for $K$ regimes, signals near-random switching that is difficult to exploit. In market microstructure, the entropy rate of the order-flow sequence (buy/sell imbalance) has been used to measure market efficiency: a perfectly efficient market would generate maximum entropy order flow, whereas an informed-trading environment generates lower entropy flow as informed traders concentrate activity in predictable patterns.
