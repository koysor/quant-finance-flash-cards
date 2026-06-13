# Black-Scholes PDE

**Topic:** Derivatives
**Tags:** Black-Scholes, PDE, delta hedging, no-arbitrage, heat equation, pricing
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Black-Scholes PDE** is the partial differential equation that the price $V(S, t)$ of any derivative on a non-dividend-paying stock must satisfy, under the assumptions of continuous trading, constant volatility $\sigma$, and a constant risk-free rate $r$. It is derived by constructing a delta-hedged portfolio — long the derivative, short $\Delta = \partial V/\partial S$ shares — and requiring it to earn the risk-free rate. The stochastic term vanishes, leaving a deterministic PDE.

## Key Formula

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

The three derivative terms represent: time decay, gamma P&L from the stock's diffusion, and rho (financing the delta hedge). The PDE holds in the **continuation region** and is solved backwards from the terminal condition:

| Derivative | Terminal condition $V(S, T)$ | Boundary conditions |
|------------|------------------------------|---------------------|
| European call | $\max(S - K, 0)$ | $V(0,t)=0$; $V(S,t)\to S$ as $S\to\infty$ |
| European put | $\max(K - S, 0)$ | $V(0,t)=Ke^{-r(T-t)}$; $V(S,t)\to 0$ as $S\to\infty$ |
| Binary cash-or-nothing | $\mathbf{1}_{S>K}$ | $V(0,t)=0$; $V(S,t)\to e^{-r(T-t)}$ as $S\to\infty$ |

The PDE transforms to the **heat equation** under the substitution $V = e^{-r(T-t)}u$, $x = \ln S$, $\tau = T - t$, unlocking the closed-form solution for European payoffs via convolution with the Gaussian kernel.

## Example

For a European call with $K=100$, $r=5\%$, $\sigma=20\%$, verify the PDE at $S=100$, $t=0$, $T=1$.

Using Black-Scholes: $V \approx 10.45$, $\Delta = \partial V/\partial S \approx 0.637$, $\Gamma = \partial^2 V/\partial S^2 \approx 0.019$, $\Theta = \partial V/\partial t \approx -6.41$ (per year).

Check: $-6.41 + \tfrac{1}{2}(0.04)(10{,}000)(0.019) + (0.05)(100)(0.637) - (0.05)(10.45)$
$= -6.41 + 3.80 + 3.19 - 0.52 \approx 0$ ✓

## Remember

The PDE is the universal pricing engine: the same equation governs calls, puts, barriers, digitals, and multi-date exotics — the only difference is the terminal payoff and boundary conditions. Delta-hedging is simultaneously the derivation strategy and the replication strategy: a bank that sells a call and continuously delta-hedges replicates the Black-Scholes price exactly (under the model assumptions). In practice, the PDE is solved numerically by finite-difference schemes on a grid of $(S, t)$ values, backward in time from the payoff — this is the approach that handles American exercise, barriers, and discrete dividends that have no closed-form solution.
