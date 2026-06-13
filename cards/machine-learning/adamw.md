# AdamW

**Topic:** Machine Learning
**Tags:** adamw, weight decay, regularisation, optimiser, adam, deep learning
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**AdamW** is a variant of the Adam optimiser that applies **decoupled weight decay**: instead of adding an L2 penalty term to the loss and letting Adam absorb it into the adaptive learning rate, AdamW subtracts a fixed proportion of the current weights directly after each gradient step. This distinction matters because Adam's adaptive scaling distorts L2 regularisation — large-gradient parameters receive less weight decay than intended — whereas AdamW restores the intended regularisation strength uniformly across all parameters.

## Key Formula

**Adam** update (weight decay folded into gradient via L2 loss penalty):

$$\theta_{t+1} = \theta_t - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$

where $\hat{m}_t$ and $\hat{v}_t$ are the bias-corrected first and second moment estimates of $\nabla \mathcal{L} + \lambda\theta_t$.

**AdamW** update (weight decay decoupled and applied after the Adam step):

$$\theta_{t+1} = \theta_t - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon} - \eta\lambda\,\theta_t$$

The only difference is the final $-\eta\lambda\theta_t$ term, which shrinks weights proportionally regardless of gradient magnitude. Here $\lambda$ is the weight decay coefficient (typically $10^{-4}$ to $10^{-2}$).

## Example

Training a TDBP pricing network with $\eta = 10^{-3}$ and $\lambda = 10^{-3}$. Suppose a weight $\theta = 2.0$ with a large second moment estimate $\hat{v} = 0.04$:

**Adam (L2):** the effective gradient passed to Adam is $g + \lambda\theta = g + 0.002$. Adam scales by $1/\sqrt{0.04} = 5$, so the weight decay contribution to the update is $5 \times 0.002 \times 10^{-3} = 10^{-5}$ — nearly zero despite $\lambda = 10^{-3}$.

**AdamW:** the weight decay term is applied independently: $\eta\lambda\theta = 10^{-3} \times 10^{-3} \times 2.0 = 2 \times 10^{-6}$, but crucially it does **not** get divided by $\sqrt{\hat{v}}$, so its effect is not suppressed by large historical gradients. The intended shrinkage is preserved.

## Remember

In deep hedging and neural SDE calibration, the network must generalise across a wide range of market conditions — not overfit to the training paths. AdamW's decoupled weight decay provides more reliable L2 regularisation than Adam+L2, which tends to under-regularise high-gradient directions (typically the output layer) and over-regularise low-gradient directions (often the first layer). This imbalance causes the network to memorise payoff shapes seen in training but fail on out-of-sample vol regimes. Switching from Adam to AdamW with the same $\lambda$ typically reduces out-of-sample Bellman error in TDBP by 5–15% without any other changes, making it the default optimiser choice for finance ML practitioners who use PyTorch or JAX.
