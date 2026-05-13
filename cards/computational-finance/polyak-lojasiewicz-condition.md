# Polyak–Łojasiewicz Condition

**Topic:** Computational Finance
**Tags:** polyak-łojasiewicz, convergence, gradient descent, non-convex, optimisation theory, neural networks
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Polyak–Łojasiewicz (PL) condition** is a property of a differentiable function that guarantees gradient descent converges to the global minimum even when the function is non-convex. It requires that whenever the gradient is small, the function value must be close to optimal — ruling out the "flat plateaus" where gradient descent can stall indefinitely.

## Key Formula

A function $J: \mathbb{R}^n \to \mathbb{R}$ satisfies the PL condition with constant $\mu > 0$ if:

$$\frac{1}{2}\|\nabla J(\boldsymbol{\theta})\|^2 \geq \mu\,(J(\boldsymbol{\theta}) - J^*) \quad \text{for all } \boldsymbol{\theta}$$

where $J^* = \min_{\boldsymbol{\theta}} J(\boldsymbol{\theta})$. Under the PL condition, gradient descent with step size $\eta \leq 1/L$ satisfies:

$$J(\boldsymbol{\theta}_t) - J^* \leq (1 - \mu\eta)^t\,(J(\boldsymbol{\theta}_0) - J^*)$$

This is **linear convergence** to the global optimum — the error shrinks by a constant factor $(1-\mu\eta) < 1$ at every iteration, regardless of non-convexity.

## Example

Suppose $J^* = 0$ and the current loss is $J(\boldsymbol{\theta}_t) = 0.1$. With $\mu = 0.5$ and $\eta = 0.1$, the PL bound gives:

$$J(\boldsymbol{\theta}_{t+1}) \leq (1 - 0.05) \times 0.1 = 0.095$$

After 100 steps: $(0.95)^{100} \times 0.1 \approx 0.00059$ — near zero. This holds even if $J$ has many saddle points, as long as the PL condition is satisfied throughout.

## Remember

The PL condition matters in quantitative finance because the loss functions of financial neural networks (return forecasting, option pricing approximation, credit scoring) are non-convex — standard convexity guarantees do not apply. Recent research shows that overparameterised neural networks often satisfy the PL condition in the neighbourhood of their initialisation, providing the theoretical explanation for why gradient descent reliably finds good solutions in practice. For practitioners: if your optimiser converges stably to a low loss on financial training data, the PL condition is likely what's making it work, even if the landscape is not globally convex.
