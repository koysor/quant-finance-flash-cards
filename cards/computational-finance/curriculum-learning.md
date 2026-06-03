# Curriculum Learning in Finance

**Topic:** Computational Finance
**Tags:** curriculum learning, training schedule, transfer learning, reinforcement learning, progressive training, model misspecification
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Curriculum learning** trains a model on progressively harder tasks, beginning with simplified versions of the target problem and gradually introducing complexity. In financial RL, this means training option pricing or hedging agents first on simple GBM paths, then on paths with increasing realism (stochastic volatility, jumps, DPLs), allowing the network to learn core price-time relationships before the dynamics become complex.

## Key Formula

The training distribution $P_k$ evolves over curriculum stage $k$ as a mixture between a simple base distribution $P_\text{easy}$ and the full target distribution $P_\text{hard}$:

$$P_k = (1 - \lambda_k)\,P_\text{easy} + \lambda_k\,P_\text{hard}, \qquad \lambda_k = \frac{k}{K}$$

A simple staged schedule for RL option pricing:

| Stage | Training paths | New complexity added |
|---|---|---|
| 1 | GBM, constant $\sigma$ | Core Bellman structure |
| 2 | Heston (stochastic vol) | Vol surface shape |
| 3 | Merton-Heston (jumps) | Tail risk, skew |
| 4 | DPL-constrained paths | Boundary effects |

## Example

A TDBP agent trained directly on Merton-Heston paths from scratch takes 2,000 epochs to converge and achieves a mean absolute error of £0.18 vs the Carr-Madan reference price. The same agent trained with a 4-stage curriculum (500 epochs per stage) converges in 1,400 total epochs to a mean absolute error of £0.09 — half the error in 30% fewer epochs — because the GBM stage correctly pre-trains the Bellman recursion structure before the network must simultaneously learn it and handle stochastic vol.

## Remember

Curriculum learning is the financial RL analogue of a trainee trader learning vanilla options before exotics — the underlying principle is that difficult patterns are learnt more efficiently when the agent already has a reliable solution for a simpler subproblem. The connection to **transfer learning** is direct: each curriculum stage fine-tunes the weights from the previous stage rather than training from scratch, so the GBM-trained Bellman recursion weights provide a warm initialisation for the Heston stage. The key design decision is the **promotion criterion**: advance to the next stage when validation loss on the current distribution falls below a threshold, not after a fixed number of epochs.
