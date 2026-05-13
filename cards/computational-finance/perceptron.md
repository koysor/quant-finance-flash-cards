# Perceptron

**Topic:** Computational Finance
**Tags:** perceptron, forward propagation, bias, weighted sum, neural network, binary classification
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **perceptron** is the fundamental computational unit of a neural network. It takes a vector of inputs, multiplies each by a learnable weight, adds a bias term, and passes the result through an activation function to produce an output. Stacking perceptrons into layers and connecting them creates a neural network capable of learning non-linear relationships.

## Key Formula

**Single perceptron output:**

$$\hat{y} = g\!\left(w_0 + \sum_{j=1}^{m} x_j w_j\right) = g\!\left(w_0 + \mathbf{w}^{\top}\mathbf{x}\right)$$

where $x_j$ are inputs, $w_j$ are learnable weights, $w_0$ is the bias, and $g$ is the activation function.

**Forward propagation** through a layer with $n$ perceptrons:

$$\mathbf{a}^{(l)} = g\!\left(\mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}\right)$$

where $\mathbf{W}^{(l)}$ is the weight matrix for layer $l$, $\mathbf{b}^{(l)}$ is the bias vector, and $\mathbf{a}^{(0)} = \mathbf{x}$ (the input).

**Biological analogy**: inputs $x_j$ are dendritic signals, weights $w_j$ are synaptic strengths, the bias shifts the firing threshold, and $g$ determines whether the neuron fires.

## Example

A single perceptron for binary credit classification with 3 inputs: debt-to-income ratio $x_1 = 0.45$, credit score (normalised) $x_2 = 0.72$, employment years (normalised) $x_3 = 0.60$. Weights: $w_0 = -0.5$, $w_1 = -1.2$, $w_2 = 1.5$, $w_3 = 0.8$.

$$z = -0.5 + (-1.2)(0.45) + (1.5)(0.72) + (0.8)(0.60) = -0.5 - 0.54 + 1.08 + 0.48 = 0.52$$

With sigmoid activation: $\hat{y} = \sigma(0.52) = 0.627$ — the perceptron assigns a 62.7% probability of repayment.

## Remember

The perceptron is structurally identical to logistic regression when $g$ is the sigmoid function — the difference is that a neural network stacks many perceptrons in layers, enabling non-linear decision boundaries that logistic regression cannot achieve. In quantitative finance, the perceptron is not used alone (a single perceptron can only separate linearly separable classes), but understanding it is essential for interpreting what a deep network does: each unit in each layer is a perceptron computing a weighted vote, and the output layer's perceptrons combine all these votes into the final prediction. The bias term $w_0$ is analogous to the intercept in a regression — it allows the decision boundary to be offset from the origin, which is critical when the financial features (credit scores, leverage ratios) are not centred at zero.
