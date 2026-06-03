# Linear Quadratic Regulator (LQR)

**Topic:** Stochastic Processes
**Tags:** lqr, linear quadratic regulator, optimal control, riccati equation, stochastic control, hjb
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **Linear Quadratic Regulator (LQR)** is the optimal control problem with linear state dynamics and a quadratic cost — the only stochastic control problem with a fully analytical solution. It is the foundational worked example of the HJB equation, producing a **Riccati equation** for the value function and a linear feedback control law. Almgren-Chriss optimal execution is a financial application of LQR.

## Key Formula

**State dynamics:** $dx_t = (Ax_t + Bu_t)\,dt + \sigma\,dW_t$

**Cost to minimise:** $J = \mathbb{E}\!\left[\int_0^T \!\left(x_t^\top Q x_t + u_t^\top R u_t\right)dt + x_T^\top P_T x_T\right]$

The HJB equation has a quadratic value function $V(t, x) = x^\top P_t x + c_t$, where $P_t$ satisfies the **matrix Riccati equation**:

$$-\dot{P}_t = A^\top P_t + P_t A - P_t B R^{-1} B^\top P_t + Q, \qquad P_T = \text{given}$$

The **optimal control** is a linear state-feedback law:

$$u_t^* = -R^{-1}B^\top P_t\, x_t$$

## Example

Almgren-Chriss liquidation in LQR form: state $x_t$ = remaining inventory, control $u_t$ = trading rate (negative = selling), $A = 0$, $B = 1$, $Q = \sigma^2/2$ (variance risk), $R = \eta$ (temporary impact), $P_T = 0$ (no terminal inventory cost). The Riccati equation gives $P_t = \sqrt{Q/R}\,\tanh(\kappa(T-t))$ where $\kappa = \sqrt{Q/R}$, and the optimal rate is $u_t^* = -\kappa x_t / \tanh(\kappa(T-t))$ — decelerating execution that is approximately TWAP for small risk aversion.

## Remember

LQR is the rare case where the HJB equation can be solved in closed form — the quadratic structure of both the dynamics and the cost makes the value function exactly quadratic, reducing the PDE to an ODE (the Riccati equation). In RL, LQR serves as the gold-standard validation benchmark: a policy gradient or TDBP agent trained on linear-Gaussian dynamics should recover the Riccati-optimal linear policy exactly, and any deviation quantifies the approximation error of the RL method. When market dynamics depart from linearity or the cost becomes non-quadratic (e.g. CVaR instead of variance), the LQR closed form breaks down and RL becomes the practical alternative.
