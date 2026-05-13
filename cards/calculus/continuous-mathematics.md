# Continuous Mathematics

**Topic:** Calculus
**Tags:** continuous, calculus, real analysis, limits, smooth functions
**Author:** Claude Sonnet 4.6

---

## Definition

Continuous mathematics is the branch of mathematics concerned with uncountably infinite structures — real numbers, smooth functions, limits, derivatives, and integrals — where quantities can take any value in an interval rather than jumping between discrete states.

## Key Formula

The Fundamental Theorem of Calculus connects differentiation and integration:

$$\int_a^b f(x)\,dx = F(b) - F(a), \qquad \text{where } F'(x) = f(x)$$

Continuous compounding of a rate $r$ over time $T$ gives the growth factor:

$$e^{rT} = \lim_{n \to \infty} \left(1 + \frac{r}{n}\right)^n$$

## Example

A zero-coupon bond paying £1,000 in 3 years at a continuously compounded rate of $r = 5\%$ is worth $1000 \cdot e^{-0.05 \times 3} = 1000 \cdot e^{-0.15} \approx £860.71$ today. The exponential function — a concept unique to continuous mathematics — gives the exact present value formula used throughout fixed-income and derivatives pricing.

## Remember

Continuous mathematics underpins the entire stochastic calculus framework used in derivatives pricing. Itô's lemma, the Black–Scholes PDE, and the Ornstein–Uhlenbeck process all require limits, smooth functions, and integration over continuous sample paths. Brownian motion itself is only defined in continuous time: its infinite-variation path cannot be expressed as a sequence of discrete steps, requiring the tools of real analysis to handle rigorously.
