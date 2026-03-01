# Stochastic Integrals

**Topic:** Stochastic Processes
**Tags:** stochastic integral, Itô integral, stochastic calculus, Brownian motion
**Author:** Claude Opus 4.6

---

## Definition

A **stochastic integral** (or Itô integral) is the integral counterpart of a stochastic differential equation. Just as ordinary differential equations can be written in integral form, SDEs have stochastic integrals — but with the extra Itô correction term carrying over from Itô's lemma.

The key technique for evaluating stochastic integrals is to rearrange Itô's lemma into integral form: find an antiderivative $F$ such that $\frac{\partial F}{\partial W} =$ integrand, then apply the master formula.

## Key Formula

**Master formula** for $\int_0^t g(W_\tau)\,dW_\tau$:

Find $F(W, \tau)$ such that $\frac{\partial F}{\partial W} = g(W)$. Then:

$$\int_0^t g(W_\tau)\,dW_\tau = F(W_t, t) - F(W_0, 0) - \int_0^t \left(\frac{\partial F}{\partial \tau} + \frac{1}{2}\frac{\partial^2 F}{\partial W^2}\right) d\tau$$

This is Itô's lemma rearranged — the $dW$ integral on the left equals the total change in $F$ minus the $dt$ integral.

**Key property of Itô integrals:**

$$E\!\left[\int_0^t g(W_\tau)\,dW_\tau\right] = 0$$

The expected value of any Itô integral is zero (the integral is a martingale).

## Example

Evaluate $\int_0^t W_\tau\,dW_\tau$:

Set $g(W) = W$, so $F = \frac{1}{2}W^2$. Then $\frac{\partial F}{\partial \tau} = 0$ and $\frac{\partial^2 F}{\partial W^2} = 1$:

$$\int_0^t W_\tau\,dW_\tau = \frac{1}{2}W_t^2 - 0 - \int_0^t \frac{1}{2}\,d\tau = \frac{1}{2}W_t^2 - \frac{1}{2}t$$

In ordinary calculus, $\int x\,dx = \frac{1}{2}x^2$. In stochastic calculus, there is an extra $-\frac{1}{2}t$ correction — the Itô integral is **not** simply the antiderivative evaluated at the endpoints.

## Remember

- The identity $\int_0^t W_\tau\,dW_\tau = \frac{1}{2}(W_t^2 - t)$ is the **canonical example** showing how stochastic integrals differ from ordinary ones. The $-\frac{1}{2}t$ is the integrated Itô correction.
- Itô integrals have **zero expectation** — they are martingales. This property is used extensively in derivatives pricing: any hedging strategy expressible as $\int \Delta_s\,dW_s$ has zero expected profit under the risk-neutral measure.
- The recipe is mechanical: anti-differentiate with respect to $W$ to find $F$, compute the partial derivatives, and substitute into the master formula. The $dt$ integral that remains is an ordinary (Riemann) integral.
