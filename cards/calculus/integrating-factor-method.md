# Integrating Factor Method

**Topic:** Calculus
**Tags:** integrating factor, ODE, linear differential equation, Vasicek, Ornstein-Uhlenbeck, SDE
**Author:** Claude Opus 4.6

---

## Definition

The **integrating factor method** is a technique for solving first-order linear differential equations by multiplying through by a specially chosen function that makes the left-hand side an exact derivative. In quantitative finance, it is the standard method for solving the Vasicek/Ornstein-Uhlenbeck SDE analytically.

## Key Formula

For the ODE $\frac{dy}{dt} + P(t) \, y = Q(t)$, the integrating factor is:

$$\mu(t) = e^{\int P(t) \, dt}$$

Multiplying through gives $\frac{d}{dt}\bigl[\mu(t) \, y\bigr] = \mu(t) \, Q(t)$, which integrates directly.

**Application to the Vasicek model** $dr = \gamma(\bar{r} - r) \, dt + \sigma \, dW$:

1. Substitute $u = r - \bar{r}$ to get $du = -\gamma u \, dt + \sigma \, dW$
2. The integrating factor is $e^{\gamma t}$
3. Multiply: $d(u \, e^{\gamma t}) = \sigma \, e^{\gamma t} \, dW$
4. Integrate from 0 to $t$ and solve:

$$r(t) = \bar{r} + (r_0 - \bar{r}) \, e^{-\gamma t} + \sigma \int_0^t e^{\gamma(s - t)} \, dW_s$$

## Example

For the ODE $\frac{dy}{dt} + 3y = 6$ with $y(0) = 1$: the integrating factor is $e^{3t}$. Multiplying gives $\frac{d}{dt}(y \, e^{3t}) = 6e^{3t}$. Integrating: $y \, e^{3t} = 2e^{3t} + C$, so $y(t) = 2 + Ce^{-3t}$. Applying $y(0) = 1$: $C = -1$, giving $y(t) = 2 - e^{-3t}$. The solution converges to 2 as $t \to \infty$.

## Remember

The integrating factor $e^{\gamma t}$ is the key trick for solving linear SDEs like the Vasicek model. In the solution $r(t) = \bar{r} + (r_0 - \bar{r})e^{-\gamma t} + \text{noise}$, you can read off three components: the long-run level $\bar{r}$, the exponentially decaying memory of the initial condition, and accumulated random shocks with recent ones weighted more heavily. This same technique applies to any linear mean-reverting model in finance.
