# Bermudan Option

**Topic:** Derivatives
**Tags:** bermudan option, early exercise, discrete exercise dates, optimal stopping, rl pricing, swaption
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

A **Bermudan option** can be exercised early, but only on a pre-specified finite set of dates $\mathcal{T} = \{t_1, t_2, \ldots, t_M, T\}$ — between a European option (exercise only at $T$) and an American option (exercise any time). They dominate the interest rate derivatives market: the overwhelming majority of callable bonds and Bermudan swaptions are the most liquidly traded exotic rate products globally.

## Key Formula

The Bermudan price is an optimal stopping problem restricted to $\mathcal{T}$:

$$V_0 = \sup_{\tau \in \mathcal{T}} e^{-r\tau}\,\mathbb{E}^{\mathbb{Q}}\!\left[g(S_\tau)\right]$$

Solved by backward induction over the exercise dates only — at each $t_k \in \mathcal{T}$:

$$V_{t_k} = \max\!\left(g(S_{t_k}),\; e^{-r(t_{k+1} - t_k)}\,\mathbb{E}\!\left[V_{t_{k+1}} \mid \mathcal{F}_{t_k}\right]\right)$$

Between exercise dates, $V_t = e^{-r(t_{k+1} - t)}\mathbb{E}[V_{t_{k+1}} \mid \mathcal{F}_t]$ — no exercise decision. At non-exercise time steps, OST-TDBP uses the standard Bellman step without the $\max$.

## Example

A Bermudan swaption on a 5-year swap, exercisable annually on years 1, 2, 3, 4, 5. The holder can enter a pay-fixed swap at any of the 5 exercise dates, paying the strike rate or doing nothing. The Bermudan price lies between the corresponding European swaption (exercise at year 1 only) and the perpetual American limit. Market participants price these with Longstaff-Schwartz on short-rate model paths; an RL agent trained on the same paths reproduces the exercise boundary without specifying the continuation regression basis.

## Remember

Bermudan options are the natural intermediate benchmark between European and American pricing for RL agents — OST-TDBP handles them by simply switching off the $\max$ operator at non-exercise time steps and activating it at exercise dates in $\mathcal{T}$. This requires no architectural change: just a mask that identifies which time steps are exercise opportunities. In the interest rate world, the Bermudan swaption is the product that motivates the entire short-rate model calibration industry, because getting its price right requires a model that correctly captures the term structure of volatility across all exercise dates simultaneously.
