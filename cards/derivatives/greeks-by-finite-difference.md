# Greeks by Finite Difference

**Topic:** Derivatives
**Level:** A Level Mathematics
**Tags:** finite difference, bumping, Greeks, numerical differentiation, sensitivity
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Greeks by finite difference (also called "bumping") compute the sensitivity of an option price to a risk factor by perturbing the input, repricing the option, and taking the ratio of price change to input change. This is the model-agnostic approach to Greeks — it works with any pricing function, whether Black-Scholes, Monte Carlo, PDE solver, or a complex exotic pricer. It is the default method when analytical Greeks are unavailable.

## Key Formula

**Central difference** (second-order accuracy):

$$\delta \approx \frac{V(S + h) - V(S - h)}{2h}$$

$$\Gamma \approx \frac{V(S + h) - 2V(S) + V(S - h)}{h^2}$$

**Forward difference** (first-order accuracy, requires only one extra pricing):

$$\delta \approx \frac{V(S + h) - V(S)}{h}$$

**Cross-gamma** (e.g. vanna $= \partial^2 V / \partial S \, \partial \sigma$):

$$\text{Vanna} \approx \frac{V(S+h_S, \sigma+h_\sigma) - V(S+h_S, \sigma-h_\sigma) - V(S-h_S, \sigma+h_\sigma) + V(S-h_S, \sigma-h_\sigma)}{4 h_S h_\sigma}$$

## Example

A barrier option is priced via Monte Carlo at $V(S) = £7.50$ with $S = £100$. Using bump size $h = £0.50$:

$$V(S + h) = V(100.50) = £7.68$$
$$V(S - h) = V(99.50) = £7.31$$

$$\delta = \frac{7.68 - 7.31}{2 \times 0.50} = \frac{0.37}{1.00} = 0.37$$

$$\Gamma = \frac{7.68 - 2 \times 7.50 + 7.31}{0.50^2} = \frac{-0.01}{0.25} = -0.04$$

The delta of 0.37 means the option gains £0.37 for every £1 rise in the underlying. Computing delta required 2 additional pricings; gamma required no extra (reuses the same three prices).

## Remember

Bumping is the "brute force" approach to Greeks that every quant developer implements first. Its great advantage is universality — it works with any model, no matter how complex. Its disadvantage is cost: computing $n$ Greeks requires $O(n)$ repricings (or $2n$ for central differences), and for Monte Carlo pricers each repricing is expensive. This is why **adjoint algorithmic differentiation (AAD)** has become the gold standard at sophisticated desks — it computes all first-order Greeks in a single backward pass at roughly the cost of one pricing. Understanding bumping is still essential, however: it serves as the benchmark for validating AAD implementations, and for second-order Greeks (gamma, cross-gamma) bumping remains the practical choice in most production systems.
