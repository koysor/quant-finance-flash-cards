# DPL Boundary Conditions

**Topic:** Computational Finance
**Tags:** boundary conditions, daily price limits, absorbing boundary, reflecting boundary, local time, stochastic processes
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

When a stock price hits a **daily price limit** boundary, the market's regulatory and trading rules determine what happens next. Three canonical boundary types — absorbing, instant-reflecting, and slow-reflecting — model different market microstructure outcomes and have materially different impacts on option prices.

## Key Formula

The constrained stock SDE including local time terms at the lower boundary $a$ and upper boundary $b$ is:

$$dS_t = \mu S_t\,\mathbf{1}_{(a,b)}(S_t)\,dt + \sigma S_t\,\mathbf{1}_{(a,b)}(S_t)\,dW_t + \delta_1\,d\phi_t - \delta_2\,d\varphi_t$$

where $\phi_t$ and $\varphi_t$ are the **local times** accumulated at the lower and upper boundaries respectively, and $\delta_1, \delta_2 \in [0,1]$ are elasticity parameters:
- $\delta = 0$: **absorbing** — price sticks at the boundary for the remainder of the session
- $\delta = 1$: **instant reflecting** — price rebounds immediately into the corridor
- $0 < \delta < 1$: **slow reflecting** — price drifts back gradually (sticky boundary)

## Example

Under an absorbing upper boundary at £110, a stock that hits £110 at 10:30 stays there for the rest of the trading day. A call with strike £108 is therefore worth less than the unconstrained Black-Scholes price: the conditional distribution above £110 is collapsed onto £110, reducing the expected payoff $\max(S_T - 108, 0)$.

## Remember

The boundary type is a market design parameter that regulators implicitly choose, yet it materially affects option prices: an absorbing cap systematically reduces call values while a reflecting boundary redistributes the truncated probability mass back into the corridor. TDBP models embed boundary behaviour implicitly by training on constrained paths — they learn the correct conditional distribution without needing the analyst to specify the SDE's local time terms explicitly.
