# Feedforward Network

**Topic:** Computational Finance
**Tags:** feedforward, neural network, multilayer perceptron, forward pass, universal approximation, deep learning
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

A **feedforward network** (also called a multilayer perceptron, MLP) is a neural network where information flows in one direction only — from input through hidden layers to output — with no cycles or feedback connections. It is the foundational architecture from which all other neural networks (convolutional, recurrent, transformer) are built.

## Key Formula

A feedforward network with $L$ layers computes its output by composing $L$ functions. For layer $l$:

$$\mathbf{a}^{(l)} = \sigma\!\left(\mathbf{W}^{(l)}\mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}\right)$$

where $\mathbf{W}^{(l)}$ are learnable weights, $\mathbf{b}^{(l)}$ are biases, and $\sigma$ is a non-linear activation function. The full network maps input $\mathbf{x} = \mathbf{a}^{(0)}$ to output $\hat{y} = \mathbf{a}^{(L)}$.

**Universal approximation theorem:** a feedforward network with one hidden layer and enough neurons can approximate any continuous function on a compact domain to arbitrary precision.

## Example

A two-layer feedforward network pricing an option from five inputs $\mathbf{x} = (S, K, T, r, \sigma)$:

1. **Hidden layer** (3 neurons, ReLU): $\mathbf{a}^{(1)} = \text{ReLU}(\mathbf{W}^{(1)}\mathbf{x} + \mathbf{b}^{(1)})$ — e.g. produces $(2.1, 0, 4.7)$
2. **Output layer** (1 neuron, linear): $\hat{y} = \mathbf{W}^{(2)}\mathbf{a}^{(1)} + b^{(2)}$ — e.g. produces $\hat{C} = 3.82$

Trained on Black–Scholes prices, the network learns the option price surface without knowing the formula — substituting millisecond inference for the analytical calculation.

## Remember

In quantitative finance, the choice between feedforward and recurrent architectures is architectural shorthand for the problem type. **Feedforward networks** process each observation independently — they have no memory of previous inputs — making them suited to cross-sectional prediction tasks: credit scoring (each loan assessed on its own features), equity factor models (each stock scored on current fundamentals), and options pricing (each contract priced from current market inputs). **Recurrent networks** (LSTM, GRU) process sequences and maintain hidden state, making them suited to time-series forecasting where the ordering of observations matters. Choosing feedforward for a time-series problem discards all temporal structure.
