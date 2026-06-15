# Discrete-Time Affine Term Structure Model

**Topic:** Fixed Income
**Tags:** discrete-time, affine model, VAR, ang-piazzesi, macro-finance, gaussian, bond pricing
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

A discrete-time affine term structure model (Ang–Piazzesi, 2003) represents the state vector as a Gaussian VAR(1), specifies the stochastic discount factor as log-normal with affine risk prices, and derives bond yields that are exactly affine (linear) functions of the state — producing the same exponential-affine pricing formula as continuous-time models but directly estimable from monthly or quarterly data without discretisation error.

## Key Formula

**State VAR(1) under $\mathbb{P}$:**

$$X_{t+1} = \mu + \Phi X_t + \Sigma\varepsilon_{t+1}, \quad \varepsilon_{t+1} \sim \mathcal{N}(0, I)$$

**Log stochastic discount factor:**

$$m_{t+1} = -r_t - \tfrac{1}{2}\lambda_t^\top\lambda_t - \lambda_t^\top\varepsilon_{t+1}$$

**Market price of risk (essentially affine):** $\lambda_t = \lambda_0 + \lambda_1 X_t$

**Short rate:** $r_t = \delta_0 + \delta_1^\top X_t$

**Risk-neutral VAR** (change of measure):

$$X_{t+1} = \mu^{\mathbb{Q}} + \Phi^{\mathbb{Q}}X_t + \Sigma\varepsilon_{t+1}^{\mathbb{Q}}$$

where $\mu^{\mathbb{Q}} = \mu - \Sigma\lambda_0$ and $\Phi^{\mathbb{Q}} = \Phi - \Sigma\lambda_1$.

**$\tau$-period zero-coupon yield** (affine in $X_t$):

$$y_t(\tau) = A_\tau + B_\tau^\top X_t$$

with $A_\tau$ and $B_\tau$ satisfying recursions:

$$B_\tau = \delta_1 + (\Phi^{\mathbb{Q}})^\top B_{\tau-1}, \quad A_\tau = \delta_0 + A_{\tau-1} + \tfrac{1}{2}B_{\tau-1}^\top\Sigma\Sigma^\top B_{\tau-1} - (\mu^{\mathbb{Q}})^\top B_{\tau-1}$$

## Example

In the Ang–Piazzesi (2003) macro-finance specification, $X_t$ contains CPI inflation $\pi_t$, the output gap $g_t$, and three yield-curve factors. Setting $N = 5$ factors and estimating on monthly US data (1964–2000) gives loadings $\delta_1 = (0.8, 0.6, 1.0, 0.4, 0.2)^\top$: a one-percentage-point rise in inflation raises the short rate by 80 bps on impact. The 10-year yield loading $B_{120}$ is then obtained by iterating the recursion 120 times — no ODE solver needed, just matrix multiplication.

## Remember

Continuous-time affine models require numerical ODE solvers (Riccati equations), which complicates statistical estimation because each parameter update needs a new solve. The discrete-time recursion replaces the ODE with simple matrix multiplications, making it straightforward to estimate all parameters by maximum likelihood or Bayesian methods from standard quarterly macro data. This is why macro-finance models linking monetary policy, inflation, and bond yields are almost always specified in discrete time — the Ang–Piazzesi framework became the template for research connecting macroeconomics to the yield curve.
