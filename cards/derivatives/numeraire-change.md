# Numéraire Change

**Topic:** Derivatives
**Tags:** numeraire, measure change, forward measure, pricing, change of numeraire
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A **numéraire** is a positive, tradeable asset used as the unit of account for pricing. Changing the numéraire from one asset to another induces a change of probability measure, simplifying certain pricing problems. The standard risk-neutral measure $\mathbb{Q}$ uses the money market account $B_t = e^{rt}$ as numéraire; switching to a different numéraire (e.g. a zero-coupon bond) yields a new measure under which the pricing formula becomes more tractable.

## Key Formula

**Numéraire invariance:** if $N_t$ is a positive tradeable asset, define the measure $\mathbb{Q}^N$ by:

$$\frac{d\mathbb{Q}^N}{d\mathbb{Q}} = \frac{N_T / N_0}{B_T / B_0}$$

Then for any claim with payoff $H$ at time $T$:

$$\frac{V_0}{N_0} = E^{\mathbb{Q}^N}\!\left[\frac{H}{N_T}\right]$$

**Forward measure** (numéraire = zero-coupon bond $P(t, T)$):

$$V_0 = P(0, T)\,E^{\mathbb{Q}^T}\![H]$$

This eliminates the need to discount inside the expectation.

## Example

Price a caplet paying $\max(L_T - K, 0)$ at time $T + \delta$, where $L_T$ is the LIBOR rate.

Under the **money market measure** $\mathbb{Q}$: the discount factor $e^{-\int_0^{T+\delta} r_s\,ds}$ is stochastic and correlated with $L_T$ — difficult to compute.

Under the **$T+\delta$ forward measure** $\mathbb{Q}^{T+\delta}$ (numéraire = $P(t, T+\delta)$):

$$V_0 = P(0, T+\delta)\,\delta\,E^{\mathbb{Q}^{T+\delta}}\!\left[\max(L_T - K, 0)\right]$$

Under this measure, $L_T$ is a martingale. If $L_T$ is lognormal, the expectation is a Black formula with forward rate $L_0$ and volatility $\sigma_L$:

$$V_0 = P(0, T+\delta)\,\delta\,\left[L_0\,\Phi(d_1) - K\,\Phi(d_2)\right]$$

The numéraire change transformed a hard problem into a standard Black–Scholes-type formula.

## Remember

Numéraire change is the power tool of interest rate derivatives pricing. By choosing the right numéraire, a quant can make the quantity of interest (a forward rate, a swap rate, a stock price relative to a bond) a martingale under the new measure — which dramatically simplifies the expectation calculation. The Black model for caps and floors uses the zero-coupon bond as numéraire; the swap measure for swaptions uses the annuity as numéraire. The underlying principle is numéraire invariance: the real-world price $V_0$ is the same regardless of which numéraire you use — the choice only affects which measure you compute the expectation under. Picking the "natural" numéraire for a given payoff is one of the key skills in fixed-income quantitative finance.
