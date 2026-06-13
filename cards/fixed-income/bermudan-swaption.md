# Bermudan Swaption

**Topic:** Fixed Income
**Tags:** Bermudan swaption, callable bond, co-terminal, short rate model, calibration, exercise boundary
**Created:** 2026-06-11
**Author:** Claude Sonnet 4.6

---

## Definition

A **Bermudan swaption** gives the holder the right to enter a fixed-for-floating interest rate swap on any of a finite set of pre-specified dates. The most common form is a **payer Bermudan swaption**: pay fixed, receive floating, exercisable annually over the life of the swap. Bermudan swaptions are the dominant exotic IR product and are the primary instrument that motivates the calibration of short-rate and LMM models.

## Key Formula

Let $\mathcal{T} = \{t_1, t_2, \ldots, t_N\}$ be the exercise dates and $K$ the fixed strike rate. At each exercise date $t_k$, the intrinsic value is the value of the underlying swap:

$$V_{\text{swap}}(t_k) = A(t_k, T_N)\bigl(S(t_k) - K\bigr)$$

where $S(t_k)$ is the fair swap rate at $t_k$ and $A(t_k, T_N)$ is the annuity to the swap maturity. The Bermudan price is found by backward induction on a tree or by simulation:

$$V(t_k) = \max\!\bigl(V_{\text{swap}}(t_k),\; \mathbb{E}^{t_k}\!\left[V(t_{k+1})\right]\bigr)$$

**Callable bond decomposition:**

$$\text{Callable bond price} = \text{Bullet bond price} - \text{Bermudan swaption value}$$

This identity is exact when the coupon equals the swap fixed rate, linking callable bond markets to the swaption market.

## Example

A 5NC1 structure (5-year swap, no-call for 1 year, then annually callable) has 4 exercise dates at years 1, 2, 3, 4. Calibration requires that the short-rate model reproduces the prices of the 4 co-terminal European swaptions: $1\text{y}\!\times\!4\text{y}$, $2\text{y}\!\times\!3\text{y}$, $3\text{y}\!\times\!2\text{y}$, $4\text{y}\!\times\!1\text{y}$. These are the European options that the Bermudan holder could exercise at each date, and matching them ensures the exercise boundary is correct.

## Remember

Bermudan swaptions are the reason that short-rate models must be calibrated to the **term structure of implied volatility** across multiple expiries, not just the ATM cap strip. A model calibrated to only the cap/floor market can badly misprice a Bermudan swaption because it may not match the co-terminal swaption vol grid. In practice, banks use Black–Karasinski or Hull–White models whose time-dependent volatility function $\sigma(t)$ is stripped from the co-terminal swaption matrix — the Bermudan price is then the output that cannot be observed directly.
