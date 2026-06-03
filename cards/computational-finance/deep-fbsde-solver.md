# Deep FBSDE Solver

**Topic:** Computational Finance
**Tags:** deep learning, bsde, fbsde, pricing, hedging, high-dimensional, pde
**Created:** 2026-06-03
**Author:** Gemini CLI

---

## Definition

A **Deep FBSDE Solver** (Han et al., 2018) is a deep learning framework used to solve high-dimensional partial differential equations (PDEs) by reformulating them as **Forward-Backward Stochastic Differential Equations (FBSDEs)**. The unknown solution (e.g., option price) and its gradient (e.g., delta) are parameterised as neural networks. The networks are trained to satisfy the terminal condition (payoff) by simulating paths of the forward process and integrating the backward SDE.

## Key Formula

Consider a derivative price $Y_t$ following the backward SDE derived from the Black-Scholes PDE:

$$dY_t = rY_t \, dt + \sigma X_t \frac{\partial Y}{\partial X} \, dW_t$$

Since $\frac{\partial Y}{\partial X}$ (the delta) is unknown, we approximate it with a neural network $N_\theta(X_t, t)$. The discretised process for $Y$ becomes:

$$Y_{t+1} \approx Y_t + rY_t \Delta t + \sigma X_t N_\theta(X_t, t) \Delta W_t$$

The network parameters $\theta$ and the initial price $Y_0$ are learned by minimising the mean squared error between the predicted terminal value $Y_T$ and the actual payoff $g(X_T)$:

$$\mathcal{L}(\theta, Y_0) = \mathbb{E}\!\left[ \lvert Y_T - g(X_T) \rvert^2 \right]$$

## Example

Pricing a 100-dimensional European basket option where the payoff depends on the average price of 100 correlated stocks. Traditional grid-based PDE solvers fail due to the **curse of dimensionality** ($100$ dimensions). A Deep FBSDE solver, parameterised with a 4-layer fully connected network, can estimate the price and the 100-dimensional delta vector simultaneously. After training on $10^5$ simulated paths, it converges to a price within $0.1\%$ of the Monte Carlo benchmark but provides the full Greeks surface in a single forward pass.

## Remember

Deep FBSDE solvers bypass the curse of dimensionality by treating the pricing problem as a **supervised learning task** on stochastic paths. The key insight is that the backward SDE describes the dynamics of the replicating portfolio; by training the network to match the payoff, we are effectively "learning" the optimal hedging strategy $(\frac{\partial Y}{\partial X})$ and the fair price $(Y_0)$ at once. This is particularly useful for valuation adjustments (XVA) and risk management in high-dimensional portfolios where Monte Carlo is too slow for real-time Greeks.
