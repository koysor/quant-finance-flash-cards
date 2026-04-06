# Differential Equations

**Topic:** Calculus
**Tags:** ODE, PDE, differential equations, Black-Scholes, option pricing
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

A **differential equation** is an equation that relates a function to one or more of its derivatives. An **ordinary differential equation** (ODE) involves derivatives with respect to a single variable; a **partial differential equation** (PDE) involves partial derivatives with respect to two or more variables.

## Key Formula

**First-order linear ODE** (general form):

$$\frac{dy}{dt} + P(t)\,y = Q(t)$$

**Second-order linear ODE** (e.g. simple harmonic motion):

$$\frac{d^2y}{dt^2} + p\,\frac{dy}{dt} + q\,y = f(t)$$

**Second-order linear PDE** in two variables (general form):

$$A\,u_{xx} + B\,u_{xy} + C\,u_{yy} + D\,u_x + E\,u_y + F\,u = G$$

**Black-Scholes PDE** (a parabolic PDE central to option pricing):

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

## Example

The Vasicek interest-rate model gives the ODE for the expected short rate $r(t)$:

$$\frac{dr}{dt} = \gamma(\bar{r} - r)$$

This first-order linear ODE has solution $r(t) = \bar{r} + (r_0 - \bar{r})\,e^{-\gamma t}$. With $\gamma = 0.5$, $\bar{r} = 0.04$, and $r_0 = 0.08$, the rate decays from 8% towards the long-run mean of 4%, halving the gap every $\ln 2 / 0.5 \approx 1.4$ years.

## Remember

Differential equations are the language of continuous-time finance. ODEs govern mean-reverting processes (Vasicek, CIR) and yield curve dynamics; PDEs govern option pricing — the Black-Scholes PDE turns a stochastic pricing problem into a deterministic boundary-value problem that can be solved analytically (European options) or numerically (American and exotic options). Recognising whether you face an ODE or a PDE determines the solution method: ODEs admit closed-form solutions via integrating factors or characteristic equations, whilst PDEs require classification (elliptic, parabolic, hyperbolic) before choosing a technique.
