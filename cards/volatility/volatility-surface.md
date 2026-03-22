# Volatility Surface

**Topic:** Volatility
**Tags:** volatility surface, implied volatility, smile, term structure, options, interpolation
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **volatility surface** is the three-dimensional function $\sigma_{\text{impl}}(K, T)$ that maps every combination of strike price $K$ and maturity $T$ to an implied volatility. It is constructed from the market prices of liquid European options and is the fundamental input for pricing and hedging exotic derivatives. The surface captures both the **volatility smile/skew** (variation across strikes at a fixed maturity) and the **term structure of volatility** (variation across maturities at a fixed strike).

## Key Formula

At each grid point $(K_i, T_j)$, implied volatility $\hat{\sigma}_{ij}$ solves:

$$C_{\text{market}}(K_i, T_j) = C_{\text{BS}}(S_0, K_i, r, T_j, \hat{\sigma}_{ij})$$

**No-arbitrage constraints** on the surface include:

- **Calendar spread:** total implied variance $\hat{\sigma}^2 T$ must be non-decreasing in $T$ for each $K$
- **Butterfly spread:** the local volatility derived from the surface must be real and positive, requiring $\partial^2 C / \partial K^2 > 0$

Interpolation between grid points commonly uses **cubic splines** in strike space and **linear-in-variance** ($\sigma^2 T$) in the time dimension.

## Example

A desk observes 3-month ATM implied volatility of 18%, 6-month ATM of 20%, and 1-year ATM of 22%. At the 3-month expiry, the 90% moneyness put has implied vol of 24% and the 110% call has 16%.

The surface slice at $T = 0.25$ shows a **skew**: low-strike vol (24%) exceeds high-strike vol (16%). The ATM term structure is upward-sloping (18% → 20% → 22%), indicating the market expects higher volatility over longer horizons.

To price a 9-month barrier option at a non-standard strike, the desk interpolates within this surface — getting the volatility wrong by even 1% can shift an exotic's value by several percent.

## Remember

The volatility surface is the central object in an options trading desk's infrastructure. Every exotic derivative price depends on it, and every hedge ratio is derived from it. Building a robust, arbitrage-free surface from sparse market quotes is one of the core challenges in quantitative finance. Models like local volatility (Dupire) and stochastic volatility (Heston, SABR) are ultimately calibrated to reproduce the observed surface — the surface is the market reality, and models are tools for interpolating and extrapolating it consistently.
