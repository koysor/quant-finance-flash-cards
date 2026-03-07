# Itô Product Rule

**Topic:** Stochastic Processes
**Tags:** ito calculus, product rule, quadratic covariation, integration by parts, stochastic
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **Itô product rule** (stochastic integration by parts) extends the classical product rule to stochastic processes. Unlike ordinary calculus, the differential of a product $d(X_t Y_t)$ includes an extra **quadratic covariation** term $dX_t\,dY_t$ because second-order terms do not vanish when Brownian motion is involved.

## Key Formula

For two Itô processes $X_t$ and $Y_t$:

$$d(X_t Y_t) = X_t\,dY_t + Y_t\,dX_t + dX_t\,dY_t$$

The multiplication rules for Brownian increments are:

$$dW \cdot dW = dt, \qquad dW \cdot dt = 0, \qquad dt \cdot dt = 0$$

For the **quotient** $X_t / Y_t$:

$$d\!\left(\frac{X}{Y}\right) = \frac{X}{Y}\!\left(\frac{dX}{X} - \frac{dY}{Y} - \frac{dX\,dY}{XY} + \left(\frac{dY}{Y}\right)^{\!2}\right)$$

## Example

Let $X_t$ and $Y_t$ be two correlated Brownian motions with $dX\,dY = \rho\,dt$. Then:

$$d(X_t Y_t) = X_t\,dY_t + Y_t\,dX_t + \rho\,dt$$

Taking expectations: $\frac{d}{dt}E[X_t Y_t] = \rho$, so $E[X_t Y_t] = \rho\,t$.

This confirms $\text{Cov}(X_t, Y_t) = \rho\,t$ since both have zero mean.

## Remember

The Itô product rule is essential for pricing and hedging multi-asset derivatives. When computing the P&L of a hedged portfolio $\Pi = V - \Delta S$ (option minus delta shares of stock), the cross term $dV\,dS$ from the product rule generates the Itô correction that produces the $\tfrac{1}{2}\sigma^2 S^2 \Gamma$ term in the P&L decomposition. For correlated assets, the $dX_i\,dX_j = \rho_{ij}\,dt$ terms drive cross-gamma exposure, basket option pricing, and correlation risk — all absent from classical calculus.
