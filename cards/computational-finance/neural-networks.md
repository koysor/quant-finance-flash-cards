# Neural Networks

**Topic:** Computational Finance
**Tags:** neural network, deep learning, layers, activation function, non-linear, universal approximator
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **neural network** is a layered function approximator built by stacking linear transformations and non-linear **activation functions**. Each layer transforms its input into a new representation; stacking many layers (deep learning) allows the network to learn arbitrarily complex mappings from inputs to outputs. By the **universal approximation theorem**, a single hidden layer with enough neurons can approximate any continuous function.

## Key Formula

**Forward pass** through layer $l$:

$$\mathbf{z}^{(l)} = \mathbf{W}^{(l)}\mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}, \qquad \mathbf{a}^{(l)} = \sigma\!\left(\mathbf{z}^{(l)}\right)$$

where $\mathbf{W}^{(l)}$ is the weight matrix, $\mathbf{b}^{(l)}$ is the bias vector, and $\sigma$ is the activation function applied element-wise.

**Common activation functions:**

$$\text{ReLU:}\; \sigma(z) = \max(0, z), \qquad \text{sigmoid:}\; \sigma(z) = \frac{1}{1+e^{-z}}, \qquad \text{tanh:}\; \sigma(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$$

**Output layer:** for regression use identity $\sigma(z) = z$; for binary classification use sigmoid.

## Example

A two-layer network prices a call option using five inputs: $S, K, T, r, \sigma$.

- Layer 1: 64 neurons, ReLU activation — learns non-linear relationships between inputs.
- Layer 2: 32 neurons, ReLU activation — refines the representation.
- Output: 1 neuron, identity activation — outputs the call price.

Trained on 100,000 Black-Scholes prices, the network achieves mean absolute error < 0.01 and runs 1,000× faster than the analytic formula for exotic options where no closed form exists.

## Remember

Neural networks have three major applications in quantitative finance. First, **option pricing for exotics**: when no closed form exists (e.g. Bermudan swaptions, multi-asset barriers), a neural network trained on Monte Carlo prices acts as a fast surrogate model — the "neural network as pricer" approach is now standard in XVA desks. Second, **volatility surface interpolation and calibration**: a network maps $(K, T)$ to implied vol, interpolating and extrapolating the smile arbitrage-free. Third, **alpha signal generation**: deep learning on alternative data (satellite images, earnings call transcripts) extracts non-linear patterns that linear factor models miss. The key limitation is interpretability — unlike logistic regression, a neural network's predictions cannot be explained in terms of individual feature contributions.
