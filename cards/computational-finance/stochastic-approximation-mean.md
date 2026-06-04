# Stochastic Approximation of a Mean

**Topic:** Computational Finance
**Tags:** stochastic approximation, robbins-monro, online learning, running mean, sgd
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Stochastic approximation** is a family of iterative algorithms for finding the root or optimum of a function that can only be observed with noise, one sample at a time. The simplest instance is the **Robbins-Monro algorithm** (1951) for estimating a mean $\mu = \mathbb{E}[X]$ without storing all data: update a running estimate $\hat{\mu}_n$ after each new observation $x_n$ using a step size $\alpha_n$ that decreases over time.

## Key Formula

The **Robbins-Monro update** for estimating a mean:

$$\hat{\mu}_{n+1} = \hat{\mu}_n + \alpha_n\,(x_n - \hat{\mu}_n)$$

Conditions for convergence to the true mean $\mu$:

$$\sum_{n=1}^\infty \alpha_n = \infty \quad \text{(steps sum to infinity — reach the truth)}$$
$$\sum_{n=1}^\infty \alpha_n^2 < \infty \quad \text{(steps square-summable — noise averages out)}$$

The choice $\alpha_n = 1/n$ reduces to the ordinary running mean $\hat{\mu}_n = \frac{1}{n}\sum_{i=1}^n x_i$. In RL, the **constant step size** $\alpha_n = \alpha$ (which violates the second condition) is often preferred for non-stationary environments because it gives more weight to recent observations.

## Example

An execution algorithm estimates the average bid-ask spread $\mu$ in real time to calibrate its order placement. After observing spreads $x_1 = 2.1$, $x_2 = 1.9$, $x_3 = 2.4$ bps with constant step size $\alpha = 0.1$:

$$\hat{\mu}_1 = 0 + 0.1(2.1 - 0) = 0.21$$
$$\hat{\mu}_2 = 0.21 + 0.1(1.9 - 0.21) = 0.21 + 0.169 = 0.379$$
$$\hat{\mu}_3 = 0.379 + 0.1(2.4 - 0.379) = 0.379 + 0.202 = 0.581$$

With $\alpha_n = 1/n$: $\hat{\mu}_3 = (2.1 + 1.9 + 2.4)/3 = 2.13$ bps — the ordinary average. The constant-step version tracks regime shifts; the $1/n$ version converges to the long-run mean.

## Remember

Stochastic approximation is the theoretical foundation of **stochastic gradient descent (SGD)** and **temporal difference learning** in reinforcement learning. Every Q-value update in Q-learning is a stochastic approximation step: $Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma \max Q(s',a') - Q(s,a)]$ is exactly the Robbins-Monro form with "error signal" $r + \gamma \max Q - Q$. The learning rate schedule — constant for non-stationary markets, decaying for stationary ones — is one of the most important hyperparameters when deploying RL execution agents in live trading, directly controlling the speed-stability trade-off.
