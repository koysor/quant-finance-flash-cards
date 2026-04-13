# Margin Valuation Adjustment (MVA)

**Topic:** Banking Regulation
**Tags:** mva, xva, initial margin, funding cost, umr
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Margin Valuation Adjustment (MVA) is the XVA component that captures the present value of the funding cost of posting initial margin over the life of a derivative. Unlike variation margin (which is economically neutral, as it tracks MtM), initial margin is a segregated asset that cannot be rehypothecated — so the firm must fund it from its treasury at its own cost of funds. MVA became material after UMR mandated bilateral IM exchange and after CCPs raised IM requirements.

## Key Formula

MVA is the integral of the funding spread applied to the expected initial margin profile:

$$\text{MVA} = s_f \int_0^T \mathbb{E}[\text{IM}(t)] \cdot df(0,t) \, dt$$

where $s_f$ is the firm's funding spread over the risk-free rate, $\mathbb{E}[\text{IM}(t)]$ is the expected initial margin at time $t$ (computed using SIMM or SPAN on the projected portfolio), and $df(0,t)$ is the discount factor. Discretised:

$$\text{MVA} \approx s_f \sum_{i} \mathbb{E}[\text{IM}(t_i)] \cdot \Delta t_i \cdot df(0,t_i)$$

## Example

A bank enters a 10-year cross-currency swap under UMR. The SIMM IM on day one is £20 m, declining approximately linearly as the trade ages. Average expected IM over 10 years ≈ £10 m. With a funding spread of 60 bps: MVA ≈ $0.006 \times £10\text{m} \times 10 = £600{,}000$. This £600k must be charged to the client upfront, as it represents the cost of funding segregated collateral for the life of the trade.

## Remember

MVA became a pricing reality only after Phase 5 and 6 of UMR (2021–2022) forced mid-sized buy-side firms to exchange bilateral IM. Before then, MVA was primarily a CCP concern. The introduction of MVA into trade pricing created a new axis of competition between dealers: a bank with a lower funding spread (stronger credit rating, larger balance sheet) can offer a lower all-in price to clients by charging less MVA. For quant developers, MVA simulation requires projecting the full SIMM IM path — not just the MtM — which requires simulating market risk factor sensitivities (delta, vega) at each future date, significantly more complex than standard exposure simulation.

