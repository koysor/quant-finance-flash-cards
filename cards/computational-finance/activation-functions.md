# Activation Functions

**Topic:** Computational Finance
**Tags:** activation function, ReLU, sigmoid, neural networks, non-linearity, deep learning
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Activation functions** are non-linear transformations applied to the weighted sum of inputs at each neuron. Without them, a neural network of any depth collapses to a single linear transformation. They determine which neurons "fire", enable the network to approximate complex functions, and affect training speed and stability.

## Key Formula

**ReLU** (Rectified Linear Unit — most common):
$$f(x) = \max(0,\, x)$$

**Sigmoid** (output layer for binary classification):
$$\sigma(x) = \frac{1}{1+e^{-x}}$$

**Softmax** (output layer for multi-class):
$$\text{softmax}(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}}$$

## Example

A neural network classifying market regimes uses ReLU in all hidden layers (fast to compute, avoids vanishing gradients) and a softmax output layer mapping to three probabilities: bull, bear, crisis. Probabilities sum to 1 by construction.

## Remember

ReLU's gradient is 1 for positive inputs and 0 otherwise — this sparse, constant gradient prevents the vanishing gradient problem that crippled earlier sigmoid-based deep networks. In quantitative finance, the choice of output activation is dictated by the task: sigmoid for default probability (output in $[0,1]$), linear (no activation) for regression tasks such as predicting next-day returns.
