# Hard Constraints in Neural Networks

**Topic:** Machine Learning
**Tags:** hard constraints, monotone neural network, input convex, arbitrage-free, architectural constraint, deep learning
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Hard constraints enforce financial properties — such as option price monotonicity or convexity — exactly by designing the network architecture so violations are structurally impossible, rather than penalising them in the loss function.

## Key Formula

**Monotone network** for call delta $\partial C/\partial S \geq 0$: constrain all weights on the path from input $S$ to the output to be non-negative, and use a non-decreasing activation $\sigma$ (e.g. ReLU, softplus). Then by the chain rule, $\partial f/\partial S \geq 0$ everywhere.

**Input Convex Neural Network (ICNN)** for strike convexity $\partial^2 C/\partial K^2 \geq 0$: at each hidden layer $l \geq 1$, constrain the recurrent weights to be non-negative:

$$\mathbf{z}^{(l)} = \sigma\!\left(W_z^{(l)}\mathbf{z}^{(l-1)} + W_x^{(l)}\mathbf{x} + \mathbf{b}^{(l)}\right), \qquad W_z^{(l)} \geq 0$$

Convexity of the composition is then guaranteed by the non-negativity of the recurrent weights and the convexity of $\sigma$.

## Example

A soft-constrained option pricer achieves 0.2% delta violations on 10,000 out-of-sample points. Replacing the penalty term with a monotone architecture (positive weight constraints on the $S$ input path) reduces violations to exactly 0 on the same test set, with pricing error increasing by 1.4% due to the reduced model capacity.

## Remember

Hard constraints are the right choice for production pricing systems where any arbitrage violation — however small — would be immediately exploited. The cost is reduced model capacity: a network that can only express monotone functions cannot model a non-monotone relationship even if noisy data suggests one. Soft constraints are preferred during research (more flexible, easier to train); hard constraints are preferred at deployment (zero-violation guarantees, auditable by regulators).
