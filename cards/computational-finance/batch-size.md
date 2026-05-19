# Batch Size

**Topic:** Computational Finance
**Tags:** batch size, gradient descent, training, deep learning, stochastic optimisation, hyperparameter
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Batch size** $B$ is the number of training examples processed in each forward-backward pass before the model parameters are updated; it is a hyperparameter that controls the trade-off between gradient noise (small $B$), computational efficiency (large $B$), and generalisation — with smaller batches often finding flatter loss-surface minima that generalise better to unseen data.

## Key Formula

For a dataset of $N$ examples with loss function $\mathcal{L}$, the exact gradient is:

$$\nabla_{\boldsymbol{\theta}}\mathcal{L} = \frac{1}{N}\sum_{i=1}^{N} \nabla_{\boldsymbol{\theta}}\ell_i$$

A mini-batch gradient uses a random subset $\mathcal{B}$ of size $B \ll N$:

$$\hat{g} = \frac{1}{B}\sum_{i \in \mathcal{B}} \nabla_{\boldsymbol{\theta}}\ell_i, \qquad \text{Var}(\hat{g}) \propto \frac{1}{B}$$

The gradient variance falls as $1/B$: full-batch ($B=N$) gives zero variance but requires one pass through all data per update; $B=1$ (SGD) gives maximum noise but updates after every example. The number of gradient updates per epoch is $\lceil N/B \rceil$.

## Example

Fine-tuning FinBERT on 8,000 labelled earnings sentences. With $B=32$: $8{,}000/32 = 250$ parameter updates per epoch. With $B=256$: only 31 updates per epoch, but each uses 8× more data so the gradient is more accurate. Empirically, $B=32$ reaches 89% sentiment accuracy in 5 epochs; $B=256$ stalls at 86% even after 20 epochs — the smaller batch's gradient noise acts as implicit regularisation, helping the model escape sharp minima that don't generalise to unseen filings.

## Remember

Batch size has a surprising effect on **generalisation** that matters for financial NLP models trained on scarce labelled data. Large batches converge to sharp minima in the loss landscape — regions where small perturbations to weights cause large performance drops, indicating poor robustness to distribution shift (e.g. a model trained on pre-2020 earnings calls that suddenly faces pandemic-era language). Small batches converge to flatter minima that are more robust. The practical rule for fine-tuning BERT variants on financial datasets with fewer than 10,000 examples: use $B \in \{16, 32\}$, not $B \geq 128$, and treat batch size as a hyperparameter to tune via walk-forward cross-validation rather than fixing it at a default.
