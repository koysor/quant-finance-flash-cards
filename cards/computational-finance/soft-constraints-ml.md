# Soft Constraints in Machine Learning

**Topic:** Computational Finance
**Tags:** soft constraints, penalty term, loss function, no-arbitrage, domain knowledge, physics-informed
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

A soft constraint encodes domain knowledge — such as a financial no-arbitrage condition — as an additive penalty in the loss function, allowing the model to violate the constraint at a cost rather than through a hard architectural restriction, balancing data fit against financial plausibility.

## Key Formula

The augmented loss combines a data-fit term with one or more penalty terms:

$$\mathcal{L}(\theta) = \underbrace{\mathcal{L}_{\text{data}}(\theta)}_{\text{fit to observations}} + \sum_k \lambda_k \underbrace{\mathcal{P}_k(\theta)}_{\text{constraint violation}}$$

Each penalty $\mathcal{P}_k(\theta) \geq 0$ is zero when the constraint is satisfied and positive when violated. The weight $\lambda_k$ controls the trade-off: large $\lambda_k$ enforces the constraint almost rigidly; small $\lambda_k$ treats it as a weak prior. A common form for a monotonicity constraint $f \geq 0$ is:

$$\mathcal{P}(\theta) = \sum_j \max\!\left(0,\, -\frac{\partial f_\theta}{\partial x}\bigg|_{x_j}\right)$$

## Example

A neural network trained to price call options without constraints learns 12% of test predictions with negative delta (price falls as the underlying rises — pure arbitrage). Adding a monotonicity penalty with $\lambda = 10$ reduces delta violations to 0.3% with only a 2% increase in pricing error. Setting $\lambda = 100$ eliminates violations entirely but increases pricing error by 8% — showing the trade-off between financial rigour and data fit.

## Remember

Hard constraints (e.g. clipping outputs, constrained architectures) are rigid and can prevent the model learning the correct function altogether. Soft constraints are the preferred approach in quantitative finance because financial rules such as put-call parity, call monotonicity, and convexity in strike are exact only in idealised theory — real market data contains microstructure noise that violates them slightly. Soft constraints guide the network towards financially consistent solutions without over-constraining it.
