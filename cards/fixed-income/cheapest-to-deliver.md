# Cheapest to Deliver

**Topic:** Fixed Income
**Tags:** cheapest to deliver, ctd, bond futures, conversion factor, delivery option, duration hedge
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

The Cheapest to Deliver (CTD) bond is the bond in a futures contract's deliverable basket that minimises the seller's cost of delivery, determined by comparing each eligible bond's invoice price (futures price × conversion factor) against its market price; the CTD bond's duration governs the effective interest rate sensitivity of the futures contract.

## Key Formula

The **delivery cost** for bond $i$ with conversion factor $CF_i$ and market price $P_i$ (both per £100 nominal) is:

$$\text{Delivery cost}_i = P_i - F \times CF_i$$

The short selects the bond that minimises this cost (most negative value):

$$\text{CTD} = \arg\min_i \left(P_i - F \times CF_i\right)$$

The **futures DV01** — the price change per 1bp move in yields — is determined by the CTD:

$$\text{DV01}_{\text{futures}} = \frac{\text{DV01}_{\text{CTD}}}{CF_{\text{CTD}}}$$

The number of futures contracts needed to hedge a portfolio with DV01 $= D$ is $n = D / \text{DV01}_{\text{futures}}$.

## Example

A trader holds a £10m 10-year gilt with DV01 = £8,500 and wants to hedge with March gilt futures ($F = 110.50$). Two bonds are eligible: Bond A ($P = 108.20$, $CF = 0.9830$, DV01 = £7,200) and Bond B ($P = 115.60$, $CF = 1.0480$, DV01 = £8,100). Delivery costs: A: $108.20 - 110.50 \times 0.9830 = -0.39$ (cheaper); B: $115.60 - 110.50 \times 1.0480 = +0.00$. Bond A is CTD. Futures DV01 $= 7200/0.9830 = £7,325$ per contract. Hedge: $n = 8500/7325 \approx 12$ contracts.

## Remember

Getting the CTD wrong — or ignoring that the CTD can switch as yields move — is one of the most common errors in fixed income hedging. When yields fall, higher-duration bonds tend to become cheaper to deliver (low-coupon, long-maturity bonds); when yields rise, shorter-duration bonds often take over. This **CTD switching** gives the futures contract negative convexity from the long's perspective: the deliverable bond always shifts to the one that is worst for the long position. Risk managers who treat the futures DV01 as constant across yield scenarios will systematically under-hedge when large yield moves trigger CTD switches.
