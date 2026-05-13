# Momentum in Optimisation

**Topic:** Computational Finance
**Tags:** momentum, gradient descent, optimisation, convergence, neural networks, machine learning
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Momentum** is a modification to gradient descent that accumulates a velocity vector in directions of persistent gradient, dampening oscillations and accelerating convergence in shallow directions. At each step, the update combines the current gradient with a fraction $\gamma$ of the previous update.

## Key Formula

$$\mathbf{v}_{t+1} = \gamma\, \mathbf{v}_t + \eta\, \nabla J(\boldsymbol{\theta}_t)$$

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \mathbf{v}_{t+1}$$

where $\gamma \in [0, 1)$ is the momentum coefficient (typically $0.9$) and $\eta$ is the learning rate. With $\gamma = 0$ this reduces to standard gradient descent. The effective update is a geometrically-weighted sum of all past gradients:

$$\mathbf{v}_{t+1} = \eta \sum_{k=0}^{t} \gamma^{t-k}\, \nabla J(\boldsymbol{\theta}_k)$$

## Example

Fitting a neural network to predict credit default. The loss surface forms a narrow valley: gradients oscillate strongly across the valley but point weakly along it. Without momentum ($\gamma = 0$), parameters bounce between valley walls and converge in 500 iterations. With $\gamma = 0.9$, oscillations cancel through accumulated velocity and convergence reaches the same loss in 120 iterations.

## Remember

Momentum in optimisation mirrors momentum in financial markets: just as a trending asset's price reflects accumulated buying pressure over recent periods, a momentum-based parameter update reflects the accumulated gradient history. This is why momentum-equipped optimisers (SGD with momentum, Adam) train financial models far faster than vanilla gradient descent — they exploit persistent curvature information rather than treating each iteration independently.
