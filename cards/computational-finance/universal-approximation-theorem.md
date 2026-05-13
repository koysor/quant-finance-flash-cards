# Universal Approximation Theorem

**Topic:** Computational Finance
**Tags:** universal approximation, neural network, expressivity, continuous function, derivatives pricing, non-linear
**Created:** 2026-04-26
**Author:** Claude Sonnet 4.6

---

## Definition

The **universal approximation theorem** (Cybenko 1989, Hornik 1991) states that a feedforward neural network with a single hidden layer containing a sufficient number of neurons and a non-linear activation function can approximate any continuous function on a compact domain to arbitrary precision.

## Key Formula

For any continuous function $f: [0,1]^d \to \mathbb{R}$ and any $\varepsilon > 0$, there exists a network $g$ with a single hidden layer of width $N$ such that:

$$\sup_{\mathbf{x} \in [0,1]^d} |f(\mathbf{x}) - g(\mathbf{x})| < \varepsilon$$

where $g(\mathbf{x}) = \sum_{j=1}^{N} \alpha_j \,\sigma\!\left(\mathbf{w}_j^\top \mathbf{x} + b_j\right)$ and $\sigma$ is any non-constant, bounded, continuous activation function.

The theorem is an **existence** result — it guarantees a network exists but does not say how large $N$ must be or how to find the weights.

## Example

The Black–Scholes call price $C(S, K, T, r, \sigma)$ is a continuous function of five inputs on any bounded domain. The universal approximation theorem guarantees a neural network exists that prices options to within $\varepsilon = \$0.01$ for any $(S, K, T, r, \sigma)$ in a specified range. In practice, a network with two hidden layers of 64 neurons each achieves sub-cent accuracy after training on 100,000 Black–Scholes prices — and then prices exotic options (where no formula exists) in microseconds.

## Remember

The universal approximation theorem is the theoretical licence for using neural networks in quantitative finance: it guarantees that a network can, in principle, represent any pricing function, risk model, or factor relationship, no matter how non-linear. However, the theorem provides no guidance on how deep the network needs to be, how many training samples are required, or whether gradient descent will find the approximating weights. These gaps — expressivity versus learnability versus data efficiency — are why the theorem is necessary but not sufficient for practical model development.
