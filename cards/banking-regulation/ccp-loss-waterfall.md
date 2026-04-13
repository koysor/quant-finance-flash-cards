# CCP Loss Waterfall

**Topic:** Banking Regulation
**Tags:** ccp, default fund, loss absorption, clearing, systemic risk
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The CCP loss waterfall is the pre-defined order in which a Central Counterparty exhausts financial resources to cover losses when a clearing member defaults. It embodies the "defaulter pays" principle: the failing member's own collateral is consumed entirely before any mutualised resources belonging to surviving members are touched.

## Key Formula

The waterfall layers are consumed in strict sequence:

| Layer | Resource | Who bears it |
|---|---|---|
| 1 | Defaulter's Initial Margin | Defaulting member |
| 2 | Defaulter's Default Fund contribution | Defaulting member |
| 3 | CCP's "skin-in-the-game" equity | CCP itself |
| 4 | Surviving members' Default Fund | Mutualised |
| 5 | Assessment powers (additional calls) | Surviving members |
| 6 | CCP's remaining equity / recovery | CCP / resolution |

The CCP's skin-in-the-game $S$ is calibrated so that the CCP has a direct incentive to price risk correctly:

$$S > 0 \implies \text{CCP absorbs losses before mutualised default fund is used}$$

## Example

A clearing member with £200 m IM and £50 m default fund contribution defaults, generating £300 m in close-out losses. The waterfall draws: £200 m from the member's IM, then £50 m from their default fund (£250 m used, £50 m short). The CCP's £10 m skin-in-the-game is consumed next. Remaining £40 m is drawn from the surviving members' pooled default fund.

## Remember

The waterfall design is central to CCP resilience and the PFMI (Principles for Financial Market Infrastructures) "Cover 2" standard, which requires a CCP to survive the simultaneous default of its two largest clearing members under extreme but plausible market conditions. Regulators stress-test CCPs against scenarios that exhaust the entire waterfall, because a CCP failure — unlike a single bank failure — could trigger simultaneous losses across all surviving members, creating contagion far worse than a bilateral default.
