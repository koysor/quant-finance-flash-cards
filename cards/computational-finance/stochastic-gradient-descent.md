# Stochastic Gradient Descent

**Topic:** Computational Finance
**Tags:** SGD, mini-batch, optimisation, gradient descent, online learning, neural networks
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Stochastic Gradient Descent (SGD)** replaces the full-dataset gradient in standard gradient descent with a gradient estimated from a single randomly sampled observation (or a small mini-batch). This introduces noise into each step but dramatically reduces per-iteration cost, making it the standard training algorithm for large-scale machine learning models.

## Key Formula

At iteration $t$, sample a mini-batch $\mathcal{B}_t$ of size $b$ uniformly at random:

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta\,\frac{1}{b}\sum_{i \in \mathcal{B}_t}\nabla_{\boldsymbol{\theta}}\,\ell(\boldsymbol{\theta}_t;\,\mathbf{x}_i,y_i)$$

| Variant | Batch size | Cost per step | Gradient noise |
|---|---|---|---|
| Batch GD | $N$ (full dataset) | High | None |
| Mini-batch SGD | $b \approx 32$–$256$ | Low | Moderate |
| Online SGD | $b = 1$ | Minimal | High |

## Example

Training a credit-scoring neural network on 500,000 loan records. Full-batch gradient descent requires summing gradients over all 500,000 samples at every step. Mini-batch SGD with $b=128$ computes 3,906 updates per epoch using only 128 samples each — converging in hours rather than days.

## Remember

Mini-batch SGD is the workhorse of deep learning in quantitative finance — from training price-prediction networks to fitting reinforcement learning agents for execution. The noise from small batches acts as an implicit regulariser, helping escape sharp local minima and find flatter, better-generalising solutions. This is why neural networks trained with SGD often outperform those trained with exact second-order methods on held-out financial data.
