# Fokker-Planck Steady State

**Topic:** Stochastic Processes
**Tags:** Fokker-Planck, steady state, probability density, inverse problem, calibration, mean reversion
**Author:** Claude Opus 4.6

---

## Definition

The **Fokker-Planck steady state** is the time-independent solution of the Fokker-Planck equation for a mean-reverting stochastic process. When $\partial p / \partial t = 0$, the probability density has converged to a stationary distribution $p_\infty(r)$. The **inverse problem** — recovering the drift function from an observed steady-state density — is a powerful calibration tool.

## Key Formula

For an SDE of the form $dr = u(r) \, dt + \nu r^\beta \, dW$, the Fokker-Planck equation is:

$$\frac{\partial p}{\partial t} = -\frac{\partial}{\partial r}\bigl[u(r) \, p\bigr] + \frac{1}{2}\frac{\partial^2}{\partial r^2}\bigl[\nu^2 r^{2\beta} \, p\bigr]$$

At steady state ($\partial p / \partial t = 0$):

$$0 = -\frac{d}{dr}\bigl[u(r) \, p_\infty\bigr] + \frac{1}{2}\frac{d^2}{dr^2}\bigl[\nu^2 r^{2\beta} \, p_\infty\bigr]$$

**Recovering drift from the density:**

$$u(r) = \nu^2 \beta r^{2\beta - 1} + \frac{1}{2}\nu^2 r^{2\beta} \frac{d}{dr}\bigl(\ln p_\infty\bigr)$$

| Direction | Given | Find |
|---|---|---|
| Forward problem | SDE (drift + diffusion) | Density $p(r, t)$ |
| Inverse problem | Steady-state density $p_\infty(r)$ | Drift function $u(r)$ |

## Example

If interest rates are observed to have a steady-state density that is approximately normal centred on 5% with standard deviation 1.2%, one can substitute this Gaussian form into the inverse formula. The resulting drift will be linear in $r$ — confirming that the Vasicek/Ornstein-Uhlenbeck model with constant diffusion ($\beta = 0$) is consistent with the data.

## Remember

The Fokker-Planck steady state links observed market distributions to the underlying stochastic model. If you can measure the empirical distribution of a variable like interest rates or volatility, you can reverse-engineer the drift function that would produce that distribution. This is a model-free calibration approach: the data tells you what the drift must be, rather than assuming a parametric model and fitting its parameters.
