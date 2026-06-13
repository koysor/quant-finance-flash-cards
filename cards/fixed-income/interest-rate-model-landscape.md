# Interest Rate Model Landscape

**Topic:** Fixed Income
**Tags:** model comparison, short rate, LMM, lognormal, Hull-White, BK, BDT, CIR, Vasicek
**Created:** 2026-06-12
**Author:** Claude Sonnet 4.6

---

## Definition

The **interest rate model landscape** spans one-factor short-rate models, multi-factor models, and forward-rate models. Each family trades off analytical tractability, positive-rate guarantee, yield-curve fit, and vol surface fit. The right model depends on the product being priced: vanilla swaps need curve fit; swaptions need vol fit; Bermudan swaptions need both simultaneously.

## Key Formula

| Model | Positive rates | Fits yield curve | Closed-form bonds | Vol surface fit | Primary use |
|---|---|---|---|---|---|
| Vasicek | No | No | Yes | Flat smile | Risk management, analytics |
| CIR | Yes | No | Yes | Moderate | Credit intensity models |
| Ho–Lee | No | Yes | Yes | Flat smile | Pedagogical |
| Hull–White (HW1) | No | Yes | Yes | Term structure | Standard exotic rates |
| Black–Derman–Toy | Yes | Yes | Tree only | Caplet vol strip | Callable bonds (older) |
| Black–Karasinski | Yes | Yes | Tree only | Caplet vol strip | Bermudan swaptions |
| G2++ (two-factor HW) | No | Yes | Yes | Richer smile | Callable bonds, CVA |
| LMM | Yes | Yes | No | Full cap surface | Exotic caps, ratchets |

The key trade-off axes are:

$$\underbrace{\text{Vasicek} \to \text{Hull-White}}_{\text{add curve fit}} \to \underbrace{\text{BK}}_{\text{add positive rates}} \qquad \underbrace{\text{HW1} \to \text{G2++}}_{\text{add second factor}}$$

## Example

Pricing a **10-year Bermudan payer swaption**: Hull-White (HW1) is calibrated to the co-terminal swaption diagonal and run on a trinomial tree. It fits the yield curve and gives a stable exercise boundary. Black-Karasinski is preferred if the desk requires positive rates throughout (e.g. for lognormal vol quoting consistency). LMM would be used if the exotic also involves spread options or SOFR compounding across multiple tenors — the BK tree cannot handle multi-currency or multi-index payoffs.

## Remember

No single model dominates across all products. The practitioner heuristic is: **use the simplest model that captures the risks of your specific product**. A vanilla swap needs no vol model at all — just a bootstrapped discount curve. A European swaption needs a vol model but not a tree — Black's formula suffices. A Bermudan swaption needs a dynamic model calibrated to co-terminal vols — HW1 or BK. A callable CMS range accrual needs a full stochastic vol term structure — LMM with SABR. The cost of model complexity is calibration instability, computational time, and harder risk management; choosing an overly complex model for a simple product introduces unnecessary noise.
