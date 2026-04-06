# Product Rule

**Topic:** Calculus
**Tags:** differentiation, product rule, calculus, option greeks, hedging
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The product rule gives the derivative of the product of two differentiable functions. If $h(x) = f(x) \cdot g(x)$, then $h'(x)$ is found by differentiating each factor in turn whilst holding the other constant, then summing the two contributions.

## Key Formula

$$\frac{d}{dx}[f(x)\,g(x)] = f'(x)\,g(x) + f(x)\,g'(x)$$

Equivalently in Leibniz notation, if $u = u(x)$ and $v = v(x)$:

$$(uv)' = u'v + uv'$$

For three factors the rule extends naturally:

$$(uvw)' = u'vw + uv'w + uvw'$$

## Example

Differentiate $h(x) = x^2 e^{-rx}$ where $r = 0.05$ (a continuous discount factor).

Set $f(x) = x^2$ and $g(x) = e^{-rx}$, so $f'(x) = 2x$ and $g'(x) = -r\,e^{-rx}$.

$$h'(x) = 2x\,e^{-rx} + x^2 \cdot (-r)\,e^{-rx} = e^{-rx}\,(2x - rx^2)$$

At $x = 10$: $h'(10) = e^{-0.5}(20 - 5) = 15\,e^{-0.5} \approx 9.10$.

## Remember

The product rule appears whenever a price or payoff is the product of two functions that both depend on the same variable. Differentiating the Black-Scholes call price formula $C = S\,N(d_1) - Ke^{-rT}N(d_2)$ with respect to $S$ to get Delta requires the product rule on $S\,N(d_1)$: Delta $= N(d_1) + S\,N'(d_1)\,\frac{\partial d_1}{\partial S}$. More broadly, any hedging strategy that weights positions by a quantity that itself changes — such as a delta-weighted portfolio where Delta depends on the underlying price — requires the product rule to compute the correct rate of change of total portfolio value.
