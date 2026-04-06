# Integrand

**Topic:** Calculus
**Tags:** calculus, integration, expectation, option pricing, payoff function
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **integrand** is the function placed inside an integral sign — the quantity being accumulated over an interval or domain. In the expression $\int_a^b f(x)\,dx$, the function $f(x)$ is the integrand; $dx$ specifies the variable with respect to which accumulation takes place.

The integrand entirely determines what is being measured: changing it changes the result from, say, an area to a probability to a present value. Identifying the integrand correctly is the first step in setting up any integral in finance or applied mathematics.

## Key Formula

General definite integral with integrand $f(x)$:

$$\int_a^b \underbrace{f(x)}_{\text{integrand}}\,dx$$

European call price as a risk-neutral expectation — the integrand is the discounted payoff weighted by the risk-neutral density $q(S_T)$:

$$C = e^{-rT}\int_0^{\infty} \underbrace{\max(S_T - K,\, 0)\cdot q(S_T)}_{\text{integrand}}\,dS_T$$

Expected value of a continuous random variable — the integrand is $x\,f(x)$:

$$E[X] = \int_{-\infty}^{\infty} \underbrace{x\,f(x)}_{\text{integrand}}\,dx$$

## Example

A bond pays a continuous coupon of £6 per year for 2 years, discounted at $r = 4\%$.

$$PV = \int_0^2 \underbrace{6\,e^{-0.04t}}_{\text{integrand}}\,dt = 6\left[\frac{-e^{-0.04t}}{0.04}\right]_0^2 = 150\left(1 - e^{-0.08}\right) \approx \textbf{£11.54}$$

The integrand $6\,e^{-0.04t}$ represents the present value of an instantaneous coupon payment at time $t$; integrating sums these over the full 2-year period.

## Remember

In risk-neutral option pricing, the integrand is the discounted payoff of the option multiplied by the risk-neutral probability density of the underlying price. Modifying the contract — for example, changing a call to an Asian option whose payoff depends on the average price — means changing the integrand inside the same expectation integral. Every exotic option's pricing formula differs from a vanilla call in exactly one place: the integrand. Recognising this makes it straightforward to extend Black-Scholes intuition to more complex payoff structures.
