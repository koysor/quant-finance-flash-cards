# Leaky ReLU and the Dying ReLU Problem

**Topic:** Computational Finance
**Tags:** leaky relu, dying relu, activation function, dead neuron, gradient, deep learning
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **dying ReLU problem** occurs when a neuron's pre-activation $z$ becomes permanently negative during training: the ReLU gradient is zero for $z < 0$, so no weight update reaches the neuron and it never recovers. **Leaky ReLU** addresses this by allowing a small non-zero gradient $\alpha$ for negative inputs, ensuring neurons can always recover from a negative state.

## Key Formula

**ReLU** (dies for $z < 0$):

$$f(z) = \max(0, z) = \begin{cases} z & z \geq 0 \\ 0 & z < 0 \end{cases}, \qquad f'(z) = \begin{cases} 1 & z > 0 \\ 0 & z < 0 \end{cases}$$

**Leaky ReLU** (slope $\alpha$ for negative region, typically $\alpha = 0.01$):

$$f_\alpha(z) = \max(\alpha z, z) = \begin{cases} z & z \geq 0 \\ \alpha z & z < 0 \end{cases}, \qquad f'_\alpha(z) = \begin{cases} 1 & z > 0 \\ \alpha & z < 0 \end{cases}$$

**ELU (Exponential Linear Unit)** — smooth alternative:

$$f(z) = \begin{cases} z & z \geq 0 \\ \alpha(e^z - 1) & z < 0 \end{cases}$$

## Example

A 5-layer network trained to predict credit default probabilities. After 20 training epochs with ReLU, 35% of hidden neurons have pre-activations permanently below zero and contribute zero gradient to every batch — these are dead neurons. Switching to Leaky ReLU ($\alpha = 0.01$): after 20 epochs, 0% of neurons are dead, the gradient flows uniformly through all layers, and the final validation AUC improves from 0.83 to 0.87 because the full network capacity is utilised.

## Remember

The dying ReLU problem is most severe in deep financial networks trained with large learning rates or on datasets with many negative-valued features — both common in finance (returns are frequently negative; momentum signals can be strongly negative during drawdowns). The practical fix is Leaky ReLU with $\alpha = 0.01$ as the default hidden-layer activation: it retains ReLU's computational simplicity and avoids the vanishing gradient of sigmoid, whilst eliminating the dead neuron failure mode. In production financial models, always monitor the fraction of dead neurons during training (count units with zero activation on the entire training set) — a dead-neuron rate above 5% is a signal to reduce the learning rate or switch activation function, not to add more layers or data.
