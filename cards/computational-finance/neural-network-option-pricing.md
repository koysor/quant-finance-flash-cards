# Neural Networks in Option Pricing

**Topic:** Computational Finance
**Tags:** neural network, option pricing, soft constraints, derivatives, monotonicity, deep learning
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Neural networks approximate option pricing functions by learning a mapping from market inputs to prices, offering sub-second inference after training; soft no-arbitrage constraints encoded as penalty terms in the loss function ensure the network produces financially consistent prices.

## Key Formula

A feedforward network $f_\theta$ maps inputs $(S, K, T, \sigma, r)$ to an option price. A monotonicity penalty on the call delta is added to prevent arbitrage violations:

$$\mathcal{L}(\theta) = \underbrace{\frac{1}{n}\sum_{i=1}^n \bigl(f_\theta(\mathbf{x}_i) - C_i\bigr)^2}_{\text{pricing error}} + \lambda\underbrace{\sum_j \max\!\left(0,\,-\frac{\partial f_\theta}{\partial S}\bigg|_{\mathbf{x}_j}\right)}_{\text{monotonicity penalty}}$$

The second term penalises negative call deltas — violations of the financial constraint $\partial C/\partial S \geq 0$ — without hard-constraining the architecture.

## Example

A network trained to price European calls without constraints produces delta violations in 8% of out-of-sample points (call prices decreasing as the underlying rises). Adding the monotonicity penalty reduces violations to 0.2% while keeping mean absolute pricing error below $\$0.03$. After training, the network prices 10,000 options per second, versus three minutes for an equivalent Monte Carlo run.

## Remember

The challenge in replacing Black-Scholes with a neural network is not prediction accuracy but financial plausibility: a model that prices a call lower when the underlying rises creates immediate arbitrage. Soft constraints bridge the gap between deep learning flexibility and financial rigour — they guide the network towards solutions satisfying economic logic without restricting its expressive power. This hybrid approach is the starting point for more advanced architectures such as TDBP and attention-based pricers.
