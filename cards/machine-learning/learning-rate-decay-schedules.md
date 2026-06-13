# Learning Rate Decay Schedules

**Topic:** Machine Learning
**Tags:** learning rate, cosine decay, exponential decay, schedule, deep learning, convergence
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Learning rate decay schedules** are rules that reduce the learning rate $\eta_t$ monotonically during training — in contrast to warm-restart schedules that reset periodically. The three main variants are **exponential decay** (constant multiplicative reduction each step), **cosine decay** (smooth reduction following a half-cosine curve), and **exponential-cosine decay** (an exponential envelope modulating a cosine curve), each offering a different balance between early convergence speed and late-stage precision.

## Key Formula

**Exponential decay** — constant proportional reduction per epoch:

$$\eta_t = \eta_0 \cdot \alpha^t, \qquad \alpha \in (0,1)$$

**Cosine decay** — smooth transition from $\eta_{\max}$ to $\eta_{\min}$ over $T$ steps:

$$\eta_t = \eta_{\min} + \tfrac{1}{2}(\eta_{\max} - \eta_{\min})\!\left(1 + \cos\!\left(\tfrac{\pi t}{T}\right)\right)$$

**Exponential-cosine decay** — exponential envelope applied to a cosine curve, combining fast initial decay with a smooth finish:

$$\eta_t = \eta_{\min} + (\eta_{\max} - \eta_{\min}) \cdot e^{-\lambda t} \cdot \tfrac{1}{2}\!\left(1 + \cos\!\left(\tfrac{\pi t}{T}\right)\right)$$

| Schedule | Early rate | Late rate | Good for |
|---|---|---|---|
| Exponential | Fast | Very fast | Quick prototyping |
| Cosine | Moderate | Slow, smooth | Stable convergence |
| Exp-cosine | Fast | Very slow, smooth | Precision tuning |

## Example

Training a TDBP network for 500 steps with $\eta_0 = 10^{-3}$, $\eta_{\min} = 10^{-5}$:

- **Exponential** ($\alpha = 0.995$): $\eta_{100} = 6.1 \times 10^{-4}$, $\eta_{500} = 8.2 \times 10^{-5}$ — steady, predictable decay
- **Cosine**: $\eta_{250} = 5.1 \times 10^{-4}$ (halfway), $\eta_{500} = 10^{-5}$ — slow start, smooth finish
- **Exp-cosine** ($\lambda = 0.003$): $\eta_{100} = 4.5 \times 10^{-4}$, $\eta_{500} = 1.2 \times 10^{-5}$ — rapid early drop, near-zero final steps

Cosine decay typically achieves lowest out-of-sample Bellman error at convergence because the slow final phase allows fine-grained parameter adjustment near the pricing surface without overshooting.

## Remember

For TDBP backward induction, the decay schedule affects each of the 30 per-step networks independently — using cosine decay, each network's learning rate follows its own cosine curve aligned with that step's training budget. The practical consequence is that the final few hundred gradient steps of cosine decay (where the learning rate is effectively zero) act as an implicit "cool-down" that stabilises the network before it becomes the bootstrap target for the next earlier step. Using exponential decay instead keeps the learning rate non-negligible for longer, which causes more noise in the target value and increases the Bellman error at earlier steps. For neural SDE calibration to market prices, exponential-cosine decay is preferred because the rapid initial phase fits the coarse shape of the vol surface quickly, and the smooth tail fine-tunes the wings where calibration error is most sensitive to small parameter changes.
