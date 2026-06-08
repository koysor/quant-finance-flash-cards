# Cross-Currency Swap

**Topic:** Fixed Income
**Tags:** cross-currency swap, xccy, fx basis, principal exchange, multi-currency, funding cost
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

A **cross-currency swap** exchanges floating interest payments in two different currencies, with **notional principal exchanged at inception and re-exchanged at maturity** at the same FX rate. The floating rate on one leg typically includes a **cross-currency basis spread** that adjusts the PV to zero at initiation.

## Key Formula

Standard structure (USD SOFR vs EUR ESTR): at initiation exchange notionals, then periodically:

$$\text{Pay: } N_{\text{EUR}} \cdot \delta \cdot ({\text{ESTR}_i + \text{basis}})$$

$$\text{Receive: } N_{\text{USD}} \cdot \delta \cdot \text{SOFR}_i$$

$$N_{\text{USD}} = N_{\text{EUR}} \times \text{FX}_0$$

At maturity: re-exchange principals at the **original** FX rate $\text{FX}_0$.

The basis spread is set so the swap's PV = 0 at initiation. A negative basis (EUR pays ESTR − spread) means USD funding is in demand relative to EUR.

## Example

A European company wants USD funding. It issues EUR bonds at ESTR and enters a cross-currency swap: pay EUR ESTR + (−15bps) to the counterparty, receive USD SOFR. At inception, exchange €100m for \$108m (at spot FX 1.08). At maturity, reverse at the same rate regardless of where FX has moved.

## Remember

Cross-currency basis spreads reflect **real-world funding imbalances** between currency areas that covered interest rate parity alone cannot explain. During the 2008 GFC and the March 2020 COVID shock, USD cross-currency basis widened dramatically (to −100bps for EUR/USD) as the whole world scrambled for USD liquidity. Banks and corporates with USD funding needs use cross-currency swaps as a central tool of liability management; central bank swap lines were activated to suppress the spread.
