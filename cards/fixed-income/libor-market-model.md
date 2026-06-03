# LIBOR Market Model (LMM)

**Topic:** Fixed Income
**Tags:** libor market model, forward rates, bgm model, interest rate derivatives, swaption, caplet
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **LIBOR Market Model** (LMM, also called the BGM model after Brace, Gatarek, Musiela, 1997) models the joint evolution of a set of discrete forward LIBOR rates $\{L_k(t)\}$ directly under their respective forward measures. Unlike Hull-White (which models the unobservable short rate), LMM models rates that are directly quoted in the market, making calibration to cap and swaption prices natural and pricing of complex multi-callable products exact within the model.

## Key Formula

Under the **spot LIBOR measure** (associated with the rolling money-market account), each forward rate $L_k(t)$ for the period $[T_k, T_{k+1}]$ evolves as:

$$\frac{dL_k(t)}{L_k(t)} = \mu_k(t)\,dt + \sigma_k(t)\cdot dW_t$$

where the **drift** $\mu_k$ under the spot measure is:

$$\mu_k(t) = \sum_{j=\eta(t)}^{k} \frac{\delta_j L_j(t)\,\sigma_j(t)\cdot\sigma_k(t)}{1 + \delta_j L_j(t)}$$

and $\delta_j = T_{j+1} - T_j$ is the accrual fraction. **Caplet** prices are log-normal by construction (Black's formula), and **swaption** prices require Monte Carlo or approximate analytical methods (Rebonato approximation).

## Example

A Bermudan swaption on a 5-year swap exercisable at years 1–4 is priced under LMM calibrated to 20 caplets and 10 co-terminal swaptions. Hull-White (1 factor) gives 82 bps; LMM with 3 factors (capturing level, slope, curvature of rates) gives 87 bps. The 5 bp difference arises because LMM correctly captures the correlation between forward rates across different maturities — a single-factor Hull-White forces all rates to move together, underestimating the optionality when rate moves are partially decorrelated across the yield curve.

## Remember

LMM is the gold standard for interest rate exotic pricing because it is **consistent with the caplet market by construction** — each forward rate follows log-normal dynamics (Black's formula), so any caplet price observed in the market is immediately reproduced without calibration. The cost is **tractability**: the drift $\mu_k$ couples all forward rates, making analytic pricing of swaptions and Bermudans intractable without approximation. RL provides a natural escape: an OST-TDBP agent trained on LMM Monte Carlo paths inherits LMM's realism without needing the Rebonato swaption approximation, pricing Bermudans as accurately as the simulation allows while avoiding the basis-function selection problem of Longstaff-Schwartz.
