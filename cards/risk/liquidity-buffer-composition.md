# Liquidity Buffer Composition

**Topic:** Risk
**Tags:** HQLA, liquidity buffer, LCR, Basel III, liquid assets, haircuts
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **liquidity buffer** is the stock of high-quality liquid assets (HQLA) a bank holds to meet the numerator of the Liquidity Coverage Ratio. Basel III classifies HQLA into three tiers — Level 1, Level 2A, and Level 2B — with increasing haircuts and caps reflecting decreasing liquidity and credit quality. The composition of the buffer determines both its regulatory value and its impact on the bank's interest rate risk profile.

## Key Formula

The **adjusted HQLA stock**:

$$\text{HQLA} = L_1 + \min(L_{2A} \times 0.85,\; 0.40 \times \text{HQLA}_{\text{adj}}) + \min(L_{2B} \times h_{2B},\; 0.15 \times \text{HQLA}_{\text{adj}})$$

where:
- $L_1$: Level 1 assets at market value (0% haircut)
- $L_{2A}$: Level 2A assets subject to 15% haircut
- $L_{2B}$: Level 2B assets subject to 25–50% haircut ($h_{2B}$)
- Level 2 assets (2A + 2B) are capped at 40% of the total buffer
- Level 2B assets are capped at 15% of the total buffer

## Example

A bank holds:
- **Level 1:** £30bn in gilts and central bank reserves (0% haircut → £30bn)
- **Level 2A:** £8bn in covered bonds (15% haircut → £6.8bn)
- **Level 2B:** £3bn in investment-grade corporate bonds (50% haircut → £1.5bn)

Total before caps: £30bn + £6.8bn + £1.5bn = £38.3bn

Check 40% cap on Level 2: £6.8bn + £1.5bn = £8.3bn. The 40% cap = 0.40 × £38.3bn = £15.3bn — not binding.

Check 15% cap on Level 2B: £1.5bn. The 15% cap = 0.15 × £38.3bn = £5.7bn — not binding.

**Adjusted HQLA = £38.3bn**

## Remember

The composition of the liquidity buffer creates a direct link between liquidity regulation and interest rate risk. Level 1 assets are dominated by government bonds, which carry significant duration — a bank holding £30bn of 10-year gilts for LCR purposes has simultaneously created a £30bn rate position. During the September 2022 UK gilt crisis, the sharp rise in yields caused mark-to-market losses on LCR buffers, creating a paradox where the assets held for liquidity protection were themselves a source of financial stress. ALM teams must balance buffer composition between shorter-dated assets (lower duration risk but potentially lower yields) and longer-dated assets (higher yields but greater EVE sensitivity). The haircut hierarchy also incentivises banks to hold Level 1 assets, concentrating sovereign exposure and creating systemic interconnection between bank solvency and government bond markets.
