# Modelling with Calculus

**Topic:** Calculus
**Tags:** rates of change, optimisation, differential equations, mathematical modelling, revenue, cost
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Modelling with calculus** translates real-world problems into mathematical functions and then uses differentiation and integration to find rates of change, optimal values, and accumulated quantities. The key step is correctly defining the variable, function, and what the derivative represents in context.

## Key Formula

**Optimisation workflow:**

1. Express the quantity to optimise as $f(x)$
2. Find $f'(x) = 0$ to locate stationary points
3. Use $f''(x)$ or sign analysis to confirm maximum or minimum
4. Interpret in context (check endpoint values if domain is bounded)

**Connected rates of change** (chain rule):

$$\frac{dy}{dt} = \frac{dy}{dx} \cdot \frac{dx}{dt}$$

## Example

A company's revenue is $R(q) = 200q - 2q^2$ (£) and cost is $C(q) = 50q + 1{,}000$ (£). Find the output $q$ that maximises profit.

$$\Pi(q) = R(q) - C(q) = 150q - 2q^2 - 1{,}000$$

$$\Pi'(q) = 150 - 4q = 0 \implies q = 37.5$$

$$\Pi''(q) = -4 < 0 \implies \text{confirmed maximum}$$

Maximum profit: $\Pi(37.5) = 150(37.5) - 2(37.5)^2 - 1000 = \text{£}1{,}812.50$.

## Remember

Calculus modelling is the foundation of **continuous-time finance**. The differential equation $\frac{dS}{dt} = \mu S$ (no randomness) produces exponential growth $S(t) = S_0 e^{\mu t}$, while adding randomness gives the stochastic differential equation $dS = \mu S\, dt + \sigma S\, dW_t$. Setting up a model — identifying what is constant, what changes, and at what rate — is the first and most critical step in derivative pricing, risk management, and portfolio optimisation alike.
