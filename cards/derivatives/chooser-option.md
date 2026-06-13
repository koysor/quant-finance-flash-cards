# Chooser Option

**Topic:** Derivatives
**Tags:** chooser option, put-call parity, static replication, straddle, directional uncertainty, exotic options
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **chooser option** gives the holder the right, at a pre-specified choice date $T_c < T$, to designate the instrument as either a European call or put — both with strike $K$ and expiry $T$. It is valued when a large price move is anticipated but its direction is unknown; it reduces to a straddle when $T_c = 0$ and to a vanilla call when $T_c = T$.

## Key Formula

At the choice date $T_c$ the holder receives whichever is larger:

$$V(T_c) = \max\!\bigl(C(S_{T_c}, K, T-T_c),\;\; P(S_{T_c}, K, T-T_c)\bigr)$$

Applying put-call parity $P = C - S + Ke^{-r(T-T_c)}$ to the put term:

$$V(T_c) = C(S_{T_c}, K, T-T_c) + \max\!\bigl(0,\;\; Ke^{-r(T-T_c)} - S_{T_c}\bigr)$$

This is the payoff of a long call expiring at $T$ **plus** a put with a discounted strike expiring at $T_c$, giving the exact model-free static decomposition:

$$\boxed{\text{Chooser}(K, T, T_c) = C(S_0, K, T) + P\!\left(S_0,\, Ke^{-r(T-T_c)},\, T_c\right)}$$

## Example

$S_0 = 100$, $K = 100$, $T = 6$ months, $T_c = 3$ months, $r = 5\%$, $\sigma = 20\%$.

Discounted strike: $Ke^{-r(T-T_c)} = 100 \times e^{-0.05 \times 0.25} \approx \pounds98.77$.

$$C(100,\, 100,\, 0.5\text{ yr}) \approx \pounds5.29, \qquad P(100,\, 98.77,\, 0.25\text{ yr}) \approx \pounds3.02$$

$$\text{Chooser price} \approx \pounds5.29 + \pounds3.02 = \pounds8.31$$

A standard 6-month straddle (call + put at $K = 100$) costs $\approx \pounds10.58$. The chooser at £8.31 is cheaper by £2.27 — because having 3 months to see the initial direction before committing is worth less than the immediate optionality a straddle provides.

## Remember

The chooser's static decomposition is one of the most elegant results in exotic option theory: a complex optionality (choose call or put in three months) reduces exactly to two vanilla options via put-call parity, with no model assumptions beyond Black-Scholes. This makes choosers cheap to hedge — just hold the vanilla call and the discounted-strike put from inception. In practice, choosers are used around binary events where direction is unknown but timing is fixed: a central bank meeting in three months, an M&A decision, or earnings. The trader waits until $T_c$ to observe the first market reaction, then locks in the optimal side — gaining information cheaply relative to a straddle that must be held from the outset through the volatility of the waiting period.
