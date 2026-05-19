# Learning Rate Scheduling

**Topic:** Computational Finance
**Tags:** learning rate, scheduling, cosine annealing, warm restarts, fine-tuning, deep learning
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Learning rate scheduling** is the practice of varying the learning rate $\eta$ during training according to a pre-defined or adaptive rule, enabling the optimiser to take large steps early in training (fast convergence) and progressively smaller steps later (precise settling into a good minimum) — or to escape local minima via periodic restarts.

## Key Formula

**Cosine annealing with warm restarts (SGDR):** the learning rate at step $t$ within the $i$-th restart cycle of length $T_i$ is:

$$\eta_t = \eta_{\min} + \frac{1}{2}(\eta_{\max} - \eta_{\min})\!\left(1 + \cos\!\left(\frac{\pi\, t_i}{T_i}\right)\right)$$

where $t_i = t \mod T_i$ is the position within the current cycle. At the start of each cycle $\eta_t = \eta_{\max}$; it decays smoothly to $\eta_{\min}$ by the end, then resets. Cycle lengths often increase geometrically: $T_{i+1} = T_{\text{mult}} \cdot T_i$ with $T_{\text{mult}} = 2$.

**Linear warmup** (used in BERT fine-tuning): for the first $W$ steps, increase linearly from 0 to $\eta_{\max}$; then decay:

$$\eta_t = \eta_{\max} \cdot \min\!\left(\frac{t}{W},\; 1 - \frac{t - W}{T_{\text{total}} - W}\right)$$

## Example

Fine-tuning FinBERT on earnings sentiment data for $T_{\text{total}} = 2{,}500$ steps. With linear warmup ($W = 250$ steps) followed by linear decay: $\eta$ rises from $0$ to $2\times10^{-5}$ over steps 1–250, then falls linearly to $0$ by step 2,500. Without warmup: the large initial learning rate corrupts pre-trained BERT attention weights in the first few batches, and validation F1 reaches only 0.82. With warmup: validation F1 reaches 0.88 — the slow start protects the pre-trained representations while the model adapts to financial vocabulary.

## Remember

Learning rate scheduling is **not optional** when fine-tuning pre-trained language models on financial data — it is the mechanism that prevents catastrophic forgetting of pre-trained representations. The core problem: BERT's attention heads encode general syntactic structure built over billions of tokens; a large initial learning rate applied to a small financial dataset destroys these representations in the first few gradient updates, replacing them with overfitted patterns from a few thousand labelled earnings sentences. Linear warmup solves this by giving the output layers (newly initialised) time to adapt first, before the learning rate is high enough to meaningfully update the earlier pre-trained layers. Cosine annealing is the preferred schedule for training from scratch on financial time series data, because periodic restarts help the model explore multiple loss-surface basins rather than committing to the first local minimum found.
