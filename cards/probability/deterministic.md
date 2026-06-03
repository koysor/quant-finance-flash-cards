# Deterministic

**Topic:** Probability
**Tags:** deterministic, stochastic, randomness, ode, modelling
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

A **deterministic** system or function is one whose output is fully determined by its inputs and initial conditions — the same inputs always produce the same output, with no random component. It is the mathematical opposite of stochastic: given initial state $x_0$, the future state $x(t)$ is known exactly without reference to any underlying probability space $(\Omega, \mathcal{F}, P)$.

## Key Formula

A deterministic dynamic is governed by an ordinary differential equation (ODE):

$$\frac{dx}{dt} = f(x, t), \quad x(0) = x_0$$

whose unique solution $x(t)$ is a plain function of time. By contrast, a stochastic dynamic adds a Brownian component:

$$dX_t = \underbrace{\mu(X_t, t)\, dt}_{\text{deterministic drift}} + \underbrace{\sigma(X_t, t)\, dW_t}_{\text{stochastic diffusion}}$$

The drift term $\mu\, dt$ is deterministic; the diffusion term $\sigma\, dW_t$ is not.

## Example

A zero-coupon bond paying £1,000 at maturity $T = 5$ years with continuously compounded rate $r = 4\%$ has a deterministic present value:

$$P = 1000\, e^{-rT} = 1000\, e^{-0.04 \times 5} \approx £819.00$$

No randomness enters — the same rate always gives the same price. If instead the short rate followed the Hull–White stochastic model, the future bond price would be a random variable with a full probability distribution.

## Remember

In quantitative finance, classifying a quantity as deterministic or stochastic determines which calculus applies. The drift $\mu$ in Black–Scholes is deterministic (a constant), so it is integrated with ordinary calculus. The stock price $S_t$ is stochastic, so any function $f(S_t)$ must be differentiated using Itô's lemma — ignoring this distinction and applying the ordinary chain rule gives the wrong answer, producing a mispriced hedge.
