# Stochastic Approximation of a Mean (SAM)

**Topic:** Computational Finance
**Tags:** reinforcement learning, stochastic approximation, robbins-monro, learning rate, mean estimation
**Author:** Gemini CLI

---

## Definition

**Stochastic Approximation** is a family of iterative methods used to estimate the properties of a system (like its mean) when only noisy observations are available. The **Stochastic Approximation of a Mean (SAM)** is the simplest version, used to update an estimate as new data points arrive.

In Reinforcement Learning, SAM is used to update value functions. It allows the agent to maintain a "running average" that can adapt to new information without storing all past observations.

## Key Formula

Given a sequence of noisy observations $x_1, x_2, \dots, x_n$ of a random variable $X$, the estimate $\mu_n$ is updated as:

$$\mu_n = \mu_{n-1} + \alpha_n (x_n - \mu_{n-1})$$

For the estimate to converge to the true mean $\mu = \mathbb{E}[X]$ almost surely (a.s.), the learning steps $\alpha_n$ must satisfy the **Robbins-Monro conditions**:

1. $\sum_{n=1}^{\infty} \alpha_n = \infty$ (Steps are large enough to overcome any initial error)
2. $\sum_{n=1}^{\infty} \alpha_n^2 < \infty$ (Steps become small enough to ensure convergence/suppress noise)

## Example

If we set $\alpha_n = 1/n$, the formula yields the standard arithmetic mean:
$\mu_n = \mu_{n-1} + \frac{1}{n}(x_n - \mu_{n-1}) = \frac{1}{n} \sum_{i=1}^n x_i$.
In finance, we often use a constant $\alpha$ (e.g., 0.01) to create an **Exponentially Weighted Moving Average (EWMA)**, which weights recent market events more heavily.

## Remember (Finance application)

Stochastic approximation is the engine behind most on-line learning algorithms. In high-frequency trading, it is used to update estimates of "fair price" or "volatility" tick-by-tick. The Robbins-Monro conditions ensure that our model eventually "settles down" on the truth, provided the environment is stationary.
