# Sensitivity

**Topic:** Calculus
**Tags:** sensitivity, partial derivatives, Greeks, dv01, risk management
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Sensitivity** is the rate of change of a financial instrument's value with respect to a change in one of its underlying risk factors, holding all other factors constant. Mathematically it is a partial derivative: if $V$ is the value of a position and $x$ is a risk factor, the sensitivity is $\partial V / \partial x$.

## Key Formula

For a value function $V(x_1, x_2, \ldots, x_n)$ depending on $n$ risk factors, the sensitivity to factor $x_i$ is:

$$S_i = \frac{\partial V}{\partial x_i}$$

In practice, sensitivities are approximated by finite differences using a small bump $h$:

$$S_i \approx \frac{V(x_i + h) - V(x_i - h)}{2h}$$

This **bump-and-reprice** approach is used when an analytic formula for $\partial V / \partial x_i$ is not available (e.g. for exotic options or complex structured products).

## Example

A fixed income trader holds a 10-year government bond worth £1,000,000. They bump the yield by $h = 1\,\text{bp} = 0.0001$:

$$V(y + h) = \text{£}999{,}550 \qquad V(y - h) = \text{£}1{,}000{,}450$$

$$S_{\text{yield}} \approx \frac{999{,}550 - 1{,}000{,}450}{2 \times 0.0001} = \frac{-900}{0.0002} = -\text{£}4{,}500{,}000 \text{ per unit}$$

The DV01 (change per one basis point) is therefore:

$$\text{DV01} = S_{\text{yield}} \times 0.0001 = \text{£}450$$

## Remember

Sensitivities are the universal language of risk management across every asset class: **DV01** (interest rate sensitivity) in fixed income, **delta/gamma/vega** (the Greeks) in derivatives, and **duration gap** in banking book ALM. Risk limits, hedges, and capital charges are all expressed in sensitivity terms. The bump-and-reprice method means that even the most complex payoff can be risk-managed using only a pricer and a loop — making sensitivity the computational bridge between derivative mathematics and daily trading practice.
