# Ordinary Differential Equations

**Topic:** Calculus
**Tags:** ODE, differential equation, continuous compounding, Vasicek, interest rates, calculus
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

An **ordinary differential equation** (ODE) is an equation that relates an unknown function of a **single variable** to its derivatives. Contrast this with a **partial differential equation** (PDE), which involves a function of two or more variables and its partial derivatives. ODEs describe how a quantity changes continuously over time and appear throughout quantitative finance wherever a single state variable — such as a short rate or portfolio value — evolves deterministically.

## Key Formula

A first-order linear ODE has the standard form:

$$\frac{dy}{dt} + P(t)\,y = Q(t)$$

The simplest case, **exponential growth/decay** ($P$ constant, $Q = 0$):

$$\frac{dy}{dt} = \lambda y \implies y(t) = y_0 \, e^{\lambda t}$$

The **Vasicek deterministic skeleton** (setting noise to zero in the Vasicek SDE) is a mean-reverting ODE:

$$\frac{dr}{dt} = \kappa(\bar{r} - r)$$

with solution $r(t) = \bar{r} + (r_0 - \bar{r})\,e^{-\kappa t}$, showing exponential decay towards $\bar{r}$.

## Example

A bank account earns a continuously compounded rate of $r = 0.05$. Starting with £1,000, the balance $V(t)$ satisfies:

$$\frac{dV}{dt} = 0.05\,V, \quad V(0) = 1000$$

This is a separable ODE. Separating variables: $\frac{dV}{V} = 0.05\,dt$. Integrating both sides:

$$\ln V = 0.05t + C \implies V(t) = 1000\,e^{0.05t}$$

After 10 years: $V(10) = 1000 \times e^{0.5} \approx £1{,}649$.

## Remember

ODEs with a **single time variable** underpin two foundational finance results. First, the continuous compounding formula $V(t) = V_0 e^{rt}$ — standard in derivatives discounting — comes directly from solving $\frac{dV}{dt} = rV$. Second, setting the stochastic noise term to zero in the Vasicek or Ornstein-Uhlenbeck SDE gives a deterministic ODE whose solution reveals the mean-reverting skeleton: every realisation of the full stochastic process is anchored to this deterministic path. Understanding ODEs is therefore the gateway to understanding SDEs — the SDE is simply an ODE with a random forcing term added.
