# Jacobian Matrix

**Topic:** Computational Finance
**Tags:** jacobian, backpropagation, partial derivatives, automatic differentiation, neural networks, optimisation
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Jacobian matrix** generalises the gradient to vector-valued functions. For $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$, the Jacobian is the $m \times n$ matrix whose $(i,j)$ entry is the partial derivative of the $i$-th output with respect to the $j$-th input.

## Key Formula

$$\mathbf{J} = \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{pmatrix} \dfrac{\partial f_1}{\partial x_1} & \cdots & \dfrac{\partial f_1}{\partial x_n} \\[8pt] \vdots & \ddots & \vdots \\[4pt] \dfrac{\partial f_m}{\partial x_1} & \cdots & \dfrac{\partial f_m}{\partial x_n} \end{pmatrix} \in \mathbb{R}^{m \times n}$$

When $m = 1$, the Jacobian reduces to the gradient $\nabla f^\top$. The multivariate chain rule for composed vector functions is:

$$\frac{\partial (\mathbf{g} \circ \mathbf{f})}{\partial \mathbf{x}} = \mathbf{J}_g \cdot \mathbf{J}_f$$

## Example

A neural network layer maps $n = 2$ inputs to $m = 3$ outputs via $\mathbf{f}(\mathbf{x}) = \sigma(\mathbf{W}\mathbf{x})$, where $\mathbf{W} \in \mathbb{R}^{3 \times 2}$. The Jacobian $\mathbf{J} \in \mathbb{R}^{3 \times 2}$ contains the partial derivatives of each output neuron with respect to each input. Backpropagation computes the upstream loss gradient as $\mathbf{J}^\top \boldsymbol{\delta}$, where $\boldsymbol{\delta} \in \mathbb{R}^3$ is the error arriving from the next layer.

## Remember

In quantitative finance, the Jacobian appears whenever a pricing function produces multiple outputs simultaneously — for example, calibrating a Heston model by matching several implied volatilities at once. Automatic differentiation (used in PyTorch and TensorFlow) constructs the Jacobian efficiently through forward or reverse mode passes, enabling gradient-based calibration of models with many parameters without finite-difference approximations.
