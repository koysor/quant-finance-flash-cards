# Neural Networks as Dynamical Systems

**Topic:** Computational Finance
**Tags:** resnet, neural ode, dynamical systems, optimal control, stability, exploding gradients
**Created:** 2026-06-03
**Author:** Gemini CLI

---

## Definition

Viewing **Neural Networks as Dynamical Systems** (specifically Residual Networks) interprets the forward pass of a network as the discretisation of a continuous-time ordinary differential equation (ODE). This perspective allows for the application of **stability theory** from dynamical systems and **optimal control theory** (e.g., Pontryagin's Maximum Principle) to design deep learning architectures that are more robust, stable, and data-efficient.

## Key Formula

A **Residual Network (ResNet)** layer is defined by the transformation:

$$X_{t+1} = X_t + f(X_t, \theta_t)$$

where $X_t$ is the state (activations) at layer $t$, and $f$ is the residual function. If we introduce a step size $\Delta t \to 0$, this converges to a **Neural ODE**:

$$\frac{dX}{dt} = f(X_t, t, \theta_t)$$

The training of the network then becomes an **Optimal Control Problem**: find the parameters $\theta(t)$ (the control) that minimise a terminal loss $J = \Phi(X_T)$ subject to the state dynamics.

## Example

In financial time-series forecasting, a standard deep network might suffer from **exploding gradients** if the weights are poorly initialised, leading to unstable predictions. By interpreting the network as a stable dynamical system, one can enforce constraints on the weights (e.g., anti-symmetric weights) such that the energy of the system $\lVert X_t \rVert^2$ is conserved or dissipated over layers. This ensures that the network remains stable even as its depth (number of layers) increases, leading to more reliable risk estimates.

## Remember

The "Networks as ODEs" viewpoint bridges the gap between machine learning and classical physics/engineering. It explains why ResNets are so successful: they are essentially stable Euler integrators of a continuous process. For quantitative finance, this is crucial for **model interpretability** and **stability**—ensuring that a pricing neural network doesn't produce wildly different prices (numerical instability) when the input market data is slightly perturbed.
