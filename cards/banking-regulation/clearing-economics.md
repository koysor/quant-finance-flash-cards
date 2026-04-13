# Bilateral vs Central Clearing Economics

**Topic:** Banking Regulation
**Tags:** ccp, bilateral, clearing, cost comparison, netting efficiency
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The choice between bilateral OTC derivatives and centrally cleared derivatives involves a trade-off between regulatory capital, margin costs, and operational complexity. Central clearing through a CCP provides multilateral netting, standardised margin, and default management benefits, but requires daily cash variation margin and contributions to the default fund. Bilateral trading allows bespoke terms but carries full CVA capital, UMR initial margin obligations, and higher SA-CCR exposure calculations.

## Key Formula

The total cost of a trade can be compared across the two regimes:

$$\text{Cost}_{\text{bilateral}} = \text{CVA capital} + \text{UMR IM cost} + \text{SA-CCR RWA cost} + \text{operational cost}$$

$$\text{Cost}_{\text{CCP}} = \text{IM cost (SPAN/SIMM)} + \text{default fund contribution} + \text{CCP fees} + \text{netting benefit}$$

The netting benefit of CCP clearing is often the dominant term for large portfolios:

$$\text{Netting benefit} = \text{Gross bilateral IM} - \text{CCP portfolio IM}$$

because the CCP offsets long and short positions across all clearing members, while bilateral agreements only net within a single counterparty relationship.

## Example

A fund has £500 m notional in IR swaps with 5 bilateral counterparties, each requiring separate SIMM IM calculations. Total bilateral IM = £60 m (no cross-counterparty netting). Moving to a CCP, the CCP nets the full portfolio: total CCP IM = £25 m (all positions against a single CCP). The £35 m reduction in IM represents a significant funding cost saving, but the fund must also contribute £5 m to the default fund and pay CCP clearing fees of £200k/year — still a net saving in this case.

## Remember

The post-2008 G20 mandate to clear standardised OTC derivatives was explicitly designed to tilt the economics in favour of CCP clearing by making bilateral trading more expensive. SA-CCR increased bilateral RWA, CVA capital added a bilateral credit charge, and UMR imposed bilateral IM obligations — together these mean that for plain-vanilla interest rate and credit derivatives, CCP clearing is almost always cheaper than bilateral for large institutions. The residual bilateral market consists primarily of: bespoke structures that CCPs will not accept, currency pairs with insufficient liquidity to meet CCP eligibility, and counterparties below UMR thresholds (Phase 5/6 smaller buy-side firms) for whom the regulatory cost difference is smaller than the operational cost of CCP onboarding.

