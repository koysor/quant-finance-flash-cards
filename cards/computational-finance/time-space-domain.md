# Time-Space Domain

**Topic:** Computational Finance
**Tags:** time-space domain, tdbp, pricing surface, function approximation, option pricing, interpolation
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

In the TDBP framework, the **time–space domain** is the product space of time steps $t \in \{0, \Delta t, \ldots, T\}$ and asset prices $S \in \mathbb{R}_{>0}$. Learning prices across the full domain produces a continuous **pricing surface** — the model can instantly return the option price at any $(t, S)$ pair without rerunning a simulation.

## Key Formula

The pricing surface is a two-argument function:

$$P: (t, S) \mapsto P(t, S)$$

approximated by the collection of trained networks $\{f_0, f_1, \ldots, f_T\}$:

$$P(t, S) \approx f_t(S;\theta_t), \qquad \forall\, t,\, S$$

The surface satisfies the Bellman boundary condition $f_T(S) = \text{payoff}(S)$ at maturity and the recursive constraint $f_t(S_t) = e^{-r\Delta t}\,\mathbb{E}[f_{t+1}(S_{t+1}) \mid S_t]$ at all earlier times.

## Example

A 100-day call option pricing surface spans 100 time slices, each a function of spot price. Monte Carlo gives prices at isolated starting points; TDBP fills the entire surface. At day 45 with $S = 105.37$, the answer is $f_{45}(105.37)$ — a single forward pass through the day-45 network, returning in under 1 ms, compared with several seconds for 10,000 Monte Carlo paths.

## Remember

The time–space domain perspective is what makes TDBP practical for **real-time risk management**: derivatives desks pre-train the surface offline overnight and query it thousands of times per second during live trading to re-price positions as the spot moves. Each query is one neural network forward pass — enabling intraday delta-hedging, Greeks calculation, and stress scenarios at a speed and granularity that Monte Carlo or finite-difference PDE solvers cannot match in production systems.
