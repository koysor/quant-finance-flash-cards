# Forward PDE vs Backward PDE

**Topic:** Computational Finance
**Tags:** dupire forward pde, black-scholes pde, calibration, kolmogorov equations, local volatility, pricing
**Created:** 2026-07-31
**Author:** Claude Opus 5

---

## Definition

A **backward PDE** evolves an option value backwards in calendar time from a known payoff, in the variables $(S, t)$ of the underlying — it prices one contract under all spot scenarios. A **forward PDE** evolves prices forwards in the contract variables $(K, T)$ from a known spot — it prices all strikes and maturities under one spot. The two describe the same market but answer opposite questions.

## Key Formula

**Backward (Black-Scholes):** solved for $V(S, t)$ with terminal condition $V(S, T) = \max(S - K, 0)$, one strike at a time.

$$\frac{\partial V}{\partial t} + \tfrac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

**Forward (Dupire):** solved for $C(K, T)$ with initial condition $C(K, 0) = \max(S_0 - K, 0)$, the whole surface at once.

$$\frac{\partial C}{\partial T} = \tfrac{1}{2}\sigma_{\text{loc}}^2(K, T)\,K^2\frac{\partial^2 C}{\partial K^2} - (r - q)K\frac{\partial C}{\partial K} - qC$$

Rearranging the forward equation for the unknown volatility gives Dupire's formula:

$$\sigma_{\text{loc}}^2(K, T) = \frac{\partial_T C + (r-q)K\,\partial_K C + qC}{\tfrac{1}{2}K^2\,\partial_{KK}C}$$

The pair mirrors the backward and forward Kolmogorov equations: backward propagates an expectation, forward propagates a density.

## Example

A desk holds 400 SPX vanillas across 20 strikes and 20 expiries.

- **Backward route:** run a Crank-Nicolson grid in $(S, t)$ once per contract — 400 solves, each giving that contract's value and Greeks in spot.
- **Forward route:** one solve in $(K, T)$ marching from $T = 0$ produces all 400 prices simultaneously, because every grid node *is* a contract.

For calibration the forward route wins outright: fitting $\sigma_{\text{loc}}$ to 400 quotes needs only 400 grid reads per iteration instead of 400 separate PDE solves.

## Remember

Recognising which direction a problem runs in is the practical skill. **Calibration is a forward problem** — you have the surface and want the volatility, so you differentiate a fitted $C(K, T)$ in $(K, T)$ and never actually march the PDE. **Pricing is a backward problem** — an exotic with a barrier, an early-exercise right, or path dependence has no representation in $(K, T)$ space, so once $\sigma_{\text{loc}}(K, T)$ is extracted it is fed into a backward Crank-Nicolson solver. The standard validation cycle in a local volatility project uses both: extract local volatility from the forward equation, then reprice the original vanillas backwards and check the error is discretisation noise rather than a modelling failure.
